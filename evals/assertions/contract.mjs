import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';

const EVALS_ROOT = path.resolve(new URL('..', import.meta.url).pathname);

function matchesPrefix(file, allowed) {
  return [].concat(allowed).some((entry) => {
    if (entry.endsWith('/**')) return file.startsWith(entry.slice(0, -3));
    if (entry.endsWith('/')) return file.startsWith(entry);
    if (entry.includes('*')) {
      const pattern = new RegExp(`^${entry.split('*').map((part) => part.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('.*')}$`);
      return pattern.test(file);
    }
    return file === entry;
  });
}

function pick(object, dotted) {
  return dotted.split('.').reduce((value, key) => (value == null ? undefined : value[key]), object);
}

function readJson(file) {
  try {
    return JSON.parse(fs.readFileSync(file, 'utf8'));
  } catch {
    return undefined;
  }
}

export default function contract(output, context) {
  const expected = context?.vars?.expect || {};
  const meta = context?.providerResponse?.metadata || {};
  const checks = [];
  const check = (name, pass, detail = '') => checks.push({ name, pass, detail });

  if (expected.exit !== undefined) {
    check('exit code', meta.exitCode === expected.exit, `expected ${expected.exit}, got ${meta.exitCode}`);
  }

  for (const needle of [].concat(expected.output_contains || [])) {
    check(`output contains ${JSON.stringify(needle)}`, String(output).includes(needle));
  }
  if (expected.output_contains_any) {
    const needles = [].concat(expected.output_contains_any);
    check(`output contains one of ${JSON.stringify(needles)}`, needles.some((needle) => String(output).includes(needle)));
  }
  for (const needle of [].concat(expected.output_not_contains || [])) {
    check(`output excludes ${JSON.stringify(needle)}`, !String(output).includes(needle));
  }
  if (expected.output_matches) {
    check(`output matches /${expected.output_matches}/i`, new RegExp(expected.output_matches, 'i').test(String(output)));
  }

  const workspace = meta.workingDir;
  const read = (file) => {
    try {
      return fs.readFileSync(path.join(workspace, file), 'utf8');
    } catch {
      return null;
    }
  };
  const files = expected.files || {};
  for (const file of [].concat(files.present || [])) check(`${file} exists`, read(file) !== null);
  for (const file of [].concat(files.absent || [])) check(`${file} absent`, read(file) === null);
  for (const [file, want] of Object.entries(files.content || {})) {
    const got = read(file);
    check(`${file} content`, got !== null && got.trim() === String(want).trim(), got === null ? 'missing' : 'content differs');
  }
  for (const [file, needles] of Object.entries(files.contains || {})) {
    const got = read(file) || '';
    for (const needle of [].concat(needles)) {
      check(`${file} contains ${JSON.stringify(needle)}`, got.toLowerCase().includes(String(needle).toLowerCase()));
    }
  }
  for (const [file, needles] of Object.entries(files.not_contains || {})) {
    const got = read(file) || '';
    for (const needle of [].concat(needles)) {
      check(`${file} excludes ${JSON.stringify(needle)}`, !got.toLowerCase().includes(String(needle).toLowerCase()));
    }
  }
  for (const [file, headings] of Object.entries(expected.headings || {})) {
    const got = read(file) || '';
    for (const heading of [].concat(headings)) {
      check(
        `${file} has heading ${JSON.stringify(heading)}`,
        new RegExp(`^#{1,6}\\s+${heading.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}`, 'im').test(got),
      );
    }
  }
  for (const [file, names] of Object.entries(files.one_per_line || {})) {
    const lines = (read(file) || '')
      .split('\n')
      .map((line) => line.trim().replace(/^[-*]\s+/, '').toLowerCase())
      .filter(Boolean);
    for (const name of [].concat(names)) {
      check(`${file} lists ${name} exactly once`, lines.filter((line) => line === name.toLowerCase()).length === 1);
    }
    const duplicates = lines.filter((line, index) => lines.indexOf(line) !== index);
    check(`${file} has no duplicate lines`, duplicates.length === 0, duplicates.join(', '));
  }
  for (const [file, links] of Object.entries(expected.links || {})) {
    const got = read(file) || '';
    for (const link of [].concat(links)) {
      const external = /^https?:/.test(link);
      const resolved = external ? got.includes(link) : fs.existsSync(path.join(workspace, path.dirname(file), link));
      check(`${file} links ${link}`, got.includes(link) && resolved);
    }
  }

  for (const [file, spec] of Object.entries(expected.json || {})) {
    const document = readJson(path.join(workspace, file));
    check(`${file} parses as JSON`, document !== undefined);
    if (document === undefined) continue;
    for (const [dotted, want] of Object.entries(spec)) {
      const got = pick(document, dotted);
      if (want && typeof want === 'object' && 'not_equals' in want) {
        check(`${file} ${dotted} != ${JSON.stringify(want.not_equals)}`, got !== want.not_equals, `got ${JSON.stringify(got)}`);
      } else if (want && typeof want === 'object' && 'contains' in want) {
        check(
          `${file} ${dotted} contains ${JSON.stringify(want.contains)}`,
          String(got ?? '').toLowerCase().includes(String(want.contains).toLowerCase()),
          `got ${JSON.stringify(got)}`,
        );
      } else {
        check(`${file} ${dotted} == ${JSON.stringify(want)}`, got === want, `got ${JSON.stringify(got)}`);
      }
    }
  }

  for (const spec of [].concat(expected.commands || [])) {
    for (const copy of [].concat(spec.copy || [])) {
      const from = path.resolve(EVALS_ROOT, copy.from);
      const to = path.join(workspace, copy.to);
      fs.mkdirSync(path.dirname(to), { recursive: true });
      fs.copyFileSync(from, to);
    }
    const proc = spawnSync('bash', ['-lc', spec.run], {
      cwd: workspace,
      encoding: 'utf8',
      timeout: Number(spec.timeout_sec || 120) * 1000,
      maxBuffer: 32 * 1024 * 1024,
    });
    const wantExit = spec.exit === undefined ? 0 : spec.exit;
    check(
      `command ${JSON.stringify(spec.run)} exit`,
      proc.status === wantExit,
      `expected ${wantExit}, got ${proc.status}: ${(proc.stderr || '').slice(-300)}`,
    );
    for (const needle of [].concat(spec.stdout_contains || [])) {
      check(`command ${JSON.stringify(spec.run)} output contains ${JSON.stringify(needle)}`, String(proc.stdout || '').includes(needle));
    }
    for (const needle of [].concat(spec.stderr_contains || [])) {
      check(`command ${JSON.stringify(spec.run)} stderr contains ${JSON.stringify(needle)}`, String(proc.stderr || '').includes(needle));
    }
  }

  const tools = expected.tools || {};
  const used = (meta.toolCalls || []).map((call) => call.tool);
  for (const tool of [].concat(tools.used || [])) check(`tool ${tool} used`, used.includes(tool));
  for (const tool of [].concat(tools.not_used || [])) check(`tool ${tool} not used`, !used.includes(tool));

  const diff = expected.diff || {};
  const changed = meta.changedFiles || [];
  if (diff.max_files !== undefined) check('diff file count', changed.length <= diff.max_files, `${changed.length} > ${diff.max_files}`);
  if (diff.allowed) {
    const outside = changed.filter((file) => !matchesPrefix(file, diff.allowed));
    check('diff scope', outside.length === 0, `outside scope: ${outside.join(', ')}`);
  }
  if (diff.forbidden) {
    const hit = changed.filter((file) => matchesPrefix(file, diff.forbidden));
    check('diff forbidden paths', hit.length === 0, `touched: ${hit.join(', ')}`);
  }

  if (expected.max_cost !== undefined) check('cost', (context.providerResponse.cost || 0) <= expected.max_cost);
  if (expected.max_total_tokens !== undefined) {
    check('tokens', (context.providerResponse.tokenUsage?.total || 0) <= expected.max_total_tokens);
  }
  if (expected.max_duration_ms !== undefined) check('duration', (meta.durationMs || 0) <= expected.max_duration_ms);
  if (!checks.length) check('no assertions configured', false);

  const failures = checks.filter((item) => !item.pass);
  return {
    pass: failures.length === 0,
    score: failures.length === 0 ? 1 : 0,
    reason:
      failures.length === 0
        ? `${checks.length} deterministic checks passed`
        : failures.map((item) => `${item.name}${item.detail ? ` (${item.detail})` : ''}`).join('; '),
    componentResults: checks.map((item) => ({
      pass: item.pass,
      score: item.pass ? 1 : 0,
      reason: `${item.name}${item.detail ? `: ${item.detail}` : ''}`,
    })),
  };
}
