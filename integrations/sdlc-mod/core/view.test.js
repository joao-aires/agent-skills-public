import assert from "node:assert/strict";
import test from "node:test";
import { emptyState } from "./state.js";
import { authorityText, decisionGlyph, summaryLabel, threadGlyph } from "./view.js";

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

test("renders empty and populated authority", () => {
  const empty = authorityText(emptyState().authority);
  assert.deepEqual(empty, {
    read: "—",
    write: "—",
    flags: "publish no · implement no · deploy no",
  });

  const granted = authorityText({
    read: ["repo", "docs"],
    write: ["docs"],
    publish: true,
    implement: false,
    deploy: true,
  });
  assert.equal(granted.read, "repo, docs");
  assert.equal(granted.write, "docs");
  assert.equal(granted.flags, "publish yes · implement no · deploy yes");
});
