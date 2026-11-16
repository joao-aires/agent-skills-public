# Kafka patterns

Use this reference for Kafka-specific mechanisms behind the event contract decisions in the parent skill. It assumes the contract, ownership and failure reasoning are already established; broker installation, cluster sizing and upgrade procedure belong to operations work. Setting names appear only where they change a design decision or prevent a false guarantee. Exact defaults, ranges and version behavior belong to the [producer](https://kafka.apache.org/documentation/#producerconfigs), [consumer](https://kafka.apache.org/documentation/#consumerconfigs) and [topic](https://kafka.apache.org/documentation/#topicconfigs) configuration and [design](https://kafka.apache.org/documentation/#design) documentation.

## Topic and key design

| Topic shape | Use when | Consequence |
| --- | --- | --- |
| Event type per topic | Consumers need one fact stream with independent retention and access | Many topics; schema and ACL per topic; cross-type joins move to consumers. |
| Entity changelog, compacted | Consumers need the latest state per key, or a rebuildable local view | History is lost per key; tombstones and compaction lag need handling. |
| Command topic | One named service must act, with its own authority and reply path | It is not a broadcast fact; multiple consumers would duplicate the command. |
| Dead-letter topic | Exhausted work needs inspection and repair | Needs an owner, longer retention, reason metadata and a replay route. |

Key decisions:

- Choose the key from the invariant that needs order: account, aggregate, tenant, entity id.
- A null key spreads records across partitions but removes per-entity order. Use it only when order does not matter and spread does.
- A hot key creates a hot partition and a lagging consumer; salting or splitting the key breaks per-key order and needs a reorder strategy.
- Co-partitioned topics need the same partition count and key strategy; a later partition-count change remaps keys, so cached per-key state and assignment assumptions must tolerate the move.

## Delivery boundaries

- Acknowledgment strength is a durability decision. Acknowledging before the full in-sync set can lose records when the leader fails; `acks=all` with an adequate `min.insync.replicas` is the usual contract. Relax it only with a stated availability-for-durability tradeoff.
- Replication factor is failure tolerance. Rack or zone spread is what prevents one zone loss from removing every replica; verify the cluster's actual placement, not only the topic's intended setting.
- A successful produce means the record is in the log, not that a consumer processed it or a derived store is current. A consumer commit records position, not business completion; track completion separately when the effect is asynchronous.

## Idempotency and transactions

The idempotent producer deduplicates retries within one producer session using a producer id and per-partition sequence numbers. It prevents duplicate log entries from retried sends; it does not deduplicate across a new producer session, a new application instance or a consumer effect.

A transactional producer extends atomicity across partitions and, with offset sending, across the consumer's committed position. Consumers reading committed data skip aborted records, which gives read-process-write atomicity inside Kafka. Transactional overhead and abort markers affect latency and storage, so enable transactions only for a read-process-write requirement that needs them. Limits to state explicitly:

- The coordinator and transaction timeout bound lifetime, so a long transaction holds back committed-read consumers. The transactional id fences producer instances; reusing one id from two live instances is an operational error.
- An external database, HTTP endpoint or email provider is outside the transaction. Use an idempotent sink, a provider idempotency key or an outbox plus consumer deduplication; reading committed data does not make a consumer's external write atomic.

An outbox relay targeting Kafka needs a stable ordering key, a publish path that preserves per-aggregate order, and a sent mark written only after broker acknowledgment. Duplicates remain part of the contract.

## Consumer groups, offsets and rebalance

- One partition is assigned to one consumer in a group. Group parallelism is capped by partition count.
- Commit offsets after the durable effect for at-least-once; before processing for at-most-once. Auto-commit can commit work that has not completed.
- Long processing between polls triggers a rebalance and duplicate work; cooperative assignment and static membership reduce churn but do not eliminate it. Reduce batch size, pause partitions or move slow work to another stage rather than only raising the liveness bound.
- A consumer that cannot keep up shows lag, not an error. Lag in records is misleading when record size or processing cost varies; estimate time lag from recent throughput.
- Separate consumer groups per logical consumer. Two different services sharing a group steal partitions from each other.

## Retention, compaction and replay

- Retention deletes whole segments after the limit, so replay is bounded by the shortest relevant retention; deletion is not per record. Tiered storage can extend replay where supported, at the cost of read latency and another operational dependency.
- Compaction keeps the latest value per key and removes history. Consumers must handle tombstones, and tombstone retention must outlive any store that could rebuild from the topic.
- Record size limits are a design boundary. Large payloads belong in object storage with a reference in the event.
- Replay by resetting offsets or starting a new group within retention. Current deserializers must read every retained schema version, and replaying side effects must be suppressed or routed to a non-effect sink. A compacted topic rebuilds the latest state only, not a history of changes.

## Schema evolution

Decide the subject strategy before the first incompatible change. Topic-name subjects suit one record type per topic; record-name subjects share a schema across topics; topic-record subjects separate several types within a topic. The registry documentation owns naming details and API behavior.

| Compatibility | Guarantee | Rollout order |
| --- | --- | --- |
| Backward | New readers can read data written with the previous schema | Upgrade consumers first, then producers. |
| Forward | Old readers can read data written with the new schema | Upgrade producers first, then consumers. |
| Full | Both directions, with tighter change limits | Either order. |
| Transitive | All previous versions, not only the last | Required for long retained history and replay. |

The registry stores schema ids in the record wire format; consumers fetch and cache schemas. A registry outage should not stop an already-cached consumer, but a cold start or a new schema can fail. Treat the registry as a production dependency with availability and access control, and check compatibility in CI rather than relying on a failed production publish.

Compatibility does not cover semantics. Renaming an enum member, changing a unit, changing a default or changing the meaning of an optional field can pass the registry and still break consumers. Test recorded events in both directions.

## Replication and failover

- Asynchronous replication has a nonzero RPO. A regional failure can lose the tail that was not replicated.
- Replicated offsets and consumer-group state are separate from replicated records. Verify offset translation and group failover rather than assuming consumers resume at the same logical point.
- Active-active writes need per-key ownership or conflict resolution; Kafka does not merge conflicting records. Loop prevention and topic naming must be explicit.
- Failover changes producer endpoints and may require client reconfiguration. Test that path, and keep a separate restore path: a replicated topic is not a backup against logical corruption or deletion.

## Retry and dead-letter patterns

| Pattern | Preserves partition progress | Preserves per-key order | Cost |
| --- | --- | --- | --- |
| Retry in place with pause/backoff | No, blocks the partition | Yes | Head-of-line blocking and lag for unrelated keys. |
| Retry topic with delay | Yes | Only with keyed sequencing and ordered consumption | More topics, delayed visibility and duplicate risk. |
| Park the key / quarantine | Yes for other keys | Yes for the parked key until repair | Needs an owner and a repair workflow. |
| Immediate dead-letter | Yes | No | Loses automatic recovery; needs triage and replay. |

Record original topic, partition, offset, key, headers, exception class, attempt count and first/last failure time in the dead-letter record. Alert on age and growth, not only count. Replay must be authorized, rate-limited and idempotent; blind replay of a poison record repeats the failure.

## Signals and capacity

- Consumer lag in records and estimated time, per group, topic and partition, plus end-to-end event age from production timestamp to durable consumption; assigned and paused partitions.
- Rebalance rate and duration; poll idle ratio; commit latency and failures; produce error rate and buffer exhaustion.
- Under-replicated and offline partitions, ISR shrink/expand, active controller count.
- Dead-letter and retry-topic age; outbox backlog; schema rejection and deserialization failure.

Capacity estimate: `bytes/sec × retention × replication factor`, plus segment indexes, transaction state, metadata and any remote tier. Add headroom for replay, consumer catch-up and broker loss. Partition count drives controller metadata, rebalance cost and per-partition overhead; very high counts are an operational commitment. Consumer throughput per partition and key skew usually bound performance before raw broker throughput.

## Common anti-patterns

- One topic for unrelated event types, with consumers filtering by type.
- Committing offsets before the business effect, then calling the pipeline reliable.
- Claiming exactly-once while writing to an external system without idempotency.
- Unbounded in-place retries that block a partition for hours.
- Replay without suppressing emails, payments or other external effects.
- Sharing a consumer group between different services.

## Sources

- Apache Kafka, [producer](https://kafka.apache.org/documentation/#producerconfigs), [consumer](https://kafka.apache.org/documentation/#consumerconfigs) and [topic](https://kafka.apache.org/documentation/#topicconfigs) configuration, [design](https://kafka.apache.org/documentation/#design) and [message delivery semantics](https://kafka.apache.org/documentation/#semantics).
- Apache Kafka, [transaction protocol](https://kafka.apache.org/documentation/#transaction_protocol) and [monitoring](https://kafka.apache.org/documentation/#monitoring).
- Confluent Schema Registry, [fundamentals](https://docs.confluent.io/platform/current/schema-registry/fundamentals/index.html) and [schema evolution](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html).

Verify the deployed broker, client and registry versions. Version-specific features, defaults and limits change, and a documented feature is not evidence that the target cluster has it enabled.
