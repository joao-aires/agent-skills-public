import assert from "node:assert/strict";
import test from "node:test";
import { emptyState } from "./state.js";
import {
  applyExtraction,
  buildExtractionPrompt,
  guardCommands,
  normaliseMessages,
  parseExtraction,
} from "./extract.js";

test("parses fenced and bare JSON extraction", () => {
  const fenced = '```json\n{"confidence":0.8,"commands":[{"type":"thread.add","activity":"design"}]}\n```';
  assert.deepEqual(parseExtraction(fenced).commands[0].activity, "design");
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

test("builds a prompt with state and recent transcript", () => {
  const state = emptyState();
  state.threads.push({ id: "T1", activity: "requirements", status: "waiting" });
  const prompt = buildExtractionPrompt({
    state,
    messages: [{ role: "user", text: "requirements are accepted" }],
    includeMessages: 4,
  });
  assert.match(prompt, /Current state:/);
  assert.match(prompt, /"id": "T1"/);
  assert.match(prompt, /USER: requirements are accepted/);
  assert.match(prompt, /Never set authority/);
});

test("guards unsupported and duplicate commands", () => {
  const state = emptyState();
  state.threads.push({ id: "T1", activity: "design", softwareType: "frontend", status: "waiting" });
  state.decisions.push({ id: "D1", statement: "Use the existing table", status: "accepted" });

  const guarded = guardCommands(
    [
      { type: "thread.add", activity: "design", softwareType: "frontend" },
      { type: "thread.add", activity: "design", softwareType: "frontend" },
      { type: "thread.add", activity: "implementation", softwareType: "frontend" },
      { type: "thread.focus", id: "T9" },
      { type: "thread.focus", id: "T1" },
      { type: "thread.close", id: "T1" },
      { type: "thread.status", id: "T1", status: "done" },
      { type: "thread.status", id: "T1", status: "blocked" },
      { type: "thread.park", id: "T1", reason: "waiting on the seam" },
      { type: "thread.resume", id: "T1" },
      { type: "decision.add", statement: "use the existing table." },
      { type: "decision.add", statement: "error copy owner" },
      { type: "decision.resolve", id: "D1" },
      { type: "authority.set", publish: true },
      { type: "reset" },
      { type: "transition.set", from: "design", to: "implementation" },
    ],
    state,
    { confidence: 0.9 },
  );

  assert.deepEqual(
    guarded.map((command) => command.type),
    ["thread.add", "thread.focus", "thread.status", "thread.park", "decision.add", "transition.set"],
  );
  assert.equal(guarded[0].source, "inferred");
  assert.equal(guarded[4].status, "open");
  assert.equal(guarded[4].source, "inferred");
});

test("drops every command below the confidence threshold", () => {
  const commands = [{ type: "thread.add", activity: "design" }];
  assert.deepEqual(guardCommands(commands, emptyState(), { confidence: 0.4, minConfidence: 0.7 }), []);
});

test("applies an extraction and marks inferred items", () => {
  const state = emptyState();
  const result = applyExtraction(
    state,
    {
      confidence: 0.9,
      commands: [
        { type: "thread.add", activity: "design", softwareType: "frontend", stoppingPoint: "design accepted" },
        { type: "decision.add", statement: "use the existing search table", owner: "user" },
        { type: "transition.set", from: "design", to: "implementation", needs: "seam accepted" },
      ],
    },
    { minConfidence: 0.7 },
  );

  assert.equal(result.applied.length, 3);
  assert.equal(result.rejected.length, 0);
  assert.equal(result.changed, true);
  assert.equal(result.state.threads[0].source, "inferred");
  assert.equal(result.state.decisions[0].status, "open");
  assert.equal(result.state.decisions[0].source, "inferred");
  assert.equal(result.state.nextTransition.to, "implementation");
  assert.equal(state.threads.length, 0, "input state must not be mutated");
});

test("is idempotent across repeated extractions", () => {
  const state = emptyState();
  const extraction = {
    confidence: 1,
    commands: [
      { type: "thread.add", activity: "design", softwareType: "frontend" },
      { type: "decision.add", statement: "use the existing table" },
    ],
  };

  const first = applyExtraction(state, extraction);
  assert.equal(first.applied.length, 2);
  const second = applyExtraction(first.state, extraction);
  assert.equal(second.applied.length, 0);
  assert.equal(second.changed, false);
});
