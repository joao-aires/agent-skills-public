/**
 * Local, session-scoped SDLC engagement state.
 *
 * This is a working cache for the current conversation. It is not the
 * durable ECR, and it never grants authority.
 */

export const THREAD_STATUSES = ["waiting", "blocked", "parked", "done"];
export const DECISION_STATUSES = ["open", "accepted", "superseded", "rejected"];
export const ACTIVITIES = ["requirements", "design", "implementation", "testing", "operations"];

export function emptyState(sessionId = null) {
  return {
    version: 2,
    sessionId,
    focusThreadId: null,
    threads: [],
    decisions: [],
  };
}

function clone(value) {
  return JSON.parse(JSON.stringify(value));
}

function nextId(prefix, items) {
  let max = 0;
  for (const item of items) {
    const match = new RegExp(`^${prefix}(\\d+)$`).exec(item.id);
    if (match) max = Math.max(max, Number(match[1]));
  }
  return `${prefix}${max + 1}`;
}

function requireString(value, name) {
  if (typeof value !== "string" || value.trim() === "") {
    throw new Error(`${name} must be a non-empty string`);
  }
  return value.trim();
}

function requireActivity(value) {
  const activity = requireString(value, "activity");
  if (!ACTIVITIES.includes(activity)) {
    throw new Error(`activity must be one of ${ACTIVITIES.join(", ")}`);
  }
  return activity;
}

function optionalString(value, name) {
  if (value === undefined || value === null || value === "") return null;
  return requireString(value, name);
}

function requireArtifacts(value) {
  if (value === undefined || value === null) return [];
  if (!Array.isArray(value)) throw new Error("artifacts must be an array");
  return value.map((artifact) => {
    if (!artifact || typeof artifact !== "object") throw new Error("artifact must be an object");
    return {
      label: requireString(artifact.label, "artifact label"),
      href: requireString(artifact.href, "artifact href"),
      kind: artifact.kind === "url" ? "url" : "file",
    };
  });
}

function findThread(state, id) {
  const thread = state.threads.find((item) => item.id === id);
  if (!thread) throw new Error(`unknown thread ${id}`);
  return thread;
}

function findDecision(state, id) {
  const decision = state.decisions.find((item) => item.id === id);
  if (!decision) throw new Error(`unknown decision ${id}`);
  return decision;
}

function validArtifacts(artifacts) {
  return (
    Array.isArray(artifacts) &&
    artifacts.every(
      (artifact) =>
        artifact &&
        typeof artifact.label === "string" &&
        artifact.label.trim() !== "" &&
        typeof artifact.href === "string" &&
        artifact.href.trim() !== "" &&
        (artifact.kind === "file" || artifact.kind === "url"),
    )
  );
}

export function validateState(state) {
  const errors = [];
  if (!state || typeof state !== "object") return ["state must be an object"];
  if (state.version !== 2) errors.push("version must be 2");
  if (!Array.isArray(state.threads)) errors.push("threads must be an array");
  if (!Array.isArray(state.decisions)) errors.push("decisions must be an array");

  const threadIds = new Set();
  for (const thread of state.threads ?? []) {
    if (!/^T\d+$/.test(thread.id)) errors.push(`invalid thread id ${thread.id}`);
    if (threadIds.has(thread.id)) errors.push(`duplicate thread id ${thread.id}`);
    threadIds.add(thread.id);
    if (typeof thread.name !== "string" || thread.name.trim() === "") errors.push(`thread ${thread.id} needs a name`);
    if (typeof thread.activity !== "string" || thread.activity.trim() === "") {
      errors.push(`thread ${thread.id} needs an activity`);
    }
    if (!THREAD_STATUSES.includes(thread.status)) errors.push(`invalid thread status ${thread.status}`);
    if (thread.ticket !== null && thread.ticket !== undefined && typeof thread.ticket !== "string") {
      errors.push(`thread ${thread.id} ticket must be a string`);
    }
    if (!validArtifacts(thread.artifacts)) errors.push(`thread ${thread.id} has invalid artifacts`);
  }
  if (state.focusThreadId && !threadIds.has(state.focusThreadId)) {
    errors.push(`focus thread ${state.focusThreadId} is not present`);
  }

  const decisionIds = new Set();
  for (const decision of state.decisions ?? []) {
    if (!/^D\d+$/.test(decision.id)) errors.push(`invalid decision id ${decision.id}`);
    if (decisionIds.has(decision.id)) errors.push(`duplicate decision id ${decision.id}`);
    decisionIds.add(decision.id);
    if (typeof decision.statement !== "string" || decision.statement.trim() === "") {
      errors.push(`decision ${decision.id} needs a statement`);
    }
    if (!DECISION_STATUSES.includes(decision.status)) {
      errors.push(`invalid decision status ${decision.status}`);
    }
    if (decision.threadId && !threadIds.has(decision.threadId)) {
      errors.push(`decision ${decision.id} references unknown thread ${decision.threadId}`);
    }
    if (!validArtifacts(decision.artifacts)) errors.push(`decision ${decision.id} has invalid artifacts`);
  }

  return errors;
}

