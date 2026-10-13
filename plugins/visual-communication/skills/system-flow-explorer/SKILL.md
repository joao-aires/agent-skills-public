---
name: system-flow-explorer
description: Build an explorable, standalone HTML architecture and message-flow explorer from repository evidence or a proposed design. Use when users want to explore a service or repository's architecture, capabilities, dataflow, request lifecycle, sequence messages, or C4 context/container/component views; also use for brainstorming and refining proposed system designs with these views. Keep user scenarios, diagram views, and architecture depth separate. Not for unrelated UI design, generic charts, or application feature implementation.
metadata:
  scope: generic
  invocation: user
compatibility: Python 3.10+ standard library for validation and rendering. Optional browser verification uses an existing Playwright installation; delivered HTML needs no dependencies or server.
---

# System flow explorer

Produce one self-contained HTML file backed by a canonical JSON model. Use the bundled renderer rather than generating scenario-specific JavaScript. Deliver the source JSON alongside the HTML for refinement.

Use this when an interactive architecture artifact is requested. For an evidence inventory or topology review without an explorer, use `system-mapping` when available; for a compact static diagram, use `architecture-diagraming`. Reuse their evidence rather than repeat discovery. The renderer is an optional documentation artifact, not application scaffolding.

## Workflow

1. Identify the repository/service or proposed design, the audience, and the user scenarios. Infer these from the conversation; ask only about material gaps. Repository analysis and ideation are both first-class modes. A mixed design should label each implemented, proposed, and unresolved part individually.
2. Read [analysis guidance](references/analysis.md). For repository work, inspect applicable agent guidance, entrypoints, route registration, service clients, persistence, and representative request paths. Treat documentation as a lead and check code. For brainstorming, record assumptions and open decisions explicitly.
3. Read [the model contract](references/schema.md), then create JSON using `assets/minimal.json` as a structural example. Model actors and ownership before messages. Record paths/line ranges or supplied design citations in `sources`. Cite implemented claims. Use illustrative payload labels unless samples were actually observed; redact secrets and personal data.
4. Add scenario roots in chronological order and optional component substeps linked by `parentId`. Preserve root IDs, payloads, and order while refining. Components belong to containers; external services/models stay in their own external systems. Flow tabs represent user scenarios only. Sequence versus C4 is a view; context/container/component is a separate depth selector.
5. Validate and render (replace paths, run from any directory):

   ```sh
   python3 <skill>/scripts/validate.py model.json
   python3 <skill>/scripts/render.py model.json explorer.html
   python3 <skill>/scripts/smoke_test.py
   ```

   The renderer validates before writing and escapes script-breaking JSON. It uses no external assets. Treat validation as structural assurance, not proof that a claim is true or that model-generated prose is grounded.
6. If an existing Playwright installation is available, verify the actual artifact:

   ```sh
   node <skill>/scripts/browser_test.cjs explorer.html /absolute/path/to/frontend/node_modules
   ```

   This checks selection across depth/view changes, parent preservation, external containment, raw JSON copying, navigation, and tab keyboard behavior. Do not install browser dependencies merely to render. Report browser checks as skipped if unavailable.
7. Deliver the HTML and JSON paths, evidence scope, uncertainty, and checks actually run. Describe conclusions and open decisions succinctly. For refinements, explain what changed and preserve stable IDs so selections remain meaningful.

## Modeling decisions

- Capture routes/methods from actual registration and clients. An existing route with a proposed envelope can have endpoint status `actual` and message status `proposed`. Unresolved endpoints have a null URL; local function calls, rendering, and navigation have no invented network endpoint.
- Use request/response/event directions and valid JSON payloads, including JSON strings for text. Copy always serializes the complete raw value, regardless of collapsed sections.
- When helpful, include context lifetime, state reads/writes, persistence ownership, transforms, prompt messages, tool schemas/results, and field provenance in `examples` and `payloadProvenance`. These are optional; do not impose LLM or persistence concepts on systems without them.
- Distinguish observed samples, illustrative examples, proposed bodies, and derived projections. Ground qualitative explanations in relevant facts/citations; matching a schema proves shape, not truth. See the reference for missing-data, failure, streaming, and cancellation coverage.
- Expand one chosen container at component depth while keeping all other containers and every outer interaction visible. Internal substeps carry parent.child numbers and map back to their parent at shallower depths. Re-expanding restores a remembered child selection.

## Resources

- `assets/explorer.html`: generic offline template, canonical data injected by renderer.
- `assets/minimal.json`: two generic scenarios, implemented/proposed/unresolved messages, a component drill-down, and an external model example.
- `scripts/validate.py`: deterministic model validation and projection shared by smoke tests.
- `scripts/render.py`: safe JSON injection, no third-party runtime dependencies.
- `scripts/smoke_test.py`, `scripts/browser_test.cjs`: structural and semantic browser checks.
- `evals/evals.json`: repository, proposal, and refinement evaluation prompts.
