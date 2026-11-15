# Implementation flow when client commands are unavailable

Use this flow when the `implement` activity's client-specific assumptions (slash commands, typechecker, code-review command or a Git commit) are unavailable. It preserves the activity's outcome: an implemented, checked change within the requested scope.

## Order

1. Read the accepted requirements, design, affected code and existing tests. Pin the starting revision or, in a non-versioned workspace, the file hashes and environment.
2. Choose the smallest useful slice. Name what is in and out.
3. Add or change one behavior at a time. Keep the code consistent with the repository's existing structure and commands.
4. Exercise the narrowest faithful seam as you go: a unit test, a command, a request or a rendered interaction.
5. Run the full relevant check suite at the end. Record failed, skipped and unavailable checks.
6. Review the actual diff or changed files against the accepted behavior and preserved behavior. Report findings with severity, location, impact and fix.
7. Record the outcome and evidence in the change record. Use the [artifact quality bar](../../artifact-system/references/quality-bar.md) for links; use the non-versioned local revision form when no Git history exists.
8. Stop at the requested implementation and checks. Do not merge, deploy or publish unless that action is separately authorized.

## Boundaries

- A missing slash command is not permission to skip tests or review.
- A non-versioned workspace does not authorize creating a repository as a side effect.
- A green build or local suite is not production verification.
- If a required target, credential or reviewer is unavailable, complete the independent work and report the exact boundary.
