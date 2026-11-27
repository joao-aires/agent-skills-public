---
name: release
description: Prepare, review or verify an application release or deployment, whether
  merge-triggered continuous deployment or an explicitly authorized target action.
  Use for release readiness, post-rollout verification or an authorized target action;
  bare invocation prepares and reports rather than deploying.
user-invocable: true
disable-model-invocation: true
metadata:
  kind: activity
  domain: delivery
  phase: deployment
  scope: generic
  invocation: user
---

# Release

Prepare or perform an authorized release and stop at the requested readiness assessment or observed deployment outcome.

Read [activity system](../activity-system/SKILL.md) for scope and stopping point. For writing the artifact this activity produces, read [guide-release-note](../guide-release-note/SKILL.md) for structure, conventions and review.

When the affected stack, architecture or domain has installed expertise or guidance, read it and carry its conclusions. If none exists, use project evidence and primary sources; this activity keeps the outcome, acceptance and stopping point.

## Establish the release boundary

Resolve the requested stopping point before touching a target:

| Mode or request | Result and execution boundary |
| --- | --- |
| Continuous deployment | The merge, tag or pipeline trigger is the release event. Readiness gates and the accepted pipeline policy authorize it; do not invent a second manual approval. Verify the rollout and served outcome after the trigger. |
| Preparation or readiness review | Return a concise release assessment by default; do not mutate a target. |
| Authorized publish, deploy or recover action | Execute against the identified target through the established CLI/MCP/pipeline. |
| Rollback or recovery request | Use the identified recovery path; a mutating recovery still requires the named target and its authorization. |

Under continuous deployment there may be no separate release command. The activity still applies to the release event: what merge will trigger, which artifact and target it selects, whether the gates and recovery path are ready, and what evidence proves the served outcome. If no release-specific decision or verification remains, do not invoke this activity. Delivery-pipeline design and testing guidance can cover the pipeline and behavior evidence.

Identify exactly what is being released, where it will run or be distributed, and which configuration belongs to that target. Connect the artifact to its source revision and check results. Review the changes that survive replacing application code, especially schema/data changes and effects in external systems, because these determine whether rollback is sufficient.

## Readiness and authority

Readiness establishes what success will look like in the target, how a failed rollout will be contained, and whether the recovery path is usable. Authorization is a separate decision: use the project's established policy, environment approval or explicit user instruction rather than inventing a second ceremony. In continuous deployment, the accepted merge and pipeline policy is the authorization. Do not turn readiness into a redundant approval gate. Preserve established authorization across a sequence. An unspecified target or action blocks execution, and an emergency action does not widen the scope.

A green pipeline, a reviewed configuration or a locally built artifact is readiness evidence, not proof that the target serves the intended revision.

Before claiming readiness, confirm that every accepted requirement ID has evidence or an explicit blocker with an owner. Do not convert a missing acceptance row into a pass because the change was small, and do not claim release readiness from a subset of the requirements set.

## Execute an authorized action and verify

1. Serialize mutations as required and record their actual effects.
2. Verify the served revision, critical journeys and async/cache paths. A successful job alone does not establish customer success.
3. Stop or recover when verification fails. Do not continue promotion on the assumption that a later stage will correct it.

Record prepared, released, deployed and target-verified states separately in the change record with actual artifact and target evidence when authorized.

Release authority is not delegable. The release delegate executes the authorized action and verifies the result. It does not decide that authorization exists, widen the target or accept a failed verification. Give it the [delegation](../activity-system/references/delegation.md) envelope with the exact target and action. Authorization is read from the project's policy or the user, never inferred from a green pipeline.

## Recover deliberately

Keep a usable rollback or roll-forward route: the previous artifact and configuration, compatibility constraints, and a clear recovery input. Reverting application code does not undo data writes or delivered events. Prefer a compatible forward fix when reversal would lose data, and point to the application's runbook and continuity design when restoration is required. Claim production recovery only for mechanics actually exercised in a safe environment.

## Report

Report configured, prepared, released, deployed and target-verified states separately, with the artifact identity, target identity and remaining gaps. A generic release request does not automatically authorize merging, production deployment or data restoration.

## Composition

Apply [artifact-system](../artifact-system/SKILL.md) to the ECR sections used or produced by this activity, and [coordination storage](../artifact-system/references/storage/coordination.md) to locate the authorized filesystem or connected-provider authority. Resolve and update the mapped release note, changelog, runbook or SLO using [artifact homes](../artifact-system/references/homes.md) and the repository artifact home map. This does not require an issue or permit unrelated writes.

When available and relevant, compose with:

- installed delivery-pipeline guidance for provider-neutral stage, promotion, gate and recovery design;
- installed tooling guidance for the selected provider's implementation mechanics;
- installed workflow-hardening guidance when a GitHub Actions workflow is in scope;
- stack and operations guidance by capability for runtime, data and observability consequences.

These are optional supports, not prerequisites. Without them, apply this activity's own boundary, identity, verification and recovery checks using the project's commands and the identified target. Do not invent provider syntax or claim unverified recovery.
