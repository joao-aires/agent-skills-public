---
name: distributed-systems
description: Reason about cross-service consistency, replication, partitioning, consensus, time, failure detection, retries, timeouts, circuit breakers, idempotency, ambiguous outcomes, multi-region recovery and capacity. Use when a design or incident depends on behavior across process, network or region boundaries; architecture decisions, service contracts, fault experiments and telemetry stay with their owning activities.
user-invocable: true
metadata:
  kind: method
  domain: backend
  phase: design
  scope: generic
  invocation: both
---

# Reason about behavior across failure boundaries

Distributed-systems reasoning is about what remains true when a process pauses, a network path partitions, a clock jumps or a region disappears. It does not choose an architecture by itself, and it is not a catalog of patterns to apply. Its job is to make a design or diagnosis honest about the guarantee, the failure model and the evidence.

Use it alongside the activities that own the surrounding decisions:

| Owner | Owns |
| --- | --- |
| `design-system` | Architecture choices, service/data/client/deployment boundaries, option comparison and the design record. |
| `backend-design` | Service behavior, authority, state, transactions, interface contracts and recovery inside the selected boundaries. |
| `testing-resilience` (when available) | Controlled fault experiments, their authorization, injection, stop conditions and evidence. |
| `design-system` observability guidance (when available) | Signal contracts, pipeline behavior and telemetry evidence. Instrumentation stays with the stack's telemetry tooling. Reliability design owns SLIs, SLOs and alert policy. |
| This skill | The cross-service reasoning those owners consume: consistency, replication, partitioning, consensus, time, failure detection, bounded interaction, idempotency, recovery, capacity and how to test the reasoning. |

Event and message contract design belongs to event-driven-design; broker mechanics are not repeated here. Read [failure and consistency](references/failure-and-consistency.md) when selecting a guarantee or diagnosing divergence, and [resilience checklist](references/resilience-checklist.md) when reviewing retries, timeouts, breakers, backpressure and recovery.

## Name the failure model and the promise

Every design assumes something about failures. State it before claiming a guarantee:

- Crash-stop, crash-recovery, pause/GC, omission, message delay, reorder, duplication, network partition, disk loss, zone or region loss, control-plane failure and operator error.
- Asynchrony: a timeout cannot distinguish a slow process from a dead one. It is a decision about how long to wait, not a fact about the other side.
- Byzantine faults only where an adversarial or compromised component is in scope. Most business systems assume non-Byzantine components but still validate input, identity and authority.
- Partial failure is normal: one dependency, shard or tenant can fail while the rest works, and the caller may not know which.

Translate the promise into operation terms: which operations survive which failure, what may be lost, how stale a read may be, what a caller sees during a partition, and how recovery is detected. "Highly available" and "strongly consistent" are not promises; a specific operation under a specific failure is.

Do not treat a component's own claim as the system guarantee. Replication, retries and failover compose into a different promise than any single part advertises.

## Choose consistency per operation

Consistency is a property of an operation and its observed history, not a database brand. Identify the reads and writes that need a guarantee and leave the rest deliberately weaker.

| Promise | Prevents | Typical mechanism | Cost or limit |
| --- | --- | --- | --- |
| Linearizable | Stale reads, split-brain writes, non-atomic visibility | Consensus or single-node serialization, quorum with read/write coordination | Latency, minority unavailability, coordination |
| Sequential | Real-time violations across clients | Single leader, serialized log | Requires ordering authority |
| Causal | Effects observed before their causes | Causal consistency, version vectors, session tracking | Metadata and conflict handling |
| Read-your-writes | A client missing its own update | Primary read, sticky session, version token | Routing complexity, load concentration |
| Monotonic reads | Going backward in time across replicas | Sticky replica or version check | Session state |
| Bounded staleness | Unbounded lag | Replica freshness check, lease | Availability when the bound cannot be met |
| Eventual | Permanent divergence after writes stop | Asynchronous replication plus convergence and repair | No bound on what a read sees meanwhile |

CAP is a partition-time choice, and PACELC adds the normal-operation latency/consistency tradeoff. Neither names a product's behavior. A "CP" database can still serve stale reads from a follower if the read path allows it, and an "AP" store can offer linearizable operations on some keys. Verify the actual read and write path.

