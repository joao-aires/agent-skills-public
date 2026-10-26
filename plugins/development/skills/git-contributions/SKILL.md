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

Make the contribution easy to inspect and reproduce. Keep the objective's implementation, tests and documentation together in its worktree, and preserve unrelated work. Before publishing, check that the branch contains the intended change against the intended base and that the description explains the result to someone who has not read the conversation.

## Establish the target and workspace

1. Inspect the intended repository, contribution instructions, status, remotes, base and worktrees before writes. Resolve ambiguity that changes the target; preserve unrelated edits.
2. Establish one named feature worktree for the objective, fetching the intended base when available. Reuse it for implementation, tests, docs and follow-up fixes; initialize an empty repository only when needed to enable isolation.
3. Verify that actual edit/test paths are inside the objective worktree, keeping the base checkout untouched.

Parallel execution, when supported and authorized, uses the objective integration branch and coordinated worktrees. If isolation is unavailable, disclose the limitation and use an agreed alternative without claiming isolation exists.


## Verify and commit

1. Use documented quality commands and the existing hook runner; [project conventions](../project-conventions/SKILL.md#establish-focused-quality-checks) owns tool setup. Verify hooks in this worktree, preserving hooksPath and partial staging.
2. Inspect formatter edits, stage intended changes, redact scan output and resolve relevant failures. Inspect the staged diff for accidental files and secrets; retain unrelated work.
3. When the contribution flow includes committing, make coherent Conventional Commits: `type(scope): concise subject`, with an optional repository-supported scope. Mark actual breaking changes and put a supplied issue reference in the repository's preferred location; otherwise omit it.

CI independently repeats required checks. A contribution needs no tracker. Report local and remote state accurately.


## Publish the verified revision

Inspect the intended remote/base and existing PR before publishing. Within established authorization, push the objective branch and create or update its PR; otherwise return the completed local result. Prefer Git and `gh`, with supported repository tools as an alternative. Preserve file modes and branch identity, check expected heads when available and reconcile shared history before rewriting it.

For multiline descriptions, use a body file or structured tool argument. Follow fork/head conventions and repository draft/readiness rules. Commit/push authority remains separate from merging or deploying.

## Explain the result to a reviewer

- Lead with the concrete problem and resulting behavior for someone outside the conversation.
- Explain why the change is needed, how it works where that aids review, and the actual validation and remaining limits.
- Follow the repository template; scale structure to complexity.
- Include risks/migrations only when material, and a diagram only when it clarifies a changed relationship.

Keep title and description about the final diff. Remove abandoned approaches and conversational history unless they explain a relevant tradeoff, and use accurate issue links and closing keywords.

Before reporting completion, verify the published head, diff and required checks. Report the PR link and actual state. Keep the worktree available for review fixes until its work is safely preserved and no longer needed.
