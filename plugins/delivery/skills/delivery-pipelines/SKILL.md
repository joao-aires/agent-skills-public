---
name: delivery-pipelines
description: Create or review provider-independent CI/CD and release contracts for application
  verification, artifact promotion, deployment and rollback or roll-forward. Apply
  when delivery infrastructure changes, within the requested repository and environment
  scope.
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: false
---

# Build delivery pipelines

## Separate verification, artifacts and deployment

Read the application commands, environment model and accepted deployment decisions. Distinguish the stage responsibilities:

| Stage | Responsibility |
| --- | --- |
| CI | Verify a change. |
| Release | Produce a versioned artifact. |
| Deployment | Promote that artifact to an environment. |

Connect the stages through explicit inputs and outputs. Verification establishes evidence about a source revision and its relevant configuration. Release creates an artifact with an identity that can be traced to that evidence. Deployment selects the artifact and target configuration, performs the change, and verifies the served outcome. This separation makes it possible to diagnose a failed stage and resume without rebuilding or republishing an unrelated result.

Combine stages for a small application when clearer. Share repeated mechanics through the selected provider's reusable interfaces with explicit inputs, permissions and outputs; avoid a generic pipeline framework.

Keep provider-required entrypoints in their required locations and component-specific build/scripts beside their owner. Run the same meaningful checks locally and in CI. Provide fast feedback before expensive integration/E2E checks, retain useful failure evidence, and make required checks stable across path filters. Do not let a skipped workflow leave a required check permanently pending.

## Use readable names

Name workflows, jobs and steps by their purpose, component and target. Preserve a consistent existing convention. Make dependency order, required gates, inputs/outputs and failure behavior visible without reading every implementation detail. Seek matching tool expertise for the selected provider's syntax and reusable adapters.

## Promote and recover deliberately

- Build once and promote the same immutable artifact/digest through environments.
- Keep environment configuration and secrets separate from the artifact.
- Use scoped deployment credentials, environment protection appropriate to the project, and concurrency controls that prevent overlapping promotions; do not cancel a deployment mid-migration casually.
- Record the deployed revision and artifact, run post-deploy smoke checks against the real target, and stop promotion on failure.

Every delivery path should have a usable rollback or roll-forward route: retain the previous artifact/configuration, identify compatibility constraints, and expose a clear recovery input or job.

- Review schema compatibility before rollout; use expand/migrate/contract when needed.
- Prefer a compatible forward fix when reversal would lose data; point to the application's data-recovery runbook when restoration is necessary.
- Verify the recovery mechanics in a safe environment and keep them current with migrations and infrastructure changes.

Rolling back application code does not undo data changes. A YAML review alone does not establish production recovery.

## Check stack-specific rollout consequences

Use backend/frontend conventions for process lifecycles, connection budgets, production entrypoints and cache/configuration behavior. Coordinate compatible schema changes and resumable backfills with releases; do not run long data work independently in every replica startup. Verify async completion and stale client/cache paths where those affect the journey. A reverted image does not reverse data writes or undo delivered events. Preserve the deployed revision, migration/backfill state and recovery preconditions in the project's existing records.

## Protect the pipeline

Separate untrusted validation from privileged publication/deployment, minimize permissions and use supported short-lived credentials where available.

- Treat source/event inputs as untrusted, protect build inputs and caches across trust boundaries, and never expose deployment credentials to arbitrary change code.
- Pin executable dependencies according to the project's supply-chain policy, bound job duration and retain sanitized failure evidence.
- Use matching provider specialists when available; no CI host is required by this method.

Report which checks and recovery paths were exercised, target identities and remaining gaps. Configuration review, local execution and a remotely completed promotion are distinct evidence.

## Branching, releases and partial completion

Distinguish branching, release and deployment contracts. Choose trunk-based or release branches from isolation and supported-version needs; team size alone does not require Gitflow. Preserve the established model unless migration is requested. Define version/tag uniqueness, candidate provenance, feature-flag retirement and hotfix propagation to every required development/support line.

