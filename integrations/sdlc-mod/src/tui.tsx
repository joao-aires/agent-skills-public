import { For, Show } from "solid-js"
import { Plugin } from "@opencode/plugin/tui"
import { emptyState, renderCompact } from "../core/state.js"
import { runCommand } from "../core/commands.js"
import { authorityText, decisionGlyph, summaryLabel, threadGlyph } from "../core/view.js"

/**
 * OpenCode TUI adapter. State lives in memory for the current TUI session.
 * It is not written to the repository or shared with other sessions.
 *
 * The state is shown in three places:
 * - a compact status line under the prompt;
 * - a collapsible sidebar section;
 * - a large dialog for the full view.
 */

function threadColor(theme, thread, focused) {
  if (thread.status === "done") return theme.text.feedback.success.base
  if (thread.status === "blocked") return theme.text.feedback.error.base
  if (thread.status === "parked") return theme.text.muted
  return focused ? theme.text.base : theme.text.muted
}

function decisionColor(theme, status) {
  if (status === "accepted") return theme.text.feedback.success.base
  if (status === "rejected") return theme.text.feedback.error.base
  if (status === "superseded") return theme.text.muted
  return theme.text.feedback.warning.base
}

function SdlcSidebar(props) {
  const theme = props.context.theme
  const state = props.state
  const focused = (thread) => thread.id === state.focusThreadId
  const auth = () => authorityText(state.authority)
  const toggle = () => {
    Promise.resolve(
      props.updateView((draft) => {
        draft.open = !draft.open
      }),
    ).catch(() => {})
  }

  return (
    <box flexDirection="column">
      <box flexDirection="row" gap={1} minWidth={0} onMouseDown={toggle}>
        <text fg={theme.text.muted}>{props.view.open ? "▼" : "▶"}</text>
        <text fg={theme.text.base}>
          <b>SDLC</b>
        </text>
        <text fg={theme.text.muted} flexGrow={1} flexShrink={1} minWidth={0} wrapMode="none" truncate>
          {summaryLabel(state)}
        </text>
      </box>

      <Show when={props.view.open}>
        <box flexDirection="column">
          <Show
            when={state.threads.length > 0}
            fallback={<text fg={theme.text.muted}>No threads · /sdlc thread add</text>}
          >
            <For each={state.threads}>
              {(thread) => (
                <box flexDirection="column">
                  <box flexDirection="row" gap={1} minWidth={0}>
                    <text fg={threadColor(theme, thread, focused(thread))}>
                      {threadGlyph(thread, focused(thread))}
                    </text>
                    <text fg={theme.text.muted} flexShrink={0}>
                      {thread.id}
                    </text>
                    <text
                      fg={focused(thread) ? theme.text.base : theme.text.muted}
                      flexGrow={1}
                      flexShrink={1}
                      minWidth={0}
                      wrapMode="none"
                      truncate
                    >
                      {thread.activity}
                      {thread.softwareType ? `:${thread.softwareType}` : ""}
                    </text>
                    <Show when={thread.status !== "waiting"}>
                      <text fg={threadColor(theme, thread, focused(thread))} flexShrink={0}>
                        {thread.status}
                      </text>
                    </Show>
                  </box>
                  <Show when={focused(thread) && thread.stoppingPoint}>
                    <text fg={theme.text.muted} wrapMode="none" truncate>
                      {"   → "}
                      {thread.stoppingPoint}
                    </text>
                  </Show>
                </box>
              )}
            </For>
          </Show>

          <Show when={state.decisions.length > 0}>
            <text fg={theme.text.base}>
              <b>Decisions</b>
            </text>
            <For each={state.decisions}>
              {(decision) => (
                <box flexDirection="row" gap={1} minWidth={0}>
                  <text fg={decisionColor(theme, decision.status)}>{decisionGlyph(decision.status)}</text>
                  <text fg={theme.text.muted} flexShrink={0}>
                    {decision.id}
                  </text>
                  <text fg={theme.text.muted} flexGrow={1} flexShrink={1} minWidth={0} wrapMode="none" truncate>
                    {decision.statement}
                  </text>
                </box>
              )}
            </For>
          </Show>

          <Show when={state.nextTransition}>
            <text fg={theme.text.base}>
              <b>Next</b>
            </text>
            <text fg={theme.text.muted} wrapMode="none" truncate>
              {state.nextTransition.from ?? "?"} → {state.nextTransition.to ?? "?"}
            </text>
            <Show when={state.nextTransition.needs}>
              <text fg={theme.text.muted} wrapMode="none" truncate>
                {"needs "}
                {state.nextTransition.needs}
              </text>
            </Show>
          </Show>

          <text fg={theme.text.base}>
            <b>Authority</b>
          </text>
          <text fg={theme.text.muted} wrapMode="none" truncate>
            {"read "}
            {auth().read}
            {" · write "}
            {auth().write}
          </text>
          <text fg={theme.text.muted} wrapMode="none" truncate>
            {auth().flags}
          </text>
        </box>
      </Show>
    </box>
  )
}

