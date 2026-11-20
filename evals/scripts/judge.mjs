import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const runDir = process.argv[2];
const stub = process.argv.includes('--stub');
if (!runDir) {
  console.error('usage: node scripts/judge.mjs <run-dir> [--stub]');
  process.exit(0);
}
const recordPath = path.join(runDir, 'record.json');
if (!fs.existsSync(recordPath)) {
  console.error(`no record.json in ${runDir}`);
  process.exit(0);
}
const record = JSON.parse(fs.readFileSync(recordPath, 'utf8'));
const model = process.env.OPENCODE_JUDGE_MODEL || process.env.OPENCODE_MODEL || '';
let changed = false;

function excerpts(entry) {
  const trace = entry.trace;
  if (trace) {
    const dir = trace.replace(/\.jsonl$/, '.files');
    if (fs.existsSync(dir)) {
      return fs
        .readdirSync(dir)
        .slice(0, 8)
        .map((name) => `--- ${name.replaceAll('__', '/')} ---\n${fs.readFileSync(path.join(dir, name), 'utf8').slice(0, 8000)}`)
        .join('\n\n');
    }
  }
  return (entry.changed_files || [])
    .slice(0, 8)
    .map((file) => {
      try {
        return `--- ${file} ---\n${fs.readFileSync(path.join(entry.workspace, file), 'utf8').slice(0, 8000)}`;
      } catch {
        return `--- ${file} --- (deleted or unreadable)`;
      }
    })
    .join('\n\n');
}

for (const entry of record.cases) {
  if (!entry.judge) continue;
  if (stub) {
    entry.judge = { status: 'advisory', verdict: 'pass', reason: 'stub judge', model: 'stub' };
    changed = true;
    continue;
  }
  if (!model) {
    entry.judge = { status: 'unavailable', reason: 'no judge model configured', model: null };
    changed = true;
    continue;
  }
  const evidence = [
    `CASE: ${entry.id}`,
    `AGENT OUTPUT:\n${entry.output}`,
    `CHANGED FILES: ${(entry.changed_files || []).join(', ') || '(none)'}`,
    `CHANGED FILE CONTENTS (a file shown here exists; do not infer absence from this prompt):\n${excerpts(entry) || '(no changed files)'}`,
  ].join('\n\n');
  const prompt = `You are an advisory grader. You never decide whether a run passes and you never change a verdict.
Return one JSON object only: {"verdict":"pass|partial|fail","reason":"one sentence"}.
Judge only coherence, proportionality and rationale quality against the rubric. Deterministic checks own the pass/fail verdict.
If the evidence is insufficient, return "partial" and say what is missing. Do not guess.
Rubric: ${JSON.stringify(entry.judge.rubric || 'Was the requested work coherent and proportionate?')}

${evidence}`;
  const cwd = fs.mkdtempSync(path.join(os.tmpdir(), 'judge-'));
  const configHome = fs.mkdtempSync(path.join(os.tmpdir(), 'judge-config-'));
  fs.mkdirSync(path.join(configHome, 'opencode'), { recursive: true });
  fs.writeFileSync(path.join(configHome, 'opencode', 'opencode.json'), '{"$schema":"https://opencode.ai/config.json","permission":{"webfetch":"deny","websearch":"deny"}}');
  const proc = spawnSync(process.env.OPENCODE_BIN || 'opencode', ['run', '--standalone', '--archived', '--format', 'json', '-m', model, '--', prompt], {
    cwd,
    encoding: 'utf8',
    timeout: 120000,
    maxBuffer: 32 * 1024 * 1024,
    env: {
      ...process.env,
      PWD: cwd,
      XDG_CONFIG_HOME: configHome,
      ...(process.env.OPENCODE_DATA_HOME ? { XDG_DATA_HOME: process.env.OPENCODE_DATA_HOME } : {}),
    },
  });
  const text = (proc.stdout || '')
    .split('\n')
    .filter((line) => line.trim().startsWith('{'))
    .map((line) => {
      try {
        return JSON.parse(line);
      } catch {
        return null;
      }
    })
    .filter((event) => event?.type === 'text')
    .map((event) => event.part?.text || '')
    .join('');
  try {
    const parsed = JSON.parse(text.match(/\{[\s\S]*\}/)?.[0] || '');
    entry.judge = { status: 'advisory', ...parsed, model };
  } catch {
    entry.judge = { status: 'unavailable', reason: 'judge did not return JSON', model };
  }
  changed = true;
}
if (changed) fs.writeFileSync(recordPath, JSON.stringify(record, null, 2) + '\n');
// Advisory lane: judge failures never fail the command.
process.exit(0);
