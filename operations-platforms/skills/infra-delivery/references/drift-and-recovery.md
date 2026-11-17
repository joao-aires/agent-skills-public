# Drift and recovery

Infrastructure delivery assumes the target will diverge. A console change, a failed partial apply, an out-of-band controller, an expiring credential or a deleted resource all produce the same question: what is actually there, who owns it, and what is safe to do next?

Use this reference with the `infra-delivery` method when the open question is detecting drift, deciding whether to reconcile, pruning safely or recovering the delivery system. Tool mechanics and sync policy are in [GitOps](gitops.md) and [configuration model](configuration-model.md).

## Classify the drift

| Source | Example | Typical response |
| --- | --- | --- |
| Manual console or CLI change | Security group rule added, replica count raised | Reconcile after confirming intent; fix access path |
| Out-of-band controller | Autoscaler, operator, policy agent changes a field | Declare the field as unmanaged or model the controller in the desired state |
| Partial apply or failed sync | Some resources updated, others not | Inspect actual state; resume or roll forward; do not assume rollback |
| Deleted or replaced resource | Provider deleted an instance; cluster lost a node group | Recreate through the declaration; verify dependent state |
| Provider-defaulted field | API returns a default not in the declaration | Normalize the comparison; do not fight the provider forever |
| Credential or permission drift | Role lost a permission; secret expired | Restore identity; verify access rather than only the policy document |
| Version skew | Controller or provider upgraded outside the path | Pin, stage, and reconcile the version as a deliberate change |
| Ownership conflict | Two tools declare the same resource | Choose one owner; remove the other declaration before applying |
| Data-bearing change | Volume, database, bucket policy changed externally | Treat as an incident or migration, not routine drift |

Not every difference is a defect. The useful output is a classified, owned difference, not a zero-diff dashboard that hides exceptions.

## Detect

| Method | Finds | Limits |
| --- | --- | --- |
| Plan with refresh | Declared-versus-observed differences for managed resources | Depends on state correctness and provider refresh; can be slow or costly |
| Controller comparison | Continuous diff for resources the controller owns | Only its scope; may not surface unmanaged resources |
| Provider inventory/export | Actual resources and configuration | Does not know intended ownership; noisy in large accounts |
| Policy/configuration scan | Non-compliant live settings | Point-in-time; may not explain how the state arose |
| Audit log review | Who changed what and when | Retention and coverage vary; not a substitute for state comparison |
| Application behavior | Whether the delivered platform still serves | Indirect; can reveal drift with no configuration diff |

Run detection on a schedule and before a consequential change. Record timestamp, target, revision and scope. A stale detection result is a hypothesis, not current state.

## Decide the response

| Situation | Reconcile automatically? | Additional action |
| --- | --- | --- |
| Unauthorized change to a stable, non-data resource | Yes, if ownership and rollback are clear | Investigate how the change bypassed the path |
| Manual fix during an active incident | No, until the incident owner releases the target | Preserve evidence; reconcile deliberately afterward |
| Field owned by an autoscaler/operator | No | Model as unmanaged or declare through the owning controller |
| Provider default or representational difference | No | Fix comparison or schema |
| Data-bearing resource changed | No blind repair | Assess data impact; use backup/recovery or a migration |
| Shared resource owned by another team | No | Coordinate with the owner; avoid a write conflict |
| Persistent unauthorized drift | No | Treat as a control failure; review credentials and access |
| Emergency break-glass change | Pause automation | Record, verify, then codify or revert |

Self-healing is appropriate when the declaration is authoritative and the live change should not exist. It is dangerous when an operator is mid-recovery, when the resource holds data, or when two owners disagree. Provide a scoped pause with an owner and an expiry rather than disabling reconciliation globally.

## Prune and delete safely

| Resource class | Default | Protection |
| --- | --- | --- |
| Stateless application resources | Prune when no longer declared | Ownership and namespace scope verified |
| Data volumes and databases | Retain or explicit delete | Deletion protection, finalizer, backup, tested restore |
| Shared network, DNS, identity, keys | Do not prune automatically | Separate ownership and review; dependency inventory |
| External resources with manual consumers | Retain | Documented consumer list and deprecation step |
| Cluster-scoped or CRD resources | Explicit order | CRD deletion can remove every custom resource; verify conversion first |
| Controller and bootstrap resources | Never pruned by the workload tree | Separate root and recovery path |

Before enabling prune:

1. Confirm the controller's ownership set and scope.
2. Protect data-bearing and shared resources.
3. Run a dry-run or diff-only prune where supported.
4. Confirm what happens to finalizers, retained volumes and external resources.
5. Test a deletion in a disposable target.

A prune that removes a resource is not wrong merely because it was unexpected; the failure is usually ownership scope or a declaration that omitted a required resource.

## Recover the delivery system

| Scenario | Recovery path | Evidence to retain |
| --- | --- | --- |
| Bad declaration applied | Revert the commit or fix forward; resync; verify target | Revisions, diff, observed state before and after |
| State lost or corrupted | Restore backup; re-import resources; verify ownership and drift | Backup identity, restore point, import list |
| Controller unavailable | Restore controller; compare before syncing; pause automation if needed | Last successful sync, outage window, target drift |
| Cluster lost | Rebuild from bootstrap; restore data separately; adopt external resources | Bootstrap revision, rebuilt health, data recovery result |
| Repository unavailable or compromised | Restore from mirror/backup; rotate credentials; audit changes | Repository revision, access audit, credential rotation |
| Provider credential compromised | Revoke/rotate; review resources created or changed; reconcile | Credential version, audit window, resource inventory delta |
| Composition or platform API regression | Roll back the platform release; verify representative claims | Composition version, claim matrix result |
| Deleted data-bearing resource | Restore from backup; verify application consistency | Backup/restore result, data-loss window |

Recovery of the controller is not recovery of the data. Keep those claims separate. A rebuilt cluster with an empty database is a different outcome from a restored one.

## Failure modes in recovery

| Mistake | Consequence | Prevention |
| --- | --- | --- |
| Resuming sync before comparing | Reapplies stale desired state over a manual recovery | Compare and classify first |
| Restoring state without verifying target | Plans against resources that no longer exist | Refresh and inventory before apply |
| Re-importing with the wrong identity | Resource adopted into the wrong account or cluster | Verify target identity and provider credentials |
| Pruning during recovery | Deletes the only working copy of a resource | Pause prune/self-heal with an owner |
| Assuming rollback reverses data | Data loss or divergence | Separate schema/data recovery; prefer compatible forward fix |
| Rotating a key needed for backups | Archived data unreadable | Retain decrypt keys for the retention period |
| Declaring recovery complete after sync | Broken dependent behavior remains | Verify served outcome and data consistency |

## Evidence

| Claim | Evidence |
| --- | --- |
| Drift is understood | Timestamped comparison, classified difference, owner |
| Reconciliation is safe | Ownership scope, protected resources, rollback path |
| Prune is safe | Dry run, protection list, disposable-target deletion test |
| Recovery is usable | Exercised restore/rebuild with observed target and data result |
| Recovery is complete | Served outcome and dependent state, not only controller health |
| Control failure is investigated | Access path, audit evidence and corrected credential or policy |

Report detected, classified, reconciled and verified states separately. A green controller or a zero-diff plan is evidence about reconciliation, not about application behavior or data integrity.
