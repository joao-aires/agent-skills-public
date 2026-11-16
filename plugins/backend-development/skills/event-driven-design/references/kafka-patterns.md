# Kafka patterns

Use this reference for Kafka-specific mechanisms behind the event contract decisions in the parent skill. It assumes the contract, ownership and failure reasoning are already established. Broker installation, cluster sizing and upgrade procedure belong to operations work.

## Topic and key design

| Topic shape | Use when | Consequence |
| --- | --- | --- |
| Event type per topic | Consumers need one fact stream with independent retention and access | Many topics; schema and ACL per topic; cross-type joins move to consumers. |
| Entity changelog, compacted | Consumers need the latest state per key, or a rebuildable local view | History is lost per key; tombstones and compaction lag need handling. |
| Command topic | One named service must act, with its own authority and reply path | It is not a broadcast fact; multiple consumers would duplicate the command. |
| Retry topic with delay | A transient failure must not block the main partition | Ordering across retries is no longer guaranteed unless keyed and sequenced. |
| Dead-letter topic | Exhausted work needs inspection and repair | Needs an owner, longer retention, reason metadata and a replay route. |

Key decisions:

- Choose the key from the invariant that needs order: account, aggregate, tenant, entity id.
- A null key spreads records across partitions but removes per-entity order. Use it only when order does not matter and spread does.
- A hot key creates a hot partition and a lagging consumer; salting or splitting the key breaks per-key order and needs a reorder strategy.
- Co-partitioned topics need the same partition count and key strategy; verify this before a stream-table join.
- Changing partition count remaps keys. Consumers that cache per-key state or rely on assignment must tolerate the move.

## Durability and acknowledgment

| Setting | Effect | Failure mode when weakened |
| --- | --- | --- |
| `acks=all` | Leader waits for the full in-sync replica set | `acks=1` or `0` can acknowledge data that a leader loss discards. |
| `min.insync.replicas` | Produce fails when the ISR is smaller than the minimum | Too low permits acknowledgment with insufficient copies; too high reduces availability. |
| Replication factor | Number of copies per partition | A factor of one has no broker-failure tolerance. |
| `unclean.leader.election.enable` | Allows an out-of-sync replica to become leader | Enabling it trades durability for availability. |
| Rack awareness | Spreads replicas across zones/racks | Without it, a zone loss can remove all replicas. |

`acks=all` plus an adequate `min.insync.replicas` is the usual durability contract. State the accepted tradeoff when availability during broker loss matters more. A successful produce means the record is in the log, not that any consumer has acted on it.

## Idempotent producer and transactions

The idempotent producer deduplicates retries within a producer session using a producer id and per-partition sequence numbers. It prevents duplicate log entries from retried sends under the configured `acks`; it does not deduplicate across a new producer session, a new application instance or a consumer effect.

A transactional producer extends atomicity across partitions and, with `sendOffsetsToTransaction`, across the consumer's offsets. Consumers using `isolation.level=read_committed` see only committed records and skip aborted ones. This gives read-process-write atomicity inside Kafka, including Kafka Streams `exactly_once_v2`.

Limits to state explicitly:

- The transaction coordinator and `transaction.timeout.ms` bound transaction lifetime; a long transaction holds back read-committed consumers.
- `transactional.id` provides fencing between producer instances; reusing one id from two live instances is an operational error.
- An external database, HTTP endpoint or email provider is outside the transaction. Use an idempotent sink, a provider idempotency key or an outbox plus consumer deduplication.
- A consumer that writes to another store still needs idempotency; `read_committed` does not make its external effect atomic.
- Transactional overhead and abort markers affect latency and storage. Do not enable transactions without a read-process-write requirement that needs them.

## Consumer groups, offsets and rebalance

