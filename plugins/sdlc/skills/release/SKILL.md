---
name: release
description: Prepare or execute a named application release/deployment with artifact,
  configuration, compatibility and recovery verification. Use for deployment readiness
  or an explicitly authorized target action; bare invocation prepares and reports
  rather than deploying.
user-invocable: true
disable-model-invocation: true
metadata:
  kind: activity
  origin: local
  pack: sdlc
  domain: delivery
  phase: release
  scope: generic
  invocation: user
  role: task
---

# Release

Read [activity system](../activity-system/SKILL.md).

For writing the artifact this activity produces, read [guide-release-note](../guide-release-note/SKILL.md) for structure, conventions and review.

## Establish the release boundary

Resolve the requested stopping point before touching a target:

| Request | Result and execution boundary |
| --- | --- |
| Preparation or readiness review | Return a concise release assessment by default; do not mutate a target. |
| Authorized publish, deploy or recover action | Execute against the identified target through the established CLI/MCP/pipeline. |
| Rollback or recovery request | Use the identified recovery path; a mutating recovery still requires the named target and its authorization. |

Identify exactly what is being released, where it will run or be distributed, and which configuration belongs to that target. Connect the artifact to its source revision and check results. Review the changes that survive replacing application code, especially schema/data changes and effects in external systems, because these determine whether rollback is sufficient.

## Readiness and authority

Readiness establishes what success will look like in the target, how a failed rollout will be contained, and whether the recovery path is usable. Authorization is a separate decision: use the project's established policy, environment approval or explicit user instruction rather than inventing a second ceremony. Preserve established authorization across a sequence; an unspecified target or action blocks execution, and an emergency action does not widen the scope.

A green pipeline, a reviewed configuration or a locally built artifact is readiness evidence, not proof that the target serves the intended revision.

## Execute an authorized action and verify

1. Serialize mutations as required and record their actual effects.
2. Verify the served revision, critical journeys and async/cache paths. A successful job alone does not establish customer success.
3. Stop or recover when verification fails; do not continue promotion on the assumption that a later stage will correct it.

Record prepared, released, deployed and target-verified states separately in the change record with actual artifact and target evidence when authorized.

## Recover deliberately

Keep a usable rollback or roll-forward route: the previous artifact and configuration, compatibility constraints, and a clear recovery input. Reverting application code does not undo data writes or delivered events; prefer a compatible forward fix when reversal would lose data, and point to the application's data-recovery runbook when restoration is required. Claim production recovery only for mechanics actually exercised in a safe environment.

## Report

Report configured, prepared, released, deployed and target-verified states separately, with the artifact identity, target identity and remaining gaps. A generic release request does not automatically authorize merging, production deployment or data restoration.

## Composition

Apply [artifact-system](../artifact-system/SKILL.md) to the ECR sections used or produced by this activity, and [coordination storage](../artifact-system/references/storage/coordination.md) to locate the authorized filesystem or connected-provider authority. Resolve and update the mapped release note, changelog, runbook or SLO using [artifact homes](../artifact-system/references/homes.md) and the repository artifact home map. This does not require an issue or permit unrelated writes.

When available and relevant, compose with:

- `ci-cd-pipelines` for provider-neutral stage, promotion, gate and recovery design;
- `tooling-conventions` for the selected provider's implementation mechanics;
- `github-actions-hardening` when a GitHub Actions workflow is in scope;
- stack and operations guidance by capability for runtime, data and observability consequences.

These are optional supports, not prerequisites. Without them, apply this activity's own boundary, identity, verification and recovery checks using the project's commands and the identified target; do not invent provider syntax or claim unverified recovery.