function SdlcDialog(props) {
  const theme = props.context.theme
  const state = props.state
  const focused = (thread) => thread.id === state.focusThreadId
  const authority = () => authorityText(state.authority)

  return (
    <box flexDirection="column" gap={1} padding={1}>
      <box flexDirection="row" gap={2}>
        <text fg={theme.text.base}>
          <b>Engagement state</b>
        </text>
        <text fg={theme.text.muted}>{summaryLabel(state)}</text>
      </box>

      <box flexDirection="column">
        <text fg={theme.text.base}>
          <b>Threads</b>
        </text>
        <Show
          when={state.threads.length > 0}
          fallback={<text fg={theme.text.muted}>No threads yet. /sdlc thread add design frontend "design accepted"</text>}
        >
          <box flexDirection="row" gap={1}>
            <text fg={theme.text.muted} width={1}>
              {" "}
            </text>
            <text fg={theme.text.muted} width={4}>
              {"  ID"}
            </text>
            <text fg={theme.text.muted} flexGrow={1}>
              Activity
            </text>
            <text fg={theme.text.muted} width={12}>
              Type
            </text>
            <text fg={theme.text.muted} width={8}>
              Status
            </text>
            <text fg={theme.text.muted} flexGrow={1}>
              Stopping point
            </text>
          </box>
          <For each={state.threads}>
            {(thread) => (
              <box flexDirection="row" gap={1} minWidth={0}>
                <text fg={threadColor(theme, thread, focused(thread))}>
                  {threadGlyph(thread, focused(thread))}
                </text>
                <text fg={theme.text.muted} width={4}>
                  {thread.id}
                </text>
                <text
                  fg={focused(thread) ? theme.text.base : theme.text.muted}
                  flexGrow={1}
                  flexShrink={1}
                  minWidth={0}
                  wrapMode="none"
                  truncate
                >
                  {thread.activity}
                </text>
                <text fg={theme.text.muted} width={12} wrapMode="none" truncate>
                  {thread.softwareType ?? "—"}
                </text>
                <text fg={threadColor(theme, thread, focused(thread))} width={8}>
                  {thread.status}
                </text>
                <text fg={theme.text.muted} flexGrow={1} flexShrink={1} minWidth={0} wrapMode="none" truncate>
                  {thread.stoppingPoint ?? "no stopping point"}
                </text>
              </box>
            )}
          </For>
        </Show>
      </box>

      <box flexDirection="column">
        <text fg={theme.text.base}>
          <b>Decisions</b>
        </text>
        <Show when={state.decisions.length > 0} fallback={<text fg={theme.text.muted}>No decisions recorded</text>}>
          <For each={state.decisions}>
            {(decision) => (
              <box flexDirection="row" gap={1} minWidth={0}>
                <text fg={decisionColor(theme, decision.status)}>{decisionGlyph(decision.status)}</text>
                <text fg={theme.text.muted} width={4}>
                  {decision.id}
                </text>
                <text fg={decisionColor(theme, decision.status)} width={10}>
                  {decision.status}
                </text>
                <text fg={theme.text.base} flexGrow={1} flexShrink={1} minWidth={0} wrapMode="none" truncate>
                  {decision.statement}
                </text>
                <text fg={theme.text.muted} flexShrink={0}>
                  {decision.owner ?? "unowned"}
                </text>
              </box>
            )}
          </For>
        </Show>
      </box>

      <Show when={state.nextTransition}>
        <box flexDirection="column">
          <text fg={theme.text.base}>
            <b>Next transition</b>
          </text>
          <text fg={theme.text.muted}>
            {state.nextTransition.from ?? "?"} → {state.nextTransition.to ?? "?"}
            {state.nextTransition.needs ? ` · needs ${state.nextTransition.needs}` : ""}
          </text>
        </box>
      </Show>

      <box flexDirection="column">
        <text fg={theme.text.base}>
          <b>Authority</b>
        </text>
        <box flexDirection="row" gap={2}>
          <text fg={theme.text.muted} width={10}>
            read
          </text>
          <text fg={theme.text.base}>{authority().read}</text>
        </box>
        <box flexDirection="row" gap={2}>
          <text fg={theme.text.muted} width={10}>
            write
          </text>
          <text fg={theme.text.base}>{authority().write}</text>
        </box>
        <text fg={theme.text.muted}>{authority().flags}</text>
      </box>

      <text fg={theme.text.muted}>Local to this session · not the ECR · Esc closes this view</text>
    </box>
  )
}

export default Plugin.define({
  id: "sdlc-mod",
  setup(context) {
    const [state, updateState] = context.storage.memory("sdlc-state", {
      initial: emptyState(),
    })
    const [view, updateView] = context.storage.memory("sdlc-view", {
      initial: { open: true },
    })

    /**
     * Replace the stored value field by field.
     *
     * `next` is never the live draft, and no key is deleted: assigning a
     * partial state would make the reactive status line read `state.threads`
     * while it is undefined.
     */
    function replaceState(next) {
      if (!next || next === state) return
      updateState((draft) => {
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
              if (result.state && result.state !== state) replaceState(result.state)
              if (result.markdown) {
                context.ui.dialog.set({ size: "large", centered: true })
                context.ui.dialog.show(() => <SdlcDialog context={context} state={state} />)
              } else if (result.message) {
                context.ui.toast.show({ message: result.message, variant: "success" })
              }
            } catch (error) {
              context.ui.toast.show({ message: String(error?.message ?? error), variant: "error" })
            }
          },
        },
        {
          id: "sdlc.sidebar",
          title: "SDLC: Toggle sidebar section",
          group: "SDLC",
          palette: true,
          run: () => {
            Promise.resolve(
              updateView((draft) => {
                draft.open = !draft.open
              }),
            ).catch(() => {})
          },
        },
      ],
      bindings: ["sdlc.state"],
    }))

    context.ui.slot({
      append: "prompt.footer.status",
      render: () => <text>{renderCompact(state)}</text>,
    })

    context.ui.slot({
      append: "sidebar.content",
      render: () => <SdlcSidebar context={context} state={state} view={view} updateView={updateView} />,
    })
  },
})
