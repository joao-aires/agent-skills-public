/**
 * Local, session-scoped SDLC engagement state.
 *
 * This is a working cache for the current conversation. It is not the
 * durable ECR, and it never grants authority.
 */

export const THREAD_STATUSES = ["current", "waiting", "blocked", "parked", "done"];
export const DECISION_STATUSES = ["open", "accepted", "superseded", "rejected"];

export function emptyState(sessionId = null) {
  return {
    version: 1,
    sessionId,
    focusThreadId: null,
    threads: [],
    decisions: [],
    nextTransition: null,
    authority: {
      read: [],
      write: [],
      publish: false,
      implement: false,
      deploy: false,
    },
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

export function validateState(state) {
  const errors = [];
  if (!state || typeof state !== "object") return ["state must be an object"];
  if (state.version !== 1) errors.push("version must be 1");
  if (!Array.isArray(state.threads)) errors.push("threads must be an array");
  if (!Array.isArray(state.decisions)) errors.push("decisions must be an array");
  const threadIds = new Set();
  for (const thread of state.threads ?? []) {
    if (!/^T\d+$/.test(thread.id)) errors.push(`invalid thread id ${thread.id}`);
    if (threadIds.has(thread.id)) errors.push(`duplicate thread id ${thread.id}`);
    threadIds.add(thread.id);
    if (!THREAD_STATUSES.includes(thread.status)) {
      errors.push(`invalid thread status ${thread.status}`);
    }
    if (!thread.activity) errors.push(`thread ${thread.id} needs an activity`);
  }
  if (state.focusThreadId && !threadIds.has(state.focusThreadId)) {
    errors.push(`focus thread ${state.focusThreadId} is not present`);
  }
  const decisionIds = new Set();
  for (const decision of state.decisions ?? []) {
    if (!/^D\d+$/.test(decision.id)) errors.push(`invalid decision id ${decision.id}`);
    if (decisionIds.has(decision.id)) errors.push(`duplicate decision id ${decision.id}`);
    decisionIds.add(decision.id);
    if (!DECISION_STATUSES.includes(decision.status)) {
      errors.push(`invalid decision status ${decision.status}`);
    }
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

  switch (command.type) {
    case "thread.add": {
      const id = nextId("T", state.threads);
      const thread = {
        id,
        activity: requireString(command.activity, "activity"),
        softwareType: command.softwareType ? requireString(command.softwareType, "softwareType") : null,
        stoppingPoint: command.stoppingPoint ? requireString(command.stoppingPoint, "stoppingPoint") : null,
        status: command.status ?? "waiting",
        owner: command.owner ?? null,
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
    case "thread.park": {
      const thread = findThread(state, requireString(command.id, "thread id"));
      thread.status = "parked";
      thread.parkReason = command.reason ? requireString(command.reason, "reason") : null;
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
      state.decisions.push({
        id,
        statement: requireString(command.statement, "decision statement"),
        owner: command.owner ? requireString(command.owner, "owner") : null,
        status: command.status ?? "open",
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
    case "transition.set":
      state.nextTransition = {
        from: command.from ? requireString(command.from, "from") : null,
        to: command.to ? requireString(command.to, "to") : null,
        needs: command.needs ? requireString(command.needs, "needs") : null,
      };
      break;
    case "authority.set":
      state.authority = {
        read: Array.isArray(command.read) ? command.read.map(String) : state.authority.read,
        write: Array.isArray(command.write) ? command.write.map(String) : state.authority.write,
        publish: Boolean(command.publish ?? state.authority.publish),
        implement: Boolean(command.implement ?? state.authority.implement),
        deploy: Boolean(command.deploy ?? state.authority.deploy),
      };
      break;
    case "reset":
      return emptyState(previous.sessionId);
    default:
      throw new Error(`unknown command ${command.type}`);
  }

  ensureValid(state);
  return state;
}

/**
 * Renderers run against host-owned reactive stores. A store update can expose
 * the value while it is still being written, so rendering reads a completed
 * shape instead of assuming every collection is present.
 */
function readable(state) {
  const fallback = emptyState();
  if (!state || typeof state !== "object") return fallback;
  const authority = state.authority && typeof state.authority === "object" ? state.authority : {};
  return {
    ...fallback,
    ...state,
    threads: Array.isArray(state.threads) ? state.threads : fallback.threads,
    decisions: Array.isArray(state.decisions) ? state.decisions : fallback.decisions,
    authority: {
      read: Array.isArray(authority.read) ? authority.read : fallback.authority.read,
      write: Array.isArray(authority.write) ? authority.write : fallback.authority.write,
      publish: Boolean(authority.publish),
      implement: Boolean(authority.implement),
      deploy: Boolean(authority.deploy),
    },
  };
}

export function focusedThread(state) {
  const current = readable(state);
  return current.threads.find((thread) => thread.id === current.focusThreadId) ?? null;
}

export function renderCompact(state) {
  const current = readable(state);
  const focus = focusedThread(current);
  const open = current.decisions.filter((decision) => decision.status === "open").length;
  const label = focus ? `${focus.activity}${focus.softwareType ? `:${focus.softwareType}` : ""}` : "no focus";
  return `SDLC · ${label} · ${current.threads.length} thread${current.threads.length === 1 ? "" : "s"} · ${open} open`;
}

export function renderMarkdown(state) {
  const current = readable(state);
  const lines = ["## Engagement state", ""];
  const focus = focusedThread(current);
  lines.push(`Focus: ${focus ? `${focus.id} — ${focus.activity}${focus.softwareType ? ` (${focus.softwareType})` : ""}` : "none"}`);
  lines.push("", "Threads:");
  if (!current.threads.length) lines.push("- None");
  for (const thread of current.threads) {
    const marker = thread.id === current.focusThreadId ? "●" : thread.status === "parked" ? "○" : "◐";
    lines.push(`- ${marker} ${thread.id} — ${thread.activity}${thread.softwareType ? ` — ${thread.softwareType}` : ""} — ${thread.stoppingPoint ?? "no stopping point"} — ${thread.status}${thread.parkReason ? ` (${thread.parkReason})` : ""}`);
  }
  lines.push("", "Decisions:");
  if (!current.decisions.length) lines.push("- None");
  for (const decision of current.decisions) {
    lines.push(`- ${decision.id} — ${decision.status} — ${decision.owner ?? "unowned"} — ${decision.statement}`);
  }
  lines.push("", `Next transition: ${current.nextTransition ? `${current.nextTransition.from ?? "?"} → ${current.nextTransition.to ?? "?"}${current.nextTransition.needs ? ` (needs ${current.nextTransition.needs})` : ""}` : "none"}`);
  lines.push("", `Authority: read=${current.authority.read.join(",") || "none"}; write=${current.authority.write.join(",") || "none"}; publish=${current.authority.publish}; implement=${current.authority.implement}; deploy=${current.authority.deploy}`);
  return lines.join("\n");
}
