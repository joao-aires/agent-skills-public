import { PHASES } from "./state.js";
import { normaliseMessages, promptState } from "./extract.js";

export const DEFAULT_DECISION_MODEL = "opencode/jev-1.13-free";

export const PHASE_CHOICES = [...PHASES, "none"];

const INTENTS = [
  { value: "none", label: "no change" },
  { value: "focus", label: "focus change" },
  { value: "decision", label: "decision" },
  { value: "phase", label: "phase change" },
  { value: "thread", label: "thread change" },
  { value: "park", label: "park" },
  { value: "resume", label: "resume" },
];

export function buildDecisionInput({ state, messages, includeMessages = 2 }) {
  const transcript = normaliseMessages(messages)
    .slice(-includeMessages)
    .map((message) => `${message.role.toUpperCase()}: ${message.text}`)
    .join("\n\n");

  return [
    "Current state:",
    JSON.stringify(promptState(state), null, 2),
    "Conversation:",
    transcript || "(no text)",
  ].join("\n\n");
}

export function buildDecisionQuestions(state) {
  const threads = Array.isArray(state?.threads) ? state.threads : [];
  const focusChoices = [
    { value: "none", label: "no focus change" },
    { value: "new", label: "new thread" },
    ...threads.map((thread) => ({
      value: thread.id,
      label: `${thread.id} ${thread.name}`,
    })),
  ];

  return [
    {
      type: "predicate",
      name: "changed",
      instructions:
        "Compared with the state above, does the latest user message change the SDLC focus, threads, decisions, or the next transition? Ignore ordinary Q&A, acknowledgements and tool chatter.",
    },
    {
      type: "choice",
      name: "intent",
      instructions:
        "What kind of state change does the latest user message make? Choose none for ordinary Q&A or acknowledgements.",
      choices: INTENTS,
    },
    {
      type: "choice",
      name: "phase",
      instructions: "Which phase is the work in after the latest user message?",
      choices: PHASE_CHOICES.map((phase) => ({ value: phase, label: phase })),
    },
    {
      type: "choice",
      name: "focus",
      instructions: "Which thread should be the focus after the latest user message?",
      choices: focusChoices,
    },
  ];
}

export function interpretDecisions(result) {
  const answers = Array.isArray(result?.answers) ? result.answers : [];
  const byName = new Map(
    answers.filter((answer) => answer && typeof answer.name === "string").map((answer) => [answer.name, answer]),
  );

  const changed = byName.get("changed");
  const intent = byName.get("intent");
  const phase = byName.get("phase");
  const focus = byName.get("focus");

  return {
    probability: typeof changed?.probability === "number" ? changed.probability : null,
    intent: typeof intent?.choice === "string" ? intent.choice : null,
    intentConfidence: typeof intent?.confidence === "number" ? intent.confidence : 0,
    phase: typeof phase?.choice === "string" ? phase.choice : null,
    phaseConfidence: typeof phase?.confidence === "number" ? phase.confidence : 0,
    focus: typeof focus?.choice === "string" ? focus.choice : null,
    focusConfidence: typeof focus?.confidence === "number" ? focus.confidence : 0,
  };
}

/**
 * True when the text extractor should run. A missing or failed decision keeps
 * the previous behaviour instead of silently dropping an update.
 */
export function shouldExtract(
  decision,
  { probabilityThreshold = 0.5, intentThreshold = 0.7, phaseThreshold = 0.8, currentPhase = null, currentFocus = null } = {},
) {
  if (!decision || decision.probability === null) return true;
  if (decision.probability >= probabilityThreshold) return true;
  if (decision.intent && decision.intent !== "none" && decision.intentConfidence >= intentThreshold) return true;
  if (
    decision.phase &&
    decision.phase !== "none" &&
    decision.phase !== currentPhase &&
    decision.phaseConfidence >= phaseThreshold
  ) {
    return true;
  }
  if (
    decision.focus &&
    decision.focus !== "none" &&
    decision.focus !== currentFocus &&
    decision.focusConfidence >= phaseThreshold
  ) {
    return true;
  }
  return false;
}

/**
 * Structural commands the gate is confident enough to apply directly.
 * Text extraction still runs afterwards for decisions and wording.
 */
function namedThreadId(threads, text) {
  const lower = String(text ?? "").toLowerCase();
  if (!lower) return null;
  const matches = threads.filter(
    (thread) =>
      lower.includes(String(thread.name ?? "").toLowerCase()) ||
      (thread.ticket && lower.includes(String(thread.ticket).toLowerCase())),
  );
  return matches.length === 1 ? matches[0].id : null;
}

export function gateCommands(
  decision,
  state,
  { phaseThreshold = 0.8, focusThreshold = 0.8, latestText = "" } = {},
) {
  if (!decision) return [];
  const threads = Array.isArray(state?.threads) ? state.threads : [];
  const currentFocus = state?.focusThreadId ?? null;
  const chosenFocus =
    decision.focus &&
    decision.focus !== "none" &&
    decision.focusConfidence >= focusThreshold &&
    threads.some((thread) => thread.id === decision.focus)
      ? decision.focus
      : null;
  const namedFocus = namedThreadId(threads, latestText);
  const target = namedFocus ?? chosenFocus ?? currentFocus;
  const commands = [];

  if (target && target !== currentFocus && (namedFocus || chosenFocus)) {
    commands.push({ type: "thread.focus", id: target });
  }

  if (
    decision.intent === "phase" &&
    decision.phase &&
    decision.phase !== "none" &&
    decision.phaseConfidence >= phaseThreshold
  ) {
    const thread = threads.find((item) => item.id === target);
    if (thread && thread.phase !== decision.phase) {
      commands.push({ type: "thread.phase", id: target, phase: decision.phase });
    }
  }

  return commands;
}

export function decisionHints(decision) {
  if (!decision) return null;
  const hints = [];
  if (decision.phase && decision.phase !== "none") hints.push(`phase=${decision.phase}`);
  if (decision.intent && decision.intent !== "none") hints.push(`intent=${decision.intent}`);
  if (decision.focus && decision.focus !== "none") hints.push(`focus=${decision.focus}`);
  return hints.length ? hints.join(", ") : null;
}
