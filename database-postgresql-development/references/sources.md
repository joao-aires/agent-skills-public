# PostgreSQL sources and interpretation

These original skills use reviewed upstream topic coverage as research references. No upstream instructions, scripts, example applications or tool/approval policies are imported. Source links are provenance, not runtime dependencies or authorization. Consult the deployed PostgreSQL version and hosting provider before applying a procedure.

## Upstream skill references

| Reviewed source | Revision | Information used |
| --- | --- | --- |
| [Neon postgres-best-practices](https://github.com/neondatabase/postgres-skills/tree/27fe45e0f71ea89a6eaf9ea4d2e4068957c81c26/skills/postgres-best-practices) | `27fe45e0f71ea89a6eaf9ea4d2e4068957c81c26` | Lifecycle topic coverage, conditional references, query diagnostics and isolation examples; repository declares Apache-2.0. |
| [Supabase Postgres best practices](https://github.com/supabase/agent-skills/tree/c9be0e931b7930f7d02126d04774d904c381e7d7/skills/supabase-postgres-best-practices) | `c9be0e931b7930f7d02126d04774d904c381e7d7` | Workload, pooling, indexing and RLS topics; repository declares MIT. Universal index/RLS prescriptions and illustrative speedups are not adopted as acceptance rules. |
| [Microsoft PostgreSQL skills](https://github.com/microsoft/postgres-skills/tree/9ba96abc800a574a0872f3d6b912ea8be1a6735e/plugin/skills/postgresql-best-practices) | `9ba96abc800a574a0872f3d6b912ea8be1a6735e` | Distinction between managed controls and server administration; repository declares MIT. No MCP server, Azure dependency, account discovery or unconditional confirmation loop is imported. |

The skill frontmatter's `metadata.references` points here for attribution and context. These are research references rather than acquired sources in upstream.lock.json.

## Primary implementation references

- For SQL representation, constraints and migrations: [data definition](https://www.postgresql.org/docs/current/ddl.html), [explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html) and [CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html).
- For concurrency and access: [transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html), [row security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) and [role attributes](https://www.postgresql.org/docs/current/role-attributes.html).
- For diagnosis: [EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html), [statistics](https://www.postgresql.org/docs/current/monitoring-stats.html) and [routine vacuuming](https://www.postgresql.org/docs/current/routine-vacuuming.html).
- For recovery and change: [backup and restore](https://www.postgresql.org/docs/current/backup.html), [continuous archiving](https://www.postgresql.org/docs/current/continuous-archiving.html), [replication](https://www.postgresql.org/docs/current/high-availability.html) and [upgrading](https://www.postgresql.org/docs/current/upgrading.html).

The current-version links are discovery points. Select the deployed major version, relevant extensions and provider controls when implementing; installing this guidance does not upgrade a database.
