---
name: plan
description: Plan implementation of agreed work using repository context, dependencies,
  verification and release consequences. Use for a bounded feature/refactor plan;
  do not turn a small fix into a mandatory planning workflow.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Plan

Read [task guidance](../../TASKS.md). Use [system-design](../system-design/SKILL.md) after product refinement or when the feature changes consequential architecture, before dependent planning/implementation. Read [project-conventions](../project-conventions/SKILL.md) for existing constraints, [deliver-reliable-changes](../deliver-reliable-changes/SKILL.md) for acceptance and verification. Load the optional stack/domain guidance selected by task guidance only when relevant and available.

Establish the agreed outcome and evidence; refine material gaps before assuming scope. Inspect affected architecture/contracts, using [backend design](../backend-design/SKILL.md) for changed service behavior, and use relevant technical conventions to choose small dependency-ordered increments. Include UI/behavior design before implementation where interactions change, migration/consumer compatibility, focused tests and delivery/recovery consequences. Reuse existing plans and commands. Return the executable next steps, assumptions and blockers; do not require a tracker, a document per slice or parallel agents. Planning alone does not implement or deploy the work.
