# Prepare implementation

Use the accepted scope and existing breakdown. For a small change, identify the next action and its check. Expand the breakdown when dependencies, compatibility, recovery or verification need coordination. If the request stops at a breakdown, return that result within the authorized scope before changing application code.

## Establish the planning basis

- Agree on the outcome and completion evidence. Refine material gaps before assuming scope.
- Inspect affected architecture and contracts. Use [design-system](../../design-system/SKILL.md) after product refinement or when the feature changes consequential architecture, before dependent planning or implementation.
- Read [project conventions](../../project-conventions/SKILL.md) for existing constraints and [verification guidance](../../test/SKILL.md) for acceptance and evidence.
- Load optional stack/domain guidance selected through the development workflow only when relevant and available. Use service-contract design expertise for changed service behavior.

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

## Check the breakdown before dependent work

Before starting a dependent increment, apply [artifact assurance](../../artifact-system/references/assurance.md): map material accepted requirements and failure/denial paths to concrete increments and observable verification, check design/sequence/plan contradictions, and mark consequential dependencies blocked until resolved. Record dependency-ordered increments, accepted design/target diagram references and verification/release implications in the ECR implementation strategy. Link the relevant design. When a slice needs pickup or coordination, follow the [issue contract](../../artifact-system/references/contracts/issue.md). Return steps in the order they can actually be carried out. Make it clear which work is ready, which depends on a decision, and which can proceed independently. For changes to persisted data or deployed consumers, explain the order in which old and new versions can coexist and when cleanup becomes safe.

Keep the plan easy to revise when implementation produces new evidence. The reader should be able to start the next step and recognize when it is done without requiring a separate planning ceremony. A tracker, a document per slice and parallel agents are optional. Planning alone does not implement or deploy the work.

## Parallel increments (optional)

When the user explicitly authorizes parallel agents or branches, the same increments can proceed concurrently. This is a mode of implementation, not another activity or artifact: the accepted breakdown and notes already describe the slices, so no tracker or tickets are required. Keep the stopping point and review expectations the same. Without that authorization, work the increments sequentially, and prefer sequential work when coordination would cost more than it saves.

- **Model the slices as a dependency graph.** Give each slice its delivered behavior, real prerequisites and completion evidence. An edge is a prerequisite that must be resolved first, not a shared folder. Keep a ready frontier of slices whose prerequisites are merged.
- **Isolate every slice.** Use the integration branch, base and merge rule the user or project already defines. Give each slice its own branch and worktree from the integration branch; do not share a working tree or let two slices edit the same branch concurrently.
- **Merge completed slices.** Merge a slice only after its focused checks and review pass. Resolve conflicts on the integration branch and check the merged result there. Merge authority and branch policy remain with the user and the project; a worker does not gain them.
- **Recompute the frontier after each merge.** Start slices that just became ready, and give each worker its slice, context pointers and expected evidence instead of relaying the conversation.
- **Communicate with context pointers.** Point workers to the accepted requirements and design, the breakdown, relevant commits and saved notes. Keep shared exploration outside the repository when it is not durable project knowledge. Do not duplicate what a pointer already provides.
- **Close on the integrated result.** Run one review pass over the integrated diff, verify at the integration head, resolve or record material findings, and clean up the slice worktrees. Report merged, remaining and blocked slices with the evidence actually observed.
