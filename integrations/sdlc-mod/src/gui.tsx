import { For, Show, createEffect, createSignal, onCleanup } from "solid-js"
import { createStore } from "solid-js/store"
import { Command, ComposerPill, Panel, Plugin, type PanelTab } from "@opencode/plugin/gui"
import { Sdlc } from "./rpc.js"
import { emptyState } from "../core/state.js"
import {
  decisionGlyph,
  summaryLabel,
  matrixCell,
  matrixThreads,
  phaseMarker,
  PHASES,
  threadCode,
  threadGlyph,
} from "../core/view.js"
import { parseCommand } from "../core/commands.js"

const PHASE_LABEL = {
  requirements: "req",
  design: "des",
  implementation: "imp",
  testing: "tst",
  operations: "ops",
}

const [states, setStates] = createStore<Record<string, any>>({})
const requested = new Set<string>()
const inFlight = new Set<string>()

function rpc(ctx) {
  return ctx.client.rpc(Sdlc)
}

function ensureState(ctx, sessionID, force = false) {
  if (!sessionID || inFlight.has(sessionID)) return
  if (!force && requested.has(sessionID)) return
  requested.add(sessionID)
  inFlight.add(sessionID)
  rpc(ctx)
    .snapshot({ sessionID })
    .then((result) => setStates(sessionID, result.state))
    .catch(() => {})
    .finally(() => inFlight.delete(sessionID))
}

function cellColor(glyph) {
  if (glyph === "✓") return "#7fd18b"
  if (glyph === "!") return "#e06c75"
  if (glyph === "◐") return "#f0b45e"
  if (glyph === "●") return "#7fd18b"
  if (glyph === "○") return "#8d9399"
  return "#5f656b"
}

function SdlcPanel(props) {
  const [page, setPage] = createSignal(0)
  const current = () => states[props.session.id] ?? emptyState(props.session.id)
  const focus = () => current().threads.find((thread) => thread.id === current().focusThreadId) ?? null
  const pages = () => matrixThreads(current(), 3, page())

  createEffect(() => {
    const sessionID = props.session.id
    void ensureState(props.ctx, sessionID)
    const timer = setInterval(() => ensureState(props.ctx, sessionID, true), 15_000)
    onCleanup(() => clearInterval(timer))
  })

  const step = (delta) => {
    const total = pages().pages
    setPage((value) => (value + delta + total) % total)
  }

  const openArtifact = (artifact) => {
    try {
      void Promise.resolve(props.ctx.system.openExternal(artifact.href)).catch(() => {})
    } catch {
      // Leave the link visible if the host cannot open it.
    }
  }

  const mono = {
    "font-family": "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace",
    "font-size": "12px",
    "line-height": "1.55",
  }

  return (
    <div style={{ display: "flex", "flex-direction": "column", gap: "8px", padding: "10px", ...mono }}>
      <div style={{ display: "flex", "align-items": "baseline", gap: "8px" }}>
        <strong>SDLC</strong>
        <span style={{ opacity: 0.62, "font-size": "11px" }}>{summaryLabel(current())}</span>
      </div>

      <div
        style={{
          display: "grid",
          "grid-template-columns": "10ch repeat(3, 8ch)",
          "align-items": "center",
          gap: "0",
          opacity: 0.96,
        }}
      >
        <div />
        <For each={pages().shown}>
          {(thread) => (
            <div style={{ "text-align": "center", "font-weight": 650 }}>
              {thread.source === "inferred" ? "~" : ""}
              {thread.id}
            </div>
          )}
        </For>
        <div />
        <For each={pages().shown}>
          {(thread) => (
            <div style={{ "text-align": "center", opacity: 0.55, "font-size": "9px" }}>{thread.ticket ?? ""}</div>
          )}
        </For>

        <For each={PHASES}>
          {(phase) => (
            <>
              <div style={{ opacity: 0.7, "white-space": "nowrap" }}>
                {phaseMarker(phase, focus()?.activity, focus()?.completedPhases ?? [])} {PHASE_LABEL[phase]}
              </div>
              <For each={pages().shown}>
                {(thread) => {
                  const glyph = matrixCell(thread, phase, current().focusThreadId)
                  return (
                    <div style={{ "text-align": "center", color: cellColor(glyph), "font-weight": 600 }}>
                      {glyph}
                    </div>
                  )
                }}
              </For>
            </>
          )}
        </For>
      </div>

      <Show when={pages().pages > 1}>
        <div style={{ display: "flex", "align-items": "center", gap: "8px", opacity: 0.7 }}>
          <button type="button" onClick={() => step(-1)} style={{ cursor: "pointer" }}>
            prev
          </button>
          <span>
            page {pages().page + 1}/{pages().pages}
          </span>
          <button type="button" onClick={() => step(1)} style={{ cursor: "pointer" }}>
            next
          </button>
        </div>
      </Show>

      <Show when={focus()}>
        <div style={{ display: "flex", "flex-direction": "column", gap: "2px" }}>
          <div>
            <span style={{ color: cellColor(threadGlyph(focus(), true)) }}>{threadGlyph(focus(), true)}</span>{" "}
            <strong>
              {threadCode(focus())} {focus().name}
            </strong>
          </div>
          <div style={{ opacity: 0.65 }}>
            {focus().activity} · {focus().status}
            {focus().status === "blocked" && focus().blockReason ? ` · ${focus().blockReason}` : ""}
          </div>
          <For each={focus().artifacts ?? []}>
            {(artifact) => (
              <a
                href={artifact.href}
                onClick={(event) => {
                  event.preventDefault()
                  openArtifact(artifact)
                }}
                style={{ color: "inherit", opacity: 0.8, "text-decoration": "underline" }}
              >
                ↗ {artifact.label}
              </a>
            )}
          </For>
        </div>
      </Show>

      <Show when={current().decisions.length > 0}>
        <div style={{ display: "flex", "flex-direction": "column", gap: "2px", "border-top": "1px solid #2a3036", "padding-top": "7px" }}>
          <strong>Decisions</strong>
          <For each={current().decisions}>
            {(decision) => (
              <div style={{ opacity: decision.status === "open" ? 0.95 : 0.62 }}>
                <span style={{ color: decision.status === "open" ? "#f0b45e" : "#7fd18b" }}>
                  {decisionGlyph(decision.status)}
                </span>{" "}
                {decision.id} {decision.statement}
                {decision.threadId ? ` · ${decision.threadId}` : ""}
              </div>
            )}
          </For>
        </div>
      </Show>

      <Show when={!current().threads.length}>
        <div style={{ opacity: 0.6 }}>No threads · /sdlc thread add</div>
      </Show>
    </div>
  )
}

