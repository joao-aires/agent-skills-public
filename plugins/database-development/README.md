# Database development plugin: engine-independent data contracts and measured performance

The `database-development` plugin carries two generic database methods: designing stored data around invariants and use, and improving a workload from measured evidence.

It deliberately names no engine, hosting model or migration tool. Engine-specific schema, diagnostics and operating mechanics belong to the PostgreSQL package when that engine is selected.

## Purpose

Use this package when the decision is about data itself: which facts must remain true, which representations are authoritative, how a schema change can be deployed safely, or where a measured workload actually spends its time. It composes with service behavior, architecture and operations methods, and leaves vendor mechanics to the selected engine package.

## Conceptual model

| Question | Owner |
| --- | --- |
| What must remain true, who owns the data, and how may it evolve? | [database-design](skills/database-design/SKILL.md) |
| Where does this workload spend time and resources, and which change improves it? | [database-performance](skills/database-performance/SKILL.md) |
| How does this engine express, diagnose and operate that decision? | The selected engine package |

The two local methods answer different questions. `database-design` decides the durable contract; `database-performance` tests an explanation of observed behavior. Neither selects an engine, and a performance result does not by itself reopen the data contract.

## Responsibilities

| Skill | Type | Owns | Stops at | Not for |
| --- | --- | --- | --- | --- |
| [database-design](skills/database-design/SKILL.md) | method | Stored representation of authoritative and derived data, enforceable constraints, consistency boundaries, atomic operations, lifecycle, backfills and schema evolution | A data contract, migration sequence and completion evidence | Engine syntax, index mechanics or vendor controls |
| [database-performance](skills/database-performance/SKILL.md) | method | Bottleneck framing, workload evidence, discriminating changes, before/after correctness and cost comparison | A supported diagnosis, chosen tradeoff and remaining uncertainty | Engine tuning recipes, infrastructure purchase or a guaranteed latency claim |

## Reading paths

1. **New persisted capability** → [database-design](skills/database-design/SKILL.md) for invariants, authority and atomicity → service behavior for operation meaning → the engine package for types, constraints and migrations.
2. **Risky schema change** → [database-design](skills/database-design/SKILL.md) for readers, writers and rollout compatibility → engine migration mechanics → deployment evidence.
3. **Slow or contended workload** → [database-performance](skills/database-performance/SKILL.md) to locate the time → engine diagnostics for plans, waits and statistics → a measured change and its write-side cost.
4. **Unclear whether the contract or the query is wrong** → [database-design](skills/database-design/SKILL.md) first; tuning around a broken invariant hides the defect.
5. **Retention, deletion or correction** → [database-design](skills/database-design/SKILL.md) for lifecycle and history semantics → the engine package for physical deletion and storage reclamation.

## Boundaries

- **Engine specifics.** Types, indexes, isolation behavior, plan interpretation, pooling and backup mechanics belong to the engine package; in this collection that is `database-postgresql-development`. Do not invent portable syntax for them here.
- **Service behavior.** Operation meaning, authority, idempotency and completion belong to backend service design. This package consumes those decisions and supplies the data contract.
- **Architecture.** Choosing a storage family or changing service boundaries belongs to the architecture design activity. This package compares storage only when a workload or contract requires it.
- **Operations.** Backup, recovery, upgrades and production diagnosis with load require the engine or operations capability and an authorized target.
- **Evidence.** `database-performance` establishes only the exercised workload under the stated conditions. Estimated plan cost is not a measurement, and a synthetic benchmark is not a production promise.

## Authority and optional tools

The package declares no MCP servers, drivers or external services. Inspecting a live database, running `EXPLAIN ANALYZE` or applying a migration requires scope from the request and access to the actual environment. Installing the package selects no database engine and authorizes no schema or data change.

## Maintenance

Owning sources are the two `skills/*/SKILL.md` files. Update this README when the design/performance split, the engine boundary or the package composition changes. Validate with `scripts/validate_plugins.py`, `scripts/check_collection.py` and the repository tests.
