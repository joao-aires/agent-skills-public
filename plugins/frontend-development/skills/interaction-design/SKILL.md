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

## Carry the accepted foundations into behavior

Use the component-system and appearance decisions established with visual design before specifying widgets. Preserve their interaction anatomy and theme ownership across the affected surfaces. If theme switching is supported, specify where its preference lives, when it takes effect, how system changes interact with an override and how an open secondary surface receives the change. Reuse adequate existing decisions; discovering a missing technical specialist does not justify inventing a different component system.

## Discover the full affected experience

Read the request, accepted UX/product decisions, references and existing components/routes. Inspect the rendered application when available and distinguish observed behavior from code assumptions. Map user roles, tasks and entry/exit points before choosing widgets. Preserve established branding, density, navigation and business language unless changing them is the request.

For a cross-cutting change, trace shared primitives, caller overrides and alternate/conditional entry points. Keep a concise coverage record of the affected surfaces, meaningful states, intended shared behavior and verification status in existing notes. Derive its scope from the request and actual application, including relevant roles/platforms.

## Specify the interaction before coding

For each reusable pattern, establish the relevant contract before implementation:

| Concern | Specify |
| --- | --- |
| Task and state | User goal, visible information hierarchy, primary/secondary actions, navigation/deep-link/back behavior, state ownership and success/failure transitions. |
| Failure and ongoing work | Loading, empty, validation, disabled/permission, error/retry, unsaved edits/cancel, duplicate submission and destructive/recovery behavior; async progress, stale responses and persistence/reload where needed. |
| Accessible interaction | Keyboard/focus, dialog open/close and focus return, labels, announcements and responsive changes. |
| Supported platforms | Touch/safe areas, Back/deep links, permission denial, offline/reconnection and foreground/background lifecycle. Preserve drafts across errors and lifecycle transitions; scope offline behavior to the accepted product. |
| Shared patterns | Page/drawer/dialog choice from task complexity and continuity, navigational submenus versus sibling tabs/context actions, shared behavior/tokens and justified contextual variants. |

Describe how the interaction unfolds. Start from the user's entry point, explain what they can do in each meaningful state, and follow the action through completion, cancellation or failure. Decide which state belongs to the URL, the local draft, the server or a background process. That ownership determines whether Back, reload, a repeated action or a late response should preserve, discard or refresh the user's work.

Choose a page, drawer or dialog according to the task's need for space, continuity and navigation. Shared controls should behave consistently, while different user goals and mobile constraints can justify explicit variants. Establish business rules from evidence; do not invent research or product decisions.

Capture the result in a short behavioral description or state/transition table. Add wireframes/wireflows for layout/navigation uncertainty or representative mockups for a new visual direction; reuse adequate existing references. A mockup establishes appearance, not persistence, authorization or complete behavior. Text, wireframe and mockup are not all required for every change.

Ask only unresolved high-impact questions. State reversible assumptions and proceed where direction is established. Wait for a genuinely required decision before dependent implementation while continuing independent work; reuse agreed direction without fresh approval per screen. Unattended work records blockers. The design can live in the conversation or existing notes.


## Validate a pattern, then apply it consistently

Select representative complex and simple surfaces, including a dialog/mobile or role variant when relevant. Establish the shared implementation against the behavioral design before propagation. Reuse the project's primitives, tokens and composed components; fix a shared pattern centrally when appropriate rather than patching pages with divergent overrides. Preserve legitimate variants with explicit reasons.

Reconcile each in-scope surface after propagation: implemented and checked, intentionally unchanged, excluded by accepted scope, or blocked/unverified. Inspect callers, portals and conditional paths as well as shared definitions. Report the remaining scope as partial until it is accounted for.

## Verify the experience

Exercise actual target layouts and critical interactions against the design, using journey and actual-platform verification expertise and supported platform tools. Component states establish shared behavior; route/device journeys establish integration. Compare rendered results with accepted references and investigate differences before changing baselines. Preserve the intended behavior while repairing discrepancies through change-verification expertise.

For contract boundaries coordinate backend authority, invariants, validation and state transitions before implementation. The UI must reflect actual constraints rather than inventing permissions or success states. Consult [interaction references](references/interaction-references.md) for deeper patterns/accessibility; no external reference is required for ordinary decisions above.


Use [interface quality](../interface-quality/SKILL.md) to assess the rendered direction, [UX writing](../ux-writing/SKILL.md) for task language and [usability research](../usability-research/SKILL.md) for requested study planning or supplied participant evidence. Responsive adaptation follows actual content/platform constraints, accepted tokens and meaningful viewport/zoom/locale tests; a single generated phone frame does not establish native or responsive-range coverage.