export default Plugin.define({
  setup(ctx) {
    const tab: PanelTab = {
      id: "main",
      get title() {
        return "SDLC"
      },
      closable: "compact",
      fallback: true,
    }

    let unsubscribe = () => {}
    try {
      unsubscribe = rpc(ctx).events.on("updated", (event) => {
        setStates(event.data.sessionID, event.data.state)
      })
    } catch {
      // The server part may not be ready yet; snapshot retries cover it.
    }

    ctx.add(Panel, {
      id: "main",
      region: "side",
      width: 420,
      mobile: {
        get title() {
          return "SDLC"
        },
        order: 45,
        kind: "menu",
      },
      list: (input) => (input.open.includes("main") ? [tab] : []),
      render: (props) => <SdlcPanel ctx={ctx} session={props.session} />,
    })

    ctx.add(ComposerPill, {
      id: "status",
      show: (input) => {
        const sessionID = input.session.id
        void ensureState(ctx, sessionID)
        const current = states[sessionID]
        if (!current) return undefined
        const focus = current.threads.find((thread) => thread.id === current.focusThreadId)
        const open = current.decisions.filter((decision) => decision.status === "open").length
        return {
          label: `SDLC · ${focus?.name ?? "no focus"} · ${open} open`,
          title: "SDLC",
          run: () => ctx.layout.toggle(`${ctx.id}:main`, input.session),
          rows: current.threads.slice(0, 4).map((thread) => ({
            id: thread.id,
            label: `${threadGlyph(thread, thread.id === current.focusThreadId)} ${threadCode(thread)} ${thread.name}`,
            detail: thread.activity,
            run: () => {
              void rpc(ctx)
                .apply({ sessionID, command: { type: "thread.focus", id: thread.id } })
                .then((result) => setStates(sessionID, result.state))
                .catch(() => {})
            },
          })),
        }
      },
    })

    ctx.add(Command, () => ({
      id: "toggle",
      title: "SDLC: Toggle panel",
      group: "SDLC",
      slash: { name: "sdlc", arguments: true },
      run: async (input) => {
        const session = ctx.sessions.current()
        if (!session) return
        try {
          const parsed = parseCommand(input)
          if (parsed.kind === "read") {
            ctx.layout.toggle(`${ctx.id}:main`, session)
            return
          }
          if (parsed.kind === "auto") {
            await rpc(ctx).setAuto({ enabled: parsed.enabled })
            return
          }
          if (parsed.kind === "help") {
            ctx.layout.toggle(`${ctx.id}:main`, session)
            return
          }
          const result = await rpc(ctx).apply({ sessionID: session.id, command: parsed.command })
          setStates(session.id, result.state)
        } catch {
          // The panel remains available for inspection.
        }
      },
    }))

    const resync = setInterval(() => {
      for (const sessionID of requested) ensureState(ctx, sessionID, true)
    }, 15_000)

    return () => {
      unsubscribe()
      clearInterval(resync)
    }
  },
})
