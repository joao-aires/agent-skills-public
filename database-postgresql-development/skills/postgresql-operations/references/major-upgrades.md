# Plan a PostgreSQL major upgrade

Use this reference when moving a cluster to a new PostgreSQL major version on infrastructure you control. It owns the compatibility, rehearsal and cutover decisions; [managed upgrades](managed-upgrades.md) covers providers that hide the server. A major upgrade changes catalogs, server behavior and extension binaries, so treat it as a compatibility project with a downtime budget, not as a package update.

## Separate major from minor

A minor release within the same major version ships compatible fixes and normally needs only new binaries and a restart, without a data migration. A major release can change system catalogs, configuration defaults, query planning, removed features, collation behavior and extension ABIs. Application SQL that still parses may return different plans or ordering.

- Do not fold a major upgrade into a routine patch window. It needs its own rehearsal, decision point and rollback plan.
- Do not assume a driver, ORM, pooler, backup agent or monitoring extension supports the new major on day one. Check each one against the target version.
- Read the target version's [release notes](https://www.postgresql.org/docs/release/) and the [upgrading overview](https://www.postgresql.org/docs/current/upgrading.html) for removed and changed behavior. Select the documentation for the deployed and target versions, not only "current".

## Choose the path

| Path | Downtime | Strengths | Costs and limits |
| --- | --- | --- | --- |
| `pg_upgrade` in place | One restart plus validation | Preserves the cluster, roles and most objects; fast for large data | Requires both binary sets and shared access; extension objects must match; `--link` removes rollback safety |
| Dump and restore | Longest | Portable across hosts, architectures and locale/encoding changes; selective | Full reload, index rebuild, sequence and ownership checks, large storage and time |
| Logical replication | Seconds to minutes at cutover | Old cluster keeps serving during initial sync; near-zero downtime | DDL is not replicated; sequences, large objects, replica identity and conflicts need explicit handling; reverse cutover is easy to get wrong |

Choose from the actual constraints: tolerable downtime, data volume, ability to run old and new binaries together, whether the host or locale must change, and whether a tested rollback is required. A small database with a short outage budget does not need logical replication; a large cluster with a strict outage budget usually does.

## Inventory before deciding

| Item | Why it can block or surprise |
| --- | --- |
| Source and target version pair | Supported direct paths differ; intermediate versions may be required |
| Extensions and versions | Shared objects must exist for the new server; some extensions block an upgrade or need a staged update |
| Extension objects outside their schema | Ownership and search path can break after a catalog change |
| Tablespaces | New cluster needs the same paths or a deliberate relocation plan; free space on each |
| Prepared transactions | Must be resolved before upgrade; an in-doubt transaction blocks progress |
| Logical replication slots | PostgreSQL 17+ can migrate slots and subscription dependencies under prerequisites; older clusters silently leave them behind. Record and recreate them, and plan downstream consumers |
| Large objects | Volume affects upgrade time and memory on older target versions |
| Custom full-text search files | Dictionaries and configurations are not carried automatically |
| `reg*` OID columns | Several OID-referencing types cannot be upgraded by `pg_upgrade` |
| Collation and ICU | Database-level collation, ICU library version and index ordering can change; verify sort behavior and plan reindex if needed |
| Event triggers and FDWs | DDL hooks and foreign extensions may need recreation or version alignment |
| Drivers, ORMs, poolers | Protocol, prepared statements, type mapping and SCRAM behavior must match the new server |
| Backup, monitoring and audit agents | Extensions and binaries must load on the new major |
| Storage and WAL headroom | Copy mode needs room for a second data set; upgrade generates WAL and logs |

The extension inventory is the most common source of late failure. List installed extensions with their versions and schemas, then confirm the new server has a compatible shared object and an upgrade path. Installing the new binary is not the same as creating the extension in the new cluster.

## Use `pg_upgrade` deliberately

