import { spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const EVALS_ROOT = path.resolve(new URL('..', import.meta.url).pathname);
const REPO_ROOT = path.resolve(EVALS_ROOT, '..');
const BIN = process.env.OPENCODE_BIN || 'opencode';

// Resolve skill sources for the bundle(s) under test. A built collection keeps
// relative resources intact; a source tree works for local smoke runs.
function skillsRoot() {
  if (process.env.EVAL_SKILLS_DIR) return path.resolve(process.env.EVAL_SKILLS_DIR);
  const built = path.join(EVALS_ROOT, '.bundle');
  if (fs.existsSync(built)) return built;
  return path.join(REPO_ROOT, 'plugins');
}

function skillSources(bundles) {
  const root = skillsRoot();
  // promptfoo expands an array var into a test grid, so a case that needs more
  // than one bundle passes a comma-separated string instead.
  const names = Array.isArray(bundles) ? bundles : String(bundles || 'sdlc').split(',');
  return names.map((bundle) => bundle.trim()).filter(Boolean).map((bundle) => path.join(root, bundle, 'skills'));
}

function version() {
  try {
    const out = spawnSync(BIN, ['--version'], { encoding: 'utf8', timeout: 20000 });
    return (out.stdout || '').trim().split('\n').pop() || 'unknown';
  } catch {
    return 'unknown';
  }
}

const OPENCODE_VERSION = version();

const IGNORED = new Set(['.git', 'node_modules', '__pycache__', '.pytest_cache', '.venv', 'venv', '.mypy_cache']);

function walk(dir, base = dir) {
  const found = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (IGNORED.has(entry.name) || entry.name.endsWith('.pyc')) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) found.push(...walk(full, base));
    else if (entry.isFile()) {
      found.push({
        path: path.relative(base, full).split(path.sep).join('/'),
        hash: createHash('sha256').update(fs.readFileSync(full)).digest('hex'),
      });
    }
  }
  return found;
}

function snapshot(dir) {
  return new Map(walk(dir).map((file) => [file.path, file.hash]));
}

function safe(name) {
  return String(name || 'case').replace(/[^a-zA-Z0-9._-]+/g, '_');
}

function writeTrace(id, stdout, stderr, metadata, excerpts) {
  const traceDir = process.env.EVAL_TRACE_DIR;
  if (!traceDir) return null;
  fs.mkdirSync(traceDir, { recursive: true });
  const base = safe(id);
  fs.writeFileSync(path.join(traceDir, `${base}.jsonl`), stdout || '');
  if (stderr) fs.writeFileSync(path.join(traceDir, `${base}.stderr.log`), stderr);
  fs.writeFileSync(path.join(traceDir, `${base}.meta.json`), JSON.stringify(metadata, null, 2) + '\n');
  if (excerpts.length) {
    const dir = path.join(traceDir, `${base}.files`);
    fs.mkdirSync(dir, { recursive: true });
    for (const { file, body } of excerpts) {
      const target = path.join(dir, safe(file.replaceAll('/', '__')));
      fs.writeFileSync(target, body);
    }
  }
  return path.join(traceDir, `${base}.jsonl`);
}

export default class OpenCodeProvider {
  id() {
    return 'opencode-run';
  }

