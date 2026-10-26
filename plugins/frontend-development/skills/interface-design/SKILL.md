---
name: interface-design
description: Design, inspect and improve complete user interfaces across navigation, visual hierarchy, behavior, shared composition and accessibility. Use for new UI, cross-screen changes, visual refinements, design reviews and design-to-implementation handoffs; preserve accepted product direction and authorized scope.
user-invocable: true
metadata:
  scope: generic
  invocation: both
  role: support
---

# Design and refine the complete interface experience

Own a coherent user-facing experience rather than separate visual, interaction and critique phases. Work from actual user tasks, accepted product decisions, existing application evidence and the requested stopping point. The method applies across web, desktop, browser extensions and native applications; the accepted technical stack owns implementation.

Use this skill to support `design`, `develop`, `implement`, `improve` and `review`. Direct requests to design, inspect or critique do not authorize source edits; authorized implementation preserves behavior and existing design commitments. A visual-only improvement should not redesign navigation, and a changed flow should not unnecessarily reopen branding.

## Choose the needed depth

| Requested work | Primary focus |
| --- | --- |
| New product or substantial redesign | User tasks, flows, foundation choices, contextual visual direction and a representative rendered slice |
| Navigation, forms or dialog changes | Destinations, state transitions, focus, error/recovery, drafts and affected callers |
| Visual refinement | Real hierarchy, spacing, typography, color, density, borders, depth, images and accepted tokens |
| Read-only critique | Observed defects, severity, specific surface/state, smallest justified correction and verification gaps |
| Design handoff and implementation | Shared composition, component/state mapping, responsive variants and actual rendered/behavioral checks |

Establish audience, task, content, platform, roles, accepted choices and scope. Distinguish evidence, hypotheses and reversible proposals. Ask only for material unresolved decisions, and do not require a brand-asset hunt or research study for routine UI work.

## Decide structure, behavior and appearance in one loop

1. **Organize the work.** Map recurring tasks, objects, entry points, navigation, current context and return paths before inventing screens. Separate operation controls from durable settings. Choose pages, panels or dialogs for task complexity and continuity, not habit. For substantial changes read [navigation and configuration](references/navigation-and-configuration.md).
2. **Specify interaction contracts.** Trace the meaningful journey through success, failure, cancellation and recovery. Resolve URL, local draft, server and background state ownership; loading/empty/error/denied/stale states, repeated actions, pending results, lost edits and focus restoration. Consider keyboard, screen reader, touch and applicable native lifecycle. Read [interaction references](references/interaction-references.md) for unfamiliar interaction patterns.
3. **Preserve compatible foundations.** Use the established design system, component anatomy, semantic tokens, shared page shell and appearance policy. For a new interface, choose a component system and supported light/dark behavior before dependent mockups. Read [UI foundations](references/ui-foundations.md) when those choices are genuinely open.
4. **Give content a visual hierarchy.** Choose composition, typography, reading measure, density, spacing, color, depth, iconography and imagery based on the task. Make primary information/action prominent without making every card, button or label compete. Read [visual principles](references/visual-principles.md) for practical decisions and [visual direction](references/visual-direction.md) for substantial visual explorations or design handoffs.
5. **Unify related views.** Establish consistent application identity, navigation, title/context, local actions, content frame and component roles. Preserve justified variants such as dense operational tables, focused editors and native surfaces without making every page look identical.

Apply the relevant subset of these decisions to a scoped request; do not impose a lengthy process on a small fix. `ux-writing` owns specialist message/copy work, and `usability-research` owns participant-study planning and analysis. SaaS dashboard semantics and tenant/context contracts remain with SaaS domain guidance; framework packages implement the accepted design.

## Inspect a representative slice, then propagate

Use text, wireframes or wireflows to settle structural uncertainty, and actual renders/prototypes to assess appearance. Choose an artifact that answers the question rather than mandating Figma, Storybook or a particular tool. Inspect realistic content and meaningful states, including long labels, an error/recovery path, relevant viewport widths and supported appearance modes.

For refinement or review, identify the precise surface and state, observation, user impact, probable shared cause and correction. Prioritize task blockers, accessibility and misleading outcomes before comprehension, efficiency and polish. Read [visual review](references/visual-review.md) for diagnosis and [component/token audits](references/component-and-token-audits.md) when reuse or cross-page drift is the problem. Fix shared definitions before copying page-specific overrides, then reconcile affected callers, dialogs, portals, routes, role variants and narrow layouts. Report unverified coverage.

Keep measured accessibility claims distinct from aesthetic judgments. When proposing numeric contrast or component-identification fixes, read [measurement and applicability](references/measurement-and-applicability.md) and check the actual rendered and proposed values against applicable requirements. A screenshot is not evidence of keyboard behavior, persistence or participant success.

## Verify the requested outcome

Compare related rendered surfaces, inspect content growth and meaningful platform/locale/theme variants, and exercise the affected primary journey and critical failure path when runtime access permits. Component stories demonstrate component states; real route/API/persistence checks are separate evidence. A design-only request stops at a clear direction and acceptance evidence plan; a review-only request leaves sources unchanged. Return decisions, affected surfaces and states, mappings to shared patterns, observed checks and precise gaps.

## Provenance and limits

[Refactoring UI](https://refactoringui.com/) by Adam Wathan and Steve Schoger informs the original contextual heuristics in [visual principles](references/visual-principles.md) and [visual review](references/visual-review.md). These are judgment aids, not universal style rules. Do not reproduce or distribute copyrighted book passages, images, templates, palettes or assets.
