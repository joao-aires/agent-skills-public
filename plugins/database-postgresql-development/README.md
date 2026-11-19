# PostgreSQL plugin: version-aware data contracts, workload diagnosis and recovery

The `database-postgresql-development` plugin applies generic data and performance decisions to one engine, with the actual server version, hosting model and roles in view. It carries schema and concurrency development, workload diagnosis, recovery and upgrade operations, plus one acquired Supabase best-practices reference.

The local methods remain the decision owners. The acquired skill is selective reference material and does not replace version- or provider-matched evidence.

## Purpose

Use this package when the selected engine is PostgreSQL and the decision depends on engine behavior: row-level security, transactions and locks, plan interpretation, pooling, maintenance, backup or a major upgrade. It composes with `database-development` for engine-independent contracts and with the project's service, security and delivery decisions.

## Conceptual model

| Question | Owner |
| --- | --- |
| How do these invariants, roles and concurrent operations become a PostgreSQL schema and transaction contract? | [postgresql-development](skills/postgresql-development/SKILL.md) |
| Where does this workload spend time, and which engine change improves it? | [postgresql-performance](skills/postgresql-performance/SKILL.md) |
| Can this database be restored, maintained and upgraded within its commitments? | [postgresql-operations](skills/postgresql-operations/SKILL.md) |
| What do reviewed external rules and provider examples suggest we verify? | `supabase-postgres-best-practices` (acquired) |

Authority runs in one direction: the local methods decide, the acquired guidance raises candidates and checks, and the deployed version plus primary documentation settle behavior.

## Responsibilities

| Skill | Type | Owns | Stops at | Not for |
| --- | --- | --- | --- | --- |
| [postgresql-development](skills/postgresql-development/SKILL.md) | method | Types, constraints, keys, row-level security, concurrent transactions, locking and schema change with the real roles | An implemented or reviewable engine contract with verification | Generic data design, application authority or provider controls |
| [postgresql-performance](skills/postgresql-performance/SKILL.md) | method | Plan and wait interpretation, index and connection choices, maintenance pressure, before/after measurement | A supported diagnosis, explicit tradeoffs and measured result | Universal tuning recipes or infrastructure purchase |
| [postgresql-operations](skills/postgresql-operations/SKILL.md) | method | Recoverability, backup and restore evidence, replication health, maintenance and major upgrades | An exercised recovery or a precise unexercised gap | Inventing superuser, filesystem or control-plane capabilities |
| [supabase-postgres-best-practices](skills/supabase-postgres-best-practices/SKILL.md) | method (upstream) | Upstream rule catalogue for queries, connections, RLS, schema, locking and diagnostics | Candidate rules to test in this deployment | Local decision authority, provider selection or a version guarantee |

## How it materialized

| Model element | Implementation |
| --- | --- |
| Engine development contract | [postgresql-development](skills/postgresql-development/SKILL.md) |
| Workload diagnosis and measurement | [postgresql-performance](skills/postgresql-performance/SKILL.md) |
| Recovery, health and upgrades | [postgresql-operations](skills/postgresql-operations/SKILL.md), [major upgrades](skills/postgresql-operations/references/major-upgrades.md), [managed upgrades](skills/postgresql-operations/references/managed-upgrades.md) |
| Acquired guidance and licence | `skills/supabase-postgres-best-practices/`, `UPSTREAM-LICENSE.txt`, `CHANGELOG.md` |
| Reviewed sources and pin | [sources](references/sources.md) |
| Generic data and performance decisions | `database-development` |

## Reading paths

1. **New schema or access rule** → [postgresql-development](skills/postgresql-development/SKILL.md) for types, constraints and RLS → the application role and connection path → verification through that role.
2. **Slow query or pool pressure** → [postgresql-performance](skills/postgresql-performance/SKILL.md) to locate the time → representative plans and waits → a measured change with its write and maintenance cost.
3. **Backup, failover or upgrade** → [postgresql-operations](skills/postgresql-operations/SKILL.md) → the hosting-model reference → an exercised recovery on an authorized target.
4. **Unfamiliar rule or optimization** → the acquired [Supabase guidance](skills/supabase-postgres-best-practices/SKILL.md) as a candidate → current primary documentation for the deployed version → the local method that owns the decision.

## Boundaries

- **Engine-independent design.** Invariants, ownership, storage choice and schema-evolution strategy belong to `database-development`. This package implements them in PostgreSQL.
- **Service behavior.** Operation meaning, authority, idempotency and completion belong to backend service design; application authorization remains necessary even when RLS is present.
- **Hosting provider.** Managed-service prechecks, clones, extension allowlists and restore-based rollback are provider behavior. Verify them in the actual account and plan; the package does not establish provider capability.
- **Security and delivery.** Credential lifecycle, threat modeling, release authorization and served-outcome verification belong to their owning capabilities.
- **Acquired guidance.** The Supabase skill is upstream text preserved at a pinned commit. Its rules are not automatically applicable to another version, extension set or hosting model, and it does not own a local decision.

## Authority and optional tools

The package declares no MCP servers and no database connection. Inspecting a cluster, running `EXPLAIN ANALYZE`, creating a role or restoring a backup requires scope from the request and access to the named environment. An `EXPLAIN ANALYZE` executes the statement; rollback cannot undo sequence consumption or external effects. Installing the package does not upgrade a database or select a provider.

## Acquired sources

| Skill | Source | Pin | Licence |
| --- | --- | --- | --- |
| `supabase-postgres-best-practices` | [supabase/agent-skills](https://github.com/supabase/agent-skills) | `c9be0e9` | MIT |

## Maintenance

Owning sources are the local `skills/*/SKILL.md` files, `references/sources.md`, and the acquired folder with its upstream notice and licence. Update this README when the local decision split, the acquisition or the provider boundary changes. Validate with `scripts/validate_plugins.py`, `scripts/check_collection.py` and the repository tests; recheck pins through upstream maintenance.
