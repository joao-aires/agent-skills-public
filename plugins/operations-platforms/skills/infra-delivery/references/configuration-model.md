# Infrastructure configuration model

Decision tables for the `infra-delivery` method: tool selection, repository structure, state ownership, promotion and validation. Reconciliation controllers are in [GitOps](gitops.md), Kubernetes-native control planes in [Crossplane](crossplane-control-plane.md), and failure response in [drift and recovery](drift-and-recovery.md).

## Desired-state mechanisms

| Mechanism | Model and strengths | Good fit | Watch-outs |
| --- | --- | --- | --- |
| Terraform / OpenTofu | Declarative resources, explicit state, plan and refresh, broad provider ecosystem, modules | Account/network/platform infrastructure; resources with a strong API and infrequent application | State is a critical asset; imports and moves are deliberate; provider upgrades change plans; drift needs refresh or plan |
| CloudFormation | AWS-native stacks, change sets, service integration, rollback on failure | AWS-only estates standardised on stacks; resources without a strong external provider | Slow feedback, stack-level coupling, limited cross-provider reach, vendor lock-in |
| CDK | Imperative language that synthesises CloudFormation or another target | Teams wanting typed constructs and reuse over AWS resources | Generated template is the real artifact; abstraction can hide resource behavior; version upgrades can change synthesis |
| Pulumi | General-purpose languages, state, preview, broad provider set | Teams wanting typed programs and multi-provider delivery | State and program supply chain need the same protection as Terraform; code review can obscure the effective diff |
| Crossplane | Kubernetes control plane, managed resources, compositions and claims | Platform APIs delivered to application teams inside Kubernetes | Control-plane availability and upgrade become platform risk; provider credential scope; composition complexity |
| Configuration management (Ansible and similar) | Ordered tasks over hosts and APIs, inventory-driven | Mutable hosts, appliances, bootstrap and migration steps | Not a resource reconciler by default; idempotence depends on module quality; ordering and partial failure are visible |
| GitOps controllers | Continuous comparison of Git-declared state to cluster state | Kubernetes and platform resources with a repository as authority | Cluster-scoped credentials; prune and self-heal are destructive; controller and repository become delivery dependencies |

Selection criteria, weighted by the actual target:

1. **Coverage.** Can the mechanism represent every resource in scope without shelling out to an unmanaged script?
2. **State.** Is there authoritative state, who protects it, and can it be rebuilt or restored?
3. **Preview.** Does it show a complete effective diff, including deletes and replacements?
4. **Ownership.** Can it import, adopt and refuse to manage a resource cleanly?
5. **Policy.** Can it be checked before application with the organisation's policy engine?
6. **Execution.** Is it run from a pipeline, a controller or a workstation, and with what credential scope?
7. **Drift.** How is out-of-band change detected, and how noisy is the comparison?
8. **Existing estate.** Does the organisation already operate this tool and its failure modes?

A plan-only tool without safe state ownership is less useful than a simpler mechanism with a reliable recovery path. A controller without a bootstrap and disaster-recovery story is a single point of failure for the platform.

## Repository structure

| Pattern | Shape | Use when | Risk |
| --- | --- | --- | --- |
| Modules plus environment roots | Reusable modules; one root per environment/account | General infrastructure with shared components | Environment roots drift in provider versions; enforce one version source |
| Stacks per component | Independently applied stack per service or capability | Blast-radius control and independent delivery | Cross-stack references become implicit contracts |
| Layered platform | Bootstrap, foundation, platform, application layers | Accounts, network, cluster and workloads have different owners | Layer ordering and hand-offs need explicit contracts |
| App-of-apps / GitOps tree | Root application points to child applications or Kustomizations | Many Kubernetes resources and teams | Recursive ownership and prune scope can surprise |
| Crossplane compositions | Platform API, composition, managed resources, claims | Application teams consume a curated platform API | Composition changes can affect many claims at once |
| Monolithic root | One state and one plan for everything | Very small estate with one owner | Slow plans, wide blast radius, serialized changes |

Repository rules that survive all patterns:

- Declare supported provider and module versions; commit locks. Avoid a floating `latest`.
- Keep one value source per environment input. Generated environment files should be reproducible and reviewed.
- Separate bootstrap from steady state. The system that creates the state backend, controller and root credentials cannot depend on them already existing.
- Mark generated files and do not hand-edit them.
- Keep policy close to the resources it governs, with a documented exception path.
- Record ownership in paths and code-owner metadata, not only in a wiki.

## State and ownership

| Concern | Requirement |
| --- | --- |
| Authority | One declared state or controller per resource; no dual writers |
| Isolation | Separate state per environment/account/component where blast radius or access requires it |
| Protection | Encryption at rest, access control, versioning and locking where the backend supports it |
| Location | Remote shared backend; never an engineer's laptop as the only copy |
| Concurrency | Lock or serialize applies; two plans on stale state can produce conflicting changes |
| Imports | Adopt existing resources deliberately; verify the planned diff before the first apply |
| Moves/renames | Use the tool's move mechanism or a planned replace; deleting and recreating is a different change |
| Secrets in state | Assume state contains sensitive values; protect it like a secret store and avoid printing plans wholesale |
| Deletion | Protect data-bearing and shared resources; make prune scope explicit |

