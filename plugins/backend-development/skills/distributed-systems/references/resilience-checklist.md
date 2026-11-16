# Resilience checklist

Use this when reviewing a cross-service design, a dependency change or an incident-prone path. It checks whether interaction limits, isolation, recovery and evidence form one coherent design. It does not authorize an experiment; use resilience-testing for execution and its target rules.

## Interaction budget

Fill the budget for one user-relevant operation, then for each hop:

| Question | Answer to record |
| --- | --- |
| What is the caller's total deadline? | A duration derived from the journey, not the sum of defaults. |
| How much remains after each hop? | Remaining budget, including retries and queueing. |
| Which calls are sequential and which are parallel? | Critical path and the effect of one slow branch. |
| What retry allowance fits inside the deadline? | Attempts, backoff and jitter bounded by remaining time. |
| What happens when the budget is exhausted? | A defined error/degraded result, not an indefinite wait. |
| Is the operation safe to repeat? | Idempotency key or a reason repetition is harmless. |

A timeout without a propagated deadline lets the caller abandon work that continues consuming capacity. A deadline without an error contract produces an ambiguous result.

## Retry decision

| Condition | Retry? | Notes |
| --- | --- | --- |
| Connection refused before a request was sent | Yes, bounded | No request reached the remote side; a prior lost response is a separate ambiguity, so still verify idempotency. |
| Timeout after the request may have been processed | Only with idempotency or reconciliation | The outcome is unknown, not failed. |
| Explicit 429/503 with `Retry-After` | Yes, respect the hint and budget | Retrying immediately amplifies overload. |
| Validation, authentication or authorization error | No | Permanent until the input or authority changes. |
| Not found | Usually no | A retry will not create the resource. |
| Conflict / version mismatch | No, re-read or resolve | Retrying the same stale write repeats the conflict. |
| Partial success in a batch | Only per item, with item identity | A whole-batch retry can duplicate successful items. |
| Dependency overload | No immediate retry | Shed, queue with a deadline or fail fast. |

Backoff should be exponential with jitter. A retry budget (ratio of retries to original requests) or token bucket prevents a small failure from doubling or tripling load. Retrying at the client, gateway and service layers multiplies attempts; assign retry ownership to one layer per call path.

Hedging is a read-only, budgeted exception. It increases load and should not be used for writes or when the dependency is already saturated.

## Timeout review

- Connect, read, write and overall timeouts are distinct where the transport supports them; a single value often hides which phase is slow.
- The timeout must be shorter than the caller's deadline, leaving time to serialize an error.
- Queue wait, connection-pool wait and DNS resolution are part of the budget; they are common hidden timeouts.
- Streaming, long-poll and batch operations need their own idle and progress timeouts, not a generic request timeout.
- A cancelled request should stop downstream work where the protocol supports cancellation; otherwise the work continues invisibly.
- Timeout values are configuration with an owner and a reason. A copied default is not a decision.

## Circuit breakers

| Use a breaker when | Avoid or reconsider when |
| --- | --- |
| A dependency fails persistently and fast failure protects the caller and the dependency | The failure is per-request validation or authorization |
| Recovery needs a bounded probe rather than a thundering herd | The breaker is shared so widely that one bad tenant opens it for everyone |
| The caller has a meaningful degraded response | The only response is the same error, and failing fast adds no value |
| The dependency's latency, not only errors, indicates failure | The breaker would hide a partial failure that still needs diagnosis |

Define the failure threshold, minimum volume, open duration, half-open probe count and what counts as success. A breaker without a minimum volume trips on a handful of requests. A half-open probe that sends full production traffic can re-trigger the outage. Breaker state is local and approximate; it does not replace timeouts, retries or load shedding.

## Bulkheads and isolation

- Separate pools, worker queues or concurrency limits per dependency, workload and tenant where one can starve another.
- Reserve capacity for critical journeys and for recovery; a pool sized exactly for steady state has no failover headroom.
- Bound queue length and wait time. An unbounded queue converts overload into latency, memory growth and timeout cascades.
- A bulkhead that is too fine fragments capacity and causes idle pools; size from measured concurrency, not per-endpoint symmetry.
- Tenant isolation may need separate credentials, quotas or deployments where noisy-neighbor or data-boundary risk justifies the cost.

## Backpressure and load shedding

| Mechanism | Use when | Failure mode |
| --- | --- | --- |
| Bounded queue with a deadline | Short bursts, work can wait | Queue age grows silently; work expires before processing |
| Concurrency limit | Protecting a dependency or local resource | Callers wait without a bound unless the wait is also bounded |
| Admission control | The system cannot serve all arrivals sustainably | Rejecting too early harms good traffic; thresholds need evidence |
| Load shedding with 429/503 and `Retry-After` | Overload is real and transient | Clients ignore the hint and retry immediately |
| Priority / tiering | Some journeys must survive degradation | Starvation of lower tiers and unclear product policy |
| Degraded response | A partial result is useful | Consumers treat a degraded result as authoritative |

Backpressure must reach the producer. Pausing a consumer, reducing prefetch or refusing new work is backpressure; buffering in memory is deferral. A queue only absorbs a burst until its drain deadline; estimate drain time from arrival rate minus sustainable service rate, and alert on age rather than depth alone.

## Idempotency and unknown outcomes

