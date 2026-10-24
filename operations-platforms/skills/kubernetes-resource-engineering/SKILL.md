---
name: kubernetes-resource-engineering
description: Design, generate, review and maintain Kubernetes application/infrastructure
  resources, Helm charts and Kustomize overlays with secure defaults, reliable lifecycle,
  controller ownership and rendered validation.
metadata:
  scope: stack-specific
  invocation: both
  stack: Kubernetes, Helm, Kustomize
  version: '1.0'
  role: task
---

# Kubernetes resource engineering

Design the resources as a connected application in the actual target. Follow selectors, references, ports, identities, configuration and storage from the workload to the objects it depends on. Establish which controller owns desired state and which values each environment overrides; the effective rendered resources are the ones whose behavior needs review.

Assess the lifecycle as well as the shape of each object. Decide how the application starts, becomes ready, accepts traffic, drains and recovers, then check whether probes, rollout settings, resources and dependent jobs support that behavior. A copied base manifest or successful schema check cannot establish those relationships by itself.

## Modes and context

- **Interactive/setup:** discover cluster/version/controller capabilities, workload requirements and local policy; explain tradeoffs and implement resources in the chosen structure.
- **Feature/maintenance:** update workload/config/network/state dependencies and every impacted rendered target while preserving unrelated environments.
- **Recurring review:** render supplied target variants, audit secure-default and semantic drift, prepare bounded patches/tests, and retain exceptions/unknowns as stable findings. Apply/prune/cloud mutations only under assigned target authority.

Establish Deployments/jobs/stateful/infrastructure roles, target namespace, image identity, ports, identities/secrets, storage, dependency flows, availability/resource budget, reconciliation owner and expected deletion behavior. Verify supported API/CRD versions and actual CNI/admission/runtime features. Consult [the resource guide](references/resource-guide.md) for deeper implementation details.

## Workflow

### Define the resource contract

| Concern | Define in the selected manifests/chart structure |
| --- | --- |
| Organization | Coherent common bases/templates, explicit target overrides, stable labels/selectors and typed/documented inputs. Distinguish required decisions from safe defaults. |
| Workload security | Compatible least-privilege identity, pod/container security, immutable images, protected configuration/secrets and narrowly exposed ports. |
| Network | Explicit allowed and denied flows, including DNS, collectors, controllers and external dependencies. |
| Resource and lifecycle | CPU/memory/storage, startup/drain/recovery, probes, rollout, replica capacity, disruption budgets, topology and scaling ownership. |
| Jobs and retained resources | Deadlines/retries/concurrency/timezone, storage retention/reclaim, infrastructure deletion policy and recovery/access paths. |

### Render, check and deliver

1. Render all affected variants with pinned tools. Test selectors/references, substitutions, image/version identity, unresolved placeholders, CRD schema coverage and exceptions; verify allowed and denied network paths.
2. Run schema/policy checks and authorized target admission/diff. Review deletes, immutable changes, reconciliation dependencies and CRD upgrades separately.
3. Deliver through the existing controller workflow within target authority. Verify readiness, routing, denied boundaries, job/data outcomes and source/live reconciliation. Distinguish local from live validation.


## Completion evidence

Return resource/config/chart changes, target render matrix, security/reliability rationale, tests/schema/policy/admission results and specific exemptions or inaccessible live checks. Use `infra-jvm-optimization` for measured runtime tuning, credential management expertise for secret authority and data recovery expertise for restore design rather than duplicate their workflows.
