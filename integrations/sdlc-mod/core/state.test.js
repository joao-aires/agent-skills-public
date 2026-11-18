import assert from "node:assert/strict";
import test from "node:test";
import { apply, emptyState, renderCompact, renderMarkdown, validateState } from "./state.js";

test("adds threads and focuses the first one", () => {
  let state = emptyState("s1");
  state = apply(state, { type: "thread.add", activity: "design", softwareType: "frontend", stoppingPoint: "design accepted" });
  assert.equal(state.threads.length, 1);
  assert.equal(state.focusThreadId, "T1");
  assert.deepEqual(validateState(state), []);
});

test("switches focus and parks a thread", () => {
  let state = emptyState();
  state = apply(state, { type: "thread.add", activity: "design", softwareType: "frontend" });
  state = apply(state, { type: "thread.add", activity: "backend contract", softwareType: "backend" });
  state = apply(state, { type: "thread.focus", id: "T2" });
  assert.equal(state.focusThreadId, "T2");
  state = apply(state, { type: "thread.park", id: "T1", reason: "waiting on contract" });
  assert.equal(state.threads[0].status, "parked");
  assert.equal(state.threads[0].parkReason, "waiting on contract");
});

test("adds and resolves decisions", () => {
  let state = emptyState();
  state = apply(state, { type: "decision.add", statement: "use existing search table", owner: "user" });
  assert.equal(state.decisions[0].id, "D1");
  assert.equal(state.decisions[0].status, "open");
  state = apply(state, { type: "decision.resolve", id: "D1" });
  assert.equal(state.decisions[0].status, "accepted");
});

test("renders compact and durable Markdown forms", () => {
  let state = emptyState();
  state = apply(state, { type: "thread.add", activity: "design", softwareType: "frontend" });
  state = apply(state, { type: "decision.add", statement: "accept seam", owner: "user" });
  assert.match(renderCompact(state), /SDLC · design:frontend · 1 thread · 1 open/);
  const markdown = renderMarkdown(state);
  assert.match(markdown, /## Engagement state/);
  assert.match(markdown, /T1 — design — frontend/);
  assert.match(markdown, /D1 — open — user — accept seam/);
});

test("rejects an unknown focus and an invalid transition", () => {
  const state = emptyState();
  assert.throws(() => apply(state, { type: "thread.focus", id: "T9" }), /unknown thread T9/);
  assert.throws(() => apply(state, { type: "unknown" }), /unknown command/);
});

test("does not mutate the input state", () => {
  const state = emptyState();
  const next = apply(state, { type: "thread.add", activity: "test" });
  assert.equal(state.threads.length, 0);
  assert.equal(next.threads.length, 1);
});
