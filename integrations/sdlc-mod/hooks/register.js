import { apply, emptyState, renderCompact, renderMarkdown } from "../core/state.js";
import { HELP, parseCommand } from "../core/commands.js";
import { applyExtraction, buildExtractionPrompt, parseExtraction } from "../core/extract.js";

/**
 * Claude Code mod adapter.
 *
 * State is module-local to this session and is discarded when the session
 * ends. After each turn, a small model call proposes state changes from the
 * conversation. The proposal is guarded before it is applied.
 */

let state = emptyState();
let auto = true;
let timer;

const MODEL = "haiku";
const DEBOUNCE_MS = 1200;

export function register(on) {
  on("session.start", async ($, event, next) => {
    await $.command.register({
      name: "sdlc",
      description: "Show or update local SDLC engagement state",
      argumentHint: "state|focus|thread|decision|transition|auto|reset",
    });
    $.ui.status(renderCompact(state));
    return next(event);
  });

  on("command.run", { command: "sdlc" }, async ($, event) => {
    try {
      const parsed = parseCommand(event.args);
      if (parsed.kind === "help") return { text: HELP };
      if (parsed.kind === "auto") {
        auto = parsed.enabled;
        if (!auto) clearTimeout(timer);
        return { text: `Automatic state inference ${auto ? "on" : "off"}.` };
      }
      if (parsed.kind === "read") return { text: renderMarkdown(state) };

      state = apply(state, parsed.command);
      $.ui.status(renderCompact(state));
      return { text: parsed.message ?? "SDLC state updated." };
    } catch (error) {
      return { text: `SDLC: ${String(error?.message ?? error)}` };
    }
  });

  on("turn.start", async ($, event, next) => {
    clearTimeout(timer);
    return next(event);
  });

  on("turn.complete", async ($, event, next) => {
    schedule($);
    return next(event);
  });

  on("session.end", async ($, event, next) => {
    clearTimeout(timer);
    state = emptyState();
    auto = true;
    return next(event);
  });
}

function schedule($) {
  if (!auto) return;
  clearTimeout(timer);
  timer = setTimeout(() => {
    void infer($);
  }, DEBOUNCE_MS);
}

async function infer($) {
  if (!auto) return;
  try {
    const messages = $.session.messages();
    const prompt = buildExtractionPrompt({ state, messages, includeMessages: 8 });
    const response = await $.model.complete({ model: MODEL, prompt });
    if (!response?.isAnswered) return;

    const parsed = parseExtraction(response.text);
    if (!parsed) return;

    const result = applyExtraction(state, parsed, { minConfidence: 0.7 });
    if (!result.changed || !result.applied.length) return;

    state = result.state;
    $.ui.status(renderCompact(state));
  } catch {
    // Inference is best effort and never blocks the turn.
  }
}
