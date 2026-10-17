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

For a new application, read [new-application flow](references/new-application-flow.md) and establish its decision outcomes in order before dependent implementation: purpose/business context, product, requirements, feasibility/system design, UX/visual direction, plan/foundations, implementation/test/repair, delivery/learning. Reuse sufficient accepted evidence; do not skip missing outcomes merely because a stack or starter kit was named.

Treat the rough idea as an outcome to shape, not an instruction to build every imagined feature. Inspect the repository and supplied references first. For a new product select a useful coherent first slice; for existing work preserve architecture, identity, UI and operations constraints. Use available strategy/domain guidance when it answers a real uncertainty.

Clarify material user/business outcomes, data/authority boundaries and high-impact UX/API/architecture choices before dependent work. Ask a small coherent set of decision-changing questions; retain answers already provided. State reversible assumptions for ordinary details and proceed within scope. In unattended mode return the concrete blocking decisions and useful independent findings instead of fabricating them.

Define concise acceptance and a proportionate plan. For meaningful frontend work use frontend-conventions for product-derived visual direction and interaction-design for behavior/surface coverage before coding; for backend work establish authority, invariants, state/failure and compatibility contracts. Use text, wireframes or mockups to settle the actual uncertainty. No compulsory document template, design approval per screen or complete scaffold is required.

Continue through implementation, tests and review using relevant supporting skills directly, preserving native invocation controls. Deliver-reliable-changes owns the scenario/test/inspect/repair loop and evidence needed to claim completion; Git contributions owns isolation and publication. Carry accepted decisions and affected knowledge forward. End with the useful implemented outcome, actual evidence and remaining blockers within the established contribution/delivery scope.
