---
name: infra-delivery
description: >-
  Expertise and methods for infrastructure delivery. Define and deliver infrastructure and
  platform configuration as reconciled desired state across Kubernetes and cloud targets. Use
  for infrastructure-as-code choice, repository structure, environment promotion, policy and
  rendered-state validation, Argo CD/Flux GitOps reconciliation, drift, pruning and recovery.
  It informs the activity that composes it; that activity owns the decision and stopping
  point.
metadata:
  kind: method
  domain: platform
  phase: deployment
  scope: generic
  invocation: both
user-invocable: true
---

# Deliver infrastructure as reconciled desired state

Infrastructure delivery is the control loop that turns a reviewed declaration into an observed target and keeps them converged. It owns the declaration, its promotion, the reconciler and the response to drift. Infrastructure-as-code is part of this method; it is not a separate skill.

This method does not own the meaning of the resources being delivered, the provider's service design, the pipeline's stage contract or the release decision. `kubernetes-resource-engineering` owns Kubernetes object semantics, lifecycle and rendered resource behavior; `aws-platform` owns AWS service choices and account mechanics; `ci-cd-pipelines` owns verification, artifact and deployment stages; `release` establishes the release boundary, authorizes the target action and verifies the served outcome. When those capabilities are absent, keep this method's ownership, validation and evidence decisions using the project's tools and the actual target.

## Establish the delivery contract

Resolve the contract before choosing or changing a tool:

| Concern | Establish |
| --- | --- |
| Desired-state owner | Repository, path and revision that own each resource |
| Target identity | Account, region, cluster, namespace and environment |
| Reconciler | Controller, pipeline job or operator; how it authenticates |
| Ownership | Which resources are managed, shared, imported or deliberately unmanaged |
| Bootstrap | How state storage, controller, permissions and the first resources are created |
| Change path | Who may merge and apply; what authorization the target requires |
| Observed state | Plan output, provider API, controller status or drift report |
| Deletion policy | What may be pruned, what is protected and how recovery works |

One resource has one declared owner. Mixed tooling is acceptable at boundaries — for example account-level infrastructure in one system and application resources in another — but overlapping ownership produces fights that no reconciliation interval can fix. Do not introduce a second tool for a one-off when the established tool can express the change.

## Choose the desired-state mechanism

Choose from the target and the operating model, not from novelty. The comparison table and its watch-outs are in [configuration model](references/configuration-model.md).

- **Declarative provisioners** (Terraform/OpenTofu, CloudFormation, Pulumi, CDK) are a good fit when the target exposes a broad API, a plan or preview is useful, and state can be owned and protected.
- **Kubernetes-native control planes** (Crossplane) fit when platform APIs should be reconciled from inside a cluster and consumed as claims. Read [Crossplane control plane](references/crossplane-control-plane.md) before choosing it.
- **Configuration management** (for example Ansible) fits mutable hosts, appliances and bootstrap steps where a provisioning plan is not the primary model. It does not replace resource reconciliation on an immutable platform.
- **GitOps controllers** (Argo CD, Flux) fit continuous reconciliation of declared Kubernetes and platform state from Git. Read [GitOps reconciliation](references/gitops.md).

Record why the chosen mechanism fits the target, who owns its state and how drift is detected. A tool that cannot represent the resource or cannot be reconciled safely is the wrong tool even if the team knows it.

## Structure the repository for promotion

- Separate reusable modules/components from environment bindings. Modules declare typed inputs, outputs and supported provider versions; environments supply values and references.
- Promote by version or reference, not by copying a directory and editing it. Copies diverge silently and make a fixed defect reappear in one environment.
- Pin providers, modules and controller versions, and commit the lock files the tool produces. An unpinned resolver makes yesterday's plan unreproducible.
- Keep state and credentials out of the repository. Separate state per environment, account and component where the blast radius requires it; encrypt, lock and restrict access to the backend.
- Store secret references, not values. Encrypted Git material is encryption at rest inside the repository, not custody; its decryption key needs the same authority as the secret. Application consumption belongs to `application-configuration`.
- Keep policy, generated manifests and tests in discoverable locations. Do not hand-edit generated output.
- Mark ownership and review boundaries in code ownership metadata. A path that changes production account permissions deserves a different reviewer from a documentation change.
- Keep environment conditionals out of shared modules when they make one environment's change alter another's behavior. Branch on declared inputs, not on the environment name embedded in a template.

## Validate before reconcile

Validation is layered because each layer catches a different mistake:

| Layer | Catches | Does not establish |
| --- | --- | --- |
| Format and syntax | Unparseable files, invalid interpolation | Valid semantics or acceptable change |
| Schema and types | Wrong field, missing required input, incompatible provider version | That the resource behaves as intended |
| Policy as code | Prohibited configuration, missing tags, public exposure, privilege | That the target admits or supports it |
| Plan or preview | Full effective diff, replacements, deletes | Applied state or runtime health |
| Rendered manifests | Selectors, references, image identity, unresolved placeholders | Live admission, controller behavior |
| Admission or dry run | Cluster policy, schema and mutation behavior | Actual reconciliation or workload readiness |
| Ephemeral target | Integration behavior and ordering | Production data, scale or provider quotas |

Review the complete effective diff, not only the field that was edited. Treat replacement of a stateful resource, an immutable field change, a CRD or controller upgrade, and a state migration as separate risks. A successful plan is evidence about the declaration; it is not evidence that the target changed.

## Reconcile and promote

