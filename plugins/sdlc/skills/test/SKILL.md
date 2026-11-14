---
name: test
description: Select, add, run and review checks; establish completion evidence for a change, journey, component or application. Use for unit/integration/contract/web/desktop/mobile verification, completion review and relevant performance or resilience checks within the authorized target scope.
user-invocable: true
disable-model-invocation: true
metadata:
  kind: activity
  origin: local
  pack: sdlc
  domain: development
  phase: verification
  scope: generic
  invocation: user
  role: task
---

# Verification

Read [activity system](../activity-system/SKILL.md) for scope and stopping point.

Verification connects the requested outcome to observable acceptance, selects checks that can observe it, and reports what was actually established at the stated boundary. It includes the completion review that was formerly separate: evidence, suite health, delivery consequences and the remaining gaps.

## Establish the claim before implementation

Read accepted decisions, instructions and affected contracts. Preserve the existing architecture and UI direction unless changing them is the objective. Reuse agreed answers; a conversation can be sufficient scope. Use [Git contributions](../git-contributions/SKILL.md) for the objective worktree and contribution flow.

For a defect, reproduce the relevant failure before repairing it. Use diagnosing-bugs, tdd or specialist review where their method fits.

Describe what will be different when the work succeeds: the starting condition, the action and the result a user or another consumer can observe. Include stored changes and denied actions where they matter, so the check can detect an implementation that appears successful while leaving the application in the wrong state.

Keep material criteria stable; change them only when the underlying requirement has changed for a reason. Investigate a mismatch before adjusting the expected result. Record consequential assumptions and unavailable capabilities so a later report cannot turn an unexecuted check into a success claim.

## Select meaningful coverage

Identify what the requested change promises and what could break that promise. Inspect the existing tests and project commands before adding another test layer. Select checks that can observe the relevant result, including the previously broken condition for a bug fix and important denial or failure paths for changed behavior.

Prefer the narrowest check that exercises the behavior faithfully, then cross a real integration boundary when a substitute would hide the risk. A test of a component with a fake service can establish its response to that service; it cannot establish that the actual service stores the right result.

Add missing coverage where needed. Keep assertions independent enough to catch a plausible faulty implementation. Diagnose a failing test before deciding whether the application, fixture or environment is wrong; do not silently alter production behavior, weaken assertions or inflate retries to pass.

## Match evidence to the claim

| Claim | Sufficient kind of evidence |
| --- | --- |
| Implemented | Relevant code/configuration exists; missing behavior is identified. |
| Behavior verified | Affected acceptance, failure and authority cases ran at the stated persistence/provider/platform boundary. |
| Ready for deployment | Required checks pass and applicable configuration, compatibility, migration and recovery consequences are resolved. |
| Verified after deployment | The intended revision is served and the affected journey works in the named target. |

These describe evidence, not additional approval ceremonies. A build, screenshot, successful transport response or runner narrative establishes only its own boundary. Use independent observable outcomes for important effects, including persistence and denied access. Verify proposed corrections as well as the current defect; distinguish a measured result from a hypothesis or unexecuted check.

| Changed concern | Verification owner |
| --- | --- |
| Domain logic | Focused behavior/regression tests at useful public interfaces |
| API, stored state or authority | Real contract/persistence integration and allowed/denied outcomes |
| UI or user journey | [Journey testing](../journey-testing/SKILL.md), implemented component states, rendered review and actual target-platform operation |
| Dependencies/configuration/runtime | Relevant lint/type/schema/build and actual startup/configuration checks |
| Delivery or data migration | Delivery expertise, compatibility and recoverability |
| Latency/load or controlled failures | Implementation expertise matching the selected load-test tool or [resilience testing](../resilience-testing/SKILL.md), selected by the claim |

## Implement, test, inspect and repair

Keep meaningful regression tests with the feature as behavior is implemented. For each useful increment:

1. Run affected fast checks and exercise the changed path using the services it needs.
2. Inspect outcomes, diagnostics and relevant state against the accepted criteria.
3. Diagnose discrepancies, repair the shared cause and recheck before dependent work. Add coverage for an observed failure at the smallest boundary that captures its cause.