function ensureValid(state) {
  const errors = validateState(state);
  if (errors.length) throw new Error(errors.join("; "));
}

/**
 * Apply one local command and return a new state. The input is not mutated.
 */
export function apply(previous, command) {
  ensureValid(previous);
  if (!command || typeof command !== "object") throw new Error("command must be an object");
  const state = clone(previous);
  const now = new Date().toISOString();
  const source = command.source === "inferred" ? "inferred" : "manual";

  switch (command.type) {
    case "thread.add": {
      const id = nextId("T", state.threads);
      const thread = {
        id,
        ticket: optionalString(command.ticket, "ticket"),
        name: requireString(command.name, "thread name"),
        activity: requireActivity(command.activity),
        softwareType: optionalString(command.softwareType, "softwareType"),
        stoppingPoint: optionalString(command.stoppingPoint, "stoppingPoint"),
        status: command.status ?? "waiting",
        artifacts: requireArtifacts(command.artifacts),
        owner: optionalString(command.owner, "owner"),
        source,
        updatedAt: now,
      };
      if (!THREAD_STATUSES.includes(thread.status)) throw new Error(`invalid thread status ${thread.status}`);
      state.threads.push(thread);
      if (!state.focusThreadId) state.focusThreadId = id;
      break;
    }
    case "thread.focus":
      state.focusThreadId = requireString(command.id, "thread id");
      findThread(state, state.focusThreadId);
      break;
    case "thread.status": {
      const thread = findThread(state, requireString(command.id, "thread id"));
      if (!THREAD_STATUSES.includes(command.status)) throw new Error(`invalid thread status ${command.status}`);
      thread.status = command.status;
      thread.updatedAt = now;
      break;
    }
    case "thread.phase": {
      const thread = findThread(state, requireString(command.id, "thread id"));
      thread.activity = requireActivity(command.activity);
      thread.updatedAt = now;
      break;
    }
    case "thread.ticket": {
      const thread = findThread(state, requireString(command.id, "thread id"));
      thread.ticket = requireString(command.ticket, "ticket");
      thread.updatedAt = now;
      break;
    }
    case "thread.artifact": {
      const thread = findThread(state, requireString(command.id, "thread id"));
      const artifact = requireArtifacts([command.artifact])[0];
      if (!thread.artifacts.some((item) => item.href === artifact.href)) thread.artifacts.push(artifact);
      thread.updatedAt = now;
      break;
    }
    case "thread.park": {
      const thread = findThread(state, requireString(command.id, "thread id"));
      thread.status = "parked";
      thread.parkReason = optionalString(command.reason, "reason");
      thread.updatedAt = now;
      break;
    }
    case "thread.resume": {
      const thread = findThread(state, requireString(command.id, "thread id"));
      thread.status = "waiting";
      thread.parkReason = null;
      thread.updatedAt = now;
      break;
    }
    case "thread.close": {
      const thread = findThread(state, requireString(command.id, "thread id"));
      thread.status = "done";
      thread.updatedAt = now;
      if (state.focusThreadId === thread.id) {
        state.focusThreadId = state.threads.find((item) => item.status !== "done")?.id ?? null;
      }
      break;
    }
    case "decision.add": {
      const id = nextId("D", state.decisions);
      if (command.threadId) findThread(state, command.threadId);
      state.decisions.push({
        id,
        statement: requireString(command.statement, "decision statement"),
        owner: optionalString(command.owner, "owner"),
        status: command.status ?? "open",
        threadId: optionalString(command.threadId, "thread id"),
        artifacts: requireArtifacts(command.artifacts),
        source,
        updatedAt: now,
      });
      if (!DECISION_STATUSES.includes(command.status ?? "open")) {
        throw new Error(`invalid decision status ${command.status}`);
      }
      break;
    }
    case "decision.resolve": {
      const decision = findDecision(state, requireString(command.id, "decision id"));
      decision.status = "accepted";
      decision.updatedAt = now;
      break;
    }
    case "decision.reopen": {
      const decision = findDecision(state, requireString(command.id, "decision id"));
      decision.status = "open";
      decision.updatedAt = now;
      break;
    }
    case "decision.thread": {
      const decision = findDecision(state, requireString(command.id, "decision id"));
      if (command.threadId) findThread(state, command.threadId);
      decision.threadId = optionalString(command.threadId, "thread id");
      decision.updatedAt = now;
      break;
    }
    case "decision.artifact": {
      const decision = findDecision(state, requireString(command.id, "decision id"));
      const artifact = requireArtifacts([command.artifact])[0];
      if (!decision.artifacts.some((item) => item.href === artifact.href)) decision.artifacts.push(artifact);
      decision.updatedAt = now;
      break;
    }
    case "reset":
      return emptyState(previous.sessionId);
    default:
      throw new Error(`unknown command ${command.type}`);
  }

  ensureValid(state);
  return state;
}