A release rerun reconciles existing tags, artifacts and deployment state before resuming; it never overwrites an immutable identity or repeats an ambiguous mutation blindly.

- Serialize writers without cancelling active release/migration jobs.
- If metadata changes the artifact, validate the new identity.
- Verify the running and served revision, cached paths, critical user outcomes and async completion; a successful release job is not customer verification.
- Record configured, locally checked, built, released, deployed and outcome-verified states separately.

Use reliability expertise for journey and alert contracts and observability expertise for signal readiness when those skills are available. Keep release verification meaningful without requiring a new monitoring vendor.

For branching, partial releases and gate decisions, read [branch to production](references/branch-to-production.md). For selected provider/container/registry implementation, use available guidance for the selected development tools and matching stack expertise.

For performance workflows, define an accepted workload and isolate application/dependency execution on the runner or use an identified authorized non-production target. Seek implementation expertise for the project's selected load-test tool. Preserve thresholds, failure status, result artifacts and cleanup; bind credentials and concurrency to the actual environment.

## Deliver configuration and flag changes

Validate settings and affected target combinations, inspect the complete effective diff and preserve code/config/artifact traceability. Distinguish desired configuration from applied state; verify the actual revision and affected outcome after application. Retain a usable compatible recovery target, accounting for rotated credentials and changed schemas rather than blindly restoring stale values. Use the existing configuration/GitOps mechanism; no new central service is required.

### Feature flags

Feature flags need a purpose, owner, intended audience, default/evaluation-failure behavior, tested relevant states and a removal condition.

- Flags control exposure, not authorization.
- Use bounded staged exposure and a kill/recovery path when risk warrants it; do not create an untested matrix of every flag combination.
- After an emergency override, reconcile source and effective state so later deployments do not restore an unintended setting.

### Runtime and dependency upgrades

For routine runtime/library/base-image upgrades, review supported versions and release notes, keep coupled versions coherent, regenerate lockfiles with the project's tools, verify affected behavior and publish a new tested artifact. Automation can propose updates; passing installation or a vulnerability scan alone does not establish compatibility. Follow accepted release/recovery conventions without imposing universal automatic merges.

## Verify application execution on the runner

For application-on-runner checks, reuse the supported local service mechanism and configuration with isolated project/data/ports and explicit migrations, seed and readiness.

- Preserve failure exit status while collecting test screenshots/traces, service logs and correlated diagnostic evidence; clean up owned resources even on failure.
- Keep fast deterministic checks routine and heavier platform, visual, load/fault and real-model evaluations at appropriate risk-based milestones.
- Use appropriate native runners/devices for desktop/mobile checks.
- A backend run does not prove native-client behavior; missing platform coverage stays visible.


## Validate code, configuration and secrets

For language/configuration/secret checks use the project's compatible tools and commands. Keep local/hook and CI semantics aligned; CI independently verifies its intended scope. A syntax check does not establish provider semantics, and a staged secret check does not establish clean history. Preserve failing status while collecting redacted evidence.

## Establish new-project artifact and deployment contracts

A new application setup includes usable CI, artifact-build/release workflows and deployment/recovery procedures, even when execution is local-only. Use project foundation expertise when available for foundation outcomes. Select publication destinations from the artifact ecosystem, accepted distribution policy and actual namespace/ownership. Internal services need not become public packages. Native artifacts require platform identity, signing/provisioning, installation/update and recovery evidence.

- Untrusted change validation runs meaningful checks and builds without privileged publication.
- Trusted release stages publish verified immutable artifacts with provenance, scoped credentials and reconciled reruns.
- Require an agreed target/configuration before deployment, verify served behavior and retain compatible recovery.
- Preparing release files is not publication permission; an unknown target is not a reason to create success-only placeholder jobs.
- Distinguish authored, linted, locally exercised, published, deployed and outcome-verified stages.
