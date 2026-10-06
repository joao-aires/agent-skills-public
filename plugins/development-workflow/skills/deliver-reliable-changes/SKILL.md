---
name: deliver-reliable-changes
description: Implement, review and prepare application changes for delivery with focused verification, practical CI/CD and operational evidence. Use for feature implementation, bug fixes, PR preparation, pipeline changes and deployment readiness.
---

Read [workflow framing](../../WORKFLOW.md) for skill selection and invocation boundaries.


# Deliver useful changes

## Preserve scope and diagnose first

Read project instructions, accepted decisions and nearby code. Connect the requested outcome to concrete acceptance criteria; preserve existing architecture and UI direction. Keep unrelated cleanup separate. Use the conversation or plan as scope without requiring tickets.

Use `contribute-with-git` for feature worktree isolation, Conventional Commits and publication to the intended remote. Keep checks and documentation in that feature workspace; reuse it for follow-up work on the same objective.

For a failure, establish a reproduction and inspect relevant logs/state before patching. Use `diagnosing-bugs` for investigation, `tdd` for behavior/regression checks and `code-review` for review when installed and relevant. Use differential/security or property-based specialists for risks that benefit from them; do not launch every available workflow. Fix the cause and preserve assertions that exposed it.

## Match verification to the change

| Change | Evidence to seek |
| --- | --- |
| Domain logic or bug fix | Focused behavior/regression tests |
| API, auth or persistence | Integration tests with real contracts, authorization and PostgreSQL where relevant |
| User journey or UI | Affected Playwright flow and rendered UI inspection |
| Dependencies or configuration | Applicable build, startup and configuration checks |
| Migration or deployment | Migration/compatibility check and a practical recovery approach |

Run applicable lint, type and build checks plus behavior tests. Use `test-end-to-end` for full-stack claims and `maintain-documentation` for affected knowledge. A passing build is not evidence that the user journey works. Report blocked checks, pre-existing failures and mocked boundaries explicitly; do not imply they passed.

## Keep delivery practical

Keep local and CI checks aligned, dependencies reproducible and pipelines focused on useful feedback. Use minimal permissions, protected secrets and reviewed dependency/action versions; use the bundled GitHub Actions hardening skill for pipeline changes. Respect provider-required workflow paths. Add deployment automation when the target is known, without inventing an infrastructure platform for an unspecified target.

Check resource authorization, configuration and sensitive-data handling at their application boundaries. Bound external calls and retries; account for duplicate side effects before retrying. Make failures diagnosable through useful logs and basic health signals. Add deeper monitoring, load testing and backup/restore checks when operational needs warrant them.

For a migration that removes data, assess old/new application compatibility and recovery before delivery. Reverting application code alone may not restore lost data. Record the consequential tradeoff; keep destructive/live actions within the user's authorization.

## Close with evidence

Review the diff for scope, correctness and avoidable complexity; resolve material findings. Keep affected docs synchronized and capture repeated mistakes as a concise instruction or check. Explain behavior changed, rationale, commands/results and remaining limitations in the PR or completion report. Distinguish implemented, verified, deployed and planned work. Publish or merge only within the requested authorization; a delivery skill is not permission to deploy.
