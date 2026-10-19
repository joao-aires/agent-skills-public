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

Read [workflow framing](../../WORKFLOW.md) for scope and invocation boundaries.

# Deliver changes with evidence

Connect the requested outcome to observable acceptance, implement useful increments and verify the affected capability at its real boundary. Choose depth from changed risk and existing project requirements.

## Establish the claim before implementation

Read accepted decisions, instructions and affected contracts. Preserve the existing architecture and UI direction unless changing them is the objective. Reuse agreed answers and the project's plan; a conversation can be sufficient scope. Use [Git contributions](../git-contributions/SKILL.md) for the objective worktree and contribution flow.

For a defect, reproduce the relevant failure before repairing it. Use diagnosing-bugs, tdd or specialist review where their method fits. Identify the state, authority, consumer and operating boundaries affected by the change. For substantial UI work, establish interaction direction and surface coverage with interaction design expertise; for backend work establish shared behavior before propagating it across entry points.

Define observable scenarios and expected outcomes before dependent implementation. Keep material criteria stable; a changed requirement needs a justified decision rather than an adjusted expectation to make a failing run pass. Keep consequential assumptions and unavailable capabilities explicit.

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
| Delivery or data migration | delivery expertise, compatibility and recoverability |
| Latency/load or controlled failures | implementation expertise matching the selected load-test tool or [resilience testing](../resilience-testing/SKILL.md), selected by the claim |

## Implement, test, inspect and repair

Keep meaningful regression tests with the feature as behavior is implemented. After each useful increment, run affected fast checks, exercise the changed path using the services it needs and inspect relevant diagnostics/state. Diagnose discrepancies, repair the shared cause and recheck before dependent work. Manual exploration complements committed tests. Add coverage for an observed failure at the smallest boundary that captures its cause.

Use isolated test data/stores and controlled providers. Journey-testing owns fixture identity, driver and platform details. Mocks demonstrate application handling; live integrations and native clients require their own evidence. Keep expensive load/fault/live-model checks at risk-appropriate milestones, rather than repeating every suite after each edit.

Before completion, reconcile all in-scope surfaces/consumers and run required broader regression. Exercise affected documented entrypoints and production build/start paths, with locked tools and real generated artifacts. Keep client, service and container configuration consistent. A failed required command or missing driver leaves the corresponding claim partial even when other tests pass.

Stop when acceptance is established or a precise blocker remains. Repeated failure without new evidence calls for diagnosis, not indefinite retries. Distinguish product defects, fixture/environment problems, stochastic evaluation and missing capabilities. Human decisions resolve unresolved product/taste questions; agent self-rating cannot supply that acceptance.

## Carry delivery consequences forward

Keep local and CI checks aligned, permissions/secrets protected and dependencies reproducible. Seek available delivery expertise for artifact/configuration compatibility, promotion and recovery. Choose operational depth from the affected journey: resource authority, bounded calls/retries, diagnosable failure and recovery come before adding a monitoring platform.

For changed critical journeys, keep accepted outcome/latency definitions, observation boundaries and signal/runbook links aligned. Distinguish admission, durable effects, acknowledgement and completion so retries preserve the business invariant. Use reliability expertise and observability expertise when installed; report unmeasured operational targets as such. Data-destructive migrations need compatibility and recovery evidence beyond application rollback.

## Maintain trustworthy coverage and close

Diagnose flaky checks before changing waits or retries. Any necessary quarantine records owner, reason, replacement evidence and repair/review condition as an explicit coverage gap. Remove redundant tests only after equivalent useful coverage exists. Choose tests by behavior and risk rather than a universal coverage percentage.

Review scope, correctness and avoidable complexity; resolve material findings. Keep affected knowledge current, seeking available knowledge-upkeep expertise when useful. For deprecation/removal, read [retiring behavior](references/retiring-behavior.md) before removing consumers, data or operating resources.

Report changed behavior, rationale, actual checks/artifacts and remaining limits, with revision/environment sufficient to reproduce material findings. Preserve useful regression evidence. Distinguish planned, implemented, verified and deployed states, and publish or execute remote actions only within established authority.
