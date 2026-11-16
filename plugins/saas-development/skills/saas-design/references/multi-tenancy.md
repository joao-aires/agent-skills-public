# Multi-tenancy decisions

Use when several customers share a product, when a customer asks for stronger separation,
or when a tenant must move between regions or tiers. Tenant isolation is a property of every
store and boundary, not only of the database.

## Choose an isolation model

| Model | Isolation | Operating cost | Appropriate when |
| --- | --- | --- | --- |
| Shared database and schema | Row-level tenant key; strongest need for query discipline and tests. | Lowest per tenant. | Many small tenants with similar requirements and a credible guard against missing filters. |
| Schema per tenant | Separate schema or namespace in one database. | Moderate; migrations and connection management multiply. | Tenants need some logical separation without dedicated infrastructure. |
| Database per tenant | Separate database or cluster. | Higher; backups, upgrades and monitoring per tenant. | Strong isolation, per-tenant recovery or regulatory expectations. |
| Dedicated deployment | Separate application and data plane. | Highest; full environment per tenant. | Contractual isolation, customization or residency that shared infrastructure cannot meet. |
| Hybrid | Shared control plane with isolated data or compute for selected tenants. | Varies by tier. | A small number of customers need stronger separation than the default. |

Choose from isolation, recovery granularity, residency, customization, cost and operating
capability. Do not treat every B2B product as a dedicated deployment, and do not treat a
shared database as automatically acceptable for every contract.

Record which model applies to which resource. A product can use a shared database for
most data and a dedicated store for documents, search or analytics; each store needs its
own tenancy decision.

## Partition every store and boundary

A tenant key must be structural, not an optional filter:

- include the tenant in primary keys, unique constraints, foreign keys and indexes;
- scope queries through a repository or policy layer that cannot silently omit the tenant;
- apply the same rule to caches, session data, search indices, object storage, queues,
  analytics, exports, audit logs and AI/tool retrieval;
- make cross-tenant joins either impossible or explicitly reviewed;
- test the actual query path, including bulk operations and admin tools.

A unique constraint that ignores the tenant can block a legitimate duplicate or leak the
existence of another tenant's record. A cache key that omits the tenant can serve one
customer's data to another.

Row-level security can enforce isolation close to the data, but only when every exposed
table has a policy, the policy uses verified tenant context and privileged service
credentials do not bypass it. Treat a missing policy as a breach path, not a configuration
gap.

## Per-tenant keys and secrets

Where the product encrypts data or calls providers on a tenant's behalf, decide whether to
use a shared key with tenant-scoped data or a per-tenant key.

- Per-tenant keys improve cryptographic separation and enable crypto-shredding on deletion.
- They add key management, rotation, backup and recovery complexity.
- A key management service can hold per-tenant keys; the product still needs a mapping and
  an access policy.
- Provider credentials, webhook secrets and signing keys should be per tenant where the
  provider supports it.

Do not claim tenant-specific encryption merely because the row has a tenant column. State
which key protects which data and who can use it.

## Noisy neighbors and fair service

Shared infrastructure means one tenant can affect another through load, storage, queue
depth, connection pools, rate limits or expensive queries.

- Set per-tenant quotas and rate limits from the product promise, not only from global
  capacity.
- Isolate or prioritize background work so one tenant's backlog does not starve others.
- Bound expensive searches, exports and reports; queue or reject rather than letting them
  exhaust shared resources.
- Monitor per-tenant latency, error rate, queue lag and storage growth.
- Decide whether a noisy tenant is throttled, moved to a stronger tier or asked to change
  behavior.

Capacity planning should use the largest tenants and the realistic distribution, not an
average that hides a heavy user.

## Regionality

Data residency is a property of the whole processing path: primary database, backups,
logs, analytics, search, queues, support access and subprocessors. A region selector in a
dashboard does not establish residency.

- Decide whether the control plane is global and the data plane regional, and what metadata
  may leave the region.
- Pin backups and disaster-recovery copies to the accepted locations.
- Check support and on-call access paths, including provider support.
- Define how a tenant is placed in a region and whether it can move.
- Keep the failover path within the same residency constraints where required.

An EU region is not a legal conclusion. Confirm the actual data flows and contractual terms
with the applicable privacy and compliance owners.

## Tenant migration

A tenant may need to move between regions, isolation tiers or infrastructure during
residency changes, an acquisition, a contract upgrade or a platform migration.

Establish:

- the trigger and the authority to move the tenant;
- the target model and its capacity;
- stable identifiers so URLs, API keys and external references survive the move;
- data copy, verification and delta handling while the source remains active;
- how provider-side objects, search indices, queues and backups move or are rebuilt;
- cutover, DNS or routing changes and the customer-visible window;
- a rollback or forward-repair path;
- deletion of the source copy after verification, including backups and derived stores.

A live migration with dual writes needs conflict rules and a clear authority. A maintenance
window is simpler but must be communicated and tested. Do not declare migration complete
until the target serves the customer journey and the source no longer processes work.

## Test isolation and recovery

Test at the granularity the promise requires:

- a member of tenant A requests tenant B's record by ID, in list, search, export, bulk and
  AI/tool paths;
- a background job or webhook for one tenant cannot change another;
- a cache, search index or analytics query returns only the intended tenant;
- a support action is scoped and attributed;
- a backup or point-in-time restore of one tenant does not expose or overwrite another;
- a tenant migration preserves identifiers and leaves no active source copy.

Restoring a whole shared database to recover one tenant can lose another tenant's recent
data. If per-tenant recovery is promised, the backup and restore design must support it;
otherwise state the actual recovery granularity.

## Owner boundary

`saas-design` owns the tenancy model and its lifecycle. `saas-identity-and-access` owns
organization authority and membership. `saas-billing` owns the commercial state that may
select a tier. `saas-supporting-services` owns the integration contract for external
stores. Keep the tenant key consistent across all of them rather than letting each
integration invent its own scope.
