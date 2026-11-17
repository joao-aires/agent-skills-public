# Upgrade managed PostgreSQL

Use this reference when PostgreSQL runs on a managed service and the provider owns the server, filesystem and upgrade tooling. [Major upgrades](major-upgrades.md) still owns the compatibility inventory and rehearsal judgment; this page covers what changes when you have a control plane instead of a shell.

## Know what the provider controls

On RDS, Aurora, Cloud SQL and Azure Database for PostgreSQL you normally cannot run `pg_upgrade`, install extension binaries, edit `postgresql.conf`, or choose arbitrary source and target versions. The provider runs the upgrade, exposes a precheck or validation step, takes a backup or snapshot, and offers a supported version pair. Some services add a blue/green or clone-based path.

That shifts the work rather than removing it. You still own schema and application compatibility, extension selection within the allowlist, data volume and object count, connection clients, cutover, and acceptance. A provider precheck passing means the control plane found no blocking condition it knows about; it is not a rehearsal of your queries, collation order or load behavior.

| Service | Upgrade shape | Consequences to plan |
| --- | --- | --- |
| [RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.html) | Provider runs `pg_upgrade`; pre- and post-upgrade snapshots when backup retention is on; blue/green deployment available | In-Region read replicas upgrade with the primary; Multi-AZ DB cluster replicas may need recreation; restore the pre-upgrade snapshot to return to the old version |
| [Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.PostgreSQL.html) | Cluster-level major upgrade; blue/green as an alternative; global databases have a separate path | The cluster, readers and endpoints move together; zero-downtime patching applies to minor versions, not major upgrades; verify the cluster's supported target |
| [Cloud SQL for PostgreSQL](https://cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace) | In-place upgrade using `pg_upgrade`, retaining instance name and address; precheck and clone-based dry run | External replicas cannot be upgraded in place; logical replication slots are dropped; database collation and object/large-object limits can block or time out |
| [Azure Database for PostgreSQL flexible server](https://learn.microsoft.com/en-us/azure/postgresql/configure-maintain/concepts-major-version-upgrade) | In-place upgrade using `pg_upgrade`; upgrade validation checks; implicit pre-upgrade backup | HA is disabled during the upgrade and re-enabled after; geo-replicas must be removed first; some extensions block the path; reverting means point-in-time restore to a new server |

Provider workflows and supported versions change frequently. Read the linked page for the actual service, region and version pair at implementation time; do not generalize one provider's procedure to another.

## Confirm the supported path

- Check the exact source and target versions the service offers in the region. A target supported by the community may not be offered by the provider yet, and a deprecated provider version may not be an allowed source.
- Read the provider's known limitations for the path: minimum storage headroom, maximum objects or large objects, timeout, unsupported flags or parameters, required collation, and extensions that block the upgrade.
- Ask whether the provider's precheck runs against the primary, whether it needs all databases reachable, and whether it works on a replica. A precheck that cannot see an inaccessible database is not comprehensive.
- Confirm the maintenance window, expected duration and whether the provider can defer or reschedule. The window is a control-plane slot, not proof that your application has low traffic then.
- Identify every dependent service that also upgrades: read replicas, cross-region replicas, logical subscribers, external replicas, poolers, CDC connectors, monitoring and backup integrations.

## Rehearse with clones and snapshots

Use the provider's clone or restore-to-new-instance capability to build a production-like target:

- Restore or clone at a known point, then run the upgrade path there. A clone that lags production or omits extensions does not test the same compatibility surface.
- Verify extension availability and versions in the clone, then run the application regression suite, critical query plans and write paths.
- Exercise the client cutover: connection strings, pooler, TLS, DNS and credentials against the clone where the provider permits it.
- Measure the clone's upgrade duration and the restore time to a new instance. Use both to set the maintenance window and the achievable recovery point.
- Clean up cloned instances only within the authorized scope; they contain production data and incur cost.

Some providers also offer a managed migration service or logical-replication path for lower downtime. Evaluate it against the same constraints as a self-managed logical upgrade: DDL is not replicated, sequences and large objects need handling, and the reverse path is not automatic.

## Handle extensions within the allowlist

The provider decides which extensions and versions exist for each engine version. An extension present in the old cluster may be unavailable, blocked or require an intermediate version in the target.

- List installed extensions, versions and schemas; compare with the provider's extension documentation for the target version.
- Some extensions must be dropped and recreated; some are updated automatically; some block the upgrade entirely. Follow the provider's current list rather than assuming community behavior.
- Shared-preload extensions need the provider's parameter or flag mechanism; you cannot add them to `shared_preload_libraries` directly.
- Extensions with large object or spatial dependencies, such as PostGIS and TimescaleDB, often have path-specific rules. Verify the supported source/target matrix.
- Recheck availability after the upgrade and update extensions through the provider-supported mechanism. An extension that silently remains at the old version can leave objects unusable.

## Plan replicas and downstream consumers

Replica behavior is provider-specific and easy to misread:

- In-Region read replicas may be upgraded automatically with the primary, may need to be included explicitly, or may need recreation. Confirm before the window and include rebuild time in the outage estimate.
- External, cross-region and geo-replicas may be unsupported for in-place upgrades. Remove or recreate them under the provider's procedure.
- Logical replication slots may be dropped by the upgrade, even on PostgreSQL 17 and later where self-managed `pg_upgrade` can migrate them. Record slot names, plugins, confirmed positions and downstream consumers, then recreate and resync.
- CDC connectors and subscribers need a defined resume point. Restarting them without checking the confirmed flush position can duplicate or lose changes.

## Cut over connections and verify

The instance name may survive while the address, certificate, parameter set or username format changes. Treat connection behavior as part of the upgrade.

- Update application configuration, poolers, background jobs, analytics, monitoring and backup tooling in one change. A single stale client can write to the old target or fail silently.
- Expect a connection storm after restart; verify pool limits and retry behavior against the new server.
- Check authentication: SCRAM settings, password encryption, role changes and provider-specific username formats. Azure automigrated servers, for example, change the username format after a major upgrade.
- For blue/green or clone-based switchover, verify DNS or endpoint movement, then confirm reads and writes through the actual application path.
- Run row-count and invariant checks, smoke journeys, plan comparisons for critical queries, and `ANALYZE` where the provider does not carry statistics. Watch locks, replication lag and error rates through a representative workload cycle.

## Rollback means restore

There is no in-place downgrade on any of these services. The provider's rollback is a restore of the pre-upgrade snapshot or backup to a new instance, followed by repointing clients. That loses writes made after the snapshot; blue/green switchback may also lose writes made after the switch.

- Record the snapshot identity and the recovery point before the upgrade starts, and verify that the restore path is available in the account and region.
- Measure restore-and-repoint time in the rehearsal. A restore that takes longer than the outage budget changes the decision, not just the runbook.
- Do not promise binary rollback, and do not assume a provider's automatic backup is retained for the period you need. Check retention and copy critical backups where the service supports it.
- Decide in advance whether failed validation means restore, forward repair or a second attempt, and who authorizes it.

| Evidence | Claim supported |
| --- | --- |
| Provider-documented target and limitations | The path is supported for this service and region |
| Precheck or validation result | The control plane found no blocking condition it checks |
| Upgrade and regression run on a clone | The schema and application work on the target |
| Measured upgrade and restore time | The window and recovery point are credible |
| Replica, slot and connector re-verification | Downstream data flow resumed from a known position |
| Post-cutover application and invariant checks | The service serves the workload, for the observed period |

Sources: [RDS for PostgreSQL upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.html), [Aurora PostgreSQL upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.PostgreSQL.html), [Cloud SQL in-place major upgrades](https://cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace), [Azure flexible server major version upgrades](https://learn.microsoft.com/en-us/azure/postgresql/configure-maintain/concepts-major-version-upgrade) and [Azure upgrade validation checks](https://learn.microsoft.com/en-us/azure/postgresql/configure-maintain/how-to-run-upgrade-validation-checks). Checked 2026-11-16 at the documentation level only; no provider upgrade was executed.
