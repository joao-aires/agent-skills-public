import { ACTIVITIES, apply } from "./state.js";

const MAX_MESSAGES = 8;
const MAX_MESSAGE_CHARS = 1200;
const MAX_COMMANDS = 20;

export const EXTRACTION_RULES = `You maintain a small SDLC engagement state for the current chat.

Return only a JSON object with this shape:
{"confidence": 0.0, "commands": []}

Allowed commands:
- {"type":"thread.focus","id":"T1"}
- {"type":"thread.add","name":"pagination works","activity":"implementation","softwareType":"backend","stoppingPoint":"pagination works"}
- {"type":"thread.phase","id":"T1","activity":"testing"}
- {"type":"thread.status","id":"T1","status":"waiting|blocked|parked"}
- {"type":"thread.park","id":"T1","reason":"why it is parked"}
- {"type":"thread.resume","id":"T1"}
- {"type":"decision.add","statement":"the decision","owner":"user or unowned","threadId":"T1"}

Rules:
- A thread is a unit of work with a short name. Its activity is the current phase: requirements, design, implementation, testing or operations.
- Report only changes supported by the conversation after the state shown below.
- Do not repeat threads or decisions that already exist.
- Add a decision only when the conversation accepts it or leaves it explicitly open; it is always recorded as open.
- Never resolve or reopen decisions, close threads or reset state.
- Use existing thread ids for focus, phase and status changes. Do not focus a thread added in the same response.
- Move an existing thread to a new phase instead of creating a second thread for the same work.
- Confidence describes this update, not the whole conversation.
- Return {"confidence":1,"commands":[]} when nothing changed.`;

export function normaliseMessages(messages) {
  return (Array.isArray(messages) ? messages : []).map(normaliseMessage).filter(Boolean);
}

function normaliseMessage(message) {
  if (!message || typeof message !== "object") return null;
  const role = message.role ?? message.type;
  if (role === "idle") return null;

  let text = "";
  if (typeof message.text === "string") {
    text = message.text.trim();
  } else if (Array.isArray(message.content)) {
    text = message.content.map(blockText).filter(Boolean).join("\n").trim();
  }

  if (Array.isArray(message.toolUses) && message.toolUses.length) {
    const names = message.toolUses.map((tool) => tool?.name).filter(Boolean);
    if (names.length) text = `${text}\n[tools: ${names.join(", ")}]`.trim();
  }

  if (!text) return null;
  return { role: role ?? "unknown", text: truncate(text) };
}

function blockText(block) {
  if (!block || typeof block !== "object") return "";
  if (block.type === "text" && typeof block.text === "string") return block.text;
  if (block.type === "tool" && block.name) return `[tool ${block.name}]`;
  return "";
}

function truncate(text) {
  return text.length > MAX_MESSAGE_CHARS ? `${text.slice(0, MAX_MESSAGE_CHARS)}…` : text;
}

export function promptState(state) {
  const artifacts = (items) => (Array.isArray(items) ? items.map(({ label, kind }) => ({ label, kind })) : []);
  return {
    ...state,
    threads: (state?.threads ?? []).map((thread) => ({ ...thread, artifacts: artifacts(thread.artifacts) })),
    decisions: (state?.decisions ?? []).map((decision) => ({ ...decision, artifacts: artifacts(decision.artifacts) })),
  };
}

export function latestUserText(messages) {
  const users = normaliseMessages(messages).filter((message) => message.role === "user");
  return users.at(-1)?.text ?? "";
}

export function buildExtractionInput({ state, messages, includeMessages = MAX_MESSAGES, hints = null }) {
  const transcript = normaliseMessages(messages)
    .slice(-includeMessages)
    .map((message) => `${message.role.toUpperCase()}: ${message.text}`)
    .join("\n\n");

  const parts = ["Current state:", JSON.stringify(promptState(state), null, 2)];
  if (hints) {
    parts.push("Decision model hints (advisory; verify against the conversation):", hints);
  }
  parts.push("Conversation:", transcript || "(no text)");
  return parts.join("\n\n");
}

export function buildExtractionPrompt(options) {
  return `${EXTRACTION_RULES}\n\n${buildExtractionInput(options)}`;
}

export function parseExtraction(text) {
  if (typeof text !== "string") return null;
  const candidate = jsonCandidate(text);
  if (!candidate) return null;

  let value;
  try {
    value = JSON.parse(candidate);
  } catch {
    return null;
  }

  if (!value || typeof value !== "object" || Array.isArray(value)) return null;
  const confidence = Number(value.confidence);
  if (!Number.isFinite(confidence) || confidence < 0 || confidence > 1) return null;
  if (!Array.isArray(value.commands)) return null;
  return { confidence, commands: value.commands };
}

