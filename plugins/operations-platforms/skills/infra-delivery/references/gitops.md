# GitOps reconciliation

GitOps is a control-loop model, not a product category. Desired state is declared, versioned, pulled automatically by a controller and continuously reconciled with the target. Argo CD and Flux are common implementations; either is optional, and a push-based apply can still satisfy the same ownership and evidence rules.

Use this reference when the open question is sync behavior, prune and self-heal, controller boundaries, multi-cluster layout, secret handling in Git or recovery of the reconciliation path. Tool syntax belongs to the selected tool's documentation and `tooling-conventions`.

Official references: [OpenGitOps principles](https://opengitops.dev/), [Argo CD documentation](https://argo-cd.readthedocs.io/en/stable/) and [Flux documentation](https://fluxcd.io/flux/concepts/). This document keeps the delivery decisions; it does not reproduce either controller's tutorial.

## The model

```text
reviewed commit  --->  desired state in Git
        |                       |
        |                       v
        |               reconciler compares
        |                       |
        |             +---------+---------+
        |             |                   |
        |         in sync              drift
        |             |                   |
        |         report health      apply / alert
        |                                 |
        +------------ observed target <---+
```

Properties worth preserving even when the implementation changes:

- The declaration is reviewable and has an immutable revision identity.
- The controller pulls; a human or CI push is not the steady-state mechanism.
- Comparison is continuous or scheduled, not a one-time deployment.
- Health is reported separately from sync status.
- The controller's credential scope matches the resources it owns.
- Bootstrap is reproducible without relying on the controller already running.

A Git commit is the declared revision. It is not the applied revision, and it is certainly not evidence that the workload serves traffic correctly.

## Argo CD and Flux comparison

Verify current behavior against the official documentation before relying on a feature.

| Concern | Argo CD | Flux |
| --- | --- | --- |
| Primary resources | `Application`, `ApplicationSet`, `AppProject` | `GitRepository`, `Kustomization`, `HelmRelease`, `HelmRepository`, `OCIRepository` |
| Sync control | Automated or manual sync, sync waves, hooks, retry | Reconciliation intervals, `dependsOn`, health checks, retry |
| Health | Built-in resource health plus custom health checks | Kustomization/HelmRelease readiness and status conditions |
| Multi-cluster | Cluster registration; one control plane can target many clusters | Cluster composition through Kustomization targeting and bootstrap patterns |
| Multi-tenancy | Projects, RBAC, repository and destination restrictions | Namespace-scoped controllers, service accounts and impersonation |
| UI | Rich web UI and CLI | CLI and ecosystem tooling; UI varies |
| Image automation | Argo CD Image Updater is a separate component | Image automation controllers are part of the project |
| Secret decryption | Plugins or external secret integration | SOPS/age and external secret integration are common |

Neither list is a complete feature inventory. Choose by tenancy model, existing platform, credential topology and the team's operating ability to run the controller.

## Sync policy decisions

| Decision | Safe default | When to relax |
| --- | --- | --- |
| Automated sync | Manual for high-blast-radius platform resources; automated for application state | Stable resources with tested rollback and observable health |
| Prune | Off or dry-run until ownership and deletion protection are proven | Explicit ownership, protected data resources and tested prune |
| Self-heal | Off for resources that operators may change during recovery; on for stable declarations | Drift should never be manual, and a pause path exists |
| Retry | Bounded with backoff | Longer retry only when a dependency is known to converge slowly |
| Replace | Force only for an understood immutable conflict | Never as a routine workaround |
| Server-side apply | Use when field ownership and conflict behavior are understood | Mixed controllers or CRDs with conflicting defaults need care |
| Sync waves / dependsOn | Reflect real dependency readiness | Sleep-based ordering is not readiness |

Self-healing and pruning are the two settings most likely to turn a small mistake into an outage. They also remove the most drift. Decide them per resource class, not once for the whole platform.

## Repository and tenancy layout

| Layout | Shape | Fit | Risk |
| --- | --- | --- | --- |
| One repository, directory per environment | Shared base and environment overlays | Small platform, one team | Broad access; one commit can affect all environments |
| One repository, app-of-apps | Root points to child applications | Many applications, central platform team | Recursive prune and ownership ambiguity |
| Repository per team | Team owns its manifests; platform registers sources | Strong team boundary | Many credentials and source registrations; consistency burden |
| Repository per environment | Promotion by repository or branch | Strong environment isolation | Divergence and cherry-pick errors |
| Generated from a platform API | Crossplane or a template produces declarations | Standardised services at scale | Generator becomes the real authority; Git may lag intent |

Rules:

- Restrict which repositories and paths a tenant's controller may read.
- Restrict destinations by cluster, namespace and resource kind.
- Keep production credentials out of tenant-visible configuration.
- Make ownership visible in the path and in the controller resource, not only in a README.
- Avoid recursive application trees whose prune scope is wider than the owning team understands.

## Secrets in GitOps

GitOps wants the full declaration in Git; secrets do not belong there in plaintext. Common patterns:

| Pattern | Declared in Git | Authority | Check |
| --- | --- | --- | --- |
| External secret reference | A reference object, not the value | External secret manager | Controller identity can read only the intended secret; sync creates/updates the target |
| Encrypted secret | Ciphertext plus metadata | Decryption key held separately | Key custody, rotation and repo access reviewed; history contains only ciphertext |
| Sealed or cluster-bound secret | Ciphertext bound to a cluster/namespace | Controller private key | Key backup and cluster recovery; cross-cluster reuse fails by design |
| Generated at bootstrap | A bootstrap job or operator | Platform secret store | Not committed; rotated after bootstrap; not printed in logs |
| Plaintext value | The value | None | Reject; rotate on discovery and purge reachable history |

A decrypting controller has broad power over every secret it can decrypt. Scope its identity and namespace access accordingly.

## Bootstrap and recovery

The controller cannot create its own initial trust. Keep a bootstrap path for:

- the Git repository and credentials or identity federation;
- the controller installation and its namespace/RBAC;
- the root application or Kustomization;
- the secret decryption identity, if any;
- the state and configuration the controller needs that is not represented in Git.

If the cluster is lost, the bootstrap plus Git should reconstruct the declared state. Data-bearing resources, external DNS, certificates and cloud resources may need separate recovery. Test the reconstructed path in a disposable cluster rather than assuming it.

## Failure modes

| Condition | Symptom | Response |
| --- | --- | --- |
| Repository or controller credential expired | Sync stops; health may remain "unknown" | Restore identity; check last successful revision; do not assume target state |
| Controller cannot reach cluster | Declared state unchanged, target drifts | Restore connectivity; compare before syncing; pause automation if manual recovery is active |
| Bad commit auto-syncs | Faulty state applied quickly to many targets | Revert or fix forward; verify target, not only sync status; bound blast radius next time |
| Prune removes a needed resource | Data or dependency loss | Restore from backup or re-declare; add deletion protection and narrower prune scope |
| Self-heal fights an operator | Manual fix repeatedly reverted during an incident | Pause reconciliation with an explicit owner; reconcile after recovery |
| Health reported green, workload broken | Sync and health do not cover the customer journey | Verify served revision and dependent behavior separately |
| Two controllers own one resource | Alternating diffs and unstable state | Establish single ownership; remove one source |
| CRD or controller upgrade changes behavior | Resources apply but fail admission or reconcile | Stage the upgrade; check CRD conversion and webhook readiness |
| Secret decryptor unavailable | Resources fail to render or sync | Restore key access; avoid a plaintext fallback |

## Evidence

| Claim | Evidence |
| --- | --- |
| Repository is the declared source | Revision, path, controller resource and sync policy |
| Target matches declaration | Synced revision, health status and a refreshed comparison |
| Drift is detected | Timestamped comparison with the resource scope |
| Prune is safe | Ownership list, protected resources, dry-run result |
| Recovery works | Rebuilt controller or cluster from bootstrap in a safe environment |
| Secret path works | Reference resolved by the intended identity; no plaintext in Git or logs |

Report sync status and served behavior separately. A green sync is a claim about reconciliation, not about the application.