Transactions are part of the same decision. Know the isolation level and its anomalies: read committed permits non-repeatable reads and lost updates; snapshot isolation permits write skew; serializable costs contention, retries and abort handling. Constraints and conditional writes often protect an invariant more cheaply than a broad serializable transaction. Eventual consistency needs a convergence mechanism, a repair path and a bound or user-visible staleness, or it is only a hope.

## Replication, partitioning and consensus

Replication decisions:

- Single leader with synchronous replication acknowledges after replicas but pays write latency and can lose availability when the quorum is unavailable. Asynchronous replication is faster and has a nonzero RPO on failover.
- Multi-leader and leaderless designs accept concurrent writes and need conflict resolution. "Last write wins" is a data-loss policy, not a merge strategy.
- Reads from followers create staleness; read-your-writes needs routing, a session token or a read barrier.
- Failover needs detection, election, fencing and a client redirect. A stale leader that continues to accept writes is data corruption, not a latency issue.
- Replication is not backup. It replicates deletion, corruption and operator error; a separate restore path is still required.

Partitioning decisions:

- Key by access, ownership and ordering needs. Hash keys spread load; range keys preserve locality and scans; tenant keys simplify isolation but concentrate hot tenants.
- Cross-partition transactions, joins and global uniqueness become application-level work or require coordination. Budget for that rather than discovering it after the split.
- A hot key or hot tenant defeats uniform sharding. Salting spreads writes but breaks per-key order and complicates reads.
- Resharding is a migration: dual read/write, backfill, cutover, rollback and ordering during the transition. Partition count is a long-lived commitment.

Consensus decisions:

- Consensus provides agreed ordering, leader election, atomic membership and linearizable compare-and-set within a group. It is not a general-purpose consistency layer for application data.
- A minority partition cannot make progress. Cross-region consensus pays wide-area round trips and couples availability to the quorum.
- Use a proven implementation such as etcd, ZooKeeper, Consul or a maintained Raft library. Implementing consensus is a research and operations project, not a feature task.
- Membership changes, snapshots, log growth and witness/arbiter placement are operational concerns with failure modes of their own.
- Leases are time assumptions. Pair leadership with a monotonically increasing fencing token that storage checks, so a paused leader cannot commit after its lease expires.

## Treat time and failure detection as heuristics

There is no global now. Wall clocks jump, skew and disagree; monotonic clocks measure elapsed time on one host only. Ordering events by timestamp silently discards concurrent updates, and a producer timestamp is not commit order.

- Use per-key versions, conditional writes or the datastore's commit order when order matters. Logical clocks and version vectors detect concurrency; they do not decide business conflict by themselves.
- Bounded-uncertainty clocks are an infrastructure commitment with specialized hardware and operations, not a default assumption.
- Keep causation and correlation identifiers for diagnosis and trace reconstruction. They are not a total order.
- Failure detection is a tradeoff between false positives and detection delay. GC pauses, CPU starvation and network delay look like failure. Health checks can pass while the service is wrong, and a dependency ping does not prove the ability to serve.
- Timeouts are budgeted across hops. A downstream timeout must leave the caller time to respond, and a retry after timeout may duplicate an effect.
- Fencing must be enforced by the resource being protected, not only by the client. A token in a request that storage ignores provides no protection.

## Bound interaction and load

Every remote interaction needs a deadline, a retry policy and a capacity limit. These are one design, not independent knobs.

- Propagate deadlines end to end. Separate connect, read and overall deadlines where the transport supports it; the caller's remaining budget bounds the callee's work.
- Retry only transient, retry-safe operations, with bounded attempts, exponential backoff and jitter. A retry budget prevents retries from becoming the dominant load. Retrying at several layers multiplies attempts and hides the real failure.
- Circuit breakers fail fast when a dependency is failing and allow a bounded probe to recover. Keep them per dependency, instance or tenant as the failure domain requires. A breaker that is shared too broadly turns one slow dependency into a global outage; one that is too local never trips.
- Bulkheads isolate pools, queues, threads and tenants so one workload cannot consume all capacity. Reserve headroom for failover and recovery.
- Backpressure is explicit: bounded queues, admission control, load shedding, priority and degradation. Queueing near saturation turns latency nonlinear, and a queue only hides overload until its drain deadline. Bound in-flight work with a concurrency limit, not hope.
- Hedging is only for idempotent reads with a strict budget; it adds load and can amplify an incident.
- Plan recovery load: restarts, cold caches, reconnects, retry synchronization and replay can exceed steady-state traffic. Add jitter, ramp admission and keep a degraded mode.

