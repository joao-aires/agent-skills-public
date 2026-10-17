---
name: git-contributions
description: Develop a feature in an isolated Git worktree, make Conventional Commits
  and publish a concise pull request to the correct repository. Apply by default when
  starting feature work, continuing a feature branch, committing changes or preparing
  a PR; respect plan-only requests and existing contribution conventions.
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: false
---

Read [workflow framing](../../WORKFLOW.md) for scope and invocation boundaries.

# Make reviewable contributions

Keep each objective isolated, verify the affected behavior and publish a clear contribution when the request authorizes it.

## Establish the target and workspace

Inspect the intended repository, contribution instructions, status, remotes, base and worktrees before writes. Resolve ambiguity that changes the target; preserve unrelated edits. Use one separate named feature worktree per objective, reusing it for implementation, tests, docs and follow-up fixes. Create it from the intended base after fetching when available; verify actual edit/test paths are inside it. Initialize an empty repository only as needed to enable that isolation.

Keep the base checkout untouched by objective changes. Parallel execution, when supported and authorized, uses the objective integration branch and coordinated worktrees. If worktree isolation is unavailable, disclose the limitation and use an agreed alternative without claiming isolation exists.

## Verify and commit

Use documented quality commands and the existing hook runner; [project conventions](../project-conventions/SKILL.md#establish-focused-quality-checks) owns tool setup. Verify hooks in this worktree, preserving hooksPath and partial staging. Inspect formatter edits, stage intended changes, redact scan output and resolve relevant failures. CI independently repeats required checks.

Review the diff and make coherent Conventional Commits: `type(scope): concise subject`, with an optional repository-supported scope. Mark actual breaking changes. Use a supplied issue reference in the repository's preferred location; absent one, omit it. Keep the contribution useful without requiring a tracker.

Actually commit when the requested contribution flow includes it. Inspect the staged diff for accidental files and secrets; retain unrelated work. Report local and remote state accurately.

## Publish the verified revision

Inspect the intended remote/base and existing PR before publishing. Within established authorization, push the objective branch and create or update its PR; otherwise return the completed local result. Prefer Git and `gh`, with supported repository tools as an alternative. Preserve file modes and branch identity, check expected heads when available and reconcile shared history before rewriting it.

For multiline descriptions, use a body file or structured tool argument. Follow fork/head conventions and repository draft/readiness rules. Commit/push authority remains separate from merging or deploying.

## Explain the result to a reviewer

Lead with the concrete problem and resulting behavior for someone outside the conversation. Explain why the change is needed, how it works where that aids review, and the actual validation and remaining limits. Follow the repository template; scale structure to complexity. Include risks/migrations only when material, and a diagram only when it clarifies a changed relationship.

Keep title and description about the final diff; remove abandoned approaches and conversational history unless they explain a relevant tradeoff. Use accurate issue links and closing keywords. Verify the published head, diff and required checks, and report the PR link and actual state. Keep the worktree available for review fixes until its work is safely preserved and no longer needed.
