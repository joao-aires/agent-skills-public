import assert from "node:assert/strict";
import test from "node:test";
import { emptyState, renderMarkdown } from "./state.js";
import { parseCommand, runCommand } from "./commands.js";

test("parses a quoted thread name, phase, type and stopping point", () => {
  let state = emptyState();
  const result = runCommand('thread add "pagination works" implementation backend "pagination works"', state);
  state = result.state;
  assert.equal(state.threads[0].name, "pagination works");
  assert.equal(state.threads[0].activity, "implementation");
  assert.equal(state.threads[0].softwareType, "backend");
  assert.equal(state.threads[0].stoppingPoint, "pagination works");
});

test("focuses, moves a thread, links tickets and artifacts, and renders state", () => {
  let state = emptyState();
  state = runCommand('thread add "pagination works" implementation backend', state).state;
  state = runCommand('thread add "API contract" design frontend', state).state;
  state = runCommand("focus T2", state).state;
  state = runCommand("thread phase T1 testing", state).state;
  state = runCommand("thread ticket T1 PROJ-142", state).state;
  state = runCommand("thread artifact T1 api-contract.md https://example.com/api", state).state;
  state = runCommand('decision add user "accept the seam"', state).state;
  state = runCommand("decision thread D1 T1", state).state;
  assert.equal(state.focusThreadId, "T2");
  assert.equal(state.threads[0].activity, "testing");
  assert.equal(state.threads[0].ticket, "PROJ-142");
  assert.equal(state.threads[0].artifacts[0].kind, "url");
  assert.equal(state.decisions[0].threadId, "T1");

  const shown = runCommand("state", state);
  assert.match(shown.markdown, /Focus: T2 — API contract/);
  assert.match(renderMarkdown(state), /D1 — open — user — accept the seam — T1/);
});

test("parses auto and read commands without applying them", () => {
  assert.deepEqual(parseCommand("auto off"), { kind: "auto", enabled: false });
  assert.deepEqual(parseCommand("auto on"), { kind: "auto", enabled: true });
  assert.equal(parseCommand("state").kind, "read");
  assert.throws(() => parseCommand("auto maybe"), /auto needs on or off/);
});

test("keeps manual additions marked as manual", () => {
  const state = runCommand('thread add "pagination works" implementation', emptyState()).state;
  assert.equal(state.threads[0].source, "manual");
});

test("the state command returns the same object so adapters can skip writes", () => {
  const state = emptyState();
  assert.equal(runCommand("state", state).state, state);
  assert.equal(runCommand("", state).state, state);
});

test("rejects an unknown command", () => {
  assert.throws(() => runCommand("nope", emptyState()), /unknown command/);
});
