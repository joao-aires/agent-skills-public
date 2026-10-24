# Go verification and performance evidence

Read when defining tests or investigating a measured bottleneck. Use actual repository commands and test targets; the examples below are tool families rather than mandatory invocation recipes.

- Test observable package/service behavior and durable invariants. Use table-driven subtests when cases share useful setup/assertions; separate cases when that is clearer. Helpers and t.Cleanup should preserve ownership and isolation. Use the existing assertion style rather than adding or removing a testing library incidentally.
- Use real selected storage/transport behavior for integration claims. A fake or SQLite fixture cannot establish a different database's transaction, locking or migration semantics. Keep expensive or external tests identifiable and report skipped/unavailable targets.
- Race detection observes executed shared-memory interactions. Passing it does not prove freedom from deadlocks, goroutine leaks, logical races or unexercised data races. Exercise relevant cancellation, blocking, ownership and shutdown cases separately. Match supported target/cgo/toolchain requirements.
- Fuzzing is useful for parsers and broad input spaces with meaningful invariants; bound the run and preserve useful minimized regressions. A percentage or an empty no-panic assertion is not a substitute for behavioral acceptance.
- Locate the bottleneck before optimizing. Use CPU/heap/block/mutex profiles, tracing and service/database evidence to distinguish process cost from external wait. Protect diagnostic endpoints and collected profiles from unintended access or sensitive-data disclosure.
- Benchmark a representative unit or boundary under comparable data, concurrency and environment. Prevent dead-code elimination, separate setup and record allocations where relevant. Use the supported b.N or newer benchmark API for the declared version. Compare repeated runs with appropriate statistical tooling and report noise and workload limits.
- Recheck correctness and full latency/resource tradeoffs after a change. A microbenchmark improvement does not establish application throughput, tail latency or lower operating cost.

Primary references: [testing](https://pkg.go.dev/testing), [race detector](https://go.dev/doc/articles/race_detector), [fuzzing](https://go.dev/doc/security/fuzz/), [diagnostics](https://go.dev/doc/diagnostics) and [dependency management](https://go.dev/doc/modules/managing-dependencies).
