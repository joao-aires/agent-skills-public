---
name: deliver-reliable-changes
description: Implement, review and prepare application changes for delivery with focused
  verification, practical CI/CD and operational evidence. Use for feature implementation,
  bug fixes, PR preparation, pipeline changes and deployment readiness.
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: false
---

Read [workflow framing](../../WORKFLOW.md) for skill selection and invocation boundaries.


# Deliver useful changes

## Preserve scope and diagnose first

Read project instructions, accepted decisions and nearby code. Connect the requested outcome to concrete acceptance criteria; preserve existing architecture and UI direction. Keep unrelated cleanup separate. Use the conversation or plan as scope without requiring tickets.

Use `git-contributions` for feature worktree isolation, Conventional Commits and publication to the intended remote. Keep checks and documentation in that feature workspace; reuse it for follow-up work on the same objective.

For a failure, establish a reproduction and inspect relevant logs/state before patching. Use `diagnosing-bugs` for investigation, `tdd` for behavior/regression checks and `code-review` for review when installed and relevant. Use differential/security or property-based specialists for risks that benefit from them; do not launch every available workflow. Fix the cause and preserve assertions that exposed it.

## Agree completion from the requested behavior

Before implementation, connect the intended outcome to the affected contracts and acceptance evidence. Reuse answers already agreed. For ordinary changes this can stay in the conversation; no required template, ticket or separate document. State material assumptions and identify which checks can be run in the available environment. Select depth from the actual risk, not every checklist in the bundle.

| Claim | Required evidence |
| --- | --- |
| Implemented | Relevant code/configuration exists; missing behavior is identified. |
| Behavior verified | Affected acceptance and failure/authorization cases were exercised, with the persistence/provider boundary stated. |
| Ready for deployment | Applicable checks pass; configuration, compatibility, migration and recovery consequences are addressed. Outstanding material gates remain blockers. |
| Verified after deployment | The intended revision is served and the affected journey works in the named target. Local tests cannot establish this state. |

For sharing a private resource, verify durable grants, intended recipient rights, denial for unrelated users and unchanged private defaults. A copy edit needs appropriate rendered verification; it does not require unrelated database/recovery work. Keep pre-existing failures distinct from regressions and respect existing required gates. Completion states are evidence descriptions, not additional permission or mandatory sequential ceremonies.

## Match verification to the change

| Change | Evidence to seek |
| --- | --- |
| Domain logic or bug fix | Focused behavior/regression tests |
| API, auth or persistence | Integration tests with real contracts, authorization and PostgreSQL where relevant |
| User journey or UI | Affected platform journey, component/state checks and rendered interaction/visual evaluation |
| Dependencies or configuration | Applicable build, startup and configuration checks |
| Migration or deployment | Migration/compatibility check and a practical recovery approach |

Run applicable lint, type and build checks plus behavior tests. Use `journey-testing` for full-stack claims and `documentation-conventions` for affected knowledge. A passing build is not evidence that the user journey works. Report blocked checks, pre-existing failures and mocked boundaries explicitly; do not imply they passed.

## Evaluate each useful increment

Before dependent implementation, connect accepted behavior and interaction/contracts to a small scenario set with observable expected outcomes. Reuse the project's test/evaluation records; no new schema or ticket is required. Keep material criteria stable through the run and resolve a consequential mismatch with the agreed intent instead of silently weakening the criterion.

After each meaningful increment: run fast affected logic/integration checks, start the required local services, exercise the changed journey, inspect relevant logs/traces/state and compare with the expected behavior/design. Fix a demonstrated discrepancy and rerun affected checks. Before completion run broader required regression and surface/platform coverage. Select expensive load/fault/live-model checks by changed risk and established authority, not after every keystroke. Mocks, screenshots and green CI each prove narrower boundaries.

Use journey-testing for repeatable critical flows plus bounded exploratory operation and visual/accessibility evaluation. Keep independent assertions for important persistence/authority outcomes; don't accept the implementing agent's self-rating as proof. Record revision, scenario/data/environment and actual artifacts/results sufficiently to reproduce a failure. Never update expected outputs, visual baselines or judge rubrics merely to obtain green results. Changes to intended behavior need a justified decision and affected checks.

Stop when acceptance is established with relevant evidence, or report precise blocked/partial results. When repair stops producing new evidence or repeats the same failure, diagnose the cause or escalate the blocker rather than retry indefinitely. Distinguish product defects, environment/fixture problems, nondeterministic evaluator results and unavailable tools. Add a focused regression check for a discovered defect at the most useful boundary. Human evaluation resolves unresolved product/experience judgments; do not fabricate it.

## Keep delivery practical

Keep local and CI checks aligned, dependencies reproducible and pipelines focused on useful feedback. Use minimal permissions, protected secrets and reviewed dependency/action versions; use the bundled GitHub Actions hardening skill for pipeline changes. Respect provider-required workflow paths. Add deployment automation when the target is known, without inventing an infrastructure platform for an unspecified target.

Check resource authorization, configuration and sensitive-data handling at their application boundaries. Bound external calls and retries; account for duplicate side effects before retrying. Make failures diagnosable through useful logs and basic health signals. Add deeper monitoring, load testing and backup/restore checks when operational needs warrant them.

For a migration that removes data, assess old/new application compatibility and recovery before delivery. Reverting application code alone may not restore lost data. Record the consequential tradeoff; keep destructive/live actions within the user's authorization.

## Close with evidence

Review the diff for scope, correctness and avoidable complexity; resolve material findings. Keep affected docs synchronized and capture repeated mistakes as a concise instruction or check. Explain behavior changed, rationale, commands/results and remaining limitations in the PR or completion report. Distinguish implemented, verified, deployed and planned work. Publish or merge only within the requested authorization; a delivery skill is not permission to deploy.

Use `performance-testing` for changed latency, throughput or concurrency claims: k6 locally, on a CI-started application, and on an identified non-production deployment. Select proportionate profiles; basic smoke checks do not prove production capacity.

## Maintain trustworthy checks and retire behavior deliberately

Keep unit/integration/contract/browser suites aligned with their claims. Diagnose flaky failures from state, timing and environment evidence. A necessary quarantine is an explicit temporary coverage gap with owner, reason, replacement evidence and review/repair condition; never quietly mark a required check green or leave an indefinite skip. Improve isolated fixtures and feedback time, and remove redundant tests only after equivalent meaningful coverage is established. Avoid a universal coverage percentage or duplicating every test in Playwright.

For deprecation/removal, identify users and consumers from code/configuration plus appropriate usage evidence; absence from sampled telemetry is not proof of no use. Preserve supported contracts while migrating callers and draining queued/scheduled work. Define the owner, compatibility period/exit criteria and fallback; use the project's communication workflow, with sending only when authorized. Resolve data retention/export/recovery needs before destruction. Remove related flags, credentials/grants, jobs/routes, infrastructure and documentation only after dependencies and retention obligations are addressed. Verify intended behavior and resource state; record residual obligations and untested steps without requiring a new retirement registry.

Use `resilience-testing` for relevant failure/recovery claims. Do not replace a performance suite with faults or trigger live experiments during routine feature work.

For substantial UI changes require a defined interaction direction and affected-surface coverage before implementation, then use interaction-design when available to verify the complete scope. For backend changes establish behavior/contracts first and reconcile every affected endpoint/job/tool. Fixing a representative example does not establish a completed global change.
