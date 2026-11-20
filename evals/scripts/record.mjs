import fs from 'node:fs';
import path from 'node:path';

const [rawPath, outDirArg] = process.argv.slice(2);
if (!rawPath) {
  console.error('usage: node scripts/record.mjs <promptfoo-output.json> [out-dir]');
  process.exit(2);
}
const raw = JSON.parse(fs.readFileSync(rawPath, 'utf8'));
const runId = raw.evalId || `run-${Date.now()}`;
const outDir = path.resolve(outDirArg || path.join('.runs', runId));
fs.mkdirSync(outDir, { recursive: true });

const results = raw.results?.results || [];
const cases = results.map((result) => {
  const vars = result.testCase?.vars || {};
  const testMeta = result.testCase?.metadata || {};
  const meta = result.response?.metadata || {};
  const rubric = vars.judge?.rubric;
  return {
    id: result.testCase?.description,
    gate: testMeta.gate || vars.gate,
    stage: testMeta.stage || vars.stage,
    kind: testMeta.kind || vars.kind,
    verdict: result.success ? 'pass' : result.error && !result.gradingResult ? 'error' : 'fail',
    score: result.score,
    reason: result.gradingResult?.reason || result.error || '',
    exit: meta.exitCode,
    duration_ms: result.latencyMs,
    cost_usd: result.cost || 0,
    tokens: result.tokenUsage?.total || 0,
    model: meta.model,
    version: meta.version,
    tools: [...new Set((meta.toolCalls || []).map((call) => call.tool))],
    changed_files: meta.changedFiles || [],
    workspace: meta.workingDir,
    trace: meta.trace || null,
    output: String(result.response?.output || '').slice(0, 3000),
    ...(rubric ? { judge: { status: 'not-run', rubric } } : {}),
  };
});

const record = {
  schema: 1,
  run: {
    id: runId,
    timestamp: raw.results?.timestamp || new Date().toISOString(),
    duration_ms: raw.results?.stats?.durationMs || 0,
    gate: process.env.EVAL_GATE || 'local',
  },
  subject: {
    opencode: process.env.OPENCODE_BIN || 'opencode',
    version: cases[0]?.version || 'unknown',
    model: process.env.OPENCODE_MODEL || 'opencode-go/deepseek-v4.1-flash',
    build: process.env.EVAL_BUILD || 'working-tree',
    data_home: process.env.OPENCODE_DATA_HOME ? 'seeded XDG_DATA_HOME' : 'inherited XDG_DATA_HOME',
    config: 'isolated XDG_CONFIG_HOME; only opencode/opencode.json; web and search denied',
  },
  totals: {
    pass: cases.filter((item) => item.verdict === 'pass').length,
    fail: cases.filter((item) => item.verdict === 'fail').length,
    error: cases.filter((item) => item.verdict === 'error').length,
    cost_usd: cases.reduce((sum, item) => sum + item.cost_usd, 0),
    tokens: cases.reduce((sum, item) => sum + item.tokens, 0),
  },
  cases,
};
fs.writeFileSync(path.join(outDir, 'record.json'), JSON.stringify(record, null, 2) + '\n');

const rows = cases
  .map(
    (item) =>
      `| ${item.id} | ${item.stage || '?'} | ${item.kind || '?'} | ${item.verdict} | ${item.tokens} | ${Math.round(item.duration_ms / 100) / 10}s | ${String(item.reason).replace(/\|/g, '\\|').slice(0, 110)} |`,
  )
  .join('\n');
const markdown = `# Eval run ${record.run.id}

- Started: ${record.run.timestamp}
- Gate: ${record.run.gate}
- Subject: \`${record.subject.model}\` on \`${record.subject.build}\`, OpenCode \`${record.subject.version}\`
- Data home: ${record.subject.data_home}
- Totals: ${record.totals.pass} pass, ${record.totals.fail} fail, ${record.totals.error} error; ${record.totals.tokens} tokens; $${record.totals.cost_usd.toFixed(3)}

| Case | Stage | Kind | Verdict | Tokens | Time | Reason |
| --- | --- | --- | --- | ---: | ---: | --- |
${rows}

Deterministic assertions carry the verdict. Judge output, when present, is advisory and does not change any result. Traces and changed-file excerpts are under \`traces/\`.
`;
fs.writeFileSync(path.join(outDir, 'summary.md'), markdown);
console.log(outDir);