## Make effects idempotent and unknown outcomes explicit

Every consequential operation crossing a process boundary needs a stable identity and a durable outcome record.

- Use an idempotency key with a defined scope, lifetime and tenant. Reusing a key with a different payload is a conflict, not a retry.
- At-least-once delivery plus an idempotent effect is the practical default. Exactly-once requires the effect and the progress record to commit atomically; across systems that requires cooperation from the sink, provider or protocol.
- After a timeout, the outcome is unknown. Reconcile with a status lookup, provider API, ledger or read-back before repeating. Record attempts and expose unknown outcomes instead of guessing.
- Prefer conditional writes, unique constraints and state transitions over read-then-write.
- External effects without idempotency (email, SMS, shipment, model calls with cost) need suppression, deduplication or human-visible reconciliation.
- Sagas compensate rather than roll back, and they do not provide isolation: intermediate states are visible. Two-phase commit blocks on coordinator failure and couples participant availability; use it only where participants support it and the cost is accepted.
- A compensation that can fail is another distributed operation. Give it its own retry, idempotency and escalation path.

## Multi-region and recovery

Decide the unit of ownership: a single-writer home region per key or tenant, active-passive, or multi-writer. Multi-writer needs conflict resolution — ownership, version vectors, CRDTs or an accepted loss policy — and a story for concurrent edits. "Active-active" without that story is a deployment diagram, not a guarantee.

- Cross-region writes and consensus pay round-trip latency. Read-local/write-global is a common compromise; read-your-writes then needs session stickiness or a version check.
- Region loss is both a capacity event and a possible data-loss event. Define RTO and RPO per journey, not per database.
- Failover must cover DNS/TTL, credentials, quotas, capacity in the standby, dependency endpoints and client reconnection. Test failover and failback; an untested standby is a hypothesis.
- Backups and restore are separate from replication. Verify restore on populated data and measure restore time, not only backup completion.
- Data residency, deletion and consent requirements constrain where replicas and backups may live and how replay behaves.
- Repair divergence with reconciliation, anti-entropy, replay or backfill, and verify invariants after recovery. Replication does not guarantee convergence after a logical bug or a partial write.

## Capacity and diagnosis

Measure arrival rate, latency distribution, saturation and errors per dependency, partition and tenant. Utilization above roughly 70–80% often makes latency nonlinear, and tail latency is what users experience. Little's law relates concurrency, arrival rate and latency; use it to bound in-flight work and drain time, not to justify unbounded queues.

Watch for hot keys and shards, connection and thread pools, queue age, GC pauses, cross-zone bandwidth and cost, and dependency rate limits. Recovery and replay are capacity events. A system that survives steady state can still fail when every worker reconnects, every cache is cold or a backlog drains at once.

Each claimed guarantee needs a signal that would disprove it: replica lag and leader changes for replication, conflict rate for multi-writer, retry and timeout rates for interaction bounds, queue age for backpressure, unknown outcomes and divergence checks for idempotency and repair, failover duration for recovery. Cross-host correlation is approximate because clocks disagree; correlate with trace and causal identifiers. Implement signals with the stack's telemetry tooling and define targets with reliability design.

## Test the reasoning, not only the code

Distinguish four evidence levels: a model, a deterministic simulation, an isolated experiment and a production observation. Each supports a different claim.

- Model the protocol or state machine and check invariants and impossible transitions before building it.
- Use deterministic simulation or model-based tests for concurrency, partitions, clock skew and crash recovery where the protocol is the risk. FoundationDB-style simulation is an example, not a requirement for every service.
- Use property-based and linearizability checks where the guarantee is the question; they find counterexamples, not proofs of production behavior.
- Inject faults at real boundaries: dropped connections, delayed responses, process pauses, partial writes, broker loss, region failover. A raised exception is not the same as a connection dropped after a remote commit.
- Test ambiguous outcomes, duplicate delivery, rebalance, failover, restore and repair, not only clean failure.
- Treat a passing suite as evidence for the exercised conditions, not for all failures.

