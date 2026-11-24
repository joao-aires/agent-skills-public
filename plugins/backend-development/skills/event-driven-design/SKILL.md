---
name: event-driven-design
description: Design event and message contracts across services, including event meaning, schema evolution, ordering and partitioning, delivery and idempotency, replay, retention and failure handling. Use when a change publishes or consumes events, introduces asynchronous integration or alters an existing event contract; not for broker installation or cluster operations.
user-invocable: true
metadata:
  kind: method
  domain: backend
  phase: design
  scope: generic
  invocation: both
---

# Design events as contracts

An event is a fact one service publishes and others may depend on. It is not a remote procedure call with a different transport, and a broker does not remove the need to decide who owns the state behind it. Architecture boundaries belong to system design; behavior and state inside a service belong to backend design. This discipline owns what crosses the event boundary: what is asserted, how it evolves, how it is ordered and delivered, and what producer and consumer each guarantee.

Read [Kafka patterns](references/kafka-patterns.md) for broker-specific mechanisms and [event contract checklist](references/event-contract-checklist.md) when reviewing a contract. Record the decision in the existing design proposal/ECR with sequence, state-machine and compatibility artifacts; do not invent a parallel event-design document.

## Start from the fact and its owner

Choose the event style deliberately, because each carries different coupling:

| Style | What it publishes | Main cost |
| --- | --- | --- |
| Event notification | A small fact that something changed, with a reference | Consumers must call back for detail, adding coupling and load. |
| Event-carried state transfer | The changed state needed to act without calling back | Payload size, duplication and stale replicated copies. |
| Event sourcing | The authoritative sequence of state-changing events | Replay, schema history, snapshots and projection ownership. |
| Command | An addressed request for another service to act | It is not a fact; it needs a named recipient, authority and response path. |

Distinguish the internal domain event from the published integration event. A domain event may use internal identifiers, rich objects and change freely with the model. An integration event is a public contract: minimal, stable, versioned, free of internal persistence shape and published only after the change is durable. Translate at the boundary rather than publishing the domain model directly.

Identify the single service authoritative for the fact. If two producers can assert the same fact, consumers need an explicit merge or conflict rule, or one producer must stop. Consumers may build derived state; an event does not grant them authority to mutate the producer's data.

Define per event type: a stable type name, an event id, the source, the subject or aggregate identity, when the fact occurred versus when it was published, the schema version, causation/correlation identifiers, tenant and partition key, and the business payload. Timestamps have different meanings; producer time is not commit order.

## Make the contract explicit

Use an envelope for cross-cutting attributes and a schema for the business payload. CloudEvents is a reasonable envelope when events cross tools or organizations; it standardizes attributes such as `id`, `source`, `type`, `subject`, `time` and `dataschema`, not the business meaning. Avro, Protobuf or JSON Schema can define the payload; a schema registry can enforce and store versions. AsyncAPI can document channels, operations and messages, but documentation does not enforce runtime compatibility.

Field decisions that cause real breakage:

- Required versus optional, and null versus absent, with one meaning each.
- Units, currency and precision; use integer minor units or decimal, never an unlabeled float.
- Enum handling: unknown values must be tolerated or rejected by explicit policy.
- UTC timestamps with a declared meaning; identifiers opaque and stable.
- Explicit deletion/tombstone semantics and failure or rejection events.
- No internal table, ORM or stack-specific shape in the public payload.

Evolve additively: add optional fields, never reuse a name or number, never change a field's meaning. Choose the compatibility mode per subject and rollout direction. Backward compatibility lets new readers read old data; forward compatibility lets old readers read new data; full requires both. The mode is only useful when the deployment order matches it. Schema compatibility is not semantic compatibility: units, enum meaning, defaults, status semantics and ordering can break consumers while types still validate. Test the old consumer against new events and the new consumer against retained old events.

Consumer inventories, dual-publish or dual-read windows, telemetry on old-version consumption and a removal date make deprecation real. Version at the event type or schema level; a topic per version needs an explicit migration and consumer plan.

## Choose ordering, partitioning and consumer topology

Ordering is a property of the selected transport and key, not of the broker brand. In a partitioned log, order holds within a partition only. Choose the partition key from the invariant that needs order — an aggregate, account or tenant — then accept the resulting skew and hot keys. Cross-aggregate ordering needs a single partition, a sequencer or an application reorder buffer; state the cost rather than implying global order.

