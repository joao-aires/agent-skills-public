# Evolve production data safely

Use for live-schema compatibility, populated-data migrations and backfills.

Inspect existing data, volume, active writers, API/event consumers and overlapping application versions before changing schema. Review Alembic output manually, especially renames, defaults, indexes and destructive changes. Apply migrations once through a controlled delivery job; application replicas must not race them.

Use expand, compatible deployment, bounded backfill, verification and later contract removal when live compatibility requires it. For a new required ownership field, introduce a compatible representation, populate existing rows from defensible mappings, report ambiguous rows, then enforce the invariant. Never fabricate ownership to satisfy a constraint. Remove old fields/paths only after their consumers and rollback needs are resolved.

Assess lock acquisition, scans/rewrites, disk/WAL growth and replication lag for the actual PostgreSQL version and operation. Bound lock waits and backfill rate/transactions; define stop conditions. Choose concurrent indexes or staged constraint validation when supported and justified, checking transaction restrictions and failed-operation cleanup. Make backfills resumable and idempotent, preserving concurrent edits with suitable conditions; review samples, totals and business invariants before enforcing constraints.

Exercise upgrades from the previous schema with representative populated data and compatible old/new code where relevant. A tiny local database does not establish large-table timing or lock safety. Separate application rollback, data repair and backup restoration; document irreversible steps and recovery evidence. Keep schema/operating notes current and live execution within task authority. See [sources and exceptions](sources-and-exceptions.md) for platform-specific details.
