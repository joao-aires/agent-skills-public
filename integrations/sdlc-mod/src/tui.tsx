import { Plugin } from "@opencode/plugin/tui"
import { emptyState, renderCompact } from "../core/state.js"
import { runCommand } from "../core/commands.js"

/**
 * OpenCode TUI-only adapter. State lives in memory for the current TUI
 * session; it is not written to the repository or shared with other sessions.
 */
export default Plugin.define({
  id: "sdlc-mod",
  setup(context) {
    const [state, updateState] = context.storage.memory("sdlc-state", {
      initial: emptyState(),
    })

    function replaceState(next) {
      updateState((draft) => {
        for (const key of Object.keys(draft)) delete draft[key]
        Object.assign(draft, next)
      })
    }

    context.keymap.layer(() => ({
      mode: "global",
      priority: 10,
      commands: [
        {
          id: "sdlc.state",
          title: "SDLC state",
          group: "SDLC",
          palette: true,
          slash: { name: "sdlc", arguments: true },
          enabled: () => true,
          suggested: true,
          run: async (input) => {
            try {
              const result = runCommand(input, state)
              if (result.state) replaceState(result.state)
              if (result.markdown) {
                await context.ui.dialog.alert({ title: "SDLC state", message: result.markdown })
              } else if (result.message) {
                context.ui.toast.show({ message: result.message, variant: "success" })
              }
            } catch (error) {
              context.ui.toast.show({ message: String(error?.message ?? error), variant: "error" })
            }
          },
        },
      ],
      bindings: ["sdlc.state"],
    }))

    context.ui.slot({
      append: "prompt.footer.status",
      render: () => <text>{renderCompact(state)}</text>,
    })
  },
})
