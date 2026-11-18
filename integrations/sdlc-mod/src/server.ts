import { Plugin } from "@opencode/plugin"
import { Sdlc } from "./rpc.js"
import { apply as applyState, emptyState } from "../core/state.js"
import { applyExtraction, buildExtractionPrompt, parseExtraction } from "../core/extract.js"
import {
  buildDecisionInput,
  buildDecisionQuestions,
  DEFAULT_DECISION_MODEL,
  decisionHints,
  interpretDecisions,
  shouldExtract,
} from "../core/decision.js"

/**
 * OpenCode server adapter.
 *
 * State lives in this server process, keyed by session, and is discarded when
 * the server stops. It is not written to the repository or synchronized with
 * the ECR. The TUI mirrors it over RPC.
 */

const sessions = new Map()
let autoEnabled = true
let options = {
  auto: true,
  debounceMs: 1500,
  minConfidence: 0.7,
  includeMessages: 8,
  gate: true,
  gateThreshold: 0.5,
  gateMessages: 2,
  decisionModel: DEFAULT_DECISION_MODEL,
}

export default Plugin.define({
  id: "sdlc-mod",
  async setup(ctx) {
    options = { ...options, ...(ctx.options ?? {}) }
    autoEnabled = options.auto !== false

    let registration
    registration = await ctx.rpc.register(Sdlc, {
      snapshot: async ({ sessionID }) => ({ state: stateFor(sessionID) }),
      apply: async ({ sessionID, command }) => {
        const next = applyState(stateFor(sessionID), command)
        sessions.set(sessionID, next)
        await registration.events.emit("updated", { sessionID, state: next })
        return { state: next }
      },
      setAuto: async ({ enabled }) => {
        autoEnabled = Boolean(enabled)
        if (!autoEnabled) clearTimers()
        return { enabled: autoEnabled }
      },
    })

    const timers = new Map()
    const running = new Set()
    const cooldown = new Map()

    function clearTimers() {
      for (const timer of timers.values()) clearTimeout(timer)
      timers.clear()
    }

    function schedule(sessionID) {
      if (!autoEnabled) return
      const existing = timers.get(sessionID)
      if (existing) clearTimeout(existing)
      const timer = setTimeout(() => {
        timers.delete(sessionID)
        void extract(sessionID)
      }, Number(options.debounceMs) || 1500)
      timers.set(sessionID, timer)
    }

    async function decide(sessionID, messages, state) {
      if (options.gate === false || !ctx.experimental?.generate?.decisions) return null
      const model = modelRef(options.decisionModel)
      if (!model) return null
      try {
        const result = await ctx.experimental.generate.decisions({
          model,
          input: [
            {
              type: "text",
              text: buildDecisionInput({
                state,
                messages,
                includeMessages: Number(options.gateMessages) || 2,
              }),
            },
          ],
          questions: buildDecisionQuestions(state),
        })
        return interpretDecisions(result)
      } catch {
        return null
      }
    }

    async function extract(sessionID) {
      if (!autoEnabled || running.has(sessionID)) return
      running.add(sessionID)
      try {
        const before = stateFor(sessionID)
        const messages = await ctx.session.context({ sessionID })
        const decision = await decide(sessionID, messages, before)
        const threshold = Number(options.gateThreshold)
        const focus = before.threads.find((thread) => thread.id === before.focusThreadId)
        if (
          decision &&
          !shouldExtract(decision, {
            probabilityThreshold: Number.isFinite(threshold) ? threshold : 0.5,
            currentActivity: focus?.activity ?? null,
            currentFocus: before.focusThreadId,
          })
        ) {
          return
        }
        const prompt = buildExtractionPrompt({
          state: before,
          messages,
          includeMessages: Number(options.includeMessages) || 8,
          hints: decisionHints(decision),
        })
        const response = await ctx.session.generate({ sessionID, prompt })
        const parsed = parseExtraction(response?.text)
        if (!parsed) return

        const result = applyExtraction(before, parsed, {
          minConfidence: Number(options.minConfidence) || 0.7,
        })
        if (!result.changed || !result.applied.length) return

        sessions.set(sessionID, result.state)
        await registration.events.emit("updated", { sessionID, state: result.state })
      } catch (error) {
      } finally {
        running.delete(sessionID)
        cooldown.set(sessionID, Date.now() + 3000)
      }
    }

    const controller = new AbortController()
    void (async () => {
      try {
        for await (const event of ctx.event.subscribe({
          types: ["session.execution.succeeded", "session.execution.started"],
          signal: controller.signal,
        })) {
          const sessionID = event?.data?.sessionID ?? event?.data?.id
          if (!sessionID) continue

          if (event.type === "session.execution.started") {
            const timer = timers.get(sessionID)
            if (timer) {
              clearTimeout(timer)
              timers.delete(sessionID)
            }
            continue
          }
          if (!autoEnabled) continue

          if (Date.now() < (cooldown.get(sessionID) ?? 0)) continue
          const session = await ctx.session.get({ sessionID }).catch(() => undefined)
          if (!session || session.parentID) continue
          schedule(sessionID)
        }
      } catch {
        // The event stream closes when the plugin unloads.
      }
    })()

    return () => {
      controller.abort()
      clearTimers()
    }
  },
})

function modelRef(value) {
  const [providerID, ...rest] = String(value ?? "").split("/")
  if (!providerID || !rest.length) return null
  return { providerID, id: rest.join("/") }
}

function stateFor(sessionID) {
  let state = sessions.get(sessionID)
  if (!state) {
    state = emptyState(sessionID)
    sessions.set(sessionID, state)
  }
  return state
}

