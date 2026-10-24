---
name: implement
description: Implement agreed work from a conversation, local spec or optional tracker,
  with repository conventions, design readiness, verification and contribution flow.
disable-model-invocation: true
user-invocable: true
metadata:
  scope: generic
  invocation: user
  role: task
---

Read [workflow framing](../../WORKFLOW.md) before applying this skill.


Read [task guidance](../../TASKS.md) for scope, unattended blockers, design readiness and feature-worktree contributions. Use the agreed request without requiring tickets; commit to the objective's feature branch, preserving unrelated work. Significant UI interactions and backend behavior contracts must be established before implementation. Read [Git contributions](../git-contributions/SKILL.md) for the objective worktree and [change verification](../deliver-reliable-changes/SKILL.md) for scenario-led verification after meaningful increments: run affected checks/journeys, inspect telemetry/state, repair and recheck without weakening acceptance.


Implement the work described by the user in the spec or tickets.

Use /tdd where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, use /code-review to review the work.

Commit your work to the current branch.
