import assert from "node:assert/strict";
import test from "node:test";
import { emptyState } from "./state.js";
import { decisionGlyph, matrixCell, matrixThreads, phaseMarker, summaryLabel, threadCode, threadGlyph } from "./view.js";

test("marks the focused thread and its lifecycle state", () => {
  assert.equal(threadGlyph({ status: "waiting" }, true), "●");
  assert.equal(threadGlyph({ status: "waiting" }, false), "◐");
  assert.equal(threadGlyph({ status: "parked" }, true), "○");
  assert.equal(threadGlyph({ status: "blocked" }, true), "!");
  assert.equal(threadGlyph({ status: "done" }, true), "✓");
  assert.equal(threadGlyph(null), "◐");
});

test("maps decision statuses to glyphs", () => {
  assert.equal(decisionGlyph("open"), "◐");
  assert.equal(decisionGlyph("accepted"), "✓");
  assert.equal(decisionGlyph("rejected"), "✗");
  assert.equal(decisionGlyph("superseded"), "⊘");
  assert.equal(decisionGlyph("unknown"), "◐");
});

test("summarises threads and open decisions", () => {
  const state = emptyState();
  assert.equal(summaryLabel(state), "0 threads · 0 open");
  state.threads.push({ id: "T1" });
  assert.equal(summaryLabel(state), "1 thread · 0 open");
  state.decisions.push({ id: "D1", status: "open" }, { id: "D2", status: "accepted" });
  assert.equal(summaryLabel(state), "1 thread · 1 open");
  assert.equal(summaryLabel(undefined), "0 threads · 0 open");
});

test("shows a local id plus the tracker id when present", () => {
  assert.equal(threadCode({ id: "T1", ticket: "PROJ-142" }), "T1 · PROJ-142");
  assert.equal(threadCode({ id: "T2", ticket: null }), "T2");
  assert.equal(threadCode(null), "");
});

test("fills a phase matrix cell from phase and status", () => {
  const thread = { id: "T1", activity: "implementation", status: "waiting" };
  assert.equal(matrixCell(thread, "requirements", "T1"), "✓");
  assert.equal(matrixCell(thread, "implementation", "T1"), "●");
  assert.equal(matrixCell({ ...thread, status: "blocked" }, "implementation", "T1"), "!");
  assert.equal(matrixCell({ ...thread, status: "parked" }, "implementation", "T1"), "○");
  assert.equal(matrixCell(thread, "testing", "T1"), "·");
  assert.equal(matrixCell(thread, "throughout", "T1"), "·");
});

test("marks previous, current and future phases", () => {
  assert.equal(phaseMarker("design", "implementation"), "✓");
  assert.equal(phaseMarker("implementation", "implementation"), "▶");
  assert.equal(phaseMarker("testing", "implementation"), "○");
  assert.equal(phaseMarker("testing", null), "○");
});

test("keeps matrix columns stable and includes the focus thread", () => {
  const threads = Array.from({ length: 5 }, (_, index) => ({
    id: `T${index + 1}`,
    activity: "design",
    status: "waiting",
  }));
  const state = { threads, focusThreadId: "T5" };
  const { shown, hidden } = matrixThreads(state, 4);
  assert.deepEqual(shown.map((thread) => thread.id), ["T1", "T2", "T3", "T5"]);
  assert.equal(hidden, 1);
});
