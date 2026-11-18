import assert from "node:assert/strict";
import test from "node:test";
import { apply, emptyState } from "./state.js";
import {
  applyExtraction,
  buildExtractionPrompt,
  guardCommands,
  normaliseMessages,
  parseExtraction,
  promptState,
} from "./extract.js";

test("parses fenced and bare JSON extraction", () => {
  const fenced = '```json\n{"confidence":0.8,"commands":[{"type":"thread.add","name":"work","activity":"design"}]}\n```';
  assert.equal(parseExtraction(fenced).commands[0].name, "work");
  assert.equal(parseExtraction('{"confidence":0.4,"commands":[]}').confidence, 0.4);
});

test("rejects malformed or out-of-range extraction", () => {
  assert.equal(parseExtraction("no json here"), null);
  assert.equal(parseExtraction('{"confidence":2,"commands":[]}'), null);
  assert.equal(parseExtraction('{"confidence":0.5}'), null);
  assert.equal(parseExtraction('{"confidence":"high","commands":[]}'), null);
  assert.equal(parseExtraction('{"confidence":0.5,"commands":"none"}'), null);
});

test("normalises host transcripts without reasoning blocks", () => {
  const messages = [
    { type: "user", text: "let's use the existing table" },
    {
      type: "assistant",
      content: [
        { type: "reasoning", text: "secret chain of thought" },
        { type: "text", text: "Accepted. Moving to design." },
        { type: "tool", name: "read" },
      ],
    },
    { type: "idle" },
  ];
  const normalised = normaliseMessages(messages);
  assert.equal(normalised.length, 2);
  assert.match(normalised[1].text, /Accepted/);
  assert.match(normalised[1].text, /\[tool read\]/);
  assert.doesNotMatch(normalised[1].text, /secret/);
});

test("builds a prompt with state, hints and recent transcript", () => {
  const state = emptyState();
  state.threads.push({ id: "T1", name: "pagination works", activity: "implementation", status: "waiting", artifacts: [] });
  const prompt = buildExtractionPrompt({
    state,
    messages: [{ role: "user", text: "pagination is moving to testing" }],
    includeMessages: 4,
    hints: "activity=testing",
  });
  assert.match(prompt, /Current state:/);
  assert.match(prompt, /"name": "pagination works"/);
  assert.match(prompt, /Decision model hints/);
  assert.match(prompt, /USER: pagination is moving to testing/);
  assert.match(prompt, /Never resolve or reopen decisions/);
});

test("guards unsupported and duplicate commands", () => {
  let state = emptyState();
  state = apply(state, { type: "thread.add", name: "pagination works", activity: "implementation" });
  state = apply(state, { type: "thread.add", name: "API contract", activity: "design" });
  state = apply(state, { type: "decision.add", statement: "Use the existing table", status: "accepted" });

  const guarded = guardCommands(
    [
      { type: "thread.add", name: "pagination works", activity: "design" },
      { type: "thread.add", name: "settings panel", activity: "design" },
      { type: "thread.add", name: "bad activity", activity: "backend" },
      { type: "thread.focus", id: "T9" },
      { type: "thread.focus", id: "T2" },
      { type: "thread.phase", id: "T1", activity: "testing" },
      { type: "thread.status", id: "T1", status: "done" },
      { type: "thread.status", id: "T1", status: "blocked" },
      { type: "thread.park", id: "T1", reason: "waiting on the seam" },
      { type: "thread.resume", id: "T1" },
      { type: "decision.add", statement: "use the existing table." },
      { type: "decision.add", statement: "error copy owner", threadId: "T1" },
      { type: "decision.add", statement: "orphan decision", threadId: "T9" },
      { type: "decision.resolve", id: "D1" },
      { type: "authority.set", publish: true },
      { type: "reset" },
    ],
    state,
    { confidence: 0.9 },
  );

  assert.deepEqual(
    guarded.map((command) => command.type),
    ["thread.add", "thread.focus", "thread.phase", "thread.status", "thread.park", "decision.add"],
  );
  assert.equal(guarded[0].source, "inferred");
  assert.equal(guarded[5].status, "open");
  assert.equal(guarded[5].threadId, "T1");
  assert.equal(guarded[5].source, "inferred");
});

test("drops every command below the confidence threshold", () => {
  const commands = [{ type: "thread.add", name: "work", activity: "design" }];
  assert.deepEqual(guardCommands(commands, emptyState(), { confidence: 0.4, minConfidence: 0.7 }), []);
});

test("applies an extraction and marks inferred items", () => {
  const state = emptyState();
  const result = applyExtraction(
    state,
    {
      confidence: 0.9,
      commands: [
        { type: "thread.add", name: "pagination works", activity: "implementation", softwareType: "backend" },
        { type: "decision.add", statement: "use the existing search table", owner: "user" },
      ],
    },
    { minConfidence: 0.7 },
  );

  assert.equal(result.applied.length, 2);
  assert.equal(result.rejected.length, 0);
  assert.equal(result.changed, true);
  assert.equal(result.state.threads[0].source, "inferred");
  assert.equal(result.state.threads[0].name, "pagination works");
  assert.equal(result.state.decisions[0].status, "open");
  assert.equal(result.state.decisions[0].source, "inferred");
  assert.equal(result.state.decisions[0].threadId, null);
  assert.equal(state.threads.length, 0, "input state must not be mutated");
});

test("is idempotent across repeated extractions", () => {
  const state = emptyState();
  const extraction = {
    confidence: 1,
    commands: [
      { type: "thread.add", name: "pagination works", activity: "implementation" },
      { type: "decision.add", statement: "use the existing table" },
    ],
  };

  const first = applyExtraction(state, extraction);
  assert.equal(first.applied.length, 2);
  const second = applyExtraction(first.state, extraction);
  assert.equal(second.applied.length, 0);
  assert.equal(second.changed, false);
});

test("redacts artifact hrefs from prompt state", () => {
  const state = emptyState();
  state.threads.push({
    id: "T1",
    name: "pagination works",
    activity: "implementation",
    status: "waiting",
    completedPhases: [],
    artifacts: [{ label: "api-contract.md", href: "file:///Users/me/secret/api-contract.md", kind: "file" }],
  });
  const prompt = buildExtractionPrompt({
    state,
    messages: [{ role: "user", text: "move it" }],
  });
  assert.match(prompt, /api-contract\.md/);
  assert.doesNotMatch(prompt, /Users\/me\/secret/);
  assert.doesNotMatch(prompt, /file:\/\//);
  assert.equal(promptState(state).threads[0].artifacts[0].href, undefined);
});
