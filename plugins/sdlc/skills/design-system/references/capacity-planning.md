# Capacity planning in design

Capacity planning asks whether the design can serve accepted demand with the accepted latency and failure behavior. At design time it produces a demand model, a headroom and scaling decision, a saturation and failure story, and the resource shape those imply. It is a planning reference: measuring the workload, computing a bill and executing a scaling change belong to the capacity and cost method.

Read [performance](performance.md) for the response-time budget and tail behavior, [reliability](reliability.md) for outcome targets and error budgets, and [cost planning](cost-planning.md) for the cost consequence of the capacity you choose.

## Start from demand

Describe demand in units the design can act on, and label each input as measured, forecast or assumed:

- **Work unit.** What one unit of demand is — a request, a journey, a job, a message, a model call, a tenant — and which stages it touches.
- **Arrival model.** Independent arrivals (open) or a fixed population waiting on its own responses (closed). A closed model can appear to meet a rate by offering less work as latency rises.
- **Concurrency and in-flight work.** How many units are simultaneously being served, including work waiting on a provider, a queue or a human.
- **Peak, burst and seasonality.** Sustained demand, expected peak, burst shape and the time it takes to reach peak. A daily average does not size a checkout path.
- **Fan-out and amplification.** Downstream calls, retries, batch expansion and model token growth per unit.
- **Population skew.** A large tenant, a bulk export or a scheduled job can dominate a shared resource even when the average is comfortable.
- **Growth and uncertainty.** The range that matters for the decision, not one projected number.

Targets arrive from accepted requirements and the [ECR](../../artifact-system/references/contracts/ecr.md); use [requirements engineering](../../requirements-engineering/SKILL.md) when they are missing. Do not derive an acceptable latency or availability target from the design.

## Headroom and saturation

Identify the resource that limits the journey — CPU, memory, connection pool, database I/O, lock contention, queue depth, provider quota, network egress or a per-tenant limit — and state its saturation point.

- Choose headroom from the cost of saturation and the time to scale, not from a round percentage. A fast-scaling stateless tier needs less than a stateful store that scales in hours.
- Include rollout headroom: a deployment, migration or cache warm-up consumes capacity before the new version serves traffic.
- State what happens before scaling takes effect. A scaling signal that reacts after users wait is not protection.
- Account for recovery load: restart, cache cold start, queue drain, replica catch-up and restore can exceed normal peak.
- Check that the downstream can absorb the replicas you add. More application instances can exhaust a database connection limit, not increase throughput.

Do not restate queueing arithmetic or provider sizing mechanics here; read [capacity](../../analyze-capacity-cost/references/capacity.md) for the measured method.

## Scaling strategy

Choose a strategy that follows demand shape and operating constraints:

| Strategy | Fits when | Design must state |
| --- | --- | --- |
| Vertical sizing | Simple or stateful workload, predictable demand | The ceiling, restart consequence and cost of the next step |
| Horizontal replicas | Stateless work with a shared dependency that can absorb it | Scaling signal, lag, bounds and connection multiplication |
| Autoscaling | Variable demand with a trustworthy signal and useful warm-up behavior | Signal, target, stabilization, minimum and maximum, quota limits |
| Scheduled or manual scaling | Predictable peaks or work that must not autoscale | Trigger, owner and lead time |
| Queue-based buffering | Work can wait and be drained later | Admission bound, queue capacity, drain rate and aging policy |
| Sharding or partitioning | One resource cannot serve the population | Key, rebalancing cost and hot-partition behavior |

Autoscaling is not a default and does not create quota. Define the upper bound explicitly: an unbounded scale-out can convert a capacity incident into a cost or provider-limit incident.

## Failure and degradation behavior

Decide what the system does when demand exceeds capacity, before writing the scaling policy:

- **Admission.** Where work is refused, queued or downgraded, and what the caller is told.
- **Overload.** Shed, serve cached or partial results, reduce quality or fail explicitly. An unbounded queue converts a latency incident into a data and recovery one.
- **Fairness.** Whether one tenant, export or batch job may consume the interactive journey's capacity.
- **Recovery.** How the system drains after overload and whether retries amplify the load that caused it.
- **Redundancy.** What capacity remains after a zone, replica or dependency is lost, and whether the remainder can carry the accepted journey.
- **Recovery-site capacity.** A recovery environment must carry restored traffic, including quota, licenses and connection limits; a warm standby that cannot scale is not a recovery strategy.

Read [disaster recovery and continuity](reliability-disaster-recovery.md) when capacity must survive the loss of a failure domain.

## Resource sizing and the cost of reliability

Translate the plan into design-level resource shape:

- replica and pool counts, concurrency and per-process limits;
- CPU, memory, storage and bandwidth classes, with what is reserved for peak and recovery;
- provider quotas, account limits and per-tenant ceilings that bound the plan;
- the capacity held for redundancy, backups, observability and the recovery environment.

Reliability has standing cost: headroom, extra replicas, cross-region copies, retained telemetry and a recovery site are paid for continuously. State the benefit that justifies each and the demand assumption that would change the answer. Read [cost planning](cost-planning.md) for the tradeoff and attribution; do not put prices or provider fee tables in the design.

## Evidence and handoff

The capacity plan is ready when it states:

- the demand model, with units, population, peaks and provenance;
- the bottleneck and saturation point, and the headroom chosen from them;
- the scaling signal, lag, bounds and dependency constraints;
- behavior at saturation, during degradation and after recovery;
- the resource shape and the capacity reserved for reliability;
- the evidence needed: load test at the real target, production telemetry, provider quota confirmation or a bounded estimate;
- what remains an estimate and which assumption would invalidate the plan.

Route measured demand, saturation analysis, provider sizing and verification to the [capacity and cost method](../../analyze-capacity-cost/SKILL.md). A local benchmark, a list price or a configuration change is not evidence of production capacity. Keep the design claim and the accepted target here; keep the measured result and the bill with the capacity decision.
