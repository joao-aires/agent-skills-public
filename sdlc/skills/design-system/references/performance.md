# Performance design

Performance design turns an accepted response-time or throughput target into a system shape: where time is spent, what happens at the tail, how much capacity is needed and what degrades first. The target belongs to requirements. The design owns the budget, the mechanism and the evidence plan.

A performance claim is only as good as the workload, population and environment behind it. State those before treating a measurement as evidence.

## Frame the claim

Establish:

- the user-visible operation or journey, and where it starts and ends for the user;
- the environment, deployment topology, data volume and cache state;
- the arrival pattern and expected concurrency, including peaks and bursts;
- the relevant percentile and time window, and whether the target covers reads, writes or both;
- which parts must remain true under load: correctness, authority, ordering, freshness.

Server response time and user-perceived latency are different claims. Rendering, network, client processing and third-party scripts can dominate a journey even when the service is fast, and a fast service can still produce a slow journey through retries, redirects or queueing. Choose the observation point that matches the target.

## Budget the journey

Allocate the accepted end-to-end target across the stages that consume it:

| Stage | What the design controls |
| --- | --- |
| Client | Payload size, render-blocking work, connection reuse, caching policy. |
| Network and edge | Round trips, TLS and redirects, CDN placement, compression. |
| Service | Query count, serialization, authentication checks, synchronous work. |
| Dependencies | Fan-out, timeouts, retry policy, circuit breaking, provider latency. |
| Asynchronous completion | Queue wait, worker concurrency, deadline and reconciliation. |

Add the stages that run in sequence; do not add concurrent work as if it were serial. Budget the safety margin explicitly: retries, timeouts and failover paths consume the same target. A design that spends the entire budget on the happy path has no room for a retry.

Where the design cannot fit the budget, return the conflict to requirements with the stages that dominate and the options that would change them. Do not quietly widen the target.

## Model demand and capacity

Performance and capacity are the same question seen from different ends: whether the system can serve accepted demand with acceptable latency and failure behavior.

- Distinguish an **open** arrival model (independent users or clients) from a **closed** one (a fixed population that waits for its own responses). A closed model can appear to meet a rate by offering less traffic as latency rises.
- Identify the bottleneck resource and its saturation point: CPU, connection pool, database, lock, queue, provider quota or network egress.
- Choose headroom from the cost of saturation and the time to scale, not from a round number. State what happens before scaling takes effect.
- Decide the scaling signal and its lag. Scaling on the wrong signal responds after the user has already waited.
- Define degradation: queue, shed, serve cached or partial results, or fail explicitly. An overloaded system that accepts unbounded work converts a latency incident into a data and recovery one.

Use [Analyze capacity and cost](../../analyze-capacity-cost/SKILL.md) for the demand model, saturation analysis, scaling mechanics and provider sizing. Do not restate its arithmetic here. For the design-time demand, headroom and scaling plan, read [capacity planning](capacity-planning.md).

## Design for the tail

Averages hide the requests users remember. Design for the slow tail:

- **Fan-out:** a page that waits for many parallel calls is bounded by the slowest one; its tail is worse than any single dependency's.
- **Retries:** retries amplify load exactly when the system is struggling. Bound them, use jitter, and make retryable operations idempotent.
- **Timeouts and queues:** a timeout shorter than the dependency's tail turns slow responses into failures; a queue absorbs a burst and then delivers it late. Both need a completion deadline, not only a request deadline.
- **Runtime effects:** garbage collection, cold starts, connection establishment, JIT warm-up and cache expiry cluster latency at inconvenient moments.
- **Shared resources:** a noisy tenant, batch job or export can consume the capacity the interactive journey needs. Decide isolation or fair sharing.

Hedged or speculative requests can cut tail latency at a direct capacity and side-effect cost. Treat them as a design choice with an authority and idempotency requirement, not a default.

## Design for efficiency

Efficiency is the work per unit of outcome: queries per request, bytes over the wire, objects per page, tokens per model call, retries per success. It affects latency, capacity and cost together.

- Remove repeated work before caching it. A cache adds a freshness, invalidation and failure question.
- Batch or coalesce where the dependency supports it, without turning one slow unit into a larger failure.
- Keep payloads and responses proportionate to what the consumer uses.
- Recheck the efficiency claim after the data volume grows; a design that is efficient at test scale may be quadratic at production scale.

## Plan the evidence

Match the measurement to the claim:

| Claim | Evidence that can support it |
| --- | --- |
| This journey meets the target for real users | Production or client telemetry over the accepted population and window. |
| The service meets the target under a defined workload | A load profile with the accepted arrival model, data and environment. |
| The design removes a known bottleneck | Before/after measurement of the same workload and revision, with the generator held constant. |
| Capacity headroom is sufficient | Saturation measurement at and beyond expected peak, including recovery after overload. |

- A smoke test checks the script, not capacity. A local benchmark is not production capacity. A CI runner result is regression evidence for that runner.
- Separate application limits from generator, network or shared-environment limits before concluding anything about the service.
- Measure the distribution, not a mean, and retain sample counts, failures and drops.
- Performance-testing expertise owns the load tooling, scenario mechanics, thresholds and execution targets when installed. Use it for the test; keep the design claim and the accepted target here.
- [Testing resilience](../../testing-resilience/SKILL.md) owns controlled failure injection. Combined load and fault testing is a separate scoped experiment.

Report the design budget, the workload and environment, the measured outcome, the limits of the evidence and the assumption that would invalidate the design. A passing load test does not establish that real users experience the target.
