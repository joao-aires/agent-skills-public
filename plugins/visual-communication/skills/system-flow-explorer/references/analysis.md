# Evidence and design analysis

## Repository mode

Start with scope: service, entrypoints, scenario, branch/revision if available, and static analysis versus an observed trace. Do not claim runtime verification from reading code. Attribute a Git revision only to evidence actually present in it; label supplied or uncommitted files as working-copy evidence. Follow applicable repository guidance without changing application files merely to visualize them.

Trace representative scenarios from user/client to ingress, authentication/validation, dispatch, domain logic, clients/storage, and response/stream handling. Inspect route mounting/prefixes and base-URL configuration, not just a function decorator. Identify who owns data, who transforms it, and which external boundaries are crossed. Cite paths and meaningful line ranges; retain contradictory or missing evidence as an unresolved decision rather than choosing an attractive story.

Inventory capabilities from actual public operations, registrations, dispatch tables, tools, and caller integrations. Separate reachable implemented behavior from unused helpers, rollback paths, tests, and proposal documents. Read tests as behavioral evidence but do not portray test fixtures as observed production payloads.

Select 1–4 useful user scenarios. Do not make tabs called “runtime,” “C4,” or “components”: those are views/depths of a scenario. Include important failure/cancellation paths as separate scenarios or explanatory substeps when they change the user outcome. Keep the full scenario visible during drill-down, including interactions outside the expanded runtime.

## Ideation mode

Translate intent into responsibilities, trust/data ownership, request lifetimes, and proposed interactions before naming libraries. Ask about consequential ambiguity; otherwise state assumptions and produce a concrete proposed design. Mark proposed endpoint URLs as proposed, not discovered. Use `unresolved` and null URLs when transport details are undecided. Cite the supplied brief as a design source, not implementation evidence.

Do not copy the source reference's domain, operation names, services, frontend framework, agent framework, or transport. It illustrates interaction patterns, not a required architecture. The bundled fixture is similarly illustrative: every invocation can use different actors, payloads, and scenarios.

## Ownership and refinement

Use person → system → container → component hierarchy with external systems as siblings of the analyzed system. An external model provider is not a runtime component. An in-process model adapter can be a runtime component calling that provider. A database deployed separately is a container or external service, not a component because one library accesses it.

At context depth project containers to their system; at container depth project components to their container. At component depth expand the chosen container only. The outer message remains present, now attached to a component only if `fromComponent`/`toComponent` is declared. Do not synthesize endpoint rewrites or duplicate root payloads. Add internal messages via `parentId` and `within`; their endpoints must be components of the declared container touched by the root. For external requests use a root interaction to the external service rather than hiding it in an internal substep.

Stable IDs carry identity; numbering is derived from the root order in each scenario. Additions preserve IDs even if numbers move. On a shallow view, selecting a child maps to the root; returning to the expanded container restores that child. View changes never change the scenario or selected message.

## Context and payload provenance

Use optional `examples` on messages for request-scoped context, session/state, persistence, transforms, prompt/tool schemas, tool results, or response bodies. Each example has a label, kind, JSON value, provenance, and optional note. Explain lifetimes and ownership in notes; show read/write/failure behavior when relevant.

Use `payloadProvenance.kind`: `observed`, `illustrative`, `derived`, or `proposed`. Observed and derived values need citations. For a projection/transform, add `fields` records identifying a JSON pointer, its upstream origin, and citations. A path explains provenance; it does not prove that a semantic inference is true. For LLM explanations, identify facts that support the statement and limitations on interpretation. Structural schema validation and factual grounding are distinct checks.

Report missing facts as missing. Avoid unsupported claims inferred from unrelated measurements. Redact real samples without presenting them as raw originals. For streamed output, show a concrete event example and describe completion, correlation, stale-response rejection, and failure behavior based on evidence or clearly labeled design choices.
