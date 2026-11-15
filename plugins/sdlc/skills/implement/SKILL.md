---
name: implement
description: Implement an agreed change in small verified increments. Use when the work is ready to build, whether the client provides slash commands and a Git flow or only local files and tests.
user-invocable: true
metadata:
  kind: activity
  origin: local
  pack: sdlc
  domain: development
  phase: implementation
  scope: generic
  invocation: both
  role: task
---

# Implement

Read [activity system](../activity-system/SKILL.md) for scope and stopping point. Use the [local implementation flow](../develop/references/implementation-flow.md), [test](../test/SKILL.md), [change review](../change-review/SKILL.md) and [Git contributions](../git-contributions/SKILL.md) as applicable.

The earlier upstream implementation entry point is preserved only as [reference provenance](references/upstream-implement.md). This activity owns the SDLC implementation step: small slices, checks, review evidence and an honest handoff.

## Establish the starting point

Read the accepted requirements, design, affected code, tests and project commands. Identify the target revision or, in a non-versioned workspace, the file hashes and environment. If the accepted context is missing or contradictory, stop at the precise blocker instead of guessing.

State the slice: what will be true afterward, what must not change and what is explicitly deferred.

## Work in verifiable increments

1. **Build one behavior at a time.** Keep the change inside the accepted scope and the repository's existing structure and conventions.
2. **Test at the narrowest faithful seam.** Prefer a focused test, command or request over a broad end-to-end run when the narrower check proves the claim.
3. **Run the relevant checks as you go.** Use the project's actual typechecker, linter, test command or build. If a tool is unavailable, say so rather than pretending it ran.
4. **Run the full relevant suite at the end.** Record failed, skipped and unavailable checks.
5. **Keep unrelated cleanup out.** If you find an unrelated defect, report it or create a separate change; do not bundle it silently.

## Use the client when it exists

When the client supports `/tdd`, a typechecker, `/code-review`, a commit or a PR flow, use them within the granted authority. When it does not, use the local implementation flow and inline checks. A missing slash command is not permission to skip verification or review.

## Review before handoff

Read the actual changed behavior from caller to result. Compare it with the accepted requirements and the preserved behavior. Use [change review](../change-review/SKILL.md) when a change-level review is requested; use [code-review](../code-review/SKILL.md) for the code-diff standards/spec axes when available.

Report findings with severity, location, impact and fix. Self-review is not independent assurance; say so.

## Record and commit

Record the implemented behavior, deviations, checks and remaining gaps in the change record. Use the [artifact quality bar](../artifact-system/references/quality-bar.md) for links. Commit only when the repository and authorization support it; in a non-versioned workspace use the local revision form instead.

## Stopping point

Stop at the implemented, verified and reviewed change within the requested scope. Do not merge, deploy or publish unless that action is separately authorized.

## Provenance

The earlier upstream entry point and its MIT license are kept for reference under `references/`. They are not the current activity instructions.
