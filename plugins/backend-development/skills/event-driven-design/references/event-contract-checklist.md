# Event contract checklist

Use this when reviewing a proposed or changed event with its producer and at least one real consumer. It is a set of decisions to resolve, not a document template. Record the result in the existing design proposal/ECR, schema or AsyncAPI file; do not create a second contract of record.

## Meaning and ownership

- What fact does the event assert, in the past tense, and which service is authoritative for it?
- Is this a domain event, an integration event, a command or a query response in disguise?
- Can any other producer assert the same fact? If so, what is the merge or conflict rule?
- Does a consumer need this event to act, or only to invalidate a cache and re-read? The second is usually cheaper and less coupled.
- Is the event published only after the change is durable, or does it describe an intention that may still fail?
- What is explicitly not promised by this event? Record it.

## Event style

| If the consumer needs | Prefer | Avoid when |
| --- | --- | --- |
| To know that something changed | Notification with a stable reference | Consumers immediately call back for every field; that is synchronous coupling. |
| To act without a callback | Event-carried state transfer with the needed fields | The payload duplicates a large mutable aggregate. |
| A full audit or rebuildable history | Event sourcing with owned snapshots and projections | The team cannot own replay, schema history and projection repair. |
| Another service to perform work | An addressed command with authority and a reply path | It is broadcast to every consumer as if it were a fact. |

## Envelope and identity

| Field | Why it exists | Failure when missing or ambiguous |
| --- | --- | --- |
| Event type | Stable routing and schema lookup | Consumers bind to a class name or topic position and break on refactor. |
| Event id | Deduplication and support | Replays cannot be distinguished from new facts. |
| Source | Producer identity and id scope | Two producers collide on the same id. |
| Subject/aggregate id | Per-entity ordering and state lookup | Consumers cannot tell which entity changed. |
| Occurred-at | Business time for ordering and diagnosis | Producer publish time is mistaken for when the fact happened. |
| Published-at / recorded-at | Delivery and lag diagnosis | End-to-end age cannot be measured. |
| Schema version | Compatibility and replay | Old events cannot be deserialized after an upgrade. |
| Causation id | Trace the command or event that caused this one | Loops and chains are hard to diagnose. |
| Correlation id | Group one business flow across services | Support cannot connect related events. |
| Tenant / partition key | Isolation and ordering | Cross-tenant leakage or lost per-entity order. |
| Payload schema id or reference | Registry lookup | Consumers guess the format. |

An event id is unique within its source, not globally, unless the contract says otherwise. Deduplication keys should combine source and id, or use a business key plus version.

## Payload review

- Required and optional fields are explicit; `null` and absent have one agreed meaning.
- Money uses integer minor units or decimal with a currency; no unlabeled float.
- Timestamps are UTC with a stated semantic; durations have units in the name.
- Enums have an unknown-value policy: tolerate and preserve, map to `unknown`, or reject with a defined failure.
- Identifiers are opaque and stable; no database sequence, row version or internal path leaks unintentionally.
- Deletion is represented explicitly, including tombstone behavior for compacted streams.
- Failure and rejection are events or responses with the same contract discipline, not an exception string.
- Payload contains only what consumers need; large blobs are references to owned storage.
- Validation happens at produce and at consume; the consumer does not trust the producer's authority.

## Evolution

| Change | Usually compatible | Check |
| --- | --- | --- |
| Add an optional field with a default | Yes, additive | Old consumers ignore it; new consumers handle absence. |
| Add a required field | No | Needs a migration window or a new event version. |
| Remove an optional field | Depends on mode | Forward/backward direction and consumer use. |
| Rename a field | No, unless aliased | Wire name, generated code and stored data all matter. |
| Change a type or widen/narrow a number | Rarely | Precision, overflow and JSON number behavior. |
| Reuse a field name or enum number | Never | Silent semantic corruption. |
| Change units, currency or timezone | No | Schema validators do not catch meaning changes. |
| Add an enum member | Depends | Old consumers must tolerate unknown values. |
| Remove or reinterpret a status value | No | State machines and reporting depend on it. |
| Change ordering or key | No | Consumers' state and dedupe assumptions break. |

