# Crossplane as a control plane

Crossplane extends a Kubernetes cluster into a control plane for external infrastructure. It is a strong fit when application teams should consume a curated platform API instead of provider-specific resources, and a poor fit for a single cluster's own manifests or a small estate that already has a working provisioner.

Use this reference when the open question is whether Crossplane belongs in the delivery architecture, how its resources are owned, or how it fails. Official mechanics are in the [Crossplane documentation](https://docs.crossplane.io/latest/); this document keeps the delivery decisions and boundaries.

## The resource model

| Concept | Role | Delivery question |
| --- | --- | --- |
| Provider | Package that reconciles a set of external resources | Which provider version, credential and resource coverage? |
| Managed resource (MR) | Direct representation of one external resource | Is it owned by a composition or by a team directly? |
| Composite resource definition (XRD) | Declares a platform API and its schema | What is the stable contract, and who may change it? |
| Composition | Maps a composite resource to managed resources, patches and readiness | Does one composition change affect many claims at once? |
| Composite resource (XR) | Cluster-scoped instance of the platform API | Who owns it, and what is its deletion policy? |
| Claim | Namespaced request for a composite resource | Is the claim's namespace the tenant boundary? |

```text
claim (namespace)
      |
      v
composite resource  --->  composition
      |                       |
      |                       v
      +---------------> managed resources  --->  provider APIs
                              |
                              v
                     external infrastructure
```

The composition is code that runs inside the control plane. Treat a composition change like a platform release: validate patches, readiness, defaults and deletion behavior against representative claims.

## When Crossplane fits

Choose it when several of these hold:

- application teams should request infrastructure through a small, stable API rather than provider resources;
- the platform already runs Kubernetes and accepts a control plane as a production dependency;
- resources should reconcile continuously inside the cluster, with Kubernetes RBAC and policy as part of the control;
- compositions can encode organisation standards once instead of in every repository;
- the team can operate provider upgrades, CRDs and control-plane availability.

Choose another mechanism when:

- the target is a single cluster's workloads, which GitOps and Kubernetes resources already cover;
- the estate is small and a declarative provisioner with a plan is simpler;
- the organisation cannot accept infrastructure reconciliation depending on cluster availability;
- the provider's Crossplane coverage is thin for the resources in scope;
- the team cannot own CRD upgrades and composition compatibility.

Crossplane and Terraform can coexist: for example, Terraform provisions the account, cluster and Crossplane bootstrap; Crossplane delivers application infrastructure. Ownership must still be one-per-resource.

## Ownership and GitOps

| Pattern | Authority | Requirement |
| --- | --- | --- |
| Git declares XRs/claims | GitOps controller | Sync order: provider and XRD before compositions, compositions before claims |
| Git declares compositions and XRDs | Platform repository | Composition changes reviewed as platform API changes |
| Application repo declares claims | Application team | Claim schema and namespace boundary restrict what can be requested |
| Direct cluster apply | Operator | Break-glass only; drift and audit need a path back to Git |

Managed resources created by a composition are owned by the composite, not by the application repository. Do not also declare the same external resource in Terraform or a cloud console. Importing an existing resource into Crossplane requires an explicit adoption step and verification of the management policy.

Deletion policies matter. A composite deletion can cascade to managed resources and external infrastructure. Protect data-bearing resources with retention or an explicit orphan policy, and verify what a claim deletion actually removes.

## Provider credentials and tenancy

A provider's credential determines the blast radius of every managed resource it reconciles.

- Scope provider credentials to the accounts, regions and resource classes the provider actually needs.
- Separate providers or provider configs per environment and tenant where isolation requires it.
- Avoid a cluster-wide provider with administrator credentials merely for convenience.
- Restrict which namespaces may create claims and which compositions they may select.
- Audit who changed a composition, XRD or provider config, because these change what every claim can create.

Tenant isolation is not provided by namespaces alone. A claim that can select an arbitrary composition or provider config can request resources outside its intended boundary.

## Failure modes

| Condition | Symptom | Response |
| --- | --- | --- |
| Provider credential expired or too narrow | Managed resources stop reconciling; errors in conditions | Restore least-privilege credential; compare actual resources before retrying |
| Provider upgrade changes resource schema | Existing MRs fail to reconcile or convert | Stage upgrade; check CRD conversion and provider release notes |
| Composition change affects many claims | Broad unexpected diff or replacement | Validate against representative claims; roll back the composition, not each claim |
| Circular ownership | Two controllers or a composition and Git fight | Establish one owner; remove the duplicate declaration |
| Deletion cascade | Claim deletion removes data-bearing infrastructure | Set retention/orphan policy before exposure; test in a disposable target |
| Control-plane outage | No reconciliation; external drift accumulates | Declare the availability requirement; restore control plane; compare before resuming |
| Orphaned external resource | Cost and security exposure after CR deletion | Inventory provider-side; delete only with ownership evidence |
| Unbounded claim schema | Teams request resources outside platform intent | Constrain XRD schema, composition selection and namespace RBAC |
| Secret in composition or claim | Credential exposure through Git or API | Use provider identity or secret references; rotate on discovery |

Kubernetes resource semantics, CRD readiness and admission behavior belong to `kubernetes-resource-engineering`. Authentication and authorization design belongs to the identity capability.

## Evidence

| Claim | Evidence |
| --- | --- |
| Platform API is usable | XRD schema and a representative claim reconciled |
| Composition produces intended resources | Managed-resource list, readiness conditions and external state |
| Ownership is single | No duplicate declaration in another tool; management and deletion policies reviewed |
| Tenancy is bounded | Claim namespace, allowed compositions, provider scope and denied cross-tenant request |
| Upgrade is safe | Provider/CRD version, conversion result and representative claim behavior |
| Deletion is safe | Retention policy and a tested delete in a disposable target |
| Recovery works | Control plane and providers rebuilt from bootstrap; existing resources adopted or recreated deliberately |

A reconciled claim proves the control loop ran for that claim. It does not prove the external resource is correctly used by an application, nor that deleting the claim is safe.
