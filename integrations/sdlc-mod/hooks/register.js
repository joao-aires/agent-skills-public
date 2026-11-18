import { emptyState, renderCompact } from "../core/state.js"
import { runCommand } from "../core/commands.js"

/**
 * Claude Code mod adapter. State is module-local to this session and is
 * discarded on session end. It is not written to the repository.
 */
let state = emptyState()

export function register(on) {
  on("session.start", async ($, event, next) => {
    await $.command.register({
      name: "sdlc",
      description: "Show or update local SDLC engagement state",
      argumentHint: "state|focus|thread|decision|transition|reset",
    })
    $.ui.status(renderCompact(state))
    return next(event)
  })

  on("command.run", { command: "sdlc" }, async ($, event) => {
    try {
      const result = runCommand(event.args, state)
      if (result.state) state = result.state
      $.ui.status(renderCompact(state))
      if (result.markdown) return { text: result.markdown }
      return { text: result.message ?? "SDLC state updated." }
    } catch (error) {
      return { text: `SDLC: ${String(error?.message ?? error)}` }
    }
  })

  on("session.end", async ($, event, next) => {
    state = emptyState()
    return next(event)
  })
}
