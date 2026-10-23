---
name: interface-quality
description: Assess and refine interface quality across hierarchy, typography, spacing, contrast, motion and component consistency. Use for a scoped UI critique or during substantial design, implementation and improvement; preserve accepted product direction and use rendered evidence for visual claims.
user-invocable: true
metadata:
  scope: generic
  invocation: both
  role: support
---

# Assess interface quality in context

Assess whether the interface helps its intended users complete the task with clear hierarchy, dependable interaction and a coherent visual character. Preserve accepted product choices, including deliberate density and unusual styling. Distinguish an evidenced usability/accessibility problem from an aesthetic preference.

Use directly for a requested critique or as support during substantial design and authorized repair. Review remains read-only; fixes and shared-design annotations follow the requested scope. For a new direction, use [visual design](../visual-design/SKILL.md); for behavior use [interaction design](../interaction-design/SKILL.md).

## Establish the intended experience

Read the brief, references, accepted decisions and existing components. Identify the audience, primary task, content, platform and affected scope. Compare plausible visual directions where the choice is still open; connect the recommendation to those constraints. Reuse an accepted direction for ordinary changes.

## Inspect and substantiate

Inspect rendered surfaces with realistic content and meaningful states, including relevant narrow layouts, failure/recovery and editing.

- Trace issues to source, tokens or component definitions where available.
- Follow the primary task and notice where the interface directs attention. Check whether the most prominent information and actions are the ones the task needs, and whether grouping and spacing explain which content belongs together.
- Trace relevant navigation through the task, configuration and return path. Check that destinations and control locations match their scope, the current context stays recognizable, and returning preserves work or explains a necessary invalidation. Repeated instructions can signal an unclear structure; distinguish that cause from wording alone.
- Examine typography at the sizes and lengths actually used, including dense data, labels and long values. Check whether semantic color, icons and motion communicate a consistent meaning and remain understandable without relying on one visual cue alone.
- Check content growth, zoom and locale/direction where they affect the task.

Verify applicable accessibility requirements and exercise keyboard/focus, labels, overlay behavior and reduced motion when runtime access permits. Separate static observations, runtime results, hypotheses and unavailable evidence. A finding must establish the user impact it claims; use an unverified label for a path that has not been exercised.

Verify proposed corrections against the same requirement and actual context as the finding. Calculate quantitative recommendations rather than estimating them visually. For contrast, control identification or focus claims, read [measurement and applicability](references/measurement-and-applicability.md); use a reliable available measurement method. Report measured values and limits. When a proposal cannot be checked, describe the required outcome without promising compliance.

## Repair shared causes and reconcile coverage

Prioritize task blockers, inaccessible controls and hidden consequences before comprehension, efficiency and polish.

- Describe the exact surface and state, what you observed, and how it affects the user's task. Recommend the smallest correction that addresses that cause and explain what needs rechecking afterward.
- Group issues caused by the same token or component so one shared repair can be assessed. Keep uncertain suggestions separate from demonstrated problems, and accept that a review may find no actionable issue.

For substantial new work, inspect a representative difficult state before propagation. For global changes, reconcile every in-scope caller and meaningful variant through interaction-design. A shared component can pass while a caller remains wrong. Use [component and token audits](references/component-and-token-audits.md) for reuse or drift questions and [UX writing](../ux-writing/SKILL.md) for task language.

### When repair is authorized

Use compatible project primitives/tokens, preserve behavior and accepted character, then re-render and exercise affected interactions.

Return assessed scope, prioritized findings, actual verification and remaining gaps. Keep aesthetic assessment, user acceptance, component checks and real application/native journeys distinct.