export function focusedThread(state) {
  const current = readable(state);
  return current.threads.find((thread) => thread.id === current.focusThreadId) ?? null;
}

/**
 * Renderers run against host-owned reactive stores. A store update can expose
 * the value while it is still being written, so rendering reads a completed
 * shape instead of assuming every collection is present.
 */
function readable(state) {
  const fallback = emptyState();
  if (!state || typeof state !== "object") return fallback;
  return {
    ...fallback,
    ...state,
    threads: Array.isArray(state.threads) ? state.threads : fallback.threads,
    decisions: Array.isArray(state.decisions) ? state.decisions : fallback.decisions,
  };
}

export function renderCompact(state) {
  const current = readable(state);
  const focus = focusedThread(current);
  const open = current.decisions.filter((decision) => decision.status === "open").length;
  const label = focus ? focus.name : "no focus";
  return `SDLC · ${label} · ${current.threads.length} thread${current.threads.length === 1 ? "" : "s"} · ${open} open`;
}

export function renderMarkdown(state) {
  const current = readable(state);
  const lines = ["## Engagement state", ""];
  const focus = focusedThread(current);
  lines.push(
    `Focus: ${focus ? `${focus.id} — ${focus.name} (${focus.activity}${focus.softwareType ? `, ${focus.softwareType}` : ""})` : "none"}`,
  );
  lines.push("", "Threads:");
  if (!current.threads.length) lines.push("- None");
  for (const thread of current.threads) {
    const marker = thread.id === current.focusThreadId ? "●" : thread.status === "parked" ? "○" : "◐";
    const ticket = thread.ticket ? ` [${thread.ticket}]` : "";
    const artifacts = thread.artifacts?.length ? ` — ${thread.artifacts.map((artifact) => artifact.label).join(", ")}` : "";
    lines.push(
      `- ${marker} ${thread.id}${ticket} — ${thread.name} — ${thread.activity}${thread.softwareType ? ` (${thread.softwareType})` : ""} — ${thread.status}${thread.stoppingPoint ? ` — ${thread.stoppingPoint}` : ""}${artifacts}`,
    );
  }
  lines.push("", "Decisions:");
  if (!current.decisions.length) lines.push("- None");
  for (const decision of current.decisions) {
    const thread = decision.threadId ? ` — ${decision.threadId}` : "";
    const artifacts = decision.artifacts?.length ? ` — ${decision.artifacts.map((artifact) => artifact.label).join(", ")}` : "";
    lines.push(
      `- ${decision.id} — ${decision.status} — ${decision.owner ?? "unowned"} — ${decision.statement}${thread}${artifacts}`,
    );
  }
  return lines.join("\n");
}