  async callApi(prompt, context) {
    const vars = context?.vars || {};
    const id = vars.id || context?.test?.description || 'case';
    const fixture = path.resolve(EVALS_ROOT, vars.fixture || 'fixtures/empty');
    const started = Date.now();
    const runRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'skill-eval-'));
    const workspace = path.join(runRoot, 'workspace');
    const configHome = path.join(runRoot, 'config');
    fs.cpSync(fixture, workspace, { recursive: true });
    fs.mkdirSync(path.join(configHome, 'opencode'), { recursive: true });

    const sources = skillSources(vars.bundles);
    fs.writeFileSync(
      path.join(configHome, 'opencode', 'opencode.json'),
      JSON.stringify(
        {
          $schema: 'https://opencode.ai/config.json',
          skills: sources,
          permission: { webfetch: 'deny', websearch: 'deny' },
        },
        null,
        2,
      ),
    );

    const before = snapshot(workspace);
    const model = process.env.OPENCODE_MODEL || context?.providerConfig?.model || 'opencode-go/deepseek-v4.1-flash';
    // A unique suffix prevents resuming a previous run's session: the agent would
    // otherwise remember an old workspace path and write outside this copy.
    const session = `ses_eval_${safe(id).replaceAll('.', '_')}_${runRoot.split('-').pop().toLowerCase()}`;
    const timeoutSec = Number(vars.timeout_sec || 300);
    const args = [
      'run',
      '--standalone',
      '--archived',
      '--auto',
      '--format',
      'json',
      '--session',
      session,
      '-m',
      model,
      '--',
      prompt,
    ];

    // XDG_CONFIG_HOME is isolated and contains one file: opencode/opencode.json.
    // XDG_DATA_HOME is NOT isolated by this harness: provider credentials live
    // there. A fresh data home fails with provider.no-route. Set
    // OPENCODE_DATA_HOME to a dedicated, seeded data home for CI.
    const env = {
      ...process.env,
      PWD: workspace,
      XDG_CONFIG_HOME: configHome,
      XDG_CACHE_HOME: path.join(runRoot, 'cache'),
      ...(process.env.OPENCODE_DATA_HOME ? { XDG_DATA_HOME: process.env.OPENCODE_DATA_HOME } : {}),
    };

    const result = spawnSync(BIN, args, {
      cwd: workspace,
      env,
      encoding: 'utf8',
      maxBuffer: 128 * 1024 * 1024,
      timeout: timeoutSec * 1000,
    });

    const events = [];
    for (const line of (result.stdout || '').split('\n')) {
      if (!line.trim().startsWith('{')) continue;
      try {
        events.push(JSON.parse(line));
      } catch {
        /* non-event line: ignore */
      }
    }
    const text = events
      .filter((event) => event.type === 'text')
      .map((event) => event.part?.text || '')
      .join('');
    const toolCalls = events
      .filter((event) => event.type === 'tool_use')
      .map((event) => ({
        tool: event.part?.tool,
        status: event.part?.state?.status,
        input: event.part?.state?.input,
      }));
    const cost = events.reduce((sum, event) => sum + (event.type === 'step_finish' ? event.part?.cost || 0 : 0), 0);
    const tokens = events.reduce(
      (acc, event) => {
        if (event.type !== 'step_finish') return acc;
        const usage = event.part?.tokens || {};
        acc.input += usage.input || 0;
        acc.output += usage.output || 0;
        acc.reasoning += usage.reasoning || 0;
        return acc;
      },
      { input: 0, output: 0, reasoning: 0 },
    );

    const after = snapshot(workspace);
    const changed = [];
    for (const [file, hash] of after) if (!before.has(file) || before.get(file) !== hash) changed.push(file);
    for (const file of before.keys()) if (!after.has(file)) changed.push(file);
    changed.sort();

    const excerpts = changed.slice(0, 12).map((file) => {
      try {
        return { file, body: fs.readFileSync(path.join(workspace, file), 'utf8').slice(0, 8000) };
      } catch {
        return { file, body: '(deleted or binary)' };
      }
    });

    const durationMs = Date.now() - started;
    const metadata = {
      caseId: id,
      exitCode: result.status,
      signal: result.signal,
      timedOut: result.signal === 'SIGTERM' && result.status === null,
      durationMs,
      model,
      opencode: BIN,
      version: OPENCODE_VERSION,
      build: process.env.EVAL_BUILD || 'working-tree',
      dataHome: process.env.OPENCODE_DATA_HOME || '(inherited)',
      skills: sources,
      workingDir: workspace,
      configHome,
      changedFiles: changed,
      toolCalls,
      stderr: (result.stderr || '').slice(-4000),
    };

    const trace = writeTrace(id, result.stdout, result.stderr, metadata, excerpts);
    metadata.trace = trace;

    return {
      output: text || '(no final text)',
      error:
        result.status === 0
          ? undefined
          : `opencode exited ${result.status}${result.signal ? ` (${result.signal})` : ''}: ${(result.stderr || '').slice(-800)}`,
      cost,
      tokenUsage: { total: tokens.input + tokens.output, prompt: tokens.input, completion: tokens.output },
      metadata,
    };
  }
}