- Every consequential request has a stable operation identity and a durable record of outcome.
- The idempotency key has a scope (tenant/user/operation), a lifetime and a conflict rule for reuse with a different payload.
- Conditional writes, unique constraints and state transitions protect against concurrent duplicates; an in-memory set or a short cache does not.
- After a timeout, reconcile through a status endpoint, provider API, ledger or read-back before repeating.
- Record attempts and expose an explicit unknown state; do not map transport failure to business failure.
- External effects without provider idempotency need suppression, deduplication or human reconciliation.
- Compensation is a new distributed operation with its own retries and escalation. It does not restore isolation.

For event consumers, use event-driven-design's inbox, outbox and dedupe-window guidance.

## Recovery review

- What is the detected failure, and who or what initiates recovery? Detection delay is part of RTO.
- Does recovery require a leader election, DNS change, credential rotation or client restart? Test that path, not only the data restore.
- Are caches cold, connection pools empty and rate limits reset? A recovered service can fail again under reconnect load.
- Is there a controlled ramp or admission limit during recovery? A full-traffic restart can reproduce the outage.
- Do queues drain within the promised time, and what happens to work that expires first?
- Are in-flight and unknown outcomes reconciled before declaring success?
- Are temporary controls, feature flags, bypasses and debug settings removed?
- Is the restored data verified against invariants, not only "the process is up"?
- Is failback planned and tested? It is another recovery event with its own data direction.

## Capacity review

- Estimate concurrency as arrival rate × latency (Little's law) and bound in-flight work; do not infer capacity from CPU alone.
- Keep utilization headroom for failover, replay, batch work and recovery. Latency often turns nonlinear before 100% utilization.
- Size connection pools and worker pools across all replicas, jobs and rollout surge, not per process in isolation.
- Identify hot keys, shards, tenants and endpoints; uniform averages hide saturation.
- Estimate queue drain time and replay time; both compete with live traffic.
- Check dependency quotas, cross-zone/region bandwidth and storage growth against the retention and replay plan.
- Separate steady-state capacity from recovery capacity and state which one the design meets.

## Signals that would disprove the design

- Timeout and deadline-exceeded rate by caller and dependency, not only by service.
- Retry rate and retry success ratio; retries that never succeed are load without benefit.
- Breaker open count and duration; half-open failure rate.
- Queue depth, age and drain rate; rejected/shed request rate.
- Pool saturation and wait time; GC pause and runtime stalls.
- Replica lag, leader changes and failover duration.
- Unknown outcomes, reconciliation backlog and duplicate-suppression hits.
- Error-budget burn and user-journey success separate from request success.

A green process metric, a passing health check or a low average latency does not prove the user outcome. Cross-host timestamps are approximate; correlate with trace and causal identifiers. Implement telemetry with observability and set targets with reliability design.

## Test matrix

| Evidence | Supports | Does not support |
| --- | --- | --- |
| Unit/property test of retry, dedupe or state transition | Application logic under modeled conditions | Real network, provider or cluster behavior |
| Deterministic simulation | Protocol invariants, partitions, pauses and recovery sequences | The deployed configuration and dependency behavior |
| Fixture/fake dependency | Error mapping, timeout branches, retry limits | Ambiguous remote commit or real latency |
| Isolated stack with a real dependency | Actual client, persistence and fault mechanism in that stack | Regional or fleet-wide behavior |
| Named non-production deployment | Routing, process lifecycle, collection and recovery interactions | Production scale, shared dependencies and all failure domains |
| Production observation or drill | The exercised conditions at that revision | Untested failures and future behavior |

Test duplicate delivery, lost responses, process pause, dependency outage, queue saturation, rebalance, failover, cold start, restore and repair. Confirm the fault actually took effect; a failed injection is not a successful resilience result. Execute under resilience-testing's authority and stop conditions.

## Common anti-patterns

- Timeouts copied from defaults, with no deadline propagation or owner.
- Retries at every layer, no jitter, no budget and no idempotency.
- A breaker that is either per-request useless or globally catastrophic.
- An unbounded queue described as decoupling.
- Load shedding that returns success or a retryable error for work that was dropped.
- Idempotency implemented as an in-memory set or a cache with a short TTL.
- Mapping a timeout to a permanent failure, or a transport success to a business success.
- Recovery declared from a green health check without reconciling data and unknown effects.
- Capacity sized for steady state with no failover or replay headroom.
- Testing only a clean dependency failure and calling the system resilient.
- Using one global pool, tenant quota or retry policy for workloads with different criticality.

## Sources

- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) and [Handling Overload](https://sre.google/sre-book/handling-overload/): retry amplification, queue growth, load shedding and recovery.
- [SRE Workbook: Managing Load](https://sre.google/workbook/managing-load/) and [Identifying and Recovering from Overload](https://sre.google/workbook/overload/): capacity, admission and recovery from saturation.
- [AWS Builder Center: Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) and [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/): bounded retries and idempotency.
- [AWS Well-Architected Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html): failure isolation, recovery objectives and testing.
- [Circuit Breaker](https://martinfowler.com/bliki/CircuitBreaker.html): breaker states and interaction tradeoffs.
- [Jepsen analyses](https://jepsen.io/analyses): failure behavior observed under real partitions and pauses.

Checked 2026-11-16. Values, thresholds and platform behavior must be verified for the target system; this checklist supplies questions and evidence expectations, not universal numbers.
