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

export function phaseMarker(phase, focusActivity, completedPhases = []) {
  const index = PHASES.indexOf(phase);
  const focus = PHASES.indexOf(focusActivity);
  if (index === -1 || focus === -1) return "·";
  if (index < focus) return completedPhases.includes(phase) ? "✓" : "←";
  if (index === focus) return "▶";
  return "·";
}

export function matrixCell(thread, phase, focusThreadId) {
  if (!thread) return "·";
  const index = PHASES.indexOf(phase);
  const current = PHASES.indexOf(thread.activity);
  if (index === -1 || current === -1) return "·";
  if (index < current) return thread.completedPhases?.includes(phase) ? "✓" : "·";
  if (index > current) return "·";
  if (thread.status === "done") return "✓";
  if (thread.status === "blocked") return "!";
  if (thread.status === "parked") return "○";
  return thread.id === focusThreadId ? "●" : "◐";
}

/**
 * Stable column paging: id order, capped. The focus block carries the focus
 * thread separately, so pages never reorder when focus changes.
 */
export function matrixThreads(state, limit = 4, page = 0) {
  const threads = Array.isArray(state?.threads) ? [...state.threads] : [];
  threads.sort((left, right) => left.id.localeCompare(right.id, undefined, { numeric: true }));
  const pages = Math.max(1, Math.ceil(threads.length / limit));
  const safePage = ((Number(page) || 0) % pages + pages) % pages;
  const shown = threads.slice(safePage * limit, safePage * limit + limit);
  return { shown, hidden: Math.max(0, threads.length - shown.length), page: safePage, pages };
}
