import { apply, emptyState, renderCompact } from "../core/state.js";
import { HELP, parseCommand } from "../core/commands.js";
import {
  applyExtraction,
  buildExtractionPrompt,
  latestUserText,
  parseExtraction,
  promptState,
} from "../core/extract.js";
import { gateCommands, decisionHints } from "../core/decision.js";
import {
  decisionGlyph,
  matrixCell,
  matrixThreads,
  phaseMarker,
  summaryLabel,
  threadCode,
  threadGlyph,
} from "../core/view.js";

const PANE = "sdlc";
const MODEL = "haiku";
const PHASE_LABEL = {
  requirements: "req",
  design: "des",
  implementation: "imp",
  testing: "tst",
  operations: "ops",
};

let state = emptyState();
let sessionID = null;
let auto = true;
let page = 0;
let queue = Promise.resolve();

function key(id) {
  return `sdlc:${id}`;
}

function mutate(task) {
  const run = queue.then(task, task);
  queue = run.catch(() => {});
  return run;
}

function migrate(saved) {
  if (!saved || typeof saved !== "object") return null;
  if (saved.version === 3) return saved;
  if (saved.version === 2) {
    return {
      ...saved,
      version: 3,
      threads: (saved.threads ?? []).map((thread) => ({
        ...thread,
        completedPhases: Array.isArray(thread.completedPhases) ? thread.completedPhases : [],
        blockReason: thread.blockReason ?? null,
      })),
      decisions: (saved.decisions ?? []).map((decision) => ({
        ...decision,
        artifacts: Array.isArray(decision.artifacts) ? decision.artifacts : [],
      })),
    };
  }
  return null;
}

async function load($) {
  sessionID = await $.session.id();
  let saved;
  try {
    saved = await $.store.get(key(sessionID));
  } catch {
    saved = undefined;
  }
  state = migrate(saved) ?? emptyState(sessionID);
  page = 0;
}

async function save($) {
  try {
    await $.store.set(key(sessionID), state);
  } catch {
    // Keep the in-memory state; a later successful write replaces it.
  }
}

function refresh($) {
  $.ui.status(renderCompact(state));
  void $.ui.invalidate("ui.render");
}

async function ensure($) {
  if (!sessionID) await load($);
}

async function openPane($) {
  const result = await $.ui.open({
    id: PANE,
    title: "SDLC",
    focus: true,
    closeOnEscape: true,
    columns: 44,
  });
  return result;
}

async function classify($, latest) {
  const input = `Current state:\n${JSON.stringify(promptState(state))}\n\nLatest user message:\n${latest}`;
  try {
    const [changed, intent, activity] = await Promise.all([
      $.model.classify(input, ["no_change", "change"]),
      $.model.classify(input, ["none", "focus", "decision", "phase", "thread", "park", "resume"]),
      $.model.classify(input, ["requirements", "design", "implementation", "testing", "operations", "none"]),
    ]);
    if (changed !== "change") {
      return {
        probability: 0,
        intent: "none",
        intentConfidence: 1,
        activity: "none",
        activityConfidence: 1,
        focus: "none",
        focusConfidence: 0,
      };
    }
    return {
      probability: 1,
      intent: intent ?? "none",
      intentConfidence: 1,
      activity: activity ?? "none",
      activityConfidence: 1,
      focus: "none",
      focusConfidence: 0,
    };
  } catch {
    return null;
  }
}

async function infer($, answer) {
  if (!auto) return;
  await ensure($);

  let messages;
  try {
    messages = await $.session.messages({ last: 12 });
  } catch {
    messages = [];
  }
  if (!Array.isArray(messages)) messages = [];
  if (answer && messages.at(-1)?.text !== answer) {
    messages = [...messages, { role: "assistant", text: answer }];
  }

  const latest = latestUserText(messages);
  if (!latest) return;
  const decision = await classify($, latest);
  if (decision?.probability === 0) return;

  if (decision) {
    const structural = gateCommands(decision, state, { latestText: latest });
    if (structural.length) {
      await mutate(async () => {
        let next = state;
        for (const command of structural) {
          try {
            next = apply(next, command);
          } catch {
            // A stale structural hint is ignored.
          }
        }
        if (JSON.stringify(next) !== JSON.stringify(state)) {
          state = next;
          await save($);
          refresh($);
        }
      });
    }
  }

  if (!decision) {
    // No gate available: fall back to the text pass.
  }

  const prompt = buildExtractionPrompt({
    state,
    messages,
    includeMessages: 8,
    hints: decisionHints(decision),
  });

  let response;
  try {
    response = await $.model.complete({ model: MODEL, prompt });
  } catch {
    return;
  }
  if (!response?.isAnswered) return;

  const parsed = parseExtraction(response.text);
  if (!parsed) return;

  await mutate(async () => {
    const result = applyExtraction(state, parsed, { minConfidence: 0.7 });
    if (!result.changed || !result.applied.length) return;
    state = result.state;
    await save($);
    refresh($);
  });
}