Use testing-resilience to design and execute controlled experiments, and its authority rules for any shared or non-production target. Testing that only exercises a mocked dependency establishes application handling, not distributed behavior.

## Decide and record

| Requirement | Candidate approach | What it costs | Evidence to require |
| --- | --- | --- | --- |
| Never lose an accepted write | Durable quorum or synchronous replica acknowledgment, single owner | Write latency, minority unavailability | Failover test, measured RPO, fencing test |
| Read your own writes | Primary read, sticky session or version token | Routing complexity, load concentration | Replica-lag and failover test |
| Global uniqueness or ordering | Single owner, consensus or coordination service | Latency, availability, operational dependency | Partition and leader-change test |
| Cross-service business transaction | Saga plus outbox and idempotent consumers | Visible intermediate states, compensation failure | Duplicate, timeout and reconciliation test |
| Concurrent or offline edits | Per-key ownership, version vectors, CRDT or conflict UI | Complexity, user-visible conflict | Concurrent-edit and merge scenarios |
| Region-loss tolerance | Backup/restore, pilot light, warm standby or active-active | Cost, conflict, failover complexity | Failover and failback drill with data checks |
| Unknown remote outcome | Idempotency key plus status/reconciliation | Extra state and latency | Lost-response and repeated-request test |

Recommend the weakest guarantee that satisfies the journey. Record the rejected stronger and weaker options, the failure behavior, the cost and the evidence that would reopen the decision. A named pattern, a vendor claim or a benchmark does not establish the guarantee for this system.

Design-only reasoning ends with the decision and the evidence needs; implementation, fault injection and telemetry remain within their owning activities and the requested scope.

## Sources and fit

- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) and [Handling Overload](https://sre.google/sre-book/handling-overload/) inform retry amplification, queue growth, load shedding, resource exhaustion and recovery. They are operational guidance, not a consistency model.
- [Google SRE: Managing Critical State](https://sre.google/sre-book/managing-critical-state/) informs consensus, quorum and critical-state operations. The [SRE Workbook: Managing Load](https://sre.google/workbook/managing-load/) and [Non-Abstract Large System Design](https://sre.google/workbook/non-abstract-design/) inform capacity and end-to-end design reasoning.
- [AWS Builder Center: Challenges with distributed systems](https://aws.amazon.com/builders-library/challenges-with-distributed-systems/), [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) and [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) inform partial failure, bounded interaction and idempotency. They describe Amazon's practice, not a universal default.
- [AWS Well-Architected Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) informs recovery objectives, multi-AZ/multi-region planning and failover testing. Verify the selected services actually provide the stated behavior.
- [Jepsen analyses](https://jepsen.io/analyses) provide independent failure testing of databases, queues and coordination services. They demonstrate that documented guarantees can fail under partitions, clock skew and process pauses; they do not certify a system you have not tested.
- [Raft](https://raft.github.io/) and the [Raft paper](https://raft.github.io/raft.pdf) document one consensus protocol and its membership and safety rules. Use a maintained implementation rather than deriving requirements from the paper alone.
- [Time, Clocks, and the Ordering of Events in a Distributed System](https://lamport.azurewebsites.net/pubs/time-clocks.pdf) and [There is no now](https://queue.acm.org/detail.cfm?id=2745385) inform logical time, clock skew and the limits of timestamp ordering.
- [Spanner: Google's Globally-Distributed Database](https://research.google/pubs/spanner-googles-globally-distributed-database/) documents bounded-uncertainty clocks and externally consistent transactions. It is a specialized infrastructure commitment, not a pattern to imitate cheaply.
- [Circuit Breaker](https://martinfowler.com/bliki/CircuitBreaker.html) and [Saga](https://microservices.io/patterns/data/saga.html) describe interaction and compensation patterns and their tradeoffs. They do not establish that a given implementation is correct under failure.
- [Please stop calling databases CP or AP](https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html) informs the CAP/PACELC discussion and the warning against product labels.
- [FoundationDB](https://www.foundationdb.org/files/fdb-paper.pdf) documents deterministic simulation as a testing strategy for distributed state. It is evidence for that method, not a claim that every service needs it.

Checked 2026-11-16. Verify the deployed versions, configuration and platform behavior; a cited mechanism is not evidence that the target system has it enabled.