- One partition is assigned to one consumer in a group. Group parallelism is capped by partition count.
- Commit offsets after the durable effect for at-least-once; before processing for at-most-once. Auto-commit can commit work that has not completed.
- A commit records position, not completion. Track business completion separately when the effect is asynchronous.
- `max.poll.interval.ms` bounds time between polls. Long processing triggers rebalance and duplicate work; reduce batch size, pause partitions or move slow work to another stage.
- Rebalances stop or shift consumption. Cooperative assignment and static membership reduce churn but do not eliminate it.
- A consumer that cannot keep up shows lag, not an error. Lag in records is misleading when record size or processing cost varies; estimate time lag from recent throughput.
- Where the target version supports share groups, they trade partition ownership for record-level sharing with different ordering and redelivery semantics. Verify that version's documentation before relying on them.
- Separate consumer groups per logical consumer. Two different services sharing a group steal partitions from each other.

## Retention, compaction and replay

| Control | What it does | Design consequence |
| --- | --- | --- |
| `retention.ms`, `retention.bytes` | Deletes whole segments after the limit | Replay is bounded by the shortest relevant retention; deletion is not per record. |
| `cleanup.policy=compact` | Keeps the latest value per key | History is gone; consumers must handle tombstones and compaction lag. |
| `delete.retention.ms` | Retains tombstones before removal | Too short can resurrect deleted keys in a rebuilt store. |
| Tiered storage | Moves older segments to remote storage where supported | Extends replay and lowers local disk cost; changes read latency and operational dependencies. |
| `max.message.bytes` | Bounds record size | Large payloads belong in object storage with a reference, not in the event. |

Replay by resetting offsets or starting a new group within retention. Replaying old events requires current deserializers to read every retained schema version, and replaying side effects must be suppressed or routed to a non-effect sink. Compacted topics cannot rebuild a history of changes; they rebuild the latest state only.

## Schema Registry

Decide the subject strategy before the first incompatible change:

| Strategy | Subject identity | Use when |
| --- | --- | --- |
| Topic name | `<topic>-key` / `<topic>-value` | A topic carries one record type; the common default. |
| Record name | Fully qualified record name | The same type appears across topics and should share a schema. |
| Topic record name | Topic plus record name | A topic carries several record types that need separate evolution. |

Compatibility modes:

| Mode | New schema can read | Old schema can read | Typical rollout |
| --- | --- | --- | --- |
| Backward | Data written with the previous schema | No | Upgrade consumers first, then producers. |
| Forward | No | Data written with the new schema | Upgrade producers first, then consumers. |
| Full | Previous data | New data | Either order, with tighter change limits. |
| Transitive variants | All previous versions, not only the last | All previous versions | Long-lived retained history and replay. |
| None | Not checked | Not checked | Only with an explicit, time-bounded exception. |

The registry stores schema IDs in the record wire format; consumers fetch and cache schemas. A registry outage should not stop an already-cached consumer, but a cold start or a new schema can fail. Treat the registry as a production dependency with availability and access control, and check compatibility in CI rather than relying on a failed production publish.

Schema compatibility does not cover semantics. Renaming an enum member, changing a unit, changing a default, or changing the meaning of an optional field can pass the registry and still break consumers. Test recorded events in both directions.

## Multi-region

- Asynchronous replication (MirrorMaker 2, cluster linking or a comparable mechanism) has a nonzero RPO. A regional failure can lose the tail that was not replicated.
- Replicated offsets and consumer-group state are separate from replicated records. Verify offset translation and group failover rather than assuming consumers resume at the same logical point.
- Active-active writes need per-key ownership or conflict resolution; Kafka does not merge conflicting records. Loop prevention and topic naming must be explicit.
- Cross-region replication consumes bandwidth and adds lag. Alert on replication lag in time, not only record count.
- Failover changes producer endpoints and may require DNS or client reconfiguration. Test the client path, not only broker replication.
- A replicated topic is not a backup against logical corruption or accidental deletion. Keep a separate restore path where the data matters.

## Retry and dead-letter patterns