GitOps makes the repository the declared source and a controller responsible for convergence. The controller compares desired and observed state, applies the difference, prunes what is no longer declared when allowed, and reports health. Argo CD and Flux implement this model with different resource shapes and health semantics; compare them in [GitOps reconciliation](references/gitops.md).

Push-based application through a pipeline remains valid where the target, credentials or policy require it. The same principles apply: reviewed declaration, explicit target, effective diff, serialized writers and post-apply verification.

Promotion rules:

- Promote the same module or artifact version; change environment values and references only.
- Order dependencies explicitly, and make sync waves or equivalent waits reflect real readiness rather than sleep.
- Serialize writers to a shared target. Two reconcilers or a human console session applying the same resource is an ownership conflict.
- An approval authorizes a target action; it is not validation. Keep plan, policy and target checks separate from the approval.
- Continuous reconciliation may deploy automatically after merge. That does not remove the need to verify the served revision and dependent behavior.
- On failure, stop promotion and reconcile the actual state before retrying. A retry that assumes the previous attempt did nothing can duplicate or destroy resources.

## Detect drift, prune safely and recover

Drift is any difference between declared and observed state, in either direction. It appears through manual console edits, out-of-band controllers, partial applies, deleted resources, provider-defaulted fields, changed credentials and controller outages.

Classify before repairing:

- **Intentional and durable:** codify it, or record an owned exception with an expiry.
- **Unauthorized or accidental:** reconcile back, then investigate how the change bypassed the path.
- **Emergency manual change:** preserve the evidence, reconcile deliberately after the incident, and do not let self-healing erase the only working state.
- **Default or representational noise:** fix the comparison or the provider field, not the resource.

Pruning and self-healing are destructive when applied blindly. Protect data-bearing, shared and externally referenced resources; use deletion protection, finalizers, retain policies and a dry-run prune where the tool supports them. Provide a documented way to pause reconciliation during a recovery without permanently disabling it.

Recovery includes the delivery system itself: lost state, a failed controller, a compromised repository or credential, and a cluster that no longer exists. Keep bootstrap reproducible, back up the state and controller configuration that cannot be regenerated, and exercise restore. Read [drift and recovery](references/drift-and-recovery.md) for the scenario table.

## Keep the boundaries explicit

| Concern | Owner |
| --- | --- |
| Kubernetes resource semantics, selectors, probes, storage, workload lifecycle | `kubernetes-resource-engineering` |
| AWS service selection, account and network design | `aws-platform` |
| Verification stages, artifact identity, promotion and pipeline gates | `ci-cd-pipelines` |
| Release boundary, authorization and served-outcome verification | `release` |
| Application configuration keys, precedence and secret consumption | `application-configuration` |
| Capacity, scaling and cost tradeoffs | `analyze-capacity-cost` |
| Provider CLI, workflow syntax and execution mechanics | `tooling-conventions` |
| Credential rotation, revocation and exposure response | security maintenance and incident response capabilities |

Infrastructure-as-code is intentionally not a separate skill. Its model, repository, promotion, validation and drift concerns are the substance of this method; creating a parallel skill would split one control loop across two owners.

## Report evidence

Separate these states and attach the actual revision and target:

- desired-state revision and the resources it claims to own;
- plan or preview, including deletes and replacements, and the policy results;
- applied or synced revision and controller health;
- observed target state, including drift status and pruned resources;
- recovery path actually exercised, or the unexercised gap;
- unresolved ownership, unreachable targets and pending authorizations.

A merged commit, a successful pipeline, a healthy sync status or a clean plan each proves only its own stage. None alone proves that the target serves the intended state or that an application built on it works.

## Composition

Use installed guidance by capability; absence changes depth, not the outcomes above.

| Need | Capability |
| --- | --- |
| Kubernetes manifests, charts, overlays and rendered behavior | `kubernetes-resource-engineering` |
| AWS accounts, IAM, VPC and service choices | `aws-platform` |
| Verification, artifact and promotion stage design | Installed delivery-pipeline stage and gate design guidance |
| Authorized release, rollout verification and recovery | Installed release, rollout-verification and recovery guidance |
| Configuration schema, environment values and secret consumption | Installed configuration and secret-consumption guidance |
| Capacity and cost effect of the delivered platform | Installed capacity and cost analysis guidance |
| Provider syntax, CLI and adapter mechanics | Selected provider's tooling and CLI guidance |
| Backup, restore and data recovery design | Installed continuity and disaster-recovery guidance, and runbook guidance |
| Security review of trust boundaries and credentials | security design and maintenance capabilities |

## Sources

Primary references for the reconciliation model and tool mechanics. Checked 2026-11-16.

- [OpenGitOps principles](https://opengitops.dev/) define declarative, versioned, automatically pulled and continuously reconciled desired state.
- [Argo CD documentation](https://argo-cd.readthedocs.io/en/stable/) and [Flux documentation](https://fluxcd.io/flux/) describe their reconciliation, sync, health and pruning mechanics.
- [Crossplane documentation](https://docs.crossplane.io/latest/) covers providers, managed resources, compositions and control-plane operation.
- Tool mechanics: [Terraform](https://developer.hashicorp.com/terraform/docs), [OpenTofu](https://opentofu.org/docs/), [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), [CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html), [Pulumi](https://www.pulumi.com/docs/), [Ansible](https://docs.ansible.com/ansible/latest/) and [Open Policy Agent](https://www.openpolicyagent.org/docs/latest/).

These references explain mechanisms and principles. They do not define this project's ownership map, target authority or recovery promise; no text is copied.