Partition count is a capacity and compatibility commitment. Increasing it remaps keys and changes ordering and state locality; decreasing it is generally not possible without rebuilding. Record the key-to-partition assumption wherever consumers rely on it.

A consumer group shares partitions for scale: one partition is processed by one member of the group, so parallelism is capped by partition count and rebalances pause consumption. Long processing can exceed liveness settings and trigger repeated rebalances. Competing consumers on a queue scale differently but do not preserve order unless the queue supports message groups, sessions or a single ordered consumer.

Where consumers can receive stale or out-of-order events, carry a per-aggregate version or sequence and reject or park older versions explicitly. A gap may mean loss, filtering or a producer that has not caught up; decide whether the gap is fatal for that consumer.

## State delivery semantics honestly

At-most-once, at-least-once and exactly-once describe different boundaries. Once a consumer performs an external effect, delivery is at-least-once unless that effect is idempotent or participates in the same transaction. Broker exactly-once, such as Kafka transactions with `read_committed`, covers reads, writes and offsets inside that broker; it does not cover an external side effect.

Define the acknowledgment boundary. Commit progress after the durable effect, not after accepting work into memory. A crash between effect and commit replays the event; a crash between commit and effect loses it. Choose which failure is acceptable for each consumer and make the choice visible. Each consumer group owns its own progress; do not share a group between logically different consumers, and do not let one process commit another's work.

Classify failures as transient or permanent. Retrying a permanent failure blocks the partition behind it; isolate the record, park the key, or route to a retry path while preserving order where order matters. A dead-letter queue is an application pattern with an owner, reason metadata, retention and a repair/replay route — not a broker checkbox. Silent discard is data loss.

## Make effects idempotent and publication atomic

Duplicates are normal. Deduplicate on a stable effect key: producer plus event id, business key plus version, or a domain operation id. Store the dedupe record durably in the same transaction as the effect, and retain it at least as long as redelivery or replay is possible. Conditional writes and unique constraints are stronger than read-then-write. Prefer idempotent state transitions such as upsert or set-status over increments, appends and sends.

Use a transactional outbox when a database change and the intent to publish must commit together. Write the domain change and an outbox row in one local transaction; a relay or change-data-capture publisher sends it, and duplicates remain possible. Per-aggregate order requires an ordering key and a publisher that preserves it. Mark sent only after broker acknowledgment, and give cleanup its own retention policy. An outbox does not create exactly-once delivery.

Use an inbox when the consumed event id and the effect must commit atomically. The dedupe table's growth is a capacity decision. For external effects such as payments or email, use the provider's idempotency key or a status/reconciliation API; a local row cannot roll back an external commit. A timeout after sending leaves the outcome unknown, so reconcile before repeating. General retry, timeout and consistency reasoning belongs to `distributed-systems` expertise when available.

## Decide replay, retention and exhausted work

Replay is a capability, not only an offset reset. Decide who may replay, which consumers and derived stores are rebuilt, whether external effects are suppressed, and how downstream load is bounded. Retention defines the available window; a compacted topic retains the latest value per key, not history. Replaying old events requires current code to read every retained schema version, so the compatibility matrix covers time as well as peers.

Derive retention from recovery, audit, reprocessing and replay needs. Estimate rate × average size × retention × replication, plus indexes, metadata and any tiered storage. Longer retention changes cost and recovery time; deleting a topic destroys replay, so archival must be a separate owned path.

After bounded retries, park exhausted work with its original payload, headers and failure context. Alert on its age, name the owner, and provide an authorized repair or replay route. A retry counter without a terminal disposition is not a policy.

## Bound capacity and observe the flow

Partition count, consumer concurrency, message size, fetch and batch settings, producer buffers and retention are capacity decisions. Bound in-flight work and let consumers pause rather than buffer without limit. A queue absorbs a burst only until its drain deadline; if arrival exceeds sustainable processing, slow producers or shed load explicitly. Broker disk, network, quotas and cross-zone replication all have limits, and restart or replay can arrive as a second load event.

