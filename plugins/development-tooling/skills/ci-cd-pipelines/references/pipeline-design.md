# Pipeline design decisions

Provider-neutral decisions for moving a verified revision to a running target. Use this reference with the `ci-cd-pipelines` entry point. Workflow syntax, adapter mechanics and security review belong to `tooling-conventions` and `github-actions-hardening`; this reference keeps stage boundaries, gates, identity and evidence.

## Stage contract

| Stage | Responsibility and result |
| --- | --- |
| CI / verification | Verify the change; establish evidence about a source revision and its relevant configuration. |
| Release | Produce a versioned artifact whose identity can be traced to that evidence. |
| Deployment | Promote that artifact with its target configuration, perform the change, and verify the served outcome. |

Connect stage responsibilities through explicit inputs and outputs. A failure then identifies the stage to resume instead of forcing an unrelated rebuild. Combine stages for a small application when that is clearer, but keep artifact identity separate from target state.

## Gate design

| Decision | Rule |
| --- | --- |
| Required or advisory | Only call a gate enforced when its outcome actually blocks promotion or merge under project policy. |
| Order | Fast deterministic checks before expensive integration, end-to-end and platform checks. |
| Local/CI alignment | Run the same meaningful command and configuration in both; CI independently verifies its intended scope. |
| Path filters | Required checks must still report on every relevant path. Do not leave a check permanently pending or silently skipped. |
| Pre-publication | Test the built artifact and check its identity before publication. |
| Post-deployment | Verify the served revision and critical journeys, not only job success. |

A syntax, schema or lint check establishes its own stage. It does not establish provider semantics, an executed workflow or a working deployment.

## Artifact identity and promotion

- Build once and promote the same immutable artifact or digest through environments. Never rebuild from a tag when the artifact bytes should be unchanged.
- Include enough source identity to trace the artifact to its revision and check evidence. Timestamps help traceability but do not replace digest identity.
- Validate version and tag uniqueness for the actual registry. Never overwrite a published version; publish a new identity instead.
- If post-build metadata changes the artifact, validate the new identity before promotion.
- A release rerun reconciles existing tags, artifacts and deployment state before resuming. Never repeat an ambiguous mutation blindly.
- Expose artifact identity as an explicit output. Do not scrape a build log for a revision-like string.

Publication destination, namespace and distribution policy come from the artifact system and accepted project decisions. An internal service need not become a public package.

## Environment and configuration

- Keep environment configuration and secrets separate from the artifact. The same artifact is promoted; configuration and credentials belong to the target.
- Review the complete effective configuration diff, not only the changed image or version field. Preserve code/config/artifact traceability.
- Distinguish desired configuration from applied state. Verify the actual revision and affected outcome after application.
- Use environment protection and scoped deployment credentials appropriate to the project. Approval is an authorization control for that job, not a substitute for least privilege or target validation.
- Serialize promotions, releases and migrations that mutate the same resource. Do not cancel deployment or migration jobs mid-application casually.
- Retain a usable compatible recovery target. Rotated credentials and changed schemas can make an old configuration value unsafe to restore blindly.

### Feature flags

A flag needs a purpose, owner, audience, default and evaluation-failure behavior, tested relevant states and a removal condition. Flags control exposure, not authorization. Prefer bounded staged exposure and a tested kill path over an untested matrix of every combination. After an emergency override, reconcile source and effective state so the next deployment does not restore an unintended setting.

## Recovery boundary

Every delivery path should have a usable rollback or roll-forward route: retain the previous artifact and configuration, identify compatibility constraints, and expose a clear recovery input or job.

- Review schema compatibility before rollout; use expand/migrate/contract when old and new versions must coexist.
- Prefer a compatible forward fix when reversal would lose data. Point to the application's data-recovery runbook when restoration is necessary.
- Verify recovery mechanics in a safe environment and keep them current with migrations and infrastructure changes.

Rolling back application code does not undo data changes or delivered events. A configuration review or an unexercised rollback job does not establish production recovery.

## Branching and release flow

Branching manages integration and supported histories; release management labels a deliverable artifact; deployment changes a runtime. A tag does not imply anything is deployed, and a feature flag can separate deployment from exposure.

- Choose the simplest model that satisfies isolation and supported-version needs. Team size alone is not a branching criterion.
- Define version candidates, tag uniqueness and candidate provenance. Development identity should include the source revision and uniqueness.
- Propagate hotfixes to every required development and support line without importing unrelated unreleased work.
- Replace or retire flags and temporary compatibility paths deliberately; do not leave them as permanent branches.
- Serialize tag/release writers. Record partial completion precisely enough to resume without duplicating a release or reusing a version for different bytes.

Branching models, hotfix operations and migration between models are in [branch to production](branch-to-production.md).

## Pipeline evidence

Record these states separately:

| State | Evidence |
| --- | --- |
| Configured | Files and settings authored; provider syntax validated where a provider is selected. |
| Locally checked | Commands, tests and build executed in the developer environment. |
| Built | Artifact exists with a traceable identity and passed artifact-level checks. |
| Released | Artifact published to the intended destination with provenance. |
| Deployed | Artifact and configuration applied to the named target. |
| Outcome verified | Served revision, critical journeys and async/cache paths observed on the target. |

Report the checks and recovery paths exercised, target and artifact identities, and remaining gaps. Configuration review, local execution, a remotely completed promotion and customer verification are distinct evidence.

## New application baseline

A new application setup includes usable CI, artifact-build/release and deployment/recovery procedures, even when execution is local-only.

- Untrusted change validation runs meaningful checks and builds without privileged publication.
- Trusted release stages publish verified immutable artifacts with provenance, scoped credentials and reconciled reruns.
- Deployment requires an agreed target and configuration, verifies served behavior and retains compatible recovery.
- Native artifacts also require platform identity, signing/provisioning, installation/update and recovery evidence.

Preparing release files is not publication permission. Use project-foundation and artifact-system guidance for the remaining destination decisions, and record unresolved targets rather than inventing placeholder success paths.
