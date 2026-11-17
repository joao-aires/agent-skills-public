# Failure and consistency

Use this reference when choosing a guarantee, explaining a stale or lost result, or reviewing a replication and recovery design. The parent skill owns the reasoning; this file supplies the comparison tables and failure modes.

## Failure models

| Model | Assumes | What still breaks | Design response |
| --- | --- | --- | --- |
| Crash-stop | A failed process stops and stays stopped | Detection delay, in-flight work, lost local state | Durable state, idempotent recovery, failover |
| Crash-recovery | A process may restart with durable state | Partial writes, stale caches, duplicate work | Write-ahead records, recovery protocol, dedupe |
| Pause / GC | A process runs but stops responding for a while | Leases expire, heartbeats miss, duplicated leadership | Fencing tokens, idempotency, generous but bounded liveness |
| Omission | Messages can be lost without notice | Silent gaps, retry ambiguity | Acknowledgments, sequence checks, repair |
| Timing | Messages arrive late, reordered or duplicated | Timeouts, stale ordering, duplicate effects | Deadlines, sequence/version checks, idempotency |
| Network partition | Nodes split into groups that cannot communicate | Split brain, unavailable minority, stale reads | Quorum, fencing, per-operation consistency choice |
| Disk / data loss | Durable media can fail or corrupt | Replica divergence, unrecoverable state | Replication plus backup, checksums, restore drills |
| Zone / region loss | A whole failure domain disappears | Capacity loss, lost unreplicated tail, dependency loss | Multi-zone placement, standby capacity, tested failover |
| Control-plane / operator | Orchestration or a human can be wrong | Mass restart, bad config, accidental deletion | Guardrails, staged rollout, independent restore |

State the model explicitly. A design that assumes crash-stop but experiences process pauses has a different failure mode than the one it was tested for.

## Choose the guarantee from the operation

| Operation | Minimum question | Candidate mechanism | Evidence |
| --- | --- | --- | --- |
| Accept money or inventory change | Can a lost or duplicated effect occur? | Idempotency key, conditional update, ledger, unique constraint | Duplicate and lost-response test |
| Read a value just written by the same user | Must the user see their own write? | Primary read, sticky session, version token | Replica-lag test under failover |
| Enforce unique username/email | Must two writers conflict? | Single owner, unique index, consensus/coordination | Concurrent-writer test |
| List records after an edit | Is bounded staleness acceptable? | Follower read with freshness check | Lag-bound measurement |
| Cross-service order/workflow | Is a visible intermediate state acceptable? | Saga, outbox, compensation | Timeout, retry, compensation-failure test |
| Global sequence or order | Is total order required across keys? | Single partition/owner, consensus, sequencer | Partition and leader-change test |
| Offline or concurrent edits | What merge rule does the user accept? | Version vectors, CRDT, per-key ownership, conflict UI | Concurrent-edit scenarios |
| Restore after corruption | How much data and time can be lost? | Backup/restore, point-in-time recovery | Restore on populated data |

The weakest sufficient guarantee is usually the right default. Record why a stronger guarantee was rejected: coordination cost, availability, latency and operational complexity are legitimate reasons.

## Consistency models

| Model | Guarantee | Typical mechanism | Does not prevent |
| --- | --- | --- | --- |
| Linearizable | Every operation appears to take effect atomically at a point between invocation and response, in real-time order | Consensus, single-node serialization, coordinated quorum reads/writes | Nothing within its assumptions; costs latency and partition availability |
| Sequential | Operations appear in some total order consistent with each client's program order | Single log or leader | Real-time violations across clients |
| Causal | Causally related operations are ordered; concurrent ones may diverge | Version vectors, causal delivery, session tracking | Conflicts between concurrent writes |
| Read-your-writes | A client observes its own completed writes | Primary/sticky routing, version token, read barrier | Other clients' staleness |
| Monotonic reads | A client never observes an older state after a newer one | Sticky replica, session token | Staleness relative to other clients |
| Monotonic writes | A client's writes are applied in its order | Single writer per key, ordered channel | Interleaving with other writers |
| Bounded staleness | Replicas lag by at most a known bound | Lease, freshness check, synchronous standby | Availability when the bound cannot be met |
| Eventual | Replicas converge if writes stop | Asynchronous replication plus repair | Anything about when or what a read sees meanwhile |

"Strong consistency" is not a single guarantee. Ask which anomalies the operation must prevent and which it can tolerate.

## Isolation levels and anomalies

