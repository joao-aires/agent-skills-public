---
name: implement
description: Implement an agreed change in small verified increments. Use when the work is ready to build, whether the client provides slash commands and a Git flow or only local files and tests.
user-invocable: true
metadata:
  kind: activity
  domain: development
  phase: implementation
  scope: generic
  invocation: both
---

# Implement

Implement the agreed slice in verified increments and stop at a pushed, green change with every review comment settled.

Read [activity system](../activity-system/SKILL.md) for scope and stopping point. Use the [local implementation flow](../develop/references/implementation-flow.md), run [test](../test/SKILL.md) before the first increment, use [Git contributions](../git-contributions/SKILL.md) when the work needs a worktree, and run the review composition (`code-review`, artifact assurance, guides/quality bar) before pushing.

When the affected stack, architecture or domain has installed guidance, read it and carry its conclusions. If none exists, use project evidence and primary sources; this activity keeps the outcome, acceptance and stopping point.

## Establish the starting point

Read the accepted requirements, design, affected code, tests and project commands. Identify the target revision or, in a non-versioned workspace, the file hashes and environment. If the accepted context is missing or contradictory, stop at the precise blocker instead of guessing.

State the slice: what will be true afterward, what must not change and what is explicitly deferred.

## Work in verifiable increments

1. **Build one behavior at a time.** Keep the change inside the accepted scope and the repository's existing structure and conventions.
2. **Test at the narrowest faithful seam.** Prefer a focused test, command or request over a broad end-to-end run when the narrower check proves the claim.
3. **Run the relevant checks as you go.** Use the project's actual typechecker, linter, test command or build. If a tool is unavailable, say so rather than pretending it ran.
4. **Run the full relevant suite at the end.** Record failed, skipped and unavailable checks.
5. **Keep unrelated cleanup out.** If you find an unrelated defect, report it or create a separate change. Do not bundle it silently.

When the authorized work contains independent slices, read [parallel increments](../activity-system/references/implementation-preparation.md#parallel-increments-optional) before starting workers or branches. Parallel agents and branches require explicit authorization. The mode changes neither the stopping point nor merge authority.

## Use the client when it exists

When the client supports `/tdd`, a typechecker, `/code-review`, a commit or a PR flow, use them within the granted authority. When it does not, use the local implementation flow and inline checks. A missing slash command is not permission to skip verification or review.

## Own the change through green

When this activity runs as a delegated context, it is the implementation delegate for one thread, and it owns the change from the first slice to a pushed branch with green checks and every review comment settled. The phase boundary is the context boundary: keep the pipeline watch and the comment resolution here, because they continue work already in this phase, and hand the result to testing as artifacts rather than as a summary.

Testing is a separate phase and delegate with its own context. Local checks are fast feedback, not certification: a passing suite you wrote does not close the testing phase unless that phase runs inline without a separate context and records the limitation.

## Review before pushing

Read the actual changed behavior from caller to result and compare it with the accepted requirements and the preserved behavior. Use [code-review](../code-review/SKILL.md) for the standards/spec axes, [test](../test/SKILL.md) for evidence gaps and [artifact assurance](../artifact-system/references/assurance.md) for cross-artifact convergence.

The review must come from a context that did not write the change: one dispatched from outside this context, or one started here when the client allows a nested context. Hand it the diff range, the accepted design and requirement IDs, the repository standards, the checks already run and the stopping point. Freshness is what makes the review independent: your own reading of the diff, or a second pass in this context, is not independent assurance — say which one happened. When the client limits nesting, let one review context run both axes itself instead of splitting them further.

The reviewer reports findings with severity, location, impact and fix. It does not rewrite the change. You decide validity and make the fixes. A finding is an argument, not authority over an accepted decision.

If `code-review` is unavailable, review inline against the same axes and record the adaptation.

## Record and commit

Record the implemented behavior, deviations, checks and remaining gaps in the change record. Link implemented behavior to the requirement IDs it satisfies where the record cites them, and name the affected ID instead of silently changing a promise. Use the [artifact quality bar](../artifact-system/references/quality-bar.md) for links. Commit only when the repository and authorization support it. In a non-versioned workspace, use the local revision form instead.

Keep one small, append-only block in the change record or pull-request description: the revision, the slice statement, the commands run with their results, the environment and known-flaky checks, and each attempt against a failing check or review comment with its outcome. A resumed context reads that instead of your transcript, and it is what you return when the work stops.

## Watch the pipeline to green

When the change is pushed, watch the pipeline here. Read the failing step's output rather than the whole run, and quote the line that supports the diagnosis: a long log is not evidence, the failing assertion is. Do not edit files another writer is holding.

The pipeline reports each failing check, the actual cause and whether it is code, configuration, environment or a flaky check, with the log line that supports the claim. Fix code and configuration failures. Do not weaken a test, skip a check, widen a timeout or disable a rule to make a red check green: a check that now asserts less is not a passing check. Retry a flaky check once and record the retry.

Stop after two repair rounds on the same check, or when the failure needs a decision, access or authority you do not have, and report it. Green proves the checks passed at that revision. It does not prove the behavior is correct.

## Resolve review comments

When the pipeline is green, work through the pull-request comments here. Read each thread with its prior replies, the accepted decisions and the checks already run, then classify every comment before changing code:

| Comment | Action |
| --- | --- |
| Valid against the standards, requirements or evidence | Fix it and link the change |
| Incorrect or based on a misreading | Reply with the evidence; do not change the code |
| A question | Answer it |
| Conflicts with an accepted decision or with another comment | Escalate as a decision request; do not split the difference |

A reviewer comment is a claim, not authority. Check it against the accepted decision, the requirement and the repository standards: valid is not the same as agreeable, and resolved is not the same as fixed.

After a fix, re-run the affected checks and the review pass for the changed surface. If accepting the comment changes accepted behavior, reopen the decision instead of editing to match.

When the change is not pushed — no repository, or no push authority — the pipeline and comment sections do not apply and the stopping point below is the reviewed change.

## Stopping point

Stop when the change is committed and pushed, the checks are green at the pushed revision and every review comment is fixed, answered or escalated with a decision request. Return the branch and revision, the checks that passed, each comment's disposition, the remaining gaps and any open decision. Merge, deploy and publish remain separately authorized.
