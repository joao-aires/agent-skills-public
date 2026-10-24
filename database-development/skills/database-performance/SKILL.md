---
name: database-performance
description: Investigate database workload performance and compare improvements while
  preserving correctness and operating budgets. Use for latency, throughput, contention,
  connection or resource bottlenecks before choosing engine-specific tuning.
license: MIT
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: true
---

# Improve the measured workload

Establish the affected user operation, target, data distribution, load/concurrency and execution environment. Reuse existing service objectives. Distinguish a single query's elapsed time from request latency, queueing, lock/pool wait, serialization, network transfer and downstream work. Ask for missing performance commitments only when the decision depends on them; keep estimates labelled.

## Diagnose before prescribing

Locate the time spent in the affected user operation before tuning a query. Separate waiting for a connection, waiting for another transaction, executing SQL, transferring results and processing them in the application. Improving the query plan will not necessarily help a request whose time is spent waiting elsewhere.

Use aggregate workload evidence to choose which operations matter. A frequently executed moderate query can consume more resources than an occasional slow one; a severe tail can still make a critical journey unusable. Compare those costs with the accepted user outcome, then form a specific explanation to test.

- Inspect representative plans, cardinalities, waits and resource pressure with matching technical expertise.
- Separate cold/warm behavior and tenant/data-size slices where they affect the conclusion.
- Estimated plan costs are not wall-clock measurements, and a scan or a particular join type is not inherently a defect.

Treat production diagnostics as workload with an impact. Confirm the target, access and permitted load; use existing traces or non-executing plans when sufficient.

A plan that runs the statement can change data or impose substantial load, and rollback does not reverse every external effect. Keep sensitive query parameters and records out of reports.

## Compare changes against the full contract

Form a testable bottleneck hypothesis. Consider the query/access pattern, data representation, indexes/statistics, connection behavior and resource limits before adding infrastructure. Choose discriminating changes and record enough conditions to attribute the outcome. An index can improve reads while worsening write latency, storage and maintenance; caches and replicas introduce staleness and failure behavior.

Measure before/after correctness, latency distribution, throughput and relevant write/resource/recovery costs under comparable representative conditions.

- Repeat enough to distinguish improvement from noise; report sample size, test duration, concurrency and differences in cache/data/configuration.
- Synthetic evidence establishes only the exercised workload.
- Preserve a rollback or forward recovery route appropriate to the change.

Return the supported diagnosis, chosen tradeoff, actual measurements and remaining uncertainty. Use accepted operating signals to detect regression when deployment is separately authorized. Missing specialist guidance does not justify skipping measurement or selecting a different engine.