For every change, state which side upgrades first and which retained events must still deserialize. A schema registry mode is not a substitute for testing a recorded old event with the new consumer.

## Ordering and topology

- Which invariant requires order: per entity, per account, per tenant, or global?
- Does the partition/queue key match that invariant, and what happens to hot keys?
- Does the consumer require order across different keys? If so, what is the cost of a single partition or an application reorder buffer?
- Can partition count change without breaking key mapping or cached state? Who owns that migration?
- Are retries routed in a way that reorders records for the same key? Is that acceptable?
- Does the consumer reject stale versions, and what does it do with a gap?
- Are multiple consumer groups intentionally independent, or are they accidentally competing?

## Delivery and idempotency

- What is the acknowledgment boundary: broker write, local durable record, external effect, or business completion?
- Which failure is accepted on crash: duplicate effect or lost work? Both need a stated mitigation.
- What is the stable deduplication key, and how long is it retained relative to replay and redelivery?
- Is the effect naturally idempotent (set state, upsert by version) or does it need a dedupe record or provider key?
- Are database change and publication intent atomic (outbox), and who relays and cleans up?
- Does the consumer record the event id in the same transaction as the effect (inbox)?
- What happens on a permanent failure, a poison record and an exhausted retry budget?
- Who owns the dead-letter queue, its retention, its repair tooling and its replay authorization?
- Is any exactly-once claim limited to a boundary that actually supports it?

## Security and privacy

- Which tenants or users may produce and consume this event, and how is that enforced at the broker and at the consumer?
- Does the payload minimize personal, financial or secret data? Can a reference replace a sensitive field?
- Is sensitive data excluded from headers, logs, traces and dead-letter copies?
- Is payload retention compatible with deletion, residency and access requirements?
- Are schema and registry access controlled, and can a consumer read a schema it should not?
- Does replay respect deletion and consent state, or resurrect data that should be gone?

## Operations and evidence

- Which signal proves production, consumption and business effect separately?
- What are the lag, event-age, retry, dead-letter and outbox-backlog expectations, and who acts on them?
- Is trace/correlation context propagated across the broker boundary?
- Is retention derived from replay and recovery needs rather than left at a default?
- Is capacity estimated from rate, size, retention, replication, consumer throughput and replay headroom?
- Is there a documented replay procedure with scope, rate limit, effect suppression and rollback?
- Does the contract have an owner, a deprecation policy and a consumer inventory?

## Review evidence

A contract is reviewable when the producer can show the schema or message definition, one representative event, the key and ordering decision, the delivery and dedupe boundary, the failure disposition, the consumer list and the compatibility test. A diagram alone, a successful publish or a generated type does not establish these.

Reject or reopen the review when:

- the event name describes an action rather than a fact;
- the payload is the internal database row;
- no consumer can be named for a published event;
- ordering is assumed but no key enforces it;
- exactly-once is claimed across an external effect;
- the dead-letter path has no owner or repair route;
- retention is shorter than the stated replay need;
- an incompatible change has no consumer migration plan.

## Common anti-patterns

- Publishing before the transaction commits, then treating a missing event as a consumer bug.
- One generic `EntityChanged` event carrying optional fields for every type.
- Using event sourcing for a simple notification requirement, or notifications for a rebuild requirement.
- Treating the schema registry as proof of semantic compatibility.
- Deduplicating in memory or with a cache shorter than the redelivery window.
- Retrying a permanent validation failure forever because the retry metric looks healthy.
- Replaying into live side effects and discovering it through customers.
- Letting every consumer share one group, one topic and one retention policy.
- Documenting a contract in a wiki that no producer or consumer test reads.

## Sources

The checklist synthesizes the contract decisions in the parent skill and the artifact guidance for sequence, state-machine and compatibility views. Primary sources for specific claims are listed in [Kafka patterns](kafka-patterns.md) and the parent skill's `Sources and fit`. Broker-specific limits, registry behavior and protocol features must be verified against the deployed versions.
