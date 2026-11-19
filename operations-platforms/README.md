# Operations platforms plugin: workload, cluster, cloud and delivery implementation

The `operations-platforms` plugin carries selected platform expertise: JVM and resource efficiency, Kubernetes resource engineering and live diagnosis, infrastructure delivery as reconciled desired state, AWS workload design, and one acquired AKS cost workflow.

It does not own the generic operations activities, service catalogue detail or the release decision. Each method is stack-specific and applies only to a platform the project has already selected.

## Purpose

Use this package when a decision depends on how a specific platform behaves: how a workload uses its JVM and cgroup budget, whether rendered Kubernetes resources express the intended lifecycle, why a running cluster object is failing, how desired state is promoted and reconciled, or how an AWS workload is bounded. Generic operations, capacity, security and release reasoning stay with their own capabilities.

## Conceptual model

| Question | Owner |
| --- | --- |
| Does this workload use its runtime, memory and scheduling budget efficiently? | [infra-jvm-optimization](skills/infra-jvm-optimization/SKILL.md) |
| Do the rendered Kubernetes resources express the intended lifecycle and boundaries? | [kubernetes-resource-engineering](skills/kubernetes-resource-engineering/SKILL.md) |
| Why is this running workload or cluster object failing now? | [kubernetes-troubleshooting](skills/kubernetes-troubleshooting/SKILL.md) |
| How does desired state move through environments and reconcile without drift? | [infra-delivery](skills/infra-delivery/SKILL.md) |
| How is this workload bounded on AWS accounts, network, identity, data and cost? | [aws-platform](skills/aws-platform/SKILL.md) |
| Which AKS cost levers apply, and what must be verified first? | `aks-cost-optimization` (acquired) |

Design, diagnosis, delivery and cost are distinct modes. A rendered manifest is not live state; a synced revision is not a served outcome; a cost recommendation is not an applied change.

## Responsibilities

| Skill | Type | Owns | Stops at | Not for |
| --- | --- | --- | --- | --- |
| [infra-jvm-optimization](skills/infra-jvm-optimization/SKILL.md) | activity | Runtime and infrastructure budget, bottleneck experiment, heap and pool strategy, startup and shutdown, scheduling and autoscaling alignment | A measured improvement or an explicitly unverified configuration proposal | Non-JVM runtimes, cluster provisioning or capacity purchase |
| [kubernetes-resource-engineering](skills/kubernetes-resource-engineering/SKILL.md) | activity | Workload resources, Helm and Kustomize structure, security defaults, probes, storage, networking, ownership and rendered validation | Rendered variants with checks and named exemptions | Cluster provisioning, upgrades or live incident diagnosis |
| [kubernetes-troubleshooting](skills/kubernetes-troubleshooting/SKILL.md) | method | Evidence gathering from observed state, discrimination among failure modes, next action and handover | A supported diagnosis within granted access | Manifest redesign, application repair outside scope or provisioning |
| [infra-delivery](skills/infra-delivery/SKILL.md) | method | Infrastructure-as-code choice, repository and promotion structure, policy and rendered-state validation, reconciliation, drift, pruning and recovery | A delivered desired-state revision with observed state and recovery evidence | Application configuration semantics, pipeline stages or release authorization |
| [aws-platform](skills/aws-platform/SKILL.md) | method | AWS identity and account boundaries, network, compute and data selection, messaging, observability, cost, continuity and edge security decisions | A workload design or review with dated service evidence | Reproducing the service catalogue, current prices or universal defaults |
| [aks-cost-optimization](skills/aks-cost-optimization/SKILL.md) | method (upstream) | Rightsizing, VPA, autoscaler tuning, spot pools, namespace cost visibility and anomaly detection on AKS | A cost hypothesis and verification plan | GPU cost, failing autoscaler incidents, cluster-creation SKU choice or automatic rightsizing |

## How it materialized

