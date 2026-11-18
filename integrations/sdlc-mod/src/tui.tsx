import { createEffect, createSignal, For, Show } from "solid-js"
import { Plugin } from "@opencode/plugin/tui"
import { emptyState, renderCompact } from "../core/state.js"
import { HELP, parseCommand } from "../core/commands.js"
import { authorityText, decisionGlyph, summaryLabel, threadGlyph } from "../core/view.js"
import { Sdlc } from "./rpc.js"

/**
 * OpenCode TUI adapter. The server part owns the state; this part mirrors it
 * over RPC and renders the status line, sidebar section and dialog.
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

function SdlcStatus(props) {
  createEffect(() => {
    props.ensure(props.sessionID)
  })
  return <text>{renderCompact(props.state())}</text>
}

function SdlcSidebar(props) {
  const theme = props.context.theme
  const current = () => props.state()
  const focused = (thread) => thread.id === current().focusThreadId
  const auth = () => authorityText(current().authority)
  createEffect(() => {
    props.ensure(props.sessionID)
  })

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
          {summaryLabel(current())}
        </text>
      </box>

      <Show when={props.view.open}>
        <box flexDirection="column">
          <Show
            when={current().threads.length > 0}
            fallback={<text fg={theme.text.muted}>No threads · /sdlc thread add</text>}
          >
            <For each={current().threads}>
              {(thread) => (
                <box flexDirection="column">
                  <box flexDirection="row" gap={1} minWidth={0}>
                    <text fg={threadColor(theme, thread, focused(thread))}>
                      {threadGlyph(thread, focused(thread))}
                    </text>
                    <text fg={theme.text.muted} flexShrink={0}>
                      {thread.source === "inferred" ? "~" : ""}
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

          <Show when={current().decisions.length > 0}>
            <text fg={theme.text.base}>
              <b>Decisions</b>
            </text>
            <For each={current().decisions}>
              {(decision) => (
                <box flexDirection="row" gap={1} minWidth={0}>
                  <text fg={decisionColor(theme, decision.status)}>{decisionGlyph(decision.status)}</text>
                  <text fg={theme.text.muted} flexShrink={0}>
                    {decision.source === "inferred" ? "~" : ""}
                    {decision.id}
                  </text>
                  <text fg={theme.text.muted} flexGrow={1} flexShrink={1} minWidth={0} wrapMode="none" truncate>
                    {decision.statement}
                  </text>
                </box>
              )}
            </For>
          </Show>

          <Show when={current().nextTransition}>
            <text fg={theme.text.base}>
              <b>Next</b>
            </text>
            <text fg={theme.text.muted} wrapMode="none" truncate>
              {current().nextTransition.source === "inferred" ? "~ " : ""}
              {current().nextTransition.from ?? "?"} → {current().nextTransition.to ?? "?"}
            </text>
            <Show when={current().nextTransition.needs}>
              <text fg={theme.text.muted} wrapMode="none" truncate>
                {"needs "}
                {current().nextTransition.needs}
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
  const current = () => props.state()
  const focused = (thread) => thread.id === current().focusThreadId
  const authority = () => authorityText(current().authority)

  return (
    <box flexDirection="column" gap={1} padding={1}>
      <box flexDirection="row" gap={2}>
        <text fg={theme.text.base}>
          <b>Engagement state</b>
        </text>
        <text fg={theme.text.muted}>{summaryLabel(current())}</text>
      </box>

      <box flexDirection="column">
        <text fg={theme.text.base}>
          <b>Threads</b>
        </text>
        <Show
          when={current().threads.length > 0}
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
          <For each={current().threads}>
            {(thread) => (
              <box flexDirection="row" gap={1} minWidth={0}>
                <text fg={threadColor(theme, thread, focused(thread))}>
                  {threadGlyph(thread, focused(thread))}
                </text>
                <text fg={theme.text.muted} width={4}>
                  {thread.source === "inferred" ? "~" : ""}
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
        <Show when={current().decisions.length > 0} fallback={<text fg={theme.text.muted}>No decisions recorded</text>}>
          <For each={current().decisions}>
            {(decision) => (
              <box flexDirection="row" gap={1} minWidth={0}>
                <text fg={decisionColor(theme, decision.status)}>{decisionGlyph(decision.status)}</text>
                <text fg={theme.text.muted} width={4}>
                  {decision.source === "inferred" ? "~" : ""}
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

      <Show when={current().nextTransition}>
        <box flexDirection="column">
          <text fg={theme.text.base}>
            <b>Next transition{current().nextTransition.source === "inferred" ? " ~" : ""}</b>
          </text>
          <text fg={theme.text.muted}>
            {current().nextTransition.from ?? "?"} → {current().nextTransition.to ?? "?"}
            {current().nextTransition.needs ? ` · needs ${current().nextTransition.needs}` : ""}
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
  id: "sdlc-mod.tui",
  setup(context) {
    const [view, updateView] = context.storage.memory("sdlc-view", {
      initial: { open: true },
    })
    const [mirror, setMirror] = createSignal(new Map())
    const requested = new Set()

    const rpc = () => context.client.rpc(Sdlc)

    const put = (sessionID, state) => {
      if (!sessionID || !state) return
      setMirror((previous) => {
        const next = new Map(previous)
        next.set(sessionID, state)
        return next
      })
    }

    const stateFor = (sessionID) => () => mirror().get(sessionID) ?? emptyState(sessionID ?? null)

    const ensure = (sessionID, attempt = 0) => {
      if (!sessionID || requested.has(sessionID)) return
      requested.add(sessionID)
      rpc()
        .snapshot({ sessionID })
        .then((result) => put(sessionID, result.state))
        .catch(() => {
          requested.delete(sessionID)
          if (attempt < 6) setTimeout(() => ensure(sessionID, attempt + 1), 500)
        })
    }

    let unsubscribe = () => {}
    try {
      unsubscribe = rpc().events.on("updated", (event) => {
        put(event.data.sessionID, event.data.state)
      })
    } catch {
      // The server part is not registered; snapshots will surface the error.
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
            const route = context.ui.router.current()
            const sessionID = route.type === "session" ? route.sessionID : undefined
            if (!sessionID) {
              context.ui.toast.show({ message: "Open a session first.", variant: "warning" })
              return
            }

            try {
              const parsed = parseCommand(input)
              if (parsed.kind === "help") {
                context.ui.dialog.alert({ title: "SDLC commands", message: HELP })
                return
              }
              if (parsed.kind === "auto") {
                const result = await rpc().setAuto({ enabled: parsed.enabled })
                context.ui.toast.show({
                  message: `Automatic state inference ${result.enabled ? "on" : "off"}.`,
                  variant: "success",
                })
                return
              }
              if (parsed.kind === "read") {
                const result = await rpc().snapshot({ sessionID })
                put(sessionID, result.state)
                context.ui.dialog.set({ size: "large", centered: true })
                context.ui.dialog.show(() => <SdlcDialog context={context} state={stateFor(sessionID)} />)
                return
              }

              const result = await rpc().apply({ sessionID, command: parsed.command })
              put(sessionID, result.state)
              context.ui.toast.show({ message: parsed.message, variant: "success" })
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
      render: (input) => (
        <SdlcStatus context={context} sessionID={input?.sessionID} state={stateFor(input?.sessionID)} ensure={ensure} />
      ),
    })

    context.ui.slot({
      append: "sidebar.content",
      render: (input) => (
        <SdlcSidebar
          context={context}
          sessionID={input?.sessionID}
          state={stateFor(input?.sessionID)}
          ensure={ensure}
          view={view}
          updateView={updateView}
        />
      ),
    })

    return () => unsubscribe()
  },
})