| Anomaly | What happens | Often permitted by | Prevention |
| --- | --- | --- | --- |
| Dirty read | Reads uncommitted data | Read uncommitted | Read committed or stronger |
| Non-repeatable read | Same row changes between reads in one transaction | Read committed | Repeatable read/snapshot, or re-read with version check |
| Phantom | A predicate returns new rows on re-read | Read committed, some snapshot implementations | Serializable or predicate locking |
| Read skew | Different rows read from different points in time | Read committed | Snapshot isolation |
| Lost update | Two read-modify-write operations, one overwrites the other | Read committed; implementation-dependent under snapshot | Conditional update, row lock, atomic increment |
| Write skew | Two transactions read overlapping data, write disjoint rows, break an invariant | Snapshot isolation; some repeatable-read implementations | Serializable, materialized conflict, constraint |
| Serialization anomaly | Concurrent result is not equivalent to any serial order | Weaker-than-serializable levels | Serializable with retry on conflict |

Vendor names are not guarantees. PostgreSQL repeatable read is snapshot isolation; MySQL/InnoDB and Oracle differ in locking and phantom behavior. Verify the actual engine and version, and test the invariant rather than the label.

## CAP and PACELC without slogans

CAP applies during a network partition: a system cannot guarantee both linearizability and availability for every request. It does not say a product is permanently one or the other, and it does not cover latency.

- Choose per operation: a payment write may sacrifice availability, while a product-view read may serve stale data.
- PACELC adds the else branch: without a partition, consistency trades against latency.
- A system can be linearizable for one key range and eventually consistent for another.
- A quorum is not automatically linearizable. Intersecting read and write sets only help if versions are compared, writes are atomic and reads wait for the required responses.
- A "CP" label does not prevent stale follower reads; an "AP" label does not prevent a linearizable compare-and-set on a single key.

## Replication topologies

| Topology | Write path | Read path | Main risk |
| --- | --- | --- | --- |
| Single leader, synchronous | Leader waits for replica acknowledgment | Leader, or followers with lag | Write latency; availability depends on the required replicas |
| Single leader, asynchronous | Leader acknowledges locally | Leader or stale followers | RPO greater than zero on failover |
| Multi-leader | Each region/leader accepts writes | Local leader, then merge | Conflicts, loops, divergent ordering |
| Leaderless quorum | Client writes to W replicas | Client reads from R replicas and compares versions | Sloppy quorums, read repair lag, concurrent-write loss |
| Chain replication | Head accepts, tail acknowledges | Tail for strong reads, others stale | Chain repair and head failover |
| Consensus-replicated log | Leader appends, quorum commits | Leader or lease/read-index path | Quorum latency and minority unavailability |

Replication does not provide backup, audit history or protection from logical corruption. It also does not guarantee that a consumer, cache or derived store converges without its own repair.

## Quorum arithmetic and its limits

`R + W > N` gives overlapping sets, not a proof of linearizability. It assumes:

- each write is atomic on a replica and carries a version;
- the read compares versions and returns the latest;
- failed writes do not partially count;
- sloppy quorums or hinted handoff do not substitute non-overlapping nodes;
- read repair or anti-entropy eventually resolves stale replicas.

Linearizable reads from a quorum system usually still need a read index, a leader lease or a consensus round. Without that, a read can return a value that was never the latest committed one.

## Failover, split brain and fencing

- Detection: heartbeat timeout, lease expiry or an external observer. All are heuristics; false positives cause unnecessary failover, false negatives extend the outage.
- Election: use the coordination system's term/epoch. Two leaders in different terms must not both commit.
- Fencing: issue a monotonically increasing token per leadership term and have the protected resource reject older tokens. This is what stops a paused old leader from writing after a new one starts.
- Leases alone are unsafe under clock skew or long pauses. A lease plus fencing is the usual pattern; a lease without enforcement is a hope.
- Client redirect: DNS, service discovery or a proxy must converge. Cached endpoints and long-lived connections keep sending to the old leader.
- Failback is another failover. Test it with the same rigor, including data direction and conflict handling.

## Time and clocks

| Mechanism | What it gives | Failure mode |
| --- | --- | --- |
| Wall clock | Human-readable time; roughly synchronized by NTP | Skew, jumps, leap seconds, client clocks untrusted |
| Monotonic clock | Elapsed duration on one host | Not comparable across hosts or restarts |
| Lamport clock | Orders events consistently with causality; concurrent events may be ordered arbitrarily | Not real time; ties need a deterministic rule |
| Vector clock | Detects concurrency and causal order | Metadata growth; does not resolve business conflict |
| Hybrid logical clock | Causality close to wall time | Still bounded by clock assumptions |
| Bounded-uncertainty clock | Interval with known error for commit-wait | Specialized infrastructure and operations |

Consequences:

- Last-write-wins by timestamp loses concurrent updates. It is acceptable only where the business accepts that loss.
- Producer timestamps are not commit order and can be wrong or malicious. Use server-assigned offsets, versions or commit order when order matters.
- Timeouts and leases are duration assumptions. Tune them to the runtime's pause behavior, and keep a fencing mechanism for correctness.
- Cross-host log correlation is approximate. Trace and causal identifiers are more reliable than timestamp joins.

