---
name: plan-application-capacity
description: Design or review application capacity, concurrency and scaling for Kubernetes or another hosting platform. Apply to growth, saturation, resource sizing, latency bottlenecks and architecture changes using measured demand and current platform-specific guidance.
---

# Plan application capacity

## Start from demand and service behavior

Identify critical journeys, expected sustained and peak demand, growth, seasonal/burst behavior and acceptable latency. Use measured traffic/service times and resource profiles where available; distinguish observations, forecasts and assumptions. Inspect tail latency, queues, saturation, throttling, memory peaks and database limits instead of sizing from average CPU alone. No telemetry means an estimate requiring validation, not an invented measurement.

Relate arrival rate and time in the system to in-flight work, with clear units and assumptions; steady-state queueing estimates do not describe overload or bursts automatically. Include fan-out, retries, long-running AI/audio work and slow providers. Decide where concurrency is bounded and where work is queued/rejected; avoid unbounded parallelism as a latency optimization.

## Design a coherent scaling path

Inspect the entire request path: worker/process counts, per-process connection pools, database connection/IO limits, caches, queues, storage and third-party quotas. Adding replicas can multiply database connections and exhaust a shared dependency. Prefer measured query/index improvements, batching, payload reduction and useful caching with explicit freshness/invalidation rules before expanding infrastructure blindly.

Estimate a normal, peak and degraded scenario, with headroom for rollout and the failure the application is expected to tolerate. Specify the bottleneck, scaling trigger, upper bound and dependency constraint; do not automatically introduce Kubernetes for a small application on another platform.

## Apply Kubernetes mechanics when relevant

Set requests from representative per-container usage and scheduling needs; choose limits deliberately, considering CPU throttling and memory OOM risk. Include sidecars, ephemeral storage, node/system overhead and placement constraints. Avoid a universal percentage buffer or CPU-limit rule. Memory working-set averages can hide fatal peaks.

Distinguish HPA workload scaling, VPA sizing recommendations and node autoscaling. Check metric availability, request-based utilization semantics, startup/warmup and stabilization. Avoid competing controllers acting on the same resource without an understood policy. Check whether quotas, node-pool bounds, topology, disruption budgets and storage/network constraints permit the proposed replicas during peaks and rollout. Autoscaling cannot create cloud quota or fix an overloaded database.

Use [Kubernetes resource guidance](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) and [HPA guidance](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) matching the cluster version. Then search first-party guidance for EKS, GKE, AKS or the actual host, database and queue; node-provisioning and managed-service limits differ. The installed `aks-cost-optimization` is an AKS-only specialist, not an infrastructure default. Treat its suggested ratios/minima as examples to validate against workload evidence and current provider documentation.

## Leave a testable decision

Record assumptions, demand range, sizing/scaling choices, dependencies and the evidence needed to revisit them. Verify changed configuration and focused performance behavior in a safe environment; compare before/after under comparable conditions. State what is estimated versus demonstrated.

Use the project's approved load/failure-testing instructions when available. This skill defines capacity and latency decisions; it does not prescribe a new load-test tool, chaos regimen, observability stack or SLO framework. Keep affected architecture and operating notes current as the application changes.
