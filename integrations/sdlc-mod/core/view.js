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

export function authorityText(authority) {
  const read = Array.isArray(authority?.read) && authority.read.length ? authority.read.join(", ") : "—";
  const write = Array.isArray(authority?.write) && authority.write.length ? authority.write.join(", ") : "—";
  const flag = (value) => (value ? "yes" : "no");
  return {
    read,
    write,
    flags: `publish ${flag(authority?.publish)} · implement ${flag(authority?.implement)} · deploy ${flag(authority?.deploy)}`,
  };
}
