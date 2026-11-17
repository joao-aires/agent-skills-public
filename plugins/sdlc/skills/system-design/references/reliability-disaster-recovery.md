# Disaster recovery and continuity design

Continuity is the part of reliability that keeps a critical journey available through the loss of a site, region, provider, cluster or dataset. It is a business property, not a backup feature: the plan starts from what users must still be able to do, how much interruption is acceptable and how much recent work may be lost.

An SLO describes normal operation; RTO/RPO bound an interruption. Do not express an RTO as an availability target, and do not treat a successful backup job as recovery evidence. [Data recovery](../../data-recovery/SKILL.md) owns backup configuration, restore mechanics and data-integrity proof. This reference owns the continuity design and the evidence that it works: critical journeys, recovery objectives, dependency order, strategy, failover/failback and exercises.

## Start from critical journeys

Tier the work by impact over time rather than by component importance:

- Safety, money, legal obligation or irreversible loss first; then customer-facing revenue and core collaboration; then internal and analytical work.
- For each tier, state the **minimum viable capability** during an interruption, not only full restoration. Read-only mode, deferred writes, a manual queue or a status page can be an accepted degraded outcome.
- Record which journeys may stay unavailable, for how long, and who accepted that.
- Include machine consumers and scheduled work: billing runs, exports, synchronizations, webhooks, reconciliation and partner integrations. A dashboard-only view of continuity misses them.
- Name the failure domain precisely. "The cloud" is not one: a region, availability zone, account, cluster, primary datastore, identity provider, DNS provider or single vendor can each be lost.

## Set RTO and RPO honestly

**RTO** is elapsed time from failure to restored capability. It includes detection, decision, provisioning, data availability, verification and traffic shift — not the duration of a restore command. Effective RTO is bounded by the slowest required dependency and by the time needed to prove the service is usable.

**RPO** is acceptable data loss, expressed in time or transactions. Set it per data class:

| Data class | Recovery question |
| --- | --- |
| Authoritative records | Can the loss be reconstructed from an external source, or is it gone? |
| Derived indexes and projections | Can they be rebuilt from the authoritative record, and how long does that take? |
| Caches | Is a cold start acceptable, and what is the resulting load? |
| Object and file storage | Are versioning, retention and cross-account copies sufficient for deletion or ransomware? |
| Secrets, keys and configuration | Can the service start and decrypt its data without the primary environment? |
| Analytics, logs and audit | Is loss acceptable, and does a legal or contractual obligation change that? |

- Partial loss needs its own objectives. One corrupted table, one tenant, one region's data and one provider's dataset have different recovery paths.
- "Zero data loss" requires synchronous durability at an availability and latency cost. State the cost rather than adopting the phrase.
- Targets come from accepted requirements. If they are unknown, label a provisional value, show what the design does under it, and return the decision.

## Establish dependency order

Recover in dependency order and shift traffic in reverse:

1. Identity, access and decision authority.
2. Network, DNS, certificates and edge configuration.
3. Secrets, encryption keys and configuration.
4. Durable data and its replication or restore.
5. Compute, runtime and scheduling.
6. Messaging, queues and workers.
7. External integrations and provider quotas.
8. Client traffic, communications and reconciliation.

Check for circular dependencies before accepting the order: a key store in the failed region, a secret needed to decrypt backups, an identity provider reached through the failed network, a package registry or CI/CD system in the same account, and observability that also disappeared. Recovery without the ability to see it is guesswork.

Also establish:

- which dependencies are assumed to survive, and what the plan is when they do not;
- whether the recovery environment can carry the restored traffic, including quotas, licenses, connection limits and provider throughput;
- which work may resume automatically and which needs an explicit release, so restored workers do not replay stale jobs into the world.

## Choose a continuity strategy

Compare strategies against journey tiers, not as a maturity ladder:

| Strategy | Mechanism | Dominant cost and risk |
| --- | --- | --- |
| Backup and restore | Rebuild infrastructure and data from protected copies. | Lowest standing cost; longest and least predictable RTO; restore and dependency order dominate. |
| Pilot light | Core data and configuration replicated; compute started at recovery time. | Moderate cost; startup, scaling and dependency verification dominate the RTO. |
| Warm standby | A scaled-down but running copy, promoted and scaled on failover. | Higher standing cost; data lag, promotion and capacity verification dominate. |
| Multi-site active/active | More than one site serves traffic continuously. | Highest cost and complexity; consistency, routing, split-brain and failback dominate. |

