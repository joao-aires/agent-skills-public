---
name: contribute-code
description: Develop a feature in an isolated Git worktree, make Conventional Commits and publish a concise pull request to the correct repository. Apply by default when starting feature work, continuing a feature branch, committing changes or preparing a PR; respect plan-only requests and existing contribution conventions.
---

Read [workflow framing](../../WORKFLOW.md) for skill selection and invocation boundaries.

# Contribute Code

## Establish the target and feature workspace

Identify the target repository from the supplied workspace. Read its AGENTS.md and contribution conventions; inspect status, remotes, base branch and existing worktrees. Use the intended base, not an arbitrary currently checked-out branch. Confirm unclear repository/base choices before dependent actions; preserve unrelated local changes.

For a new feature, fetch the intended remote when available and create a named branch in a separate worktree. Place it beside the repository or in the workspace's designated worktree area. Use that worktree for all code, tests, migrations, docs and CI changes belonging to the objective. Keep unrelated changes out of the feature.

Adapt these example paths, branch and base to the inspected repository:

```bash
git -C /workspace/application status --short
git -C /workspace/application remote -v
git -C /workspace/application worktree list
git -C /workspace/application fetch origin
git -C /workspace/application worktree add -b feat/saved-searches \
  /workspace/application-worktrees/saved-searches origin/main
```

Continue in an existing worktree for the same objective rather than creating another branch or PR on every turn. If `implement`/`implement-spec` orchestrates work, use the feature workspace as the integration worktree; base any parallel worktrees on its integration branch. Do not create conflicting orchestration. If worktrees are unavailable, state the limitation and use an agreed supported isolation approach without claiming a worktree exists. Never force-remove another agent's worktree or reset/stash the user's edits to make setup convenient.

## Commit the objective clearly

Use Conventional Commits: `type(scope): concise subject`, with optional scope. Choose `feat`, `fix`, `docs`, `test`, `refactor`, `ci` or another repository-supported type; describe the change in plain language. Mark actual breaking changes according to the convention, not ordinary implementation changes.

Use a supplied issue/tracker reference where applicable and compatible with repository conventions. If the repository uses component scopes, retain those and put the issue in a footer/body. Otherwise an agreed issue ID can be the scope, for example `feat(APP-42): save named searches`. With no associated issue, omit the issue scope: `feat: save named searches`. Never invent an ID or require tracker setup. If association is unclear, ask once whether an existing issue should be referenced while continuing independent work; absent an answer, omit the issue reference. Do not ask again when the user already said there is no tracker.

Review the diff, run relevant checks and stage only intended paths. Make coherent commits containing related implementation, tests and documentation. Check the staged diff for accidental files and secrets; preserve unrelated work. Use `git` CLI when available and authorized repository tools otherwise. Actually create commits within the requested contribution flow, rather than returning suggested commands. Report blockers accurately and do not claim a remote commit from a local-only result.

## Publish to the intended remote

Push the feature branch to the correct remote, then create or update its PR against the inspected target/base. Prefer Git and `gh` CLI; use GitHub MCP tools when CLI authentication or capabilities are unavailable. Preserve content, modes and base when publishing through APIs; verify the resulting commit and branch. Use expected-head checks where supported and never blindly force-push shared history.

With verified example targets and a prepared Markdown body file:

```bash
git -C /workspace/application-worktrees/saved-searches push -u origin feat/saved-searches
gh pr create --repo owner/application --base main --head feat/saved-searches \
  --title 'feat: save named searches' --body-file /workspace/pr-description.md
```

For a fork, specify the correct head owner and target repository. Look for an existing PR first; update it rather than duplicating it. Follow repository draft/readiness conventions. Commit/push/PR instructions do not authorize merging or deploying; honor the user's scope, including plan-only requests.

## Write for a reviewer

Lead with the problem and resulting behavior: what this accomplishes, why it was needed and who or what is affected. Use intuitive language, a concrete before/after example when helpful, and only implementation details needed to assess the change. Follow the repository's PR template without padding. Keep simple changes to a short paragraph plus validation; add risks, migrations or compatibility notes when material.

Use a small Mermaid diagram only when a changed boundary, sequence or dependency is easier to understand visually. Do not add a diagram to every PR. Rewrite the title/body around the final diff, not conversation history. Put exact multiline text in a body file for CLI calls or a structured MCP argument; avoid fragile shell interpolation. Link issues accurately; use closing keywords only when appropriate for the completed work.

Example: “Saved filters disappeared after reload. Users can now save, reopen and delete their own named searches; the API enforces ownership so another user cannot read or delete them. Validation: PostgreSQL/API authorization tests and the save–reload–delete browser journey pass.”

Review the final diff and relevant CI; report the PR URL, actual checks and remaining gaps. Distinguish local, pushed, reviewed and merged states. Keep the worktree available for review fixes; remove it only when the work is finished and its changes are safely preserved.
