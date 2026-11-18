import { ACTIVITIES } from "./state.js";

export const PHASES = ACTIVITIES;

/**
 * Pure display helpers shared by the host adapters.
 *
 * Glyphs, labels and one-line summaries live here so the JSX stays about
 * layout and the meaning of each state is covered by Node tests.
 */

export function threadGlyph(thread, isFocus = false) {
  if (!thread) return "◐";
  if (thread.status === "done") return "✓";
  if (thread.status === "blocked") return "!";
  if (thread.status === "parked") return "○";
  return isFocus ? "●" : "◐";
}

export function decisionGlyph(status) {
  if (status === "accepted") return "✓";
  if (status === "rejected") return "✗";
  if (status === "superseded") return "⊘";
  return "◐";
}

export function summaryLabel(state) {
  const threads = Array.isArray(state?.threads) ? state.threads.length : 0;
  const open = Array.isArray(state?.decisions)
    ? state.decisions.filter((decision) => decision.status === "open").length
    : 0;
  return `${threads} thread${threads === 1 ? "" : "s"} · ${open} open`;
}

export function threadCode(thread) {
  if (!thread) return "";
  return thread.ticket ? `${thread.id} · ${thread.ticket}` : thread.id;
}

export function phaseMarker(phase, focusActivity) {
  const index = PHASES.indexOf(phase);
  const focus = PHASES.indexOf(focusActivity);
  if (index === -1 || focus === -1) return "○";
  if (index < focus) return "✓";
  if (index === focus) return "▶";
  return "○";
}

export function matrixCell(thread, phase, focusThreadId) {
  if (!thread) return "·";
  const index = PHASES.indexOf(phase);
  const current = PHASES.indexOf(thread.activity);
  if (index === -1 || current === -1) return "·";
  if (index < current) return "✓";
  if (index > current) return "·";
  if (thread.status === "done") return "✓";
  if (thread.status === "blocked") return "!";
  if (thread.status === "parked") return "○";
  return thread.id === focusThreadId ? "●" : "◐";
}

/**
 * Stable column selection: id order, capped, with the focus thread included.
 */
export function matrixThreads(state, limit = 4) {
  const threads = Array.isArray(state?.threads) ? [...state.threads] : [];
  threads.sort((left, right) => left.id.localeCompare(right.id, undefined, { numeric: true }));
  const focus = threads.find((thread) => thread.id === state?.focusThreadId);
  let shown = threads.slice(0, limit);
  if (focus && !shown.includes(focus)) {
    shown = [...threads.slice(0, Math.max(0, limit - 1)), focus];
    shown.sort((left, right) => left.id.localeCompare(right.id, undefined, { numeric: true }));
  }
  return { shown, hidden: Math.max(0, threads.length - shown.length) };
}
