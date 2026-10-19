# Recovery record

## Backup review

| Datastore / environment | Mechanism / owner | Last successful point | Retention evidence | Key/tool access | Last verified restore | Objective gap |
| --- | --- | --- | --- | --- | --- | --- |
| Fill from evidence | | | | | | |

## Restore record

```text
Recovery objective: RTO / RPO / source of policy
Scope and dependency order:
Recovery point and integrity evidence:
Destination and surviving resources:
Expected data-loss window:
Writer/job/consumer isolation and controller handling:
Ordered steps, preconditions, and checks:
Abort / rollback / cutover conditions:
UTC start, recovery-point time, cutover, verified recovery:
Data invariants and journey verification:
Actual RTO / RPO result:
Reconciliation resumed / temporary artifacts removed:
Residual gaps and accountable owners:
```

Infrastructure success and data success are separate checkpoints. A recreated cluster with empty storage has not recovered the service.

## Acceptance scenarios

1. **Monthly backup review finds fresh objects but no restore exercise.** Expect freshness/retention coverage and a recoverability gap; recommend an isolated verified restore rather than declaring backups healthy solely from object dates.
2. **Recover a service where the database survived but the cluster did not.** Expect surviving-resource inventory, current dependency order, isolation of competing writers/controllers, integrity and journey checks; no deletion of the surviving database by assumption.

## Preparation reference

Read [application-recovery.md](application-recovery.md) for backup design, consistency, protected copies and rehearsal. These records capture actual evidence; they do not prescribe a particular cloud or datastore.
