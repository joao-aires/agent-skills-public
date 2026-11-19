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
  const thread = { id: "T1", phase: "implementation", status: "waiting", completedPhases: ["requirements"] };
  assert.equal(matrixCell(thread, "requirements", "T1"), "✓");
  assert.equal(matrixCell(thread, "implementation", "T1"), "●");
  assert.equal(matrixCell({ ...thread, status: "blocked" }, "implementation", "T1"), "!");
  assert.equal(matrixCell({ ...thread, status: "parked" }, "implementation", "T1"), "○");
  assert.equal(matrixCell(thread, "testing", "T1"), "·");
  assert.equal(matrixCell(thread, "maintenance", "T1"), "·");
});

test("marks previous, current and future phases", () => {
  assert.equal(phaseMarker("design", "implementation", ["design"]), "✓");
  assert.equal(phaseMarker("design", "implementation"), "←");
  assert.equal(phaseMarker("implementation", "implementation"), "▶");
  assert.equal(phaseMarker("testing", "implementation"), "·");
  assert.equal(phaseMarker("testing", null), "·");
});

test("pages matrix columns without reordering around focus", () => {
  const threads = Array.from({ length: 5 }, (_, index) => ({
    id: `T${index + 1}`,
    phase: "design",
    status: "waiting",
  }));
  const state = { threads, focusThreadId: "T5" };
  const first = matrixThreads(state, 3, 0);
  assert.deepEqual(first.shown.map((thread) => thread.id), ["T1", "T2", "T3"]);
  assert.equal(first.pages, 2);
  const second = matrixThreads(state, 3, 1);
  assert.deepEqual(second.shown.map((thread) => thread.id), ["T4", "T5"]);
  assert.equal(second.page, 1);
  assert.equal(second.hidden, 3);
});

test("does not mark unreached phases as done", () => {
  const thread = { id: "T3", phase: "maintenance", status: "parked", completedPhases: [] };
  assert.equal(matrixCell(thread, "implementation", "T3"), "·");
  assert.equal(
    matrixCell({ ...thread, completedPhases: ["implementation"] }, "implementation", "T3"),
    "✓",
  );
});