Signals worth defining: publish failure rate, end-to-end event age, consumer lag in records and in time, per-partition skew, rebalance rate, retry and dead-letter counts and age, dedupe hits, outbox backlog, schema rejection and deserialization failure. Propagate trace and correlation context; log event id, type and source rather than full sensitive payloads. Publication success is not business-effect success.

Defer SLO targets to reliability design; implement signals with the stack's telemetry tooling, using `design-system` observability guidance when available. Define what a healthy flow looks like, including a consumer that is running but not progressing.

## Test the contract and its failure modes

- Check schema compatibility in CI against every retained version, and fail the producer change when it breaks the declared mode.
- Run consumer contract tests with recorded old and new events, in both producer/consumer version directions.
- Exercise duplicate, delayed, out-of-order, missing, unknown-field and poison events; retry, dead-letter, repair and replay.
- Exercise producer crash after commit and before publish, consumer crash after effect and before commit, rebalance mid-batch, broker unavailability and schema-registry unavailability.
- For an external effect, prove the provider deduplicates or reconciliation prevents repetition.

Use `testing-resilience` when available for controlled fault experiments, their authorization and their evidence rules. A local or embedded broker, a mocked producer or a successful publish does not establish cluster behavior.

## Keep the reasoning when the broker changes

The same contract questions apply to queues and streams; only the mechanisms move.

| Family | Ordering scope | Acknowledgment and redelivery | Replay |
| --- | --- | --- | --- |
| Partitioned log (Kafka, Redpanda, Kinesis, Pulsar) | Per partition or shard | Consumer/checkpoint commit; replay from a retained offset | Within retention, by offset/sequence |
| Queue with lease (SQS, RabbitMQ, Service Bus, Pub/Sub) | Per message unless FIFO, message groups or sessions are used | Visibility timeout or ack deadline; redelivery after expiry | Limited or absent; depends on retention and redrive |
| Subscription-based stream (Pulsar, JetStream) | Per partition, or per key where supported | Per-message or cumulative ack; redelivery policy and dedupe window | By subscription position within retention |

Verify the exact semantics, limits and version support in the selected broker's documentation rather than inferring them from the family. A visibility timeout is a lease, not proof of completion. A deduplication window is finite. Message groups and sessions buy order with reduced parallelism.

## Sources and fit

- [Apache Kafka design](https://kafka.apache.org/documentation/#design), [producer configuration](https://kafka.apache.org/documentation/#producerconfigs), [topic configuration](https://kafka.apache.org/documentation/#topicconfigs) and [monitoring](https://kafka.apache.org/documentation/#monitoring) document partitions, ISR, idempotent producers, transactions, compaction, retention and lag. Kafka-specific mechanisms are in the reference; cluster operation is out of scope here.
- [Confluent Schema Registry: schema evolution](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html) and [fundamentals](https://docs.confluent.io/platform/current/schema-registry/fundamentals/index.html) document subject strategies, compatibility modes and registry architecture. Compatibility semantics are vendor-documented; verify the registry actually deployed.
- [AsyncAPI specification](https://github.com/asyncapi/spec) describes channels, operations and messages across protocols. It documents a contract; it does not enforce delivery or compatibility.
- [CloudEvents specification](https://github.com/cloudevents/spec) defines a vendor-neutral event envelope. It does not define business payload meaning or deduplication scope.
- [Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html), [idempotent consumer](https://microservices.io/patterns/communication-style/idempotent-consumer.html) and [AWS transactional outbox guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html) describe the dual-write problem, duplicate publication and deduplication. They describe patterns, not a guarantee that a selected broker or relay provides them.
- [Debezium outbox event router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) documents one CDC relay implementation. It is an example of the relay boundary, not a required design.
- [What do you mean by "Event-Driven"?](https://martinfowler.com/articles/201701-event-driven.html) separates notification, state transfer, event sourcing and CQRS, and informs the style comparison and coupling warnings.
- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) and [Handling Overload](https://sre.google/sre-book/handling-overload/) inform retry amplification, queue growth, load shedding and recovery load. Apply them through the reliability activity rather than treating them as event-specific rules.
- [AWS Builder Center: Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) informs bounded retry and jitter. It does not justify retrying a non-idempotent effect.

Broker installation, cluster sizing, upgrade procedure and vendor account setup are operations work, not event contract design. No specific broker, schema format or registry is selected by this skill.