function jsonCandidate(text) {
  const fenced = /```(?:json)?\s*([\s\S]*?)```/i.exec(text);
  if (fenced) return fenced[1].trim();
  const start = text.indexOf("{");
  const end = text.lastIndexOf("}");
  if (start === -1 || end <= start) return null;
  return text.slice(start, end + 1);
}

/**
 * Keep only safe, supported, non-duplicate changes.
 */
export function guardCommands(commands, state, { confidence = 1, minConfidence = 0.7 } = {}) {
  if (confidence < minConfidence) return [];

  const threads = Array.isArray(state?.threads) ? state.threads : [];
  const decisions = Array.isArray(state?.decisions) ? state.decisions : [];
  const threadById = new Map(threads.map((thread) => [thread.id, thread]));
  const threadNames = new Set(threads.map((thread) => nameKey(thread.name)));
  const decisionKeys = new Set(decisions.map((decision) => statementKey(decision.statement)));
  const batchThreads = new Set();
  const batchDecisions = new Set();
  const guarded = [];

  for (const raw of Array.isArray(commands) ? commands.slice(0, MAX_COMMANDS) : []) {
    if (!raw || typeof raw !== "object") continue;

    if (raw.type === "thread.add") {
      const name = text(raw.name);
      const activity = text(raw.activity);
      if (!name || !ACTIVITIES.includes(activity)) continue;
      const key = nameKey(name);
      if (threadNames.has(key) || batchThreads.has(key)) continue;
      batchThreads.add(key);
      guarded.push({
        type: "thread.add",
        name,
        activity,
        softwareType: text(raw.softwareType) || null,
        stoppingPoint: text(raw.stoppingPoint) || null,
        source: "inferred",
      });
      continue;
    }

    if (raw.type === "thread.focus") {
      const id = text(raw.id);
      if (!threadById.has(id) || id === state.focusThreadId) continue;
      guarded.push({ type: "thread.focus", id });
      continue;
    }

    if (raw.type === "thread.phase") {
      const thread = threadById.get(text(raw.id));
      if (!thread || !ACTIVITIES.includes(raw.activity)) continue;
      if (thread.activity === raw.activity) continue;
      guarded.push({ type: "thread.phase", id: thread.id, activity: raw.activity });
      continue;
    }

    if (raw.type === "thread.status") {
      const thread = threadById.get(text(raw.id));
      if (!thread || !["waiting", "blocked", "parked"].includes(raw.status)) continue;
      if (thread.status === raw.status) continue;
      guarded.push({ type: "thread.status", id: thread.id, status: raw.status });
      continue;
    }

    if (raw.type === "thread.park") {
      const thread = threadById.get(text(raw.id));
      if (!thread || thread.status === "parked") continue;
      guarded.push({ type: "thread.park", id: thread.id, reason: text(raw.reason) || null });
      continue;
    }

    if (raw.type === "thread.resume") {
      const thread = threadById.get(text(raw.id));
      if (!thread || thread.status !== "parked") continue;
      guarded.push({ type: "thread.resume", id: thread.id });
      continue;
    }

    if (raw.type === "decision.add") {
      const statement = text(raw.statement);
      if (!statement) continue;
      const key = statementKey(statement);
      if (decisionKeys.has(key) || batchDecisions.has(key)) continue;
      const threadId = text(raw.threadId) || null;
      if (threadId && !threadById.has(threadId)) continue;
      batchDecisions.add(key);
      guarded.push({
        type: "decision.add",
        statement,
        owner: text(raw.owner) || "unassigned",
        status: "open",
        threadId,
        source: "inferred",
      });
    }
  }

  return guarded;
}

export function applyExtraction(state, extraction, options = {}) {
  const confidence = Number(extraction?.confidence);
  const safeConfidence = Number.isFinite(confidence) ? confidence : 0;
  const guarded = guardCommands(extraction?.commands, state, {
    confidence: safeConfidence,
    minConfidence: options.minConfidence ?? 0.7,
  });

  let next = state;
  const applied = [];
  const rejected = [];

  for (const command of guarded) {
    try {
      next = apply(next, command);
      applied.push(command);
    } catch (error) {
      rejected.push({ command, reason: String(error?.message ?? error) });
    }
  }

  return {
    state: next,
    applied,
    rejected,
    confidence: safeConfidence,
    changed: JSON.stringify(next) !== JSON.stringify(state),
  };
}

function nameKey(name) {
  return String(name ?? "").toLowerCase().replace(/\s+/g, " ").trim();
}

function statementKey(statement) {
  return String(statement ?? "").toLowerCase().replace(/\s+/g, " ").replace(/[.!?]+$/, "").trim();
}

function text(value) {
  return typeof value === "string" ? value.trim() : "";
}
