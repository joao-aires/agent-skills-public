---
name: infra-jvm-optimization
description: "Measure and improve application/infrastructure resource efficiency, JVM memory and GC, startup/shutdown, autoscaling, scheduling and resilience during setup, feature changes or recurring optimization reviews."
metadata:
  scope: stack-specific
  invocation: both
  stack: Java, JVM, Kubernetes
  version: "1.0"
---

# Infrastructure and JVM optimization

Optimize cost or throughput subject to user outcomes and stability. A smaller pod or lower heap chart alone is not proof of improvement.

Use JVM flags and ergonomics only for a Java/JVM workload. For Python, Node.js or another runtime, use `plan-application-capacity` and that runtime's current guidance; do not introduce Java or Kubernetes to use this skill.

## Modes and evidence

- **Interactive:** explain the resource budget, bottleneck and experiment options; resolve workload objectives with the user.
- **Setup/feature:** configure and test runtime/infra together, including probes, graceful shutdown, pools and load-sensitive behavior.
- **Recurring review:** audit rendered settings and metrics against the previous baseline, identify inconsistencies, prepare measured bounded changes, and track experiments. Do not auto-promote unbenchmarked collector/resource changes to production.

Consult [references/optimization-guide.md](references/optimization-guide.md). Discover runtime/JDK version, architecture/libc, container launch flags, application/consumer/job roles, deployment overrides, autoscaler metric semantics, resource limits and normal/peak behavior. Inspect effective rendered configuration, not only base YAML or comments for deeper implementation details when needed.

## Workflow

1. Record objectives and baseline: journey errors/latency, throughput, startup, restarts, GC pauses/CPU, RSS/heap/native memory, throttling, queue/backlog, downstream load and cost per useful work.
2. Locate the bottleneck with failing/healthy replica and node comparisons. Distinguish warmup, sustained load, leaks, mounts/inodes/quotas and external saturation.
3. Build the total memory/CPU/storage budget, including agents, thread stacks, direct buffers, metaspace, code cache, OS overhead and memory-backed volumes.
4. Inspect CPU requests/limits versus JVM processor detection and framework pool sizing. A processor-count flag shapes ergonomics; it does not reserve/enforce CPU.
5. Choose a small experiment: collector, heap strategy, pool/buffer bounds, workload concurrency, requests/limits, scheduling or scaling signal. Explain the workload-specific hypothesis and tradeoffs.
6. Align application and infrastructure: heap/resources/scaling units; startup/readiness/liveness; preStop/application shutdown/pod grace; worker offsets/jobs; topology/PDB/rollout capacity; GitOps/autoscaler ownership.
7. Test cold start, representative steady/peak load, long-running soak, dependency slowness, draining and scale behavior. Monitor user outcome and resource budget together.
8. Promote progressively with source/artifact/config identities, rollback triggers and observation window. Preserve explicit production overrides while lower environments validate changes.
9. Document before/after measurements, regression checks and limits. Retain or revert experiments based on evidence.

## Guard against misleading optimization

GC choice depends on CPU/heap/pause needs and JDK; Serial/G1/ZGC are not ranked universally. Heap caps do not bound process RSS. Scaling replicas may worsen database pressure or a memory leak. Aggregated external metrics with `AverageValue` need adapter/unit verification. Hard spread constraints can leave replicas Pending.

## Completion evidence

Deliver effective configuration matrix, bottleneck evidence, resource budget, experiment changes, representative measurements, rollout status and residual risks. If benchmarks/live access are missing, call the result a configuration proposal, not a verified optimization. Coordinate telemetry with `observability-operations` and user-outcome requirements with `reliability-design` as needed.
