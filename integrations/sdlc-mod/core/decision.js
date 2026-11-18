import { ACTIVITIES as PHASES } from "./state.js";
import { normaliseMessages } from "./extract.js";

export const DEFAULT_DECISION_MODEL = "opencode/jev-1.13-free";

export const ACTIVITIES = [...PHASES, "none"];

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
    JSON.stringify(state, null, 2),
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
      name: "activity",
      instructions: "Which phase is the work in after the latest user message?",
      choices: ACTIVITIES.map((activity) => ({ value: activity, label: activity })),
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
  const activity = byName.get("activity");
  const focus = byName.get("focus");

  return {
    probability: typeof changed?.probability === "number" ? changed.probability : null,
    intent: typeof intent?.choice === "string" ? intent.choice : null,
    intentConfidence: typeof intent?.confidence === "number" ? intent.confidence : 0,
    activity: typeof activity?.choice === "string" ? activity.choice : null,
    activityConfidence: typeof activity?.confidence === "number" ? activity.confidence : 0,
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
  { probabilityThreshold = 0.5, intentThreshold = 0.7, activityThreshold = 0.8, currentActivity = null, currentFocus = null } = {},
) {
  if (!decision || decision.probability === null) return true;
  if (decision.probability >= probabilityThreshold) return true;
  if (decision.intent && decision.intent !== "none" && decision.intentConfidence >= intentThreshold) return true;
  if (
    decision.activity &&
    decision.activity !== "none" &&
    decision.activity !== currentActivity &&
    decision.activityConfidence >= activityThreshold
  ) {
    return true;
  }
  if (
    decision.focus &&
    decision.focus !== "none" &&
    decision.focus !== currentFocus &&
    decision.focusConfidence >= activityThreshold
  ) {
    return true;
  }
  return false;
}

export function decisionHints(decision) {
  if (!decision) return null;
  const hints = [];
  if (decision.activity && decision.activity !== "none") hints.push(`activity=${decision.activity}`);
  if (decision.intent && decision.intent !== "none") hints.push(`intent=${decision.intent}`);
  if (decision.focus && decision.focus !== "none") hints.push(`focus=${decision.focus}`);
  return hints.length ? hints.join(", ") : null;
}
