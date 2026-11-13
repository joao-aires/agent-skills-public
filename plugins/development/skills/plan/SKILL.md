---
name: plan
description: Decide whether and what to pursue for a feature, structural change, product area
  or new application. Use when discussion turns to what to ship first, what is in scope,
  whether it is feasible, or how to sequence and coordinate multiple changes.
user-invocable: true
metadata:
  scope: generic
  invocation: both
  role: task
---

# Plan

Read [development workflow](../../WORKFLOW.md). Use this method for an open decision about pursuing or shaping work. When the outcome and scope are settled and the request is to break delivery into tasks and checks, use [implementation preparation](../deliver-reliable-changes/references/implementation-preparation.md) and stop at the requested breakdown.

## Decide what to pursue

Use the conversation, accepted product direction, relevant repository facts and feedback as evidence. Reuse settled decisions. Scale the investigation to what could change the decision.

- **Outcome and scope.** Identify who benefits, the problem or engineering outcome, what would count as success, the smallest useful slice and what to defer. Seek installed product discovery and prioritization expertise when user value, priority or the first slice is open. For structural work, ground the outcome in the affected behavior or operating constraint.
- **Feasibility.** Check constraints, current system boundaries and dependencies that could change the scope or decision to proceed. Identify what is known and what needs investigation. Compare options at the depth needed for that decision. Carry solution choices into design when they require deeper work.
- **Coordination.** Where delivery depends on several owners or changes, identify sequencing, prerequisites, likely owners and milestones. Distinguish proposals from commitments. A single feature may only need one prerequisite and a next decision.

Recommend proceeding, investigating or deferring. State the evidence behind the recommendation, unresolved decisions and the next action with its owner if known. Carry accepted context forward when the user requests another phase.

## Record the handoff

Use [artifact-system](../artifact-system/SKILL.md) for artifact selection and content/presentation review, and [engineering-workspace](../engineering-workspace/SKILL.md) for discovery and authorized persistence. Resolve the artifact home with [artifact homes](../artifact-system/references/homes.md) before writing; if the repository map is missing or ambiguous, say so rather than choosing an arbitrary path. For a coherent change being carried forward, record the outcome, scope, feasibility and next decision in its ECR or link the existing authority. Keep exploratory ideas together in their existing home until there is a change to carry forward.

A brief or PRD can serve independent product review. A roadmap can coordinate several changes. A ticket can hand off a concrete feasibility investigation or defined change once its work and acceptance are clear. Use [refine](../refine/SKILL.md) when the intended behavior or acceptance needs definition. A planning request stops at the planning decision and any in-scope handoff.
