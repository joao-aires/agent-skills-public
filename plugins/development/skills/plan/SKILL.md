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

Read [task guidance](../../TASKS.md). Reuse existing plans and commands; scale the plan to the agreed work.

## Establish the planning basis

- Agree on the outcome and completion evidence. Refine material gaps before assuming scope.
- Inspect affected architecture and contracts. Use [system-design](../system-design/SKILL.md) after product refinement or when the feature changes consequential architecture, before dependent planning or implementation.
- Read [project conventions](../project-conventions/SKILL.md) for existing constraints and [delivery guidance](../deliver-reliable-changes/SKILL.md) for acceptance and verification.
- Load optional stack/domain guidance selected by task guidance only when relevant and available. Use service-contract design expertise for changed service behavior.

## Order the work by its dependencies

Start from a useful observable result and work backward to its prerequisites. A good increment joins enough of the application to prove something meaningful: a caller can exercise the operation, the necessary data changes occur, and a check can distinguish success from failure. Organizing the plan only by folders or technical layers can postpone discovery that those parts do not work together.

Put uncertain or constraining work early enough that it can change the remaining plan. For each increment, name the behavior it delivers, the important prerequisite and the evidence needed before moving on. Reuse the project's technical conventions to choose implementation detail. Include the consequences that apply:

| Affected concern | Include in the plan |
| --- | --- |
| UI or interaction behavior | UI/behavior design before dependent implementation |
| Persistence or consumers | Migration and compatibility work |
| Acceptance and regression risk | Focused tests and their evidence |
| Delivery and failure | Release and recovery consequences |

Make each step specific enough for another contributor to begin it:

- Identify the affected component or verified code location.
- Name the existing mechanism to reuse and the responsibility being added or changed.
- Identify the integration check that connects the increment to its consumer.

Label new components as proposals; do not invent existing files or function names. Leave ordinary local choices to implementation so the plan can accommodate new evidence without losing its intended outcome.

## Return an executable plan

Return steps in the order they can actually be carried out. Make it clear which work is ready, which depends on a decision, and which can proceed independently. For changes to persisted data or deployed consumers, explain the order in which old and new versions can coexist and when cleanup becomes safe.

Keep the plan easy to revise when implementation produces new evidence. The reader should be able to start the next step and recognize when it is done without requiring a separate planning ceremony. A tracker, a document per slice and parallel agents are optional. Planning alone does not implement or deploy the work.
