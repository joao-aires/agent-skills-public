---
name: protect-and-restore-data
description: Plan, implement or review database backups, restore verification and
  application disaster recovery. Apply when persistence, deployment topology, migrations
  or recovery requirements change; use the actual database, Kubernetes operator and
  cloud provider guidance.
metadata:
  scope: generic
  invocation: both
  role: task
---

# Protect and restore application data

Read [composition guidance](../../COMPOSITION.md) for optional expertise, fallback and scope.

## Recover the user capability

Identify durable state and dependencies: databases, uploaded objects, persistent volumes, infrastructure/configuration, secrets and encryption keys, external services and DNS. Agree acceptable data loss (RPO) and time to restore service (RTO) from user/business needs; label assumptions when these are unknown. Cover accidental deletion/corruption and infrastructure failure separately. Replication and high availability do not replace backups.

Choose the simplest recovery approach that meets those needs. Define backup scope, frequency, retention, access and encryption; protect recovery copies from the same deletion/credential failure that can affect production. Cross-account or cross-region copies are conditional on the threat, residency constraints and recovery objectives, not default complexity. Ensure recovery credentials and keys remain accessible if the primary environment is unavailable.

## Use the database's recovery mechanism

For PostgreSQL, distinguish logical dumps from physical backups plus continuous WAL archiving/PITR. Verify version/extension compatibility, archive continuity and retention of everything needed to reach the recovery point. A volume snapshot alone is not proof of application-consistent recovery. For managed databases, inspect actual backup configuration, retention, latest restorable time, region/account limitations and restore behavior; do not assume provider defaults meet the objectives.

For Kubernetes, recover declarative application/infrastructure configuration and necessary cluster resources as well as data. Use the database operator's supported backup method; a Kubernetes object backup does not itself back up PostgreSQL contents. Consider Velero for suitable cluster/volume recovery without treating it as a substitute for database-native recovery. Include dependencies outside the cluster.

## Prove restoration safely

Rehearse the path from a known backup or recovery point to a usable application. Identify the exact source and isolated destination, obtain the required keys and configuration, and prevent restored services from acting on the outside world before verification. Restored jobs and credentials may still be able to reach real providers, so isolation must cover behavior as well as database naming.

Verify the recovered state through the application and the intended users' access, not only the database tool's success message. Measure recovery from the point used by the agreed objective, including preparation or dependency work that affects when service can resume. Keep the recovery point, elapsed time and remaining uncertainty in the evidence.

- Avoid overwriting production or letting restored workers send emails, payments or duplicate external side effects.
- Check access, schema, representative data and an application read/write journey; measure elapsed recovery time and actual data loss.
- Recovering a file is not the same as recovering the service.

Record a concise runbook covering rebuild, restore, configuration, verification, cutover and return to normal backups. Include DNS/connection changes, incompatible migrations and the point at which further writes make reversal unsafe. Keep application rollback/roll-forward in CI/CD; data restoration is a separate recovery operation with its own consequences.

Rehearse at a frequency justified by risk and after material schema, storage, key or topology changes. Update the inventory/runbook in the same change and retain the latest restore evidence. Report untested steps clearly; do not claim disaster recovery from backup-job success.

## Check the actual platform

Consult current version-specific guidance before writing commands or provisioning services:

| Target | Starting reference |
| --- | --- |
| PostgreSQL | [Backup methods](https://www.postgresql.org/docs/current/backup.html), [PITR](https://www.postgresql.org/docs/current/continuous-archiving.html) |
| Kubernetes database/operator | [CloudNativePG backups](https://cloudnative-pg.io/documentation/current/backup/), or the chosen operator's documentation |
| Cluster/volume recovery | [Velero](https://velero.io/docs/main/) for the installed release and storage plugins |
| AWS RDS | [Point-in-time restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html); use Aurora-specific guidance when applicable |
| Google Cloud SQL | [Restore overview](https://cloud.google.com/sql/docs/postgres/backup-recovery/restore) and the chosen backup/PITR mode |
| Azure PostgreSQL | [Backup and restore](https://learn.microsoft.com/en-us/azure/postgresql/backup-restore/concepts-backup-restore) |

For another platform, search its first-party documentation and record relevant restrictions. Do not transplant commands or guarantees across providers.

## Operate and recover from partial failure

Audit job failures, newest usable recovery point, coverage, access/key availability, retention behavior and the latest integrity-tested restoration. Carry unresolved findings forward with their original dates. Green backup jobs alone do not meet recovery objectives.

Before rebuilding, inventory surviving resources; an old bootstrap procedure is not authority to delete a surviving datastore. Define ordered infrastructure, identities, storage, data and application recovery with idempotent preconditions.

### When restoring in place

1. Isolate writers, consumers and scheduled jobs and control reconcilers before restoration.
2. Recheck the exact destination and recovery point before restoring.
3. Validate schema, relationships, invariants and representative data before resuming writers or cutover.

Account for queued/in-flight work, duplicate external effects and reconciliation ownership in the recovery plan.

### Report the recovery

Record actual RPO/RTO, residual loss, temporary controls and return to normal backups. Rehearsal, in-place restoration and traffic cutover have different consequences; use the authority already granted for the task and target. With no execution access, deliver a plan and mark live checks outstanding. `incident-response` coordinates an outage; this skill owns restoration and data-integrity proof.

Optional deeper guidance: [application recovery](references/application-recovery.md) and [recovery evidence](references/recovery-record.md). Adapt record fields to existing runbooks instead of creating a parallel register.
