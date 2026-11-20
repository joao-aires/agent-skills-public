#!/usr/bin/env node
/* Case lint: structure only. It never calls a model. */
import fs from 'node:fs';
import path from 'node:path';
import yaml from 'js-yaml';

const ROOT = path.resolve(new URL('..', import.meta.url).pathname);
const CASES = path.join(ROOT, 'cases');
const GATES = new Set(['pr', 'nightly', 'release']);
const STAGES = new Set(['setup', 'refine', 'design', 'implement', 'test', 'release', 'operations', 'cross-phase']);
const KINDS = new Set(['discovery', 'artifact', 'boundary', 'help', 'decision', 'journey', 'review', 'proposal']);
const errors = [];
const cases = [];

for (const name of fs.readdirSync(CASES).filter((entry) => entry.endsWith('.yaml')).sort()) {
  const file = path.join(CASES, name);
  let data;
  try {
    data = yaml.load(fs.readFileSync(file, 'utf8'));
  } catch (error) {
    errors.push(`${name}: invalid YAML: ${error.message}`);
    continue;
  }
  const where = `cases/${name}`;
  const id = data?.vars?.id;
  if (!id) errors.push(`${where}: vars.id is required`);
  const expectedName = `${id}.yaml`;
  if (id && expectedName !== name) errors.push(`${where}: file must be named ${expectedName}`);
  if (data?.description !== id) errors.push(`${where}: description must equal vars.id`);

  const meta = data?.metadata || {};
  if (!GATES.has(meta.gate)) errors.push(`${where}: invalid gate ${JSON.stringify(meta.gate)}`);
  if (!STAGES.has(meta.stage)) errors.push(`${where}: invalid stage ${JSON.stringify(meta.stage)}`);
  if (!KINDS.has(meta.kind)) errors.push(`${where}: invalid kind ${JSON.stringify(meta.kind)}`);

  if (!String(data?.vars?.prompt || '').trim()) errors.push(`${where}: vars.prompt is required`);
  const fixture = data?.vars?.fixture;
  if (!fixture || !fs.existsSync(path.join(ROOT, fixture))) errors.push(`${where}: fixture ${JSON.stringify(fixture)} does not exist`);

  const expect = data?.vars?.expect;
  const keys = expect && typeof expect === 'object' ? Object.keys(expect) : [];
  if (keys.length < 2 || keys.length > 4) errors.push(`${where}: expect must have 2-4 deterministic groups, got ${keys.length}`);
  if (!keys.some((key) => ['exit', 'files', 'json', 'commands', 'diff', 'tools', 'headings', 'links'].includes(key))) {
    errors.push(`${where}: expect needs an observable check (files, json, commands, diff, tools, headings or links)`);
  }
  if (data?.vars?.judge && !String(data.vars.judge.rubric || '').trim()) errors.push(`${where}: judge.rubric is required when judge is set`);
  const assertions = [].concat(data?.assert || []);
  if (!assertions.some((item) => item?.value === 'file://assertions/contract.mjs')) {
    errors.push(`${where}: must use assertions/contract.mjs`);
  }
  for (const bundle of String(data?.vars?.bundles || '').split(',').map((item) => item.trim()).filter(Boolean)) {
    if (!fs.existsSync(path.join(ROOT, '..', 'plugins', bundle, 'skills'))) errors.push(`${where}: unknown bundle ${bundle}`);
  }
  cases.push({ id, name, gate: meta.gate, stage: meta.stage, kind: meta.kind, file });
}

const ids = cases.map((item) => item.id).filter(Boolean);
for (const id of ids) {
  if (ids.indexOf(id) !== ids.lastIndexOf(id)) errors.push(`duplicate case id ${id}`);
}

const pr = cases.filter((item) => item.gate === 'pr');
if (cases.length > 60) errors.push(`suite has ${cases.length} cases; the cap is about 60`);
if (pr.length > 12) errors.push(`pr gate has ${pr.length} cases; the cap is 12`);
if (pr.length === 0) errors.push('pr gate needs at least one case');

const flowsPath = path.join(ROOT, 'flows.yaml');
if (!fs.existsSync(flowsPath)) {
  errors.push('flows.yaml is missing');
} else {
  const flows = yaml.load(fs.readFileSync(flowsPath, 'utf8'))?.flows || [];
  if (flows.length !== 8) errors.push(`flows.yaml must define 8 outcomes, got ${flows.length}`);
  const flowIds = new Set(flows.map((flow) => flow.id));
  if (flowIds.size !== flows.length) errors.push('flows.yaml has duplicate outcome ids');
  const mapped = new Set();
  for (const flow of flows) {
    if (!String(flow.outcome || '').trim()) errors.push(`flows.yaml ${flow.id}: outcome is required`);
    for (const id of [].concat(flow.cases || [])) {
      if (!ids.includes(id)) errors.push(`flows.yaml ${flow.id}: unknown case ${id}`);
      mapped.add(id);
    }
  }
  for (const id of ids) if (!mapped.has(id)) errors.push(`flows.yaml does not map case ${id}`);
}

if (errors.length) {
  console.error(`case lint failed (${errors.length}):`);
  for (const error of errors) console.error(`  - ${error}`);
  process.exit(1);
}
const byGate = (gate) => cases.filter((item) => item.gate === gate).length;
console.log(`case lint ok: ${cases.length} cases (pr ${byGate('pr')}, nightly ${byGate('nightly')}, release ${byGate('release')})`);
