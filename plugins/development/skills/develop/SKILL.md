---
name: develop
description: Take a rough business idea, feature, refactor or improvement through
  clarification, design, implementation, testing and review in one requested engagement.
  Use for end-to-end development with consequential questions and explicit assumptions,
  not a promise of zero interaction or automatic deployment.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Develop

Read [task guidance](../../TASKS.md). Use [system-design](../system-design/SKILL.md) after product refinement or when the feature changes consequential architecture, before dependent planning/implementation. Read [git-contributions](../git-contributions/SKILL.md) for the objective's feature worktree, [deliver-reliable-changes](../deliver-reliable-changes/SKILL.md) for verification and completion. Load the optional stack/domain guidance selected by task guidance only when relevant and available.

## When starting a new application

Read [new-application flow](references/new-application-flow.md). Reuse sufficient accepted evidence and establish missing outcomes before work that depends on them:

1. Purpose and business context.
2. Product outcome and useful slice.
3. Requirements and observable acceptance.
4. Feasibility and system design.
5. UX and visual direction.
6. Implementation plan and foundations.
7. Implementation, testing and repair.
8. Delivery and learning.

A named stack or starter kit does not supply missing decisions. Defined existing work reuses accepted context; it does not restart the full lifecycle.

## Establish a useful slice

Treat the rough idea as an outcome to shape, not an instruction to build every imagined feature. Inspect the repository and supplied references first.

For existing behavior, use [system mapping](../system-mapping/SKILL.md#trace-a-feature-before-changing-it) to follow the relevant path and a comparable implementation. Establish how users enter the feature, where decisions and state changes happen, and which tests observe the result.

Use that evidence to answer technical questions and expose material unknowns before designing the extension. Keep the trace narrow enough for the slice; a new application needs its constraints and intended journey rather than an invented existing architecture.

- For a new product select a useful coherent first slice; for existing work preserve architecture, identity, UI and operations constraints.
- When users, product value or priorities are uncertain, use installed product discovery and prioritization expertise to establish the product decision before dependent requirements/design.
- Use business strategy when business direction or viability is actually unresolved.
- Reuse accepted context for defined work.

## Resolve decisions before dependent work

Clarify material user/business outcomes, data/authority boundaries and high-impact UX/API/architecture choices before dependent work.

- Ask a small coherent set of decision-changing questions; retain answers already provided.
- State reversible assumptions for ordinary details and proceed within scope.
- In unattended mode return the concrete blocking decisions and useful independent findings instead of fabricating them.

## Design and plan the slice

Turn the selected slice into a small set of outcomes that can be demonstrated. Then identify the design choices that could change those outcomes or force substantial rework. Resolve those before coding their dependents, while leaving ordinary implementation details to the implementation work.

Keep the reasoning connected across phases. The product outcome should explain the requirements; the requirements should explain the design; the design should explain the implementation order and verification. Producing separate documents with inconsistent decisions does not establish this continuity. Reuse an existing brief or conversation when it already carries the necessary information.

- For meaningful frontend work establish product-derived visual direction, interaction behavior and affected-surface coverage before coding, using available visual and interaction design expertise.
- For backend work establish authority, invariants, state/failure and compatibility contracts using service-contract design expertise when available.
- Apply only matching accepted-stack conventions; missing optional methods do not remove these decision outcomes.
- Use text, wireframes or mockups to settle the actual uncertainty. No compulsory document template, design approval per screen or complete scaffold is required.

## Implement and verify

Implement in increments that can be exercised, using relevant supporting skills directly and preserving native invocation controls. After each meaningful change, run the checks that observe its behavior, inspect the result, and repair defects before extending the same approach elsewhere. If implementation disproves an assumption, revisit the affected design or requirement and carry that change through the remaining work.

Deliver-reliable-changes owns this scenario/test/inspect/repair loop and the evidence needed to claim completion; Git contributions owns isolation and publication. Keep the accepted decisions and affected documentation consistent with what was built. For UI work, inspect the running experience; for stored behavior, check what can be read back through the real application path.

## Review and close

Use deliver-reliable-changes for final review of the integrated change and resolution of material findings. Carry the accepted outcome and actual verification evidence into that review; identify an independent review as such only when it occurred. Revisit the affected design or check if a finding changes its premise.

Finish with the implemented user outcome, the checks actually performed, and any unfinished or blocked part. Delivery and learning are part of considering the result, but publishing, deploying or contacting users still follows the established contribution/delivery scope.
