import assert from "node:assert/strict";
import test from "node:test";
import { emptyState, renderMarkdown } from "./state.js";
import { runCommand, parseCommand } from "./commands.js";

test("parses quoted activity and stopping point", () => {
  let state = emptyState();
  let result = runCommand('thread add "backend contract" backend "seam accepted"', state);
  state = result.state;
  assert.equal(state.threads[0].activity, "backend contract");
  assert.equal(state.threads[0].stoppingPoint, "seam accepted");
});

test("focuses, adds a decision, and renders state", () => {
  let state = emptyState();
  state = runCommand("thread add design frontend", state).state;
  state = runCommand("thread add backend backend", state).state;
  state = runCommand("focus T2", state).state;
  state = runCommand('decision add user "accept the seam"', state).state;
  assert.equal(state.focusThreadId, "T2");
  assert.match(renderMarkdown(state), /D1 — open — user — accept the seam/);
  const shown = runCommand("state", state);
  assert.match(shown.markdown, /Focus: T2/);
});

test("the state command returns the same object so adapters can skip writes", () => {
  const state = emptyState();
  assert.equal(runCommand("state", state).state, state);
  assert.equal(runCommand("", state).state, state);
});

test("parses auto and read commands without applying them", () => {
  assert.deepEqual(parseCommand("auto off"), { kind: "auto", enabled: false });
  assert.deepEqual(parseCommand("auto on"), { kind: "auto", enabled: true });
  assert.equal(parseCommand("state").kind, "read");
  assert.throws(() => parseCommand("auto maybe"), /auto needs on or off/);
});

test("keeps manual additions marked as manual", () => {
  const state = runCommand("thread add design frontend", emptyState()).state;
  assert.equal(state.threads[0].source, "manual");
});

test("rejects an unknown command", () => {
  assert.throws(() => runCommand("nope", emptyState()), /unknown command/);
});