| Pattern | Preserves partition progress | Preserves per-key order | Cost |
| --- | --- | --- | --- |
| Retry in place with pause/backoff | No, blocks the partition | Yes | Head-of-line blocking and lag for unrelated keys. |
| Retry topic with delay | Yes | Only with keyed sequencing and ordered consumption | More topics, delayed visibility and duplicate risk. |
| Park the key / quarantine | Yes for other keys | Yes for the parked key until repair | Needs an owner and a repair workflow. |
| Immediate dead-letter | Yes | No | Loses automatic recovery; needs triage and replay. |

Record original topic, partition, offset, key, headers, exception class, attempt count and first/last failure time in the dead-letter record. Alert on age and growth, not only count. Replay must be authorized, rate-limited and idempotent; blind replay of a poison record repeats the failure.

## Signals and capacity

Useful broker and client signals:

- Consumer lag in records and estimated time, per group, topic and partition; assigned and paused partitions.
- Rebalance rate and duration; poll idle ratio; commit latency and failures.
- Produce error rate, retry rate, request latency and buffer exhaustion.
- Under-replicated and offline partitions, ISR shrink/expand, active controller count.
- Disk, network, request-handler idle and quota throttling.
- End-to-end event age from production timestamp to durable consumption, not only broker lag.
- Dead-letter and retry-topic age; outbox backlog; schema rejection and deserialization failure.

Capacity estimate: `bytes/sec × retention × replication factor`, plus segment indexes, transaction state, metadata and any remote tier. Add headroom for replay, consumer catch-up and broker loss. Partition count drives controller metadata, rebalance cost and per-partition overhead; very high counts are an operational commitment. Consumer throughput per partition and key skew usually bound performance before raw broker throughput.

## Common anti-patterns

- One topic for unrelated event types, with consumers filtering by type.
- Null keys where per-entity order is required.
- Increasing partitions to fix lag without rechecking key mapping, state locality and ordering.
- Committing offsets before the business effect, then calling the pipeline reliable.
- Claiming exactly-once while writing to an external system without idempotency.
- Unbounded in-place retries that block a partition for hours.
- Treating a compacted topic as a database or an audit log.
- Replay without suppressing emails, payments or other external effects.
- Sharing a consumer group between different services.
- Auto-resetting to earliest on a production consumer and calling the resulting reprocessing a replay plan.
- Using Kafka for synchronous request/response and then adding timeouts to hide the mismatch.
- Setting short retention and discovering the replay requirement during an incident.

## Sources

- [Apache Kafka design](https://kafka.apache.org/documentation/#design): partitions, ordering, replication, producer idempotence, transactions, compaction and consumer position.
- [Kafka producer configuration](https://kafka.apache.org/documentation/#producerconfigs) and [topic configuration](https://kafka.apache.org/documentation/#topicconfigs): acknowledgment, idempotence, transaction, retention and compaction settings.
- [Kafka monitoring](https://kafka.apache.org/documentation/#monitoring): broker, producer and consumer metrics.
- [KIP-98](https://cwiki.apache.org/confluence/display/KAFKA/KIP-98+-+Exactly+Once+Delivery+and+Transactional+Messaging) and [KIP-890](https://cwiki.apache.org/confluence/x/B40ODg): transactional delivery and server-side defense.
- [KIP-405](https://cwiki.apache.org/confluence/display/KAFKA/KIP-405%3A+Kafka+Tiered+Storage): tiered storage.
- [KIP-848](https://cwiki.apache.org/confluence/display/KAFKA/KIP-848%3A+The+Next+Generation+of+the+Consumer+Rebalance+Protocol): consumer rebalance protocol.
- [Confluent Schema Registry](https://docs.confluent.io/platform/current/schema-registry/fundamentals/index.html) and [schema evolution](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html): subjects, compatibility modes and registry behavior.

Verify the deployed broker, client and registry versions. Version-specific features, defaults and limits change, and a documented feature is not evidence that the target cluster has it enabled.