A strategy name is not evidence. Record what it actually covers: which journeys, which data classes, which failure domains and which dependencies. A warm standby for compute with a single-region primary database does not meet a regional-loss objective. Conversely, a lower tier may legitimately accept backup and restore.

## Design failover and failback

Failover is a decision and an operation; failback is a second, often riskier migration.

**Triggers and authority**

- Define the health signal that starts a failover, including hysteresis and false-positive handling. A provider status page is not the only signal, and an internal health check can fail while the site is healthy.
- Name who may declare a disaster, who authorizes failover, who may accept data loss and spend, and how that authority is reached out of hours. Pre-authorize what can be pre-authorized; escalation during an outage is expensive.
- Separate the decision to fail over from the decision to fail back.

**Data readiness**

- Measure replication lag; it determines the achievable RPO, not the configured interval.
- Check schema and application compatibility between sites. A recovery site running an older schema is not a recovery site.
- Prevent split-brain with a single-writer or fencing mechanism, and decide how divergent writes will be reconciled. Two sites accepting writes creates a data problem that failover does not solve.
- Account for in-flight work: queued messages, open transactions, accepted orders and external side effects that may be duplicated or lost.

**Traffic and clients**

- DNS TTL and resolver caching bound how fast traffic actually moves. Lower TTLs are a standing cost and a partial measure.
- Global load balancers, health checks, certificates, CDN configuration and partner allowlists must exist in the recovery path.
- Clients that pin addresses, cache endpoints, use certificate pinning or ship fixed configuration may not follow a DNS change. Include mobile, desktop, browser extensions and machine clients.
- Verify the recovery site's capacity with realistic traffic, not a health endpoint.

**Failback**

Plan the return before the disaster:

- reverse replication and reconcile writes made in the recovery site;
- rebuild and verify the failed site, including backups and monitoring;
- cut traffic back deliberately, verify, and only then decommission the temporary environment;
- keep data written during the recovery period. Failing back by discarding it converts one incident into two.

An untested failback path is a known gap, not an assumed capability.

## Protect data across the failure

Replication and high availability do not replace backups. Backups must survive the credential, deletion or encryption event that affects production: account or region separation, immutability and retention are choices with cost and residency consequences.

- Prefer asynchronous replication for distance and cost, and state the resulting RPO. Synchronous replication reduces loss and couples availability.
- Replicate or escrow keys where data will be restored; a backup that cannot be decrypted is not a recovery point.
- Rebuild derived state from its source rather than restoring it as truth.
- Check residency and contractual constraints on every recovery copy and region.
- Data-integrity proof, restore verification and point-in-time recovery mechanics belong to [data recovery](../../data-recovery/SKILL.md).

## Exercise the plan

Three levels answer different questions:

| Exercise | Question it answers | What it does not prove |
| --- | --- | --- |
| Restore test | Can the data be recovered to a usable point? | Failover, dependencies or traffic shift. |
| Failover test | Can traffic and dependencies move to the recovery environment? | Failback or sustained operation. |
| Game day | Can the organization detect, decide, communicate, fail over and later fail back? | Nothing beyond the scenario and scale exercised. |

Run exercises against an isolated target with external side effects suppressed, and rotate any credentials exposed to the exercise. Start from a realistic failure, not a convenient one. Measure detection, decision, execution and verification separately, then compare the total with the RTO and the actual loss with the RPO.

- Include the runbook's real gaps: missing access, stale contacts, undocumented dependencies, provider quotas, expired certificates and unavailable keys.
- Repeat after material changes in topology, schema, provider, keys or ownership, and after an incident that revealed a new dependency.
- Record what was not exercised. A successful restore does not prove failover; a successful failover does not prove failback.

Use [resilience testing](../../resilience-testing/SKILL.md) for controlled component and dependency faults, and [capacity and cost](../../capacity-and-cost/SKILL.md) when the strategy's standing cost or recovery-site capacity is the question.

## Record the continuity design

Return:

- critical journeys, tiers and accepted degraded capability;
- named failure domains and the dependencies assumed to survive;
- RTO/RPO per journey and data class, with the source or the unresolved decision;
- the chosen strategy, rejected alternatives and the tradeoff that justified it;
- dependency order and circular-dependency findings;
- failover and failback outline, including triggers, authority, traffic and reconciliation;
- replication mode, measured lag and data-protection boundary;
- exercise plan, last measured result and gaps with owners.

Track **designed**, **exercised** and **verified** separately. Hand the procedure to the [runbook guide](../../guide-runbook/SKILL.md) and the restore mechanics to [data recovery](../../data-recovery/SKILL.md). A design document is not a tested recovery capability, and a provider's disaster-recovery feature does not set our RTO.
