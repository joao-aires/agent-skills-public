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

Use this directly for a requested critique or within authorized UI design/development/improvement. A review is read-only unless fixes are requested; findings do not authorize a redesign. Read [frontend conventions](../frontend-conventions/SKILL.md) for the accepted product-derived direction, stack and tokens, and [interaction design](../interaction-design/SKILL.md) for flows and affected surfaces. Do not start a full craft audit for a typo or tiny unchanged interaction.

## Establish the intended experience

Resolve the screen, flow, component or changed surfaces from the request and evidence. Identify the audience, primary task, realistic content, accepted visual character, density and supported platforms. Reuse established decisions; missing brand assets need a reversible proposal, not invented research. State the inspected boundary and any inaccessible states.

For new visual work, help compare coherent alternatives and explain their fit with the task. For existing UI, judge against its intended experience and usable platform behavior. A deliberate compact layout, unusual type pairing or restrained palette is not a defect merely because a reviewer prefers another style. Do not impose fixed spacing, font counts, radii or animation recipes across products.

## Inspect the actual experience

Inspect rendered surfaces and meaningful states where available: populated/empty, loading, validation, failure/retry, selection/editing and relevant narrow layouts. Use source, tokens and component definitions to explain causes; distinguish a code observation, static design observation, runtime result and hypothesis. A screenshot can reveal clipping but cannot prove focus behavior or persistence. Supplied static artifacts permit a bounded review; name runtime gaps without treating them as confirmed defects. Keep agent-authored inspection scripts and screenshots in the request's permitted output location; a client scratch directory is not an implied exception. Disclose a host-enforced location conflict before substituting another destination.

Evaluate information hierarchy and primary actions, content grouping, reading measure/type hierarchy, spacing rhythm, alignment, semantic color/contrast, icon clarity and purposeful motion. Check long content, zoom and relevant locale/direction growth. Verify keyboard access, visible focus, overlay containment/restoration, labels and reduced-motion behavior when runtime access permits. Use applicable accessibility standards and established primitives; visual inspection alone cannot establish accessibility conformance.

Verify numerical recommendations as well as the current state: calculate contrast for the proposed foreground/background pair, account for opacity and state, and identify the applicable requirement. A low-contrast decorative separator or labelled button outline does not by itself establish a non-text contrast failure; determine whether that boundary is needed to identify the control. Use the bundled [contrast calculator](scripts/contrast.py) for opaque sRGB pairs when Python 3 is available (`python3 scripts/contrast.py --foreground '#000000' --background '#ffffff'` from this skill directory), or an equivalent checked method. It reports unrounded ratios and distinct text/non-text thresholds; it cannot decide which requirement applies. A readable text value alone does not establish that an input's editable area is identifiable. Do not present an unmeasured replacement as compliant. Clipping establishes hidden visual content, not inability to copy, expand or retrieve it; exercise those paths before claiming they are unavailable.

For substantial new design, first inspect one representative real slice with a difficult state before propagating it. For a global change, reconcile every in-scope caller/state with interaction-design; a good shared component does not prove callers use it correctly. Use [component and token audits](references/component-and-token-audits.md) when reuse, drift or library cleanup is the concern. Use [UX writing](../ux-writing/SKILL.md) for material copy issues rather than duplicating its method.

## Prioritize and repair within scope

Report confirmed task blockers, hidden consequences, inaccessible controls and data-loss risks first; then comprehension/efficiency issues and useful polish. Each finding identifies the exact surface/component or file, reproduction/state, evidence, user impact and smallest suitable fix. Consolidate one shared cause with its confirmed locations. Separate uncertain suggestions and uninspected coverage; do not pad a report with invented rejected candidates or force a fixed finding count.

When fixes are authorized, correct a shared cause using compatible project primitives and tokens, preserve behavior and accepted character, then re-render and exercise the affected interaction. Do not substitute handwritten visual lookalikes for available accessible primitives. Keep visual changes separate from changes to product functionality or authority that require a decision under the active workflow.

Before returning, check the recommendations themselves: execute the calculator or an equivalent verified method for every concrete replacement color against its actual adjacent colors, and attach the measured result. Current-palette measurements do not verify a proposed replacement. If the replacement cannot be checked, recommend the required outcome without a hex value or compliance promise. A high focus contrast ratio alone does not establish AAA focus appearance. Check the report's other strong claims too: if copying, undo or another recovery path was not exercised, describe that path as unverified instead of impossible. Restrict a boundary-contrast finding to controls whose boundary is needed for identification; readable labels can already identify a button, so a faint optional button outline is not itself a failure. Keep decorative separators and labelled-button outlines as applicability controls when reviewing input boundaries.

Return the assessed scope, prioritized findings or no actionable findings, actual verification and remaining gaps. Distinguish the agent's aesthetic assessment from user acceptance. Relevant component/Storybook checks and real application/native journeys protect implementation; a build, a model score or a new screenshot cannot establish taste or task success.
