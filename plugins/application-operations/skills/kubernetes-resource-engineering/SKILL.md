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

Engineer the rendered resource graph for the actual target. A copied base manifest or successful schema check is not enough to establish security, availability or maintainability.

## Modes and context

- **Interactive/setup:** discover cluster/version/controller capabilities, workload requirements and local policy; explain tradeoffs and implement resources in the chosen structure.
- **Feature/maintenance:** update workload/config/network/state dependencies and every impacted rendered target while preserving unrelated environments.
- **Recurring review:** render supplied target variants, audit secure-default and semantic drift, prepare bounded patches/tests, and retain exceptions/unknowns as stable findings. Apply/prune/cloud mutations only under assigned target authority.

Consult [references/resource-guide.md](references/resource-guide.md). Establish Deployments/jobs/stateful/infrastructure roles, target namespace, image identity, ports, identities/secrets, storage, dependency flows, availability/resource budget, reconciliation owner and expected deletion behavior. Verify supported API/CRD versions and actual CNI/admission/runtime features for deeper implementation details when needed.

## Workflow

1. Organize coherent common bases/chart templates and explicit target overrides. Use stable labels/selectors and typed/documented inputs; distinguish mandatory decisions from safe defaults.
2. Apply compatible least-privilege workload identity, pod/container security, immutable images, protected configuration/secrets and narrowly exposed ports.
3. Define explicit traffic flows and network isolation, including DNS, collectors, controllers and external dependencies; verify allowed and denied paths.
4. Budget CPU/memory/storage and startup/drain/recovery. Align probes, shutdown, rollout, replica capacity, disruption budgets, topology and scaling ownership with the actual workload.
5. Define jobs' deadlines/retries/concurrency/timezone, storage retention/reclaim, infrastructure deletion policy and required recovery/access paths.
6. Render all affected variants with pinned tools. Test cross-resource selectors/references, config substitutions, image/version identity, unresolved placeholders, CRD schema coverage and exceptions.
7. Run schema/policy checks plus target admission/diff where authorized. Review deletes, immutable changes, reconciliation dependencies and CRD upgrades separately.
8. Deliver through the existing controller workflow; verify readiness, routing, denied boundaries, job/data outcomes and source/live reconciliation. Track staged local versus live validation honestly.

## Completion evidence

Return resource/config/chart changes, target render matrix, security/reliability rationale, tests/schema/policy/admission results and specific exemptions or inaccessible live checks. Use `infra-jvm-optimization` for measured runtime tuning, `credential-lifecycle` for secret authority and `protect-and-restore-data` for restore design rather than duplicate their workflows.
