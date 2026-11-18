import { apply, renderMarkdown } from "./state.js";

export const HELP = [
  "Usage: /sdlc <command>",
  "  state                              show the current state",
  "  focus <thread>                     switch focus (T1, T2, ...)",
  "  thread add <name> <phase> [type] [stopping point]",
  "  thread phase <thread> <phase>      move a thread to a phase",
  "  thread ticket <thread> <ticket>    attach a tracker id",
  "  thread artifact <thread> <label> <href>",
  "  thread block <thread> [reason]",
  "  thread park|resume|close <thread>",
  "  decision add <owner> <statement>",
  "  decision resolve|reopen <decision>",
  "  decision thread <decision> <thread>",
  "  decision artifact <decision> <label> <href>",
  "  auto on|off                        infer state after each turn",
  "  reset                              clear the local session state",
].join("\n");

function tokenize(text) {
  return (text.match(/(?:[^\s"]+|"[^"]*")+/g) ?? []).map((token) =>
    token.startsWith('"') && token.endsWith('"') ? token.slice(1, -1) : token,
  );
}

function command(type, message, fields = {}) {
  return { kind: "command", command: { type, ...fields }, message };
}

function artifact(label, href) {
  return { label, href, kind: /^https?:\/\//i.test(href) ? "url" : "file" };
}

/**
 * Parse one textual command without applying it.
 *
 * Returns { kind: "read" } | { kind: "help" } | { kind: "auto", enabled } |
 * { kind: "command", command, message }.
 */
export function parseCommand(input) {
  const text = String(input ?? "").trim();
  const parts = text ? tokenize(text) : [];
  const [name, ...rest] = parts;

  if (!name || name === "state") return { kind: "read" };
  if (name === "help" || name === "-h" || name === "--help") return { kind: "help" };
  if (name === "auto") {
    const mode = rest[0];
    if (mode !== "on" && mode !== "off") throw new Error("auto needs on or off");
    return { kind: "auto", enabled: mode === "on" };
  }
  if (name === "reset") return command("reset", "Local SDLC state reset.");
  if (name === "focus") {
    if (!rest[0]) throw new Error("focus needs a thread id");
    return command("thread.focus", `Focus: ${rest[0]}`, { id: rest[0] });
  }

  if (name === "thread") {
    const [action, id, ...tail] = rest;
    if (action === "add") {
      const [threadName, phase, softwareType, ...stopping] = [id, ...tail];
      if (!threadName) throw new Error("thread add needs a name");
      if (!phase) throw new Error("thread add needs a phase");
      return command("thread.add", "Thread added.", {
        name: threadName,
        activity: phase,
        softwareType: softwareType ?? null,
        stoppingPoint: stopping.length ? stopping.join(" ") : null,
      });
    }
    if (!id) throw new Error(`thread ${action} needs a thread id`);
    if (action === "phase") {
      if (!tail[0]) throw new Error("thread phase needs a phase");
      return command("thread.phase", `Moved ${id} to ${tail[0]}.`, { id, activity: tail[0] });
    }
    if (action === "ticket") {
      if (!tail[0]) throw new Error("thread ticket needs a ticket id");
      return command("thread.ticket", `Ticket ${tail[0]} linked to ${id}.`, { id, ticket: tail[0] });
    }
    if (action === "artifact") {
      const [label, href] = tail;
      if (!label || !href) throw new Error("thread artifact needs a label and href");
      return command("thread.artifact", `Artifact ${label} linked to ${id}.`, {
        id,
        artifact: artifact(label, href),
      });
    }
    if (action === "block") {
      return command("thread.status", `Blocked ${id}.`, { id, status: "blocked", reason: tail.join(" ") || null });
    }
    if (action === "close") return command("thread.close", `Closed ${id}.`, { id });
    if (action === "park") {
      return command("thread.park", `Parked ${id}.`, { id, reason: tail.join(" ") || null });
    }
    if (action === "resume") return command("thread.resume", `Resumed ${id}.`, { id });
    throw new Error(`unknown thread action ${action}`);
  }

  if (name === "decision") {
    const [action, ...tail] = rest;
    if (action === "add") {
      const [owner, ...statement] = tail;
      if (!owner || !statement.length) throw new Error("decision add needs an owner and statement");
      return command("decision.add", "Decision added.", { owner, statement: statement.join(" ") });
    }
    if (!tail[0]) throw new Error(`decision ${action} needs a decision id`);
    const id = tail[0];
    if (action === "resolve" || action === "reopen") {
      return command(
        action === "resolve" ? "decision.resolve" : "decision.reopen",
        `${action === "resolve" ? "Resolved" : "Reopened"} ${id}.`,
        { id },
      );
    }
    if (action === "thread") {
      if (!tail[1]) throw new Error("decision thread needs a thread id");
      return command("decision.thread", `Linked ${id} to ${tail[1]}.`, { id, threadId: tail[1] });
    }
    if (action === "artifact") {
      const [label, href] = tail.slice(1);
      if (!label || !href) throw new Error("decision artifact needs a label and href");
      return command("decision.artifact", `Artifact ${label} linked to ${id}.`, {
        id,
        artifact: artifact(label, href),
      });
    }
    throw new Error(`unknown decision action ${action}`);
  }

  throw new Error("unknown command. Run /sdlc help.");
}

/**
 * Run one textual command against local state.
 * Returns { state, message, markdown? }. Never persists anything.
 */
export function runCommand(input, state) {
  const parsed = parseCommand(input);
  if (parsed.kind === "read") return { state, markdown: renderMarkdown(state) };
  if (parsed.kind === "help") return { state, message: HELP };
  if (parsed.kind === "auto") return { state, auto: parsed.enabled };
  return { state: apply(state, parsed.command), message: parsed.message };
}
