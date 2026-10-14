---
name: design-interactions
description: Define and verify frontend user journeys, navigation, menus, dialogs,
  forms and shared interaction patterns before meaningful UI implementation. Use for
  new UX, cross-screen redesigns, global component changes or inconsistent behavior;
  inventory all affected surfaces and states instead of improvising each page.
user-invocable: false
metadata:
  scope: generic
  invocation: both
  role: support
---

# Design interactions before implementation

Use this with frontend-conventions for the actual stack/design direction. It defines behavior and coverage, not a new visual framework. Apply it automatically to relevant requested work; users do not need to remember the skill name. A typo, a tiny token adjustment or unchanged interaction needs proportionate reasoning, not a fresh full design document.

## Discover the full affected experience

Read the request, accepted UX/product decisions, references and existing components/routes. Inspect the rendered application when available and distinguish observed behavior from code assumptions. Map user roles, tasks and entry/exit points before choosing widgets. Preserve established branding, density, navigation and business language unless changing them is the request.

For global work, inventory affected menus/submenus, routes, tabs, forms, dialogs/drawers, tables, mobile variants and role/feature-conditional views. Trace shared primitives and route-level overrides; a component search alone does not prove all actual surfaces are covered. Keep a concise coverage list in existing notes/plan with surface, intended pattern/behavior, relevant states, implementation and verification status. Mark unknown/inaccessible surfaces and exclusions explicitly. Do not quietly reduce “all menus and dialogs” to the first page visited.

## Specify the interaction before coding

For each reusable interaction pattern, define user goal, visible information hierarchy, primary/secondary actions, navigation/deep-link/back behavior, state ownership and success/failure transitions. Cover relevant loading, empty, validation, disabled/permission, error/retry, unsaved edits/cancel, duplicate submission and destructive/recovery behavior. Include async progress, stale responses and persistence/reload where the flow depends on them. Do not invent user research or business rules.

Specify keyboard/focus behavior, dialog open/close and focus return, labels, announcements and responsive changes. Choose page versus drawer versus dialog from task complexity and continuity, not a different preference per screen. Distinguish navigational submenus from sibling page tabs and context actions. Define shared behavior/tokens and intentional contextual variants; consistency does not mean ignoring different user goals or mobile constraints.

Write a short behavioral description or state/transition table before implementation. Add low-fidelity wireframes/wireflows for layout/navigation uncertainty or representative mockups for a new visual direction. Existing text/visual references can be reused; do not require text plus wireframe plus mockup for every change. A mockup shows appearance, not persistence, authorization or complete interaction behavior.

Ask only unresolved high-impact design/product questions. State reversible visual assumptions and proceed where the direction is established. If a material decision is genuinely required, wait for it before dependent implementation; continue independent work. Do not demand fresh approval per screen or re-open previously agreed direction. Unattended work records blocking decisions instead of inventing stakeholder answers. The design can live in the conversation or an existing project note, without a compulsory format.

## Validate a pattern, then apply it consistently

Select representative complex and simple surfaces, including a dialog/mobile or role variant when relevant. Establish the shared implementation against the behavioral design before propagation. Reuse the project's primitives, tokens and composed components; fix a shared pattern centrally when appropriate rather than patching pages with divergent overrides. Preserve legitimate variants with explicit reasons.

Apply the change to every in-scope surface in the coverage list. An unfinished batch remains partial; do not silently defer inconvenient menus/dialogs. Reconcile the list after implementation and search for old patterns, alternate entry points, portals, route overrides and conditional rendering that can escape the main component. Treat an unexplained exception as a finding to resolve, not another ad hoc design.

## Verify the experience and coverage

Inspect actual desktop/mobile surfaces and critical interactions against the specified behavior, not only screenshots of one representative page. Exercise keyboard/focus, errors, validation and permission differences; use test-end-to-end and relevant browser tools when available. Capture useful visual evidence and checks for repeated patterns, but do not duplicate every logic test in the browser. A shared component test does not prove every caller uses it correctly.

For a request changing all menus/dialogs, account for each surface: implemented and observed/checked, unchanged with a reason, explicitly out of scope, or blocked/unverified. Report unresolved coverage and material deviations. Do not label global consistency verified when only one route or the build was checked. Keep the accepted interaction patterns and affected docs/tests aligned; later features should reuse this design instead of improvising again.

For contract boundaries coordinate backend authority, invariants, validation and state transitions before implementation. The UI must reflect actual constraints rather than inventing permissions or success states. Consult [interaction references](references/interaction-references.md) for deeper patterns/accessibility; no external reference is required for ordinary decisions above.