function renderPane($, e) {
  const elements = $.ui.resolve(e);
  const { Box, Text, Button, Link } = elements;
  const columns = Math.max(1, Math.min(3, Math.floor(((e.props.bodyColumns ?? 60) - 10) / 8)));
  const pages = matrixThreads(state, columns, page);
  const focus = state.threads.find((thread) => thread.id === state.focusThreadId) ?? null;
  const rows = [];

  const cell = (value, options = {}) =>
    Box({
      width: 8,
      flexShrink: 0,
      flexDirection: "row",
      justifyContent: "center",
      children: [Text({ children: [String(value ?? "")], ...options })],
    });

  rows.push(
    Box({
      flexDirection: "row",
      children: [
        Box({ width: 10, flexShrink: 0, children: [Text({ children: [""] })] }),
        ...pages.shown.map((thread) => cell(thread.id, { weight: "semibold" })),
      ],
    }),
  );
  rows.push(
    Box({
      flexDirection: "row",
      children: [
        Box({ width: 10, flexShrink: 0, children: [Text({ children: [""] })] }),
        ...pages.shown.map((thread) => cell(thread.ticket ?? "", { dimColor: true })),
      ],
    }),
  );

  for (const phase of Object.keys(PHASE_LABEL)) {
    rows.push(
      Box({
        flexDirection: "row",
        children: [
          Box({
            width: 10,
            flexShrink: 0,
            children: [
              Text({
                children: [`${phaseMarker(phase, focus?.activity, focus?.completedPhases ?? [])} ${PHASE_LABEL[phase]}`],
                dimColor: true,
              }),
            ],
          }),
          ...pages.shown.map((thread) => cell(matrixCell(thread, phase, state.focusThreadId))),
        ],
      }),
    );
  }

  if (pages.pages > 1) {
    rows.push(
      Box({
        flexDirection: "row",
        columnGap: 1,
        children: [
          Text({ children: [`page ${pages.page + 1}/${pages.pages}`], dimColor: true }),
          Button({
            label: "prev",
            hotkey: "p",
            onPress: async () => {
              page = pages.page - 1;
              await $.ui.invalidate("ui.render");
            },
          }),
          Button({
            label: "next",
            hotkey: "n",
            onPress: async () => {
              page = pages.page + 1;
              await $.ui.invalidate("ui.render");
            },
          }),
        ],
      }),
    );
  }

  if (focus) {
    rows.push(
      Box({
        flexDirection: "column",
        children: [
          Text({
            children: [`${threadGlyph(focus, true)} ${threadCode(focus)} ${focus.name}`],
            weight: "semibold",
          }),
          Text({
            children: [
              `${focus.activity} · ${focus.status}${focus.status === "blocked" && focus.blockReason ? ` · ${focus.blockReason}` : ""}`,
            ],
            dimColor: true,
          }),
        ],
      }),
    );
    for (const artifact of focus.artifacts ?? []) {
      rows.push(Link({ href: artifact.href, label: `  ↗ ${artifact.label}` }));
    }
  }

  if (state.decisions.length) {
    rows.push(Text({ children: ["Decisions"], weight: "semibold" }));
    for (const decision of state.decisions) {
      rows.push(
        Text({
          children: [
            `${decisionGlyph(decision.status)} ${decision.id} ${decision.statement}${decision.threadId ? ` · ${decision.threadId}` : ""}`,
          ],
          dimColor: decision.status !== "open",
        }),
      );
    }
  }

  if (!state.threads.length) {
    rows.push(Text({ children: ["No threads · /sdlc thread add"], dimColor: true }));
  }

  return Box({
    flexDirection: "column",
    paddingX: 1,
    paddingY: 1,
    rowGap: 1,
    children: [
      Text({ children: [`SDLC · ${summaryLabel(state)}`], weight: "semibold" }),
      Box({ flexDirection: "column", children: rows }),
    ],
  });
}

export function register(on) {
  on("session.start", async ($, event, next) => {
    try {
      await $.command.register({
        name: "sdlc",
        description: "Open the local SDLC engagement state",
        argumentHint: "state|focus|thread|decision|auto|reset",
        immediate: true,
      });
    } catch {
      // A built-in or another plugin already owns the command.
    }
    await load($);
    refresh($);
    return next(event);
  });

  on("classic.SessionStart", { source: ["clear", "resume", "fork"] }, async ($, event, next) => {
    await load($);
    refresh($);
    return next(event);
  });

  on("turn.complete", async ($, event, next) => {
    const result = await next(event);
    if (event.agentId === undefined && !event.isAborted) {
      await infer($, event.answer);
    }
    return result;
  });

  on("session.end", async ($, event, next) => {
    if (sessionID) await save($);
    return next(event);
  });

  on("command.run", { command: "sdlc" }, async ($, event) => {
    try {
      await ensure($);
      const parsed = parseCommand(event.args);
      if (parsed.kind === "help") return { text: HELP };
      if (parsed.kind === "auto") {
        auto = parsed.enabled;
        refresh($);
        return { text: `Automatic state inference ${auto ? "on" : "off"}.` };
      }
      if (parsed.kind === "read") {
        const result = await openPane($);
        return result?.isPlaced === false ? { text: "The SDLC pane could not open in this terminal." } : {};
      }

      await mutate(async () => {
        state = apply(state, parsed.command);
        await save($);
        refresh($);
      });
      return { text: parsed.message ?? "SDLC state updated." };
    } catch (error) {
      return { text: `SDLC: ${String(error?.message ?? error)}` };
    }
  });

  on("ui.render", { component: "Pane" }, async ($, event, next) => {
    if (event.requestId !== PANE) return next(event);
    return renderPane($, event);
  });
}
