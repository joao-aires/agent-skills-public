import { apply, renderMarkdown } from "./state.js";

const HELP = [
  "Usage: /sdlc <command>",
  "  state                         show the current state",
  "  focus <thread>                switch focus (T1, T2, ...)",
  "  thread add <activity> [type] [stopping point]",
  "  thread close|park|resume <thread>",
  "  decision add <owner> <statement>",
  "  decision resolve|reopen <decision>",
  "  transition <from> <to> [needs]",
  "  reset                         clear the local session state",
].join("\n");

/**
 * Run one textual command against local state.
 * Returns { state, message, markdown? }. Never persists anything.
 */
function tokenize(text) {
  return (text.match(/(?:[^\s"]+|"[^"]*")+/g) ?? []).map((token) =>
    token.startsWith('"') && token.endsWith('"') ? token.slice(1, -1) : token,
  );
}

export function runCommand(input, state) {
  const text = String(input ?? "").trim();
  const parts = text ? tokenize(text) : [];
  const [command, ...rest] = parts;

  if (!command || command === "state") {
    return { state, markdown: renderMarkdown(state) };
  }
  if (command === "help" || command === "-h" || command === "--help") {
    return { state, message: HELP };
  }
  if (command === "reset") {
    return { state: apply(state, { type: "reset" }), message: "Local SDLC state reset." };
  }
  if (command === "focus") {
    if (!rest[0]) throw new Error("focus needs a thread id");
    return { state: apply(state, { type: "thread.focus", id: rest[0] }), message: `Focus: ${rest[0]}` };
  }
  if (command === "thread") {
    const [action, id, ...tail] = rest;
    if (action === "add") {
      const [activity, softwareType, ...stopping] = [id, ...tail];
      if (!activity) throw new Error("thread add needs an activity");
      return {
        state: apply(state, {
          type: "thread.add",
          activity,
          softwareType: softwareType ?? null,
          stoppingPoint: stopping.length ? stopping.join(" ") : null,
        }),
        message: "Thread added.",
      };
    }
    if (!id) throw new Error(`thread ${action} needs a thread id`);
    if (action === "close") return { state: apply(state, { type: "thread.close", id }), message: `Closed ${id}.` };
    if (action === "park") return { state: apply(state, { type: "thread.park", id, reason: tail.join(" ") || null }), message: `Parked ${id}.` };
    if (action === "resume") return { state: apply(state, { type: "thread.resume", id }), message: `Resumed ${id}.` };
    throw new Error(`unknown thread action ${action}`);
  }
  if (command === "decision") {
    const [action, ...tail] = rest;
    if (action === "add") {
      const [owner, ...statement] = tail;
      if (!owner || !statement.length) throw new Error("decision add needs an owner and statement");
      return {
        state: apply(state, { type: "decision.add", owner, statement: statement.join(" ") }),
        message: "Decision added.",
      };
    }
    if (action === "resolve" || action === "reopen") {
      const id = tail[0];
      if (!id) throw new Error(`decision ${action} needs a decision id`);
      return {
        state: apply(state, { type: action === "resolve" ? "decision.resolve" : "decision.reopen", id }),
        message: `${action === "resolve" ? "Resolved" : "Reopened"} ${id}.`,
      };
    }
    throw new Error(`unknown decision action ${action}`);
  }
  if (command === "transition") {
    const [from, to, ...needs] = rest;
    if (!from || !to) throw new Error("transition needs from and to");
    return {
      state: apply(state, { type: "transition.set", from, to, needs: needs.join(" ") || null }),
      message: `Next transition: ${from} → ${to}`,
    };
  }

  throw new Error(`unknown command. Run /sdlc help.`);
}