## Failure detection and degraded states

- Heartbeat interval and timeout trade detection speed against false positives. GC, CPU starvation and network delay can exceed any fixed timeout.
- Phi-accrual and adaptive detectors reduce false positives but still cannot distinguish slow from dead.
- Liveness, readiness and dependency health answer different questions. A readiness check that fans out to every dependency can take the whole fleet out during a partial outage.
- Gray failure: a component is degraded but its health check passes. Detect it with end-to-end outcomes, differential latency and error rates, not only process liveness.
- Metastable failure: retries, caches or load keep the system in a bad state after the trigger is gone. Recovery needs load shedding and a controlled ramp, not just removing the fault.
- A successful health check is not evidence that the user journey works.

## Multi-region patterns

| Pattern | RPO | RTO | Main cost or risk |
| --- | --- | --- | --- |
| Backup and restore | Hours or more | Hours to days | Cheapest; slow and manual; verify restore |
| Pilot light | Minutes | Tens of minutes to hours | Core data replicated; capacity must be started |
| Warm standby | Seconds to minutes | Minutes | Duplicate capacity; failover automation must be tested |
| Active-passive | Seconds to minutes | Minutes | Idle capacity; DNS/client convergence |
| Active-active, single writer per key | Near zero with synchronous or quorum replication; otherwise the replication lag | Seconds to minutes | Routing/ownership complexity; no write conflicts per key |
| Active-active, multi-writer | Same replication assumption; conflicts are the larger risk | Low | Conflict resolution, loops, data residency, higher cost |

Define RTO/RPO per journey. A database RPO is not the user RPO if a queue, cache or derived store loses its tail. Data residency and deletion obligations apply to replicas and backups, not only the primary region.

## Divergence and repair

- Detect divergence with checksums, counts, per-key versions, sampled reads and business invariants. Absence of errors is not convergence.
- Repair with read repair, anti-entropy (for example Merkle-tree comparison), reconciliation jobs, replay or backfill. Repair operations need idempotency, rate limits and an audit trail.
- Repair can resurrect deleted or unauthorized data if it ignores tombstones, consent state or retention.
- After failover, verify invariants and reconcile unknown outcomes before declaring recovery. A serving system can still have lost or duplicated effects.
- Keep the repair path exercised; an untested repair job is a hypothesis.

## Common anti-patterns

- Retrying every error, at every layer, without a budget or idempotency.
- A timeout with no end-to-end deadline, so the caller gives up while work continues.
- Treating a quorum, a replica count or a vendor label as a consistency proof.
- Using last-write-wins for money, inventory, permissions or anything with concurrent editors.
- Assuming a health check proves the ability to serve.
- Calling replication a backup, or a backup a disaster-recovery plan.
- Active-active without conflict resolution or a tested failover.
- A stale leader with a lease but no fencing.
- Ordering events by client timestamps.
- Unbounded queues presented as backpressure.
- Consensus for data that only needs a single owner, or single-owner writes for data that needs global agreement.
- Testing only clean failures and calling the system resilient.
- Declaring recovery when the process is up but data is divergent or effects are unknown.

## Sources

- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) and [Handling Overload](https://sre.google/sre-book/handling-overload/): overload, retries, queue growth, load shedding and recovery.
- [Google SRE: Managing Critical State](https://sre.google/sre-book/managing-critical-state/): consensus, quorum, leases and critical state.
- [AWS Builder Center: Challenges with distributed systems](https://aws.amazon.com/builders-library/challenges-with-distributed-systems/): partial failure, retries, timeouts and unpredictable latency.
- [AWS Well-Architected Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html): recovery objectives, multi-AZ/multi-region planning and testing.
- [Jepsen analyses](https://jepsen.io/analyses): independent failure testing and documented anomalies under partitions, pauses and clock skew.
- [Raft](https://raft.github.io/): leader election, log replication, membership and safety.
- [Time, Clocks, and the Ordering of Events in a Distributed System](https://lamport.azurewebsites.net/pubs/time-clocks.pdf) and [There is no now](https://queue.acm.org/detail.cfm?id=2745385): logical time, clock skew and timestamp ordering limits.
- [Spanner](https://research.google/pubs/spanner-googles-globally-distributed-database/): bounded-uncertainty clocks and externally consistent transactions.
- [Please stop calling databases CP or AP](https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html): CAP/PACELC interpretation.
- [Circuit Breaker](https://martinfowler.com/bliki/CircuitBreaker.html) and [Saga](https://microservices.io/patterns/data/saga.html): interaction and compensation tradeoffs.
- [FoundationDB](https://www.foundationdb.org/files/fdb-paper.pdf): deterministic simulation for distributed state.

Checked 2026-11-16. Verify the actual engine, version and configuration; documented anomalies and defaults vary.