The [pg_upgrade documentation](https://www.postgresql.org/docs/current/pgupgrade.html) owns the exact flags and steps; these are the decisions that change the outcome:

1. Install the new server binaries alongside the old ones. Keep the old binaries until the upgrade is accepted.
2. Initialize the new cluster with compatible encoding, locale and checksums. A locale mismatch is a correctness problem, not a warning.
3. Install extension shared objects for the new server. Do not run `CREATE EXTENSION` in the new cluster; the extension definitions come from the old catalog.
4. Stop the old server cleanly and take a verified backup or snapshot.
5. Run `pg_upgrade --check` first. It checks cluster compatibility without changing data. A clean check is necessary, not sufficient: it does not exercise application queries, collation ordering or extension behavior.
6. Decide how files are transferred. Copy mode leaves the old cluster intact and needs free space roughly equal to the data set. `--link` is faster and needs less space but hard-links files, so starting the new cluster mutates the old one; the old cluster is no longer a safe rollback. `--clone` uses copy-on-write where the filesystem supports it. Verify the option on the deployed version.
7. Use `--jobs` for parallelism where I/O and CPU allow, and watch the upgrade log for the actual bottleneck.
8. Start the new cluster, run the extension update script `pg_upgrade` produces, refresh statistics where the version or provider does not carry them, and run application-level checks before switching traffic.

Recent `pg_upgrade` versions transfer planner statistics by default and expose `--no-statistics`; older versions do not. Run `ANALYZE` after the upgrade in either case unless the target version and provider documentation explicitly say statistics were carried, and treat missing statistics as a plan-regression risk.

## Rehearse on real shape

A schema-only copy does not test collation, data-dependent plans, large objects or extension runtime behavior. Rehearse with a production-like copy, on comparable storage, with the same extension versions and configuration.

- Run the application's regression and journey checks against the new cluster, not only SQL smoke tests.
- Compare query plans and timings for the critical statements before and after; a major version can change plans without changing SQL.
- Exercise connection pooling, failover, read replicas and backup/restore against the new version.
- Compare collation output on representative sorted and indexed data, especially when ICU or the OS locale changed.
- Measure the actual `--check` and full-upgrade duration, plus validation and rollback time. These numbers set the maintenance window.
- Rehearse rollback: restore the backup, repoint a client, and confirm the old application still works. A plan that assumes an untested reverse path is not a rollback plan.

## Cut over and protect the exit

Freeze schema changes during the final window. Stop or drain writes, resolve prepared transactions, disable scheduled jobs and subscriptions that would write to the old cluster, and record sequence values and replication positions needed after the switch.

- Run the upgrade, validate row counts and application invariants, then move traffic. Fence stale writers: a pooled connection or job still pointed at the old cluster can write data the new primary will never see.
- Update connection strings, pooler configuration, DNS or service discovery, monitoring targets and backup jobs together. A successful server start is not a completed cutover.
- Keep the old cluster read-only or stopped according to the rollback decision. Do not restart a cluster upgraded with `--link`; its files are shared with the new one.

There is no in-place downgrade. Rolling back means restoring the pre-upgrade backup or reversing a logical replication setup, and both lose or complicate writes made after cutover. State the achievable recovery point before the window, and decide in advance whether a failed validation means restore-and-repoint or forward repair. Application rollback and data rollback are separate operations.

After cutover, re-create logical slots, update extensions, verify sequences and scheduled jobs, refresh statistics, and watch plan regressions, lock waits, bloat and replication lag through at least one representative workload cycle.

| Evidence | Claim supported |
| --- | --- |
| Clean `pg_upgrade --check` | The clusters pass tool-level compatibility checks |
| Rehearsal on production-like data | The path works for this schema and workload |
| Application regression run on the new version | Tested behavior still works |
| Measured upgrade and restore time | The maintenance window and recovery point are credible |
| Post-cutover invariant and plan checks | The new cluster serves the workload, for the observed period |
| Exercised restore-and-repoint | A rollback path exists beyond intent |

Sources: [pg_upgrade](https://www.postgresql.org/docs/current/pgupgrade.html), [upgrading a cluster](https://www.postgresql.org/docs/current/upgrading.html), [logical replication upgrade](https://www.postgresql.org/docs/current/logical-replication-upgrade.html) and [logical replication](https://www.postgresql.org/docs/current/logical-replication.html). Checked 2026-11-16; behavior differs by version, so confirm against the deployed and target major versions.
