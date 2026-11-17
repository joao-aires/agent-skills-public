# Analyze capacity and saturation

Use this reference when the question is whether the system can serve a stated demand with acceptable latency and failure behavior, and which resource limits that outcome. The plan that chooses demand targets or a scaling strategy belongs to design; this reference covers measurement and interpretation.

## Define the measured question

Name the service, critical journeys, environment, population and time window. State the claim: an observed saturation point, a sizing mismatch, available headroom or the effect of a change. Separate measurement, forecast and assumption.

Identify the accepted reliability and latency objective in the project record rather than inventing one. If no objective exists, report the observed behavior and the missing decision.

## Measure demand and work in flight

- Use measured arrival rate and service time where available. Relate them to simultaneous work with units and assumptions.
- Account for fan-out, retries and operations that hold a resource while waiting. Long-running AI, audio or provider calls can consume concurrency even when local CPU is low.
- Check seasonal, burst and batch behavior. Steady-state queueing estimates do not describe overload or bursts automatically.
- No telemetry means an estimate requiring validation, not an invented measurement.

State the population, sampling window and missing data with every number. Averages can hide the tail and the memory peak that determine failure.

## Find the bottleneck and saturation

Inspect the entire request path: worker and process counts, per-process connection pools, database connection and IO limits, caches, queues, storage and third-party quotas. Adding replicas can multiply connections to a shared dependency.

Look for saturation before it becomes an outage:

- tail latency and queue wait rather than average CPU alone;
- throttling, rejected requests and retry growth;
- memory peaks, OOM events, garbage-collection pauses and ephemeral-storage pressure;
- database locks, slow queries and connection-pool exhaustion;
- provider rate limits and quota consumption;
- storage growth, retention backlog and backup duration.

Establish where the application stops admitting work, where it queues work and what the caller sees at the bound. Check how long queued work remains useful and how recovery drains it. Increasing parallelism helps only while downstream resources can serve it.

## Analyze sizing and headroom

Compare the observed usage distribution with provisioned capacity. Headroom is the gap you measured, not a percentage assumed in advance.

- For Kubernetes, requests drive scheduling and limits drive throttling or OOM behavior. Include sidecars, ephemeral storage and node/system overhead. Working-set averages can hide fatal peaks.
- Distinguish workload autoscaling, vertical sizing recommendations and node autoscaling when interpreting behavior. Check metric availability, utilization semantics, startup and warmup, stabilization, and whether controllers compete on the same resource.
- Check whether quotas, node-pool bounds, topology, disruption budgets and storage or network constraints permit the replicas observed during a peak or rollout.
- Autoscaling cannot create provider quota or fix an overloaded database. Name the limiting dependency instead of attributing the symptom to the autoscaler.

Use [Kubernetes resource guidance](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) and [HPA guidance](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) matching the cluster version. For EKS, GKE, AKS or another host, read the first-party guidance for that platform and service. Platform recommendations and example ratios are hypotheses to check against this workload, not defaults.

## Analyze the effect of an optimization

Query and index changes, batching, payload reduction, caching and concurrency changes all alter the observed capacity profile. Establish the mechanism and the expected direction before measuring.

- Define the baseline period and the comparison conditions.
- Use the project's approved load or failure-testing instructions when available.
- Size and observe the generator separately; runner contention and unachieved offered load constrain the conclusion.
- Compare before and after under comparable demand; normalizing for traffic is part of the claim.
- A local benchmark is not production capacity, and a CI-runner result is regression evidence for that runner only.

Cache changes need an explicit freshness and invalidation rule; a cache that hides a slow dependency also changes failure behavior.

## State the limits of the analysis

- Distinguish estimated, projected and demonstrated capacity.
- Report scenario coverage, missing signals, sampling bias and known noise.
- A smoke test checks the script, not capacity.
- An unexercised degraded scenario remains an open risk, not a passed check.

Hand the planning and scaling decision to [capacity planning](../../design-system/references/capacity-planning.md). Use [Run operations review](../../run-operations-review/SKILL.md) for the recurring measured review and [observability](../../design-system/references/observability-and-monitoring.md) for measurement quality. Retain the demand range, sizing findings, dependencies and the evidence needed to revisit them.
