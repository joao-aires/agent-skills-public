---
name: ci-cd-pipelines
description: >-
  Design or review provider-neutral CI/CD delivery: verification, artifact
  and deployment stages, artifact identity and promotion, environment and configuration
  separation, gate design, branching and release flow, recovery, and pipeline evidence.
  Use when choosing or auditing a pipeline shape rather than implementing a specific
  provider's syntax.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: technical
  domain: tooling
  phase: release
  scope: generic
  invocation: both
  role: support
---

# Design CI/CD pipelines

A pipeline is the durable contract between a verified source revision, an immutable artifact and the target that serves it. This method owns the provider-neutral shape of that contract: which stage owns which decision, how identities connect, where gates block promotion, and what evidence a completed delivery leaves behind.

It does not own the release decision or a host's implementation. The `release` activity establishes the boundary, authorizes the target action and verifies the outcome. A selected provider's syntax and execution features belong to `tooling-conventions`, and workflow security belongs to `github-actions-hardening`. No CI host is required by this method; when none is selected, keep the stage and evidence decisions and record the unresolved target.

## Reading path

| Need | Read |
| --- | --- |
| Stage contracts, gate checklists, promotion and recovery decision tables | [Pipeline design](references/pipeline-design.md) |
| Branching models, release lines, hotfix propagation and migration between models | [Branch to production](references/branch-to-production.md) |
| Selected provider workflow mechanics, adapters and execution features | `tooling-conventions` |
| GitHub Actions trust boundaries, injection and token scope | `github-actions-hardening` |
| Release authority, target verification and reporting states | `release` activity |
| Artifact destinations, provenance and release-note contracts | `artifact-system`, `guide-release-note` |

Read only the reference that matches the open decision.

## Keep three identities separate

| Stage | Result |
| --- | --- |
| Verification | Evidence about a source revision and its relevant configuration. |
| Release | A versioned artifact whose identity traces to that evidence. |
| Deployment | That artifact, promoted with target configuration, exercising the change and verifying the served outcome. |

Keeping the identities connected lets a failed stage be diagnosed and resumed without rebuilding or republishing an unrelated result. Combine stages for a small application when that stays clearer, but do not collapse artifact identity into the deployment job.

## Decide the durable parts

- **Gates.** Decide what blocks promotion and what is advisory. Run the same meaningful checks locally and in CI, put fast feedback before expensive integration checks, and keep required checks present on every path. A skipped or absent check is not a pass.
- **Artifact identity.** Build once, promote the same immutable artifact or digest, and keep environment configuration out of it. Never overwrite a published identity. A rerun reconciles existing tags, artifacts and target state before resuming.
- **Environment separation.** Distinguish desired configuration from applied state, review the complete effective diff, and bind credentials and protection to the environment rather than the artifact. Serialize writers for shared targets, releases and migrations.
- **Recovery.** Design the rollback or roll-forward route before promotion, retain a usable previous artifact and configuration, and identify schema and data compatibility constraints. Reverting code does not undo data writes or delivered events.
- **Flow.** Distinguish branching, release and deployment contracts. Choose trunk or release branches from isolation and supported-version needs, not team size. Preserve the established model unless migration is requested, and propagate hotfixes to every supported line.

Use [pipeline design](references/pipeline-design.md) for the stable checklists and decision tables behind these choices.

## Bound the implementation

Provider syntax, reusable interfaces, shell steps, matrices, caches and concurrency mechanics belong to `tooling-conventions`. Security review of the selected host's trust boundaries belongs to `github-actions-hardening`. Artifact destinations and provenance expectations belong to `artifact-system`. Use stack and operations guidance by capability when it is installed and relevant; without it, retain the decision and evidence standard here using project commands and the actual target.

An unconfigured target is not a reason to create success-only placeholder jobs. Record the unresolved destination or deployment decision instead of asserting readiness.

## Report distinct evidence

Separate authored, linted, built, released, deployed and outcome-verified states. A workflow file, a YAML parse, a lint pass or a successful job establishes only its own stage; none proves that the target serves the intended revision or that a customer journey completed. Report which gates and recovery paths were actually exercised, the artifact and target identities, and the remaining gaps.