State loss is a delivery incident, not a formatting problem. A recoverable backend, documented import path and recent backup matter more than a tidy module tree.

## Promotion

| Model | How a change moves | Use when | Watch-outs |
| --- | --- | --- | --- |
| Environment branches | Merge or cherry-pick between long-lived branches | Regulated promotion needs a visible branch | Divergence and hotfix propagation; merge is not proof of target state |
| Directory per environment | Same modules, different environment values | Most GitOps and IaC repositories | Copy drift; enforce shared modules |
| Versioned module/artifact | Publish a version and reference it from each environment | Platform teams shipping reusable components | Version skew across environments is intentional but must be tracked |
| Progressive rollout | Apply to a canary target or subset first | High-blast-radius platform change | Extra target and observation cost; ordering must be real |
| Manual apply | Authorized operator runs plan/apply | Break-glass or targets without a controller | Human drift, missing evidence and serialized access |

Promotion rules:

- Promote the same declaration or version; environment values may differ, behavior should not.
- Review the effective diff in the destination environment, not the source environment's plan.
- Apply dependencies first and prove readiness rather than waiting a fixed time.
- Serialize changes to shared accounts, clusters, DNS zones, network ranges and databases.
- Keep a compatible previous declaration and know whether reverting it is safe for data and state.
- Record partial completion precisely enough to resume without duplicating a create or deleting a resource that was adopted manually.

## Validation layers

| Check | Question | Failure is |
| --- | --- | --- |
| Format/syntax | Can the tool parse every file? | Immediate; no semantic meaning |
| Schema/type | Are required inputs, types and provider versions valid? | Usually immediate |
| Policy | Does the declaration violate an organisational or security rule? | Blocking unless an owned exception exists |
| Plan/preview | What will be created, changed, replaced or deleted? | Review required; replacements need explicit acceptance |
| Rendered state | Do selectors, references, image identities and placeholders resolve? | Blocking for the affected target |
| Admission/dry run | Will the target accept and mutate it as expected? | Blocking for that cluster |
| Cost/impact | Does the change alter capacity or spend beyond the accepted bound? | Review or block by policy |
| Ephemeral apply | Does the change work end to end in a disposable target? | Strong evidence, not production proof |

A plan that reports no changes can still be wrong if the tool did not refresh, used the wrong workspace or ignored a resource it does not manage. State the scope of the check.

## Secret handling in delivery

| Pattern | Suitable when | Requirement |
| --- | --- | --- |
| Reference to external secret manager | Workload or controller can authenticate to the manager | Per-secret scope; no broad read role; reload path verified |
| Workload identity / federation | Provider supports it | Audience, subject and target restricted |
| Encrypted value in Git | GitOps requires the declaration in the same repository | Decryption key custody, rotation and repository access are equivalent to secret access |
| Generated secret at bootstrap | Initial credential for a controller or database | Store outside the repository; rotate after bootstrap; never print |
| Secret in state or plan | Unavoidable for some providers | Protect and restrict state; redact logs; avoid exporting plans |
| Plaintext in Git | Never | Remove, rotate, purge reachable copies; assume permanent exposure |

Infrastructure delivery owns the reference and the delivery path; the application's configuration contract and secret consumption belong to `application-configuration`.

## Failure modes

| Condition | Symptom | Response |
| --- | --- | --- |
| Wrong workspace or account | Plan looks plausible; apply targets the wrong place | Verify target identity and provider account before apply |
| Stale state or lock | Apply blocked or changes conflict | Resolve lock owner; refresh; never force-unlock blindly |
| Unmanaged resource collides | Create fails because the resource exists | Import/adopt deliberately or rename; do not delete unknown state |
| Replacement of stateful resource | Data loss or downtime | Treat replacement as a migration; backup and plan data movement |
| Provider upgrade changes plan | Unexpected diff after a version bump | Pin, review changelog, test in a disposable target |
| Policy bypass | Resource applied manually outside the path | Detect drift, reconcile, investigate credential scope |
| Partial apply | Some resources changed, others not | Inspect actual state; resume or roll forward; do not assume rollback |
| Secret leaked in plan/state | Credential exposure | Revoke/rotate; restrict state; clean logs; treat as incident |
| Orphaned resources | Billing and security exposure after prune | Inventory provider-side; delete only with ownership evidence |

## Evidence

| Claim | Evidence |
| --- | --- |
| Declaration is valid | Parse, schema and policy results over the exact revision |
| Change is understood | Complete plan/diff including deletes, replacements and state moves |
| Target accepted it | Applied or synced revision, controller status and provider resource state |
| Drift is known | Refreshed plan or controller comparison with timestamp and scope |
| Promotion succeeded | Same version in destination, environment values as intended, dependent behavior verified |
| Recovery works | Restore, rollback or re-import exercised in a safe target |
| Secret path is safe | Reference resolved by the intended identity; no value in repository, plan or logs |

Separate declared, planned, applied and observed states. A clean plan and a merged commit are not observations of the target.
