import { Plugin } from "@opencode/plugin"
import { Sdlc } from "./rpc.js"
import { apply as applyState, emptyState, migrateState } from "../core/state.js"
import { createQueue } from "../core/queue.js"
import { applyExtraction, buildExtractionPrompt, latestUserText, parseExtraction } from "../core/extract.js"
import {
  buildDecisionInput,
  buildDecisionQuestions,
  DEFAULT_DECISION_MODEL,
  decisionHints,
  gateCommands,
  interpretDecisions,
  shouldExtract,
} from "../core/decision.js"

/**
 * OpenCode server adapter.
 *
 * State is stored per session in the plugin's durable server storage, cached
 * in this process, and mirrored by the TUI over RPC. It is not written to the
 * repository or synchronized with the ECR.
 */

const store = ((globalThis as any).__sdlcModSessions ??= new Map())
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

    const loading = new Map()
    const keyFor = (sessionID) => `session/${sessionID}`

    async function ensureState(sessionID) {
      const cached = store.get(sessionID)
      if (cached && cached.version === 3) return cached
      if (loading.has(sessionID)) return loading.get(sessionID)

      const promise = (async () => {
        const saved = await ctx.storage.get(keyFor(sessionID))
        const state = migrateState(saved as any) ?? emptyState(sessionID)
        store.set(sessionID, state)
        return state
      })()

      loading.set(sessionID, promise)
      try {
        return await promise
      } finally {
        loading.delete(sessionID)
      }
    }

    async function persist(sessionID, state) {
      store.set(sessionID, state)
      try {
        await ctx.storage.set(keyFor(sessionID), state)
      } catch {
        // The in-memory state is still valid for this server lifetime.
      }
    }

    const withMutation = createQueue()

    function assertSessionID(value) {
      if (typeof value !== "string" || !/^[A-Za-z0-9_-]+$/.test(value)) {
        throw new Error("invalid session id")
      }
      return value
    }

    let registration
    registration = await ctx.rpc.register(Sdlc, {
      snapshot: async ({ sessionID }) => ({ state: await ensureState(assertSessionID(sessionID)) }),
      apply: async ({ sessionID, command }) => {
        assertSessionID(sessionID)
        return withMutation(async () => {
          const next = applyState(await ensureState(sessionID), command)
          await persist(sessionID, next)
          await registration.events.emit("updated", { sessionID, state: next })
          return { state: next }
        })
      },
      setAuto: async ({ enabled }) => {
        autoEnabled = Boolean(enabled)
        if (!autoEnabled) clearTimers()
        return { enabled: autoEnabled }
      },
    })

    const timers = new Map()
    const running = new Set()
    const generating = new Set()
    const lastExtracted = new Map()
    const deleted = new Set()

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
      if (!autoEnabled || running.has(sessionID) || deleted.has(sessionID)) return
      running.add(sessionID)
      try {
        let before = await ensureState(sessionID)
        const messages = await ctx.session.context({ sessionID })
        const lastMessage = [...messages].reverse().find((message) => message?.id)
        if (lastMessage?.id && lastExtracted.get(sessionID) === lastMessage.id) return
        if (lastMessage?.id) lastExtracted.set(sessionID, lastMessage.id)
        const decision = await decide(sessionID, messages, before)
        const threshold = Number(options.gateThreshold)
        const focus = before.threads.find((thread) => thread.id === before.focusThreadId)
        const extract =
          !decision ||
          shouldExtract(decision, {
            probabilityThreshold: Number.isFinite(threshold) ? threshold : 0.5,
            currentActivity: focus?.activity ?? null,
            currentFocus: before.focusThreadId,
          })

        const hints = latestUserText(messages)
        const structural = await withMutation(async () => {
          if (deleted.has(sessionID)) return null
          const current = await ensureState(sessionID)
          let next = current
          for (const command of gateCommands(decision, current, { latestText: hints })) {
            try {
              next = applyState(next, command)
            } catch {
              // A structural hint that no longer applies is ignored.
            }
          }
          if (JSON.stringify(next) === JSON.stringify(current)) return current
          await persist(sessionID, next)
          await registration.events.emit("updated", { sessionID, state: next })
          return next
        })
        if (structural) before = structural
        if (!extract) return

        const prompt = buildExtractionPrompt({
          state: before,
          messages,
          includeMessages: Number(options.includeMessages) || 8,
          hints: decisionHints(decision),
        })
        generating.add(sessionID)
        let response
        try {
          response = await ctx.session.generate({ sessionID, prompt })
        } finally {
          generating.delete(sessionID)
        }
        if (deleted.has(sessionID)) return
        const parsed = parseExtraction(response?.text)
        if (!parsed) return

        await withMutation(async () => {
          if (deleted.has(sessionID)) return
          const current = await ensureState(sessionID)
          const result = applyExtraction(current, parsed, {
            minConfidence: Number(options.minConfidence) || 0.7,
          })
          if (!result.changed || !result.applied.length) return
          await persist(sessionID, result.state)
          await registration.events.emit("updated", { sessionID, state: result.state })
        })
      } catch (error) {
      } finally {
        running.delete(sessionID)
      }
    }

    const controller = new AbortController()
    void (async () => {
      try {
        for await (const event of ctx.event.subscribe({
          types: ["session.execution.succeeded", "session.execution.started", "session.deleted"],
          signal: controller.signal,
        })) {
          const sessionID = event?.data?.sessionID ?? event?.data?.id
          if (!sessionID) continue

          if (event.type === "session.deleted") {
            deleted.add(sessionID)
            const timer = timers.get(sessionID)
            if (timer) clearTimeout(timer)
            timers.delete(sessionID)
            lastExtracted.delete(sessionID)
            generating.delete(sessionID)
            store.delete(sessionID)
            loading.delete(sessionID)
            void ctx.storage.remove(keyFor(sessionID)).catch(() => {})
            continue
          }

          if (event.type === "session.execution.started") {
            deleted.delete(sessionID)
            const timer = timers.get(sessionID)
            if (timer) {
              clearTimeout(timer)
              timers.delete(sessionID)
            }
            continue
          }
          if (!autoEnabled) continue

          if (generating.has(sessionID)) continue
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


