import { createEffect, createSignal, For, Show } from "solid-js"
import { Plugin } from "@opencode/plugin/tui"
import { emptyState, renderCompact } from "../core/state.js"
import { HELP, parseCommand } from "../core/commands.js"
import { decisionGlyph, matrixCell, matrixThreads, phaseMarker, PHASES, summaryLabel, threadCode, threadGlyph } from "../core/view.js"
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

const PHASE_LABEL = {
  requirements: "req",
  design: "des",
  implementation: "imp",
  testing: "tst",
  operations: "ops",
}


function SdlcSidebar(props) {
  const theme = props.context.theme
  const current = () => props.state()
  const columns = () => matrixThreads(current(), 3)
  const focus = () => current().threads.find((thread) => thread.id === current().focusThreadId) ?? null
  const focusPhase = () => focus()?.activity ?? null

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

  const phaseColor = (phase) => {
    const marker = phaseMarker(phase, focusPhase())
    if (marker === "✓") return theme.text.feedback.success.base
    if (marker === "▶") return theme.text.base
    return theme.text.muted
  }

  const cellColor = (thread, phase) => {
    const cell = matrixCell(thread, phase, current().focusThreadId)
    if (cell === "✓") return theme.text.feedback.success.base
    if (cell === "!") return theme.text.feedback.error.base
    if (cell === "◐") return theme.text.feedback.warning.base
    if (cell === "·" || cell === "○") return theme.text.muted
    return theme.text.base
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

      <Show
        when={columns().shown.length > 0}
        fallback={<text fg={theme.text.muted}>No threads · /sdlc thread add</text>}
      >
        <box flexDirection="column">
          <box flexDirection="row">
            <box width={10} flexShrink={0}>
              <text> </text>
            </box>
            <For each={columns().shown}>
              {(thread) => (
                <box width={9} flexShrink={0} flexDirection="row" justifyContent="center">
                  <text fg={thread.id === current().focusThreadId ? theme.text.base : theme.text.muted}>
                    {thread.source === "inferred" ? "~" : ""}
                    {thread.id}
                  </text>
                </box>
              )}
            </For>
          </box>
          <box flexDirection="row">
            <box width={10} flexShrink={0}>
              <text> </text>
            </box>
            <For each={columns().shown}>
              {(thread) => (
                <box width={9} flexShrink={0} flexDirection="row" justifyContent="center">
                  <text fg={theme.text.muted} wrapMode="none" truncate>
                    {thread.ticket ?? ""}
                  </text>
                </box>
              )}
            </For>
          </box>
          <For each={PHASES}>
            {(phase) => (
              <box flexDirection="row">
                <box width={10} flexShrink={0}>
                  <text fg={phaseColor(phase)}>
                    {phaseMarker(phase, focusPhase())} {PHASE_LABEL[phase]}
                  </text>
                </box>
                <For each={columns().shown}>
                  {(thread) => (
                    <box width={9} flexShrink={0} flexDirection="row" justifyContent="center">
                      <text fg={cellColor(thread, phase)}>{matrixCell(thread, phase, current().focusThreadId)}</text>
                    </box>
                  )}
                </For>
              </box>
            )}
          </For>
          <Show when={columns().hidden > 0}>
            <text fg={theme.text.muted}>
              {"+"}
              {columns().hidden}
              {" more threads"}
            </text>
          </Show>
        </box>
      </Show>

      <Show when={focus()}>
        <box flexDirection="column">
          <box flexDirection="row" gap={1} minWidth={0}>
            <text fg={threadColor(theme, focus(), true)}>{threadGlyph(focus(), true)}</text>
            <text fg={theme.text.muted} flexShrink={0}>
              {threadCode(focus())}
            </text>
            <text fg={theme.text.base} flexGrow={1} flexShrink={1} minWidth={0} wrapMode="none" truncate>
              <b>{focus().name}</b>
            </text>
          </box>
          <text fg={theme.text.muted} wrapMode="none" truncate>
            {"  "}
            {focus().activity}
            {" · "}
            {focus().status}
          </text>
        </box>
      </Show>

      <Show when={props.view.open}>
        <Show when={focus()?.artifacts?.length}>
          <For each={focus().artifacts}>
            {(artifact) => (
              <text fg={theme.text.muted} wrapMode="none" truncate>
                {"  ↗ "}
                {artifact.label}
              </text>
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
      </Show>

      <Show when={!props.view.open}>
        <text fg={theme.text.muted}>expand for artifacts and decisions</text>
      </Show>
    </box>
  )
}

function SdlcDialog(props) {
  const theme = props.context.theme
  const current = () => props.state()
  const focused = (thread) => thread.id === current().focusThreadId

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
          fallback={<text fg={theme.text.muted}>No threads yet. /sdlc thread add "pagination works" implementation</text>}
        >
          <box flexDirection="row" gap={1}>
            <text fg={theme.text.muted} width={1}>
              {" "}
            </text>
            <text fg={theme.text.muted} width={14}>
              ID
            </text>
            <text fg={theme.text.muted} flexGrow={3}>
              Work
            </text>
            <text fg={theme.text.muted} width={14}>
              Phase
            </text>
            <text fg={theme.text.muted} width={8}>
              Status
            </text>
          </box>
          <For each={current().threads}>
            {(thread) => (
              <box flexDirection="column">
                <box flexDirection="row" gap={1} minWidth={0}>
                  <text fg={threadColor(theme, thread, focused(thread))}>{threadGlyph(thread, focused(thread))}</text>
                  <text fg={theme.text.muted} width={14} wrapMode="none" truncate>
                    {thread.source === "inferred" ? "~" : ""}
                    {threadCode(thread)}
                  </text>
                  <text
                    fg={focused(thread) ? theme.text.base : theme.text.muted}
                    flexGrow={3}
                    flexShrink={1}
                    minWidth={0}
                    wrapMode="none"
                    truncate
                  >
                    {thread.name}
                  </text>
                  <text fg={theme.text.muted} width={14} wrapMode="none" truncate>
                    {thread.activity}
                  </text>
                  <text fg={threadColor(theme, thread, focused(thread))} width={8}>
                    {thread.status}
                  </text>
                </box>
                <Show when={thread.stoppingPoint || thread.artifacts?.length}>
                  <text fg={theme.text.muted} wrapMode="none" truncate>
                    {"    "}
                    {thread.stoppingPoint ?? "no stopping point"}
                    {thread.artifacts?.length ? ` · ${thread.artifacts.map((artifact) => artifact.label).join(" · ")}` : ""}
                  </text>
                </Show>
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
                  {decision.threadId ?? decision.owner ?? "unowned"}
                </text>
              </box>
            )}
          </For>
        </Show>
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