| Model element | Implementation |
| --- | --- |
| JVM and resource optimization workflow | [optimization guide](skills/infra-jvm-optimization/references/optimization-guide.md) |
| Kubernetes resource contract and render checks | [resource guide](skills/kubernetes-resource-engineering/references/resource-guide.md) |
| Troubleshooting evidence order | [diagnostic workflow](skills/kubernetes-troubleshooting/references/diagnostic-workflow.md), [failure modes](skills/kubernetes-troubleshooting/references/failure-modes.md) |
| Desired-state delivery and recovery | [GitOps](skills/infra-delivery/references/gitops.md), [drift and recovery](skills/infra-delivery/references/drift-and-recovery.md) |
| AWS identity, network, compute and operations | [identity and network](skills/aws-platform/references/identity-and-network.md), [compute and data](skills/aws-platform/references/compute-and-data.md), [operations and cost](skills/aws-platform/references/operations-and-cost.md) |
| Acquired AKS guidance | `skills/aks-cost-optimization/` with six `azure-aks-*.md` step guides and `UPSTREAM-LICENSE.txt` |

### Acquired sources

| Skill | Source | Pin | Licence |
| --- | --- | --- | --- |
| `aks-cost-optimization` | [Azure/AKS-Skills](https://github.com/Azure/AKS-Skills) | `20bf352` | MIT |

## Reading paths

1. **New Kubernetes workload** → [kubernetes-resource-engineering](skills/kubernetes-resource-engineering/SKILL.md) → [infra-delivery](skills/infra-delivery/SKILL.md) for promotion and reconciliation → [infra-jvm-optimization](skills/infra-jvm-optimization/SKILL.md) when the runtime budget matters.
2. **Running workload failing** → [kubernetes-troubleshooting](skills/kubernetes-troubleshooting/SKILL.md) from observed state → [kubernetes-resource-engineering](skills/kubernetes-resource-engineering/SKILL.md) only if the repair changes the resource contract.
3. **New AWS service or account** → [aws-platform](skills/aws-platform/SKILL.md) identity and network first → compute and data → [infra-delivery](skills/infra-delivery/SKILL.md) for the delivery loop.
4. **Cost or density review** → [infra-jvm-optimization](skills/infra-jvm-optimization/SKILL.md) for measured runtime cost, or [aks-cost-optimization](skills/aks-cost-optimization/SKILL.md) for AKS-specific levers → the generic capacity and cost activity for the tradeoff.

## Boundaries

- **Generic operations.** Release authorization, incident command, postmortems, operations reviews, capacity tradeoffs, observability design and security maintenance belong to `sdlc` security methods (`design-security`, `run-security-maintenance`). These methods provide platform evidence to those owners.
- **Service catalogue.** `aws-platform` names the services a workload decision touches; it does not reproduce AWS documentation, current quotas, regional availability or prices. Verify those at use time.
- **Local decision authority.** The acquired AKS skill is Microsoft-authored guidance at a pinned commit. It does not replace the local method, the current AKS documentation or the actual cluster and subscription. The six `azure-aks-*.md` step guides are packaged beside `SKILL.md`. The sibling AKS skills the router defers to (`aks-gpu-inference`, `aks-troubleshooting`, `aks-cluster-setup`) are not packaged; use only steps supported by the packaged guides and current Azure documentation.
- **Application behavior.** Application configuration, service behavior and data contracts belong to their own methods. Infrastructure delivery does not absorb them.
- **Evidence.** A clean plan, merged commit, healthy sync, running task or cost dashboard is not proof that the target serves the intended outcome.

## Authority and optional tools

The package declares no MCP servers. It does not install `kubectl`, Helm, Kustomize, a cloud CLI or an IaC tool. Reading a cluster, applying a manifest, reconciling a control plane, changing an AWS resource or implementing an AKS cost change requires scope from the request, the named target and the relevant account. `aws-platform` may use a read-only AWS MCP server when the client provides one; a client connection is not a package declaration.

## Maintenance

Owning sources are `skills/*/SKILL.md` and their references, plus the acquired AKS folder. Update this README when platform ownership, the generic-operations boundary or an acquisition changes. Validate with `scripts/validate_plugins.py`, `scripts/check_collection.py` and the repository tests; recheck cloud and Kubernetes claims against current first-party documentation.
