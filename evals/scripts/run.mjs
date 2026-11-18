import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';

const mode = process.argv[2];
const rest = process.argv.slice(3);
const stamp = new Date().toISOString().replace(/[:.]/g, '-');
const runDir = path.resolve('.runs', `${stamp}-${mode}`);
fs.mkdirSync(path.join(runDir, 'traces'), { recursive: true });

const gates = { case: null, pr: 'pr', ci: 'pr', nightly: 'nightly', full: null };
if (!(mode in gates)) {
  console.error('usage: node scripts/run.mjs <case|pr|ci|nightly|full> [--yes]');
  process.exit(2);
}

const filter = [];
if (mode === 'case') {
  const id = rest[0];
  if (!id) {
    console.error('usage: npm run eval:case -- <case-id>');
    process.exit(2);
  }
  filter.push('--filter-pattern', `^${id.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}$`);
} else if (gates[mode]) {
  filter.push('--filter-metadata', `gate=${gates[mode]}`);
} else if (mode === 'full' && (process.env.EVAL_FULL !== '1' || !rest.includes('--yes'))) {
  console.error('Refusing to run the full suite. Use EVAL_FULL=1 npm run eval:full -- --yes');
  process.exit(2);
}

const rawPath = path.join(runDir, 'raw.json');
const args = [
  'promptfoo',
  'eval',
  '-c',
  'promptfooconfig.yaml',
  '--no-cache',
  '--no-write',
  '--no-share',
  '--no-progress-bar',
  '--no-table',
  '--max-concurrency',
  String(process.env.EVAL_CONCURRENCY || 2),
  '--output',
  rawPath,
  ...filter,
];
const env = {
  ...process.env,
  EVAL_GATE: mode,
  EVAL_TRACE_DIR: path.join(runDir, 'traces'),
  EVAL_ROOT: process.cwd(),
};
const proc = spawnSync('npx', args, { stdio: 'inherit', env });

if (fs.existsSync(rawPath)) {
  const rec = spawnSync('node', ['scripts/record.mjs', rawPath, runDir], { stdio: 'inherit', env });
  if (rec.status !== 0) process.exit(rec.status || 2);
  if (process.env.EVAL_JUDGE === '1') {
    // Advisory only: the judge never changes this exit code.
    spawnSync('node', ['scripts/judge.mjs', runDir], { stdio: 'inherit', env });
  }
}

process.exit(proc.status ?? 2);
