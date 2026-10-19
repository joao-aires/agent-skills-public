---
name: interaction-design
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

Use this with [visual design](../visual-design/SKILL.md) for product-derived visual direction, tokens and representative rendered review. This skill owns behavior and coverage; technical conventions own implementation for the selected stack. Use both disciplines for a new interface. Apply it automatically to relevant requested work; users do not need to remember the skill name. A typo, a tiny token adjustment or unchanged interaction needs proportionate reasoning, not a fresh full design document.

## Discover the full affected experience

Read the request, accepted UX/product decisions, references and existing components/routes. Inspect the rendered application when available and distinguish observed behavior from code assumptions. Map user roles, tasks and entry/exit points before choosing widgets. Preserve established branding, density, navigation and business language unless changing them is the request.

For a cross-cutting change, trace shared primitives, caller overrides and alternate/conditional entry points. Keep a concise coverage record of the affected surfaces, meaningful states, intended shared behavior and verification status in existing notes. Derive its scope from the request and actual application, including relevant roles/platforms.

## Specify the interaction before coding

For each reusable interaction pattern, define user goal, visible information hierarchy, primary/secondary actions, navigation/deep-link/back behavior, state ownership and success/failure transitions. Cover relevant loading, empty, validation, disabled/permission, error/retry, unsaved edits/cancel, duplicate submission and destructive/recovery behavior. Include async progress, stale responses and persistence/reload where the flow depends on them. Do not invent user research or business rules.

Specify keyboard/focus behavior, dialog open/close and focus return, labels, announcements and responsive changes. Across supported platforms, account for touch and safe areas, Back/deep links, permission denial, offline/reconnection and foreground/background lifecycle. Preserve human drafts through errors and lifecycle transitions; scope supported behavior from the accepted product rather than inventing offline parity. Choose page versus drawer versus dialog from task complexity and continuity, not a different preference per screen. Distinguish navigational submenus from sibling page tabs and context actions. Define shared behavior/tokens and intentional contextual variants; consistency does not mean ignoring different user goals or mobile constraints.

Write a short behavioral description or state/transition table before implementation. Add low-fidelity wireframes/wireflows for layout/navigation uncertainty or representative mockups for a new visual direction. Existing text/visual references can be reused; do not require text plus wireframe plus mockup for every change. A mockup shows appearance, not persistence, authorization or complete interaction behavior.

Ask only unresolved high-impact design/product questions. State reversible visual assumptions and proceed where the direction is established. If a material decision is genuinely required, wait for it before dependent implementation; continue independent work. Do not demand fresh approval per screen or re-open previously agreed direction. Unattended work records blocking decisions instead of inventing stakeholder answers. The design can live in the conversation or an existing project note, without a compulsory format.

## Validate a pattern, then apply it consistently

Select representative complex and simple surfaces, including a dialog/mobile or role variant when relevant. Establish the shared implementation against the behavioral design before propagation. Reuse the project's primitives, tokens and composed components; fix a shared pattern centrally when appropriate rather than patching pages with divergent overrides. Preserve legitimate variants with explicit reasons.

Reconcile each in-scope surface after propagation: implemented and checked, intentionally unchanged, excluded by accepted scope, or blocked/unverified. Inspect callers, portals and conditional paths as well as shared definitions. Report the remaining scope as partial until it is accounted for.

## Verify the experience

Exercise actual target layouts and critical interactions against the design, using journey and actual-platform verification expertise and supported platform tools. Component states establish shared behavior; route/device journeys establish integration. Compare rendered results with accepted references and investigate differences before changing baselines. Preserve the intended behavior while repairing discrepancies through change-verification expertise.

For contract boundaries coordinate backend authority, invariants, validation and state transitions before implementation. The UI must reflect actual constraints rather than inventing permissions or success states. Consult [interaction references](references/interaction-references.md) for deeper patterns/accessibility; no external reference is required for ordinary decisions above.


Use [interface quality](../interface-quality/SKILL.md) to assess the rendered direction, [UX writing](../ux-writing/SKILL.md) for task language and [usability research](../usability-research/SKILL.md) for requested study planning or supplied participant evidence. Responsive adaptation follows actual content/platform constraints, accepted tokens and meaningful viewport/zoom/locale tests; a single generated phone frame does not establish native or responsive-range coverage.
