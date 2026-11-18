import assert from "node:assert/strict";
import test from "node:test";
import { apply, emptyState, renderCompact, renderMarkdown, validateState } from "./state.js";

function sample() {
  let state = emptyState("s1");
  state = apply(state, {
    type: "thread.add",
    name: "pagination works",
    activity: "implementation",
    softwareType: "backend",
    ticket: "PROJ-142",
    stoppingPoint: "pagination works",
  });
  return state;
}

test("adds a named thread and focuses the first one", () => {
  const state = sample();
  assert.equal(state.version, 2);
  assert.equal(state.threads.length, 1);
  assert.equal(state.threads[0].name, "pagination works");
  assert.equal(state.threads[0].ticket, "PROJ-142");
  assert.equal(state.focusThreadId, "T1");
  assert.deepEqual(validateState(state), []);
});

test("moves a thread between phases and attaches a ticket", () => {
  let state = sample();
  state = apply(state, { type: "thread.phase", id: "T1", activity: "testing" });
  assert.equal(state.threads[0].activity, "testing");
  state = apply(state, { type: "thread.ticket", id: "T1", ticket: "PROJ-999" });
  assert.equal(state.threads[0].ticket, "PROJ-999");
});

test("attaches artifacts to threads and decisions", () => {
  let state = sample();
  state = apply(state, {
    type: "thread.artifact",
    id: "T1",
    artifact: { label: "api-contract.md", href: "file:///tmp/api-contract.md", kind: "file" },
  });
  state = apply(state, {
    type: "decision.add",
    statement: "reuse the search table",
    owner: "user",
    threadId: "T1",
  });
  state = apply(state, {
    type: "decision.artifact",
    id: "D1",
    artifact: { label: "PROJ-151", href: "https://linear.app/acme/issue/PROJ-151", kind: "url" },
  });
  assert.equal(state.threads[0].artifacts.length, 1);
  assert.equal(state.decisions[0].threadId, "T1");
  assert.equal(state.decisions[0].artifacts[0].kind, "url");
  assert.deepEqual(validateState(state), []);
});

test("switches focus and parks a thread", () => {
  let state = sample();
  state = apply(state, {
    type: "thread.add",
    name: "API contract",
    activity: "design",
    softwareType: "frontend",
  });
  state = apply(state, { type: "thread.focus", id: "T2" });
  assert.equal(state.focusThreadId, "T2");
  state = apply(state, { type: "thread.park", id: "T1", reason: "waiting on contract" });
  assert.equal(state.threads[0].status, "parked");
  assert.equal(state.threads[0].parkReason, "waiting on contract");
  state = apply(state, { type: "thread.resume", id: "T1" });
  assert.equal(state.threads[0].status, "waiting");
});

test("adds and resolves decisions", () => {
  let state = emptyState();
  state = apply(state, { type: "decision.add", statement: "use the existing search table", owner: "user" });
  assert.equal(state.decisions[0].id, "D1");
  assert.equal(state.decisions[0].status, "open");
  state = apply(state, { type: "decision.resolve", id: "D1" });
  assert.equal(state.decisions[0].status, "accepted");
});

test("renders compact and durable Markdown forms", () => {
  let state = sample();
  state = apply(state, { type: "decision.add", statement: "accept the seam", owner: "user", threadId: "T1" });
  assert.match(renderCompact(state), /SDLC · pagination works · 1 thread · 1 open/);
  const markdown = renderMarkdown(state);
  assert.match(markdown, /## Engagement state/);
  assert.match(markdown, /T1 \[PROJ-142\] — pagination works — implementation/);
  assert.match(markdown, /D1 — open — user — accept the seam — T1/);
});

test("rejects an unknown focus, invalid phase and unknown command", () => {
  const state = emptyState();
  assert.throws(() => apply(state, { type: "thread.focus", id: "T9" }), /unknown thread T9/);
  assert.throws(
    () => apply(state, { type: "thread.add", name: "work", activity: "backend" }),
    /activity must be one of/,
  );
  assert.throws(() => apply(state, { type: "unknown" }), /unknown command/);
});

test("renders partial or missing state without throwing", () => {
  assert.match(renderCompact(undefined), /no focus · 0 threads · 0 open/);
  assert.match(renderCompact({ focusThreadId: null }), /no focus/);
  assert.match(renderMarkdown({}), /Threads:\n- None/);
  assert.match(renderMarkdown({ threads: undefined, decisions: undefined }), /Decisions:\n- None/);
});

test("does not mutate the input state", () => {
  const state = emptyState();
  const next = apply(state, { type: "thread.add", name: "work", activity: "design" });
  assert.equal(state.threads.length, 0);
  assert.equal(next.threads.length, 1);
});