Read the test results and inspect the behavior they are meant to establish. A passing assertion can still exercise the wrong route, use a privileged test identity or bypass persistence. Check important effects through an observation that does not merely repeat the implementation's own success response. Manual exploration complements committed tests by exposing unexpected interaction and configuration problems; preserve useful reproductions as regression coverage.

Use isolated test data/stores and controlled providers. Journey-testing owns fixture identity, driver and platform details. Mocks demonstrate application handling; live integrations and native clients require their own evidence. Keep expensive load/fault/live-model checks at risk-appropriate milestones, rather than repeating every suite after each edit.

Before completion, reconcile all in-scope surfaces/consumers and run required broader regression.

- Exercise affected documented entrypoints and production build/start paths, with locked tools and real generated artifacts.
- Keep client, service and container configuration consistent.

A failed required command or missing driver leaves the corresponding claim partial even when other tests pass.

Stop when acceptance is established or a precise blocker remains. Repeated failure without new evidence calls for diagnosis, not indefinite retries. Distinguish product defects, fixture/environment problems, stochastic evaluation and missing capabilities. Human decisions resolve unresolved product/taste questions; agent self-rating cannot supply that acceptance.

## Carry delivery consequences forward

Keep local and CI checks aligned, permissions/secrets protected and dependencies reproducible. Seek available delivery expertise for artifact/configuration compatibility, promotion and recovery. Choose operational depth from the affected journey: resource authority, bounded calls/retries, diagnosable failure and recovery come before adding a monitoring platform.

For changed critical journeys, keep accepted outcome/latency definitions, observation boundaries and signal/runbook links aligned.

- Distinguish admission, durable effects, acknowledgement and completion so retries preserve the business invariant.
- Use reliability expertise and observability expertise when installed; report unmeasured operational targets as such.
- Data-destructive migrations need compatibility and recovery evidence beyond application rollback.

## Maintain trustworthy coverage and close

Diagnose flaky checks before changing waits or retries.

- Any necessary quarantine records owner, reason, replacement evidence and repair/review condition as an explicit coverage gap.
- Remove redundant tests only after equivalent useful coverage exists.
- Choose tests by behavior and risk rather than a universal coverage percentage.

Review scope, correctness and avoidable complexity; resolve material findings. Keep affected knowledge current, seeking available knowledge-upkeep expertise when useful. For deprecation/removal, read [retiring behavior](references/retiring-behavior.md) before removing consumers, data or operating resources.

Report changed behavior, rationale, actual checks/artifacts and remaining limits, with revision/environment sufficient to reproduce material findings. Preserve useful regression evidence. Distinguish planned, implemented, verified and deployed states, and publish or execute remote actions only within established authority.

When work crosses actors or sessions, retain the provenance needed to interpret completion. Distinguish initial implementation, later repairs, independent review and the revision actually exercised. An interrupted run is not proof it would never have completed.

## Record the verification result

Apply [artifact assurance](../artifact-system/references/assurance.md) to compare actual checked behavior with accepted requirements, protected existing behavior and proposed design. Missing or failed acceptance evidence remains explicit nonconvergence, not an automatic green result.

Record observations at the checked revision/target, the command or scenario, environment, result, evidence path, failed/skipped/unavailable checks, coverage gaps and design/diagram differences in the change record when authorized, or return a structured unpersisted record. Return results, artifacts, actual boundaries and the next action. A green build alone does not establish behavior.

## Composition

Apply [artifact-system](../artifact-system/SKILL.md) to the ECR sections used or produced by this activity, and [coordination storage](../artifact-system/references/storage/coordination.md) to locate the authorized filesystem or connected-provider authority. This does not require an issue or permit unrelated writes. Read [project conventions](../project-conventions/SKILL.md) for the project's checks and [journey-testing](../journey-testing/SKILL.md) for changed user journeys. Load optional stack/domain guidance only when relevant and available.
