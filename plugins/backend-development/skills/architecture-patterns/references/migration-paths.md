# Migration paths

A pattern migration is a sequence of deployable, observable and reversible states, not a rewrite. Choose the smallest step that tests the force, keep the old path until the new one is proven, and decide who owns writes at each step.

These paths describe structural moves. Event and message contract mechanics belong to event-driven-design; cross-service consistency and failure evidence belong to distributed-systems; service behavior inside a boundary belongs to backend-design.

## Common rules

- Change one dimension at a time. Do not move a boundary, change data ownership and alter the external contract in the same release.
- Keep the external contract stable behind a facade, version or route while internals move.
- Decide the write owner for every overlap. Dual writes have ordering and partial-failure problems; prefer one owner with a sync direction and reconciliation.
- Treat rollback as a state, not a command. Data written in the new shape may not be reversible by reverting code.
- Delete the old path only after parity is measured, remaining usage is zero or explicitly accepted, rollback has been exercised and an owner exists.
- Use expand-and-contract for schema changes: add the new shape, dual-read or backfill, switch writes, verify, then remove the old shape after the compatibility window.

## Modularize a monolith

Use when the deployable is tangled and boundaries are unclear, but independent deployment is not yet required.

1. Map business capabilities, current data ownership and change coupling. Pick one seam with a clear owner and real behavior behind it.
2. Define a module interface. Route cross-module calls through it rather than importing internals.
3. Give the module its own tables or, at minimum, explicit write ownership; stop cross-module joins and writes.
4. Enforce the dependency rule in CI and with module contract tests.
5. Extract a deployable only if a measured ownership, deployment or scaling force remains after modularization.

- **Rollback:** revert the module boundary as an internal refactor; no external contract changed.
- **Compatibility:** internal interfaces and database expand/contract; old and new code may run during a rolling deploy.
- **Evidence:** dependency graph before and after, ownership map, dependency-rule failure in CI, module contract tests, single-command deploy.

## Introduce ports or a dependency rule

Use when a module or service needs replaceable infrastructure, multiple delivery mechanisms or IO-free core tests, but does not need a new deployment boundary. Layered, hexagonal and clean/onion are internal dependency decisions; migrate them in place.

1. Choose the core behavior that must survive framework or infrastructure change, and the adapter that changes most often.
2. Extract a port at the boundary the core already uses; move framework, database or transport code behind an adapter.
3. Make the dependency direction enforceable: imports point inward, and the build or tests fail on a violation.
4. Convert one path at a time. Keep the old call site until the new adapter passes contract tests against the same behavior.
5. Collapse speculative ports that never gained a second adapter or a test benefit.

- **Rollback:** keep the old adapter call path behind a flag or thin factory until the new one is proven; this is an internal refactor with no data-ownership change.
- **Compatibility:** external contracts do not change; database access still follows expand-and-contract when the adapter changes persistence.
- **Evidence:** core tests running without IO, adapter contract tests, dependency-rule failure in CI, measured reduction in framework coupling or replacement effort.
- **Stop condition:** a port with one adapter and no plausible replacement is ceremony. Remove it or state the test or replacement it protects.

## Strangle a capability

Use when a slice of behavior can move behind a stable boundary and the old implementation must keep serving during the transition.

1. Choose a capability with a measurable contract and a stable entry point; keep the facade unchanged.
2. Run the new path in shadow or for a small traffic slice; compare results and record divergence.
3. Move data ownership deliberately. Define sync direction, reconciliation and what happens when both paths write.
4. Cut over per consumer or capability, not for the whole system at once. Watch errors, latency, duplicates and data checks.
5. Remove the old path after its usage is zero or accepted; keep the route back until then.

- **Rollback:** route traffic back, reverse-sync or compensate changes made only in the new path, and verify data before declaring success.
- **Compatibility:** same external contract; internal data shape may differ. Test old client/new path and new client/old path during the window.
- **Evidence:** shadow diffs, parity metrics, reconciliation report, rollback drill, per-consumer usage before removal.

## Split a service

Use when independent ownership, deployment or scaling is a measured constraint and the data boundary is separable. Do not split by layer, by team count alone, or while the shared database remains authoritative.

1. Modularize first. Define the future service's data ownership, contract and failure behavior.
2. Separate the schema. Remove shared-table access; introduce an API or events for the data other services need.
3. Extract the deployable and dual-run it. Migrate traffic by capability or consumer.
4. Make isolation real: deadlines, retries, idempotency, dashboards, alerts and on-call for the new service.
5. Stop writes to the old store, reconcile, then decommission the old path.

- **Rollback:** feature flag or route back; keep dual-write or reverse sync during the window; reconcile data before switching again.
- **Compatibility:** versioned contract, consumer inventory, tested old/new combinations, and an explicit consistency promise across the seam.
- **Evidence:** deploy one service without the others, isolate its failure, reconcile its data, measure latency and cost, confirm on-call ownership.
- **Stop condition:** a shared database, lockstep deployment or a synchronous chain for one transaction means the split is producing a distributed monolith. Re-scope before proceeding.

## Introduce CQRS

Use when measured read/write asymmetry or divergent read shapes justify a separate model, and the journey can tolerate or explicitly handle projection lag.

1. Keep the write model authoritative. Define the read contract and its freshness promise.
2. Add a projection that consumes events or change data, applies idempotently and records its position.
3. Measure lag, expose it, and define rebuild and backfill. Test duplicate, out-of-order and missed changes.
4. Route reads by capability. Fall back to the write model where read-after-write is required.
5. Remove dual-read only after parity and lag behavior are accepted.

- **Rollback:** route reads back to the write model and disable the projection. The write path and its contract remain unchanged.
- **Compatibility:** the read API is a contract; ordering, versions, gaps and staleness are visible. Event schemas and delivery belong to event-driven-design.
- **Evidence:** projection lag distribution, rebuild duration, duplicate handling, read-your-writes test, load on the write side.

## Introduce event sourcing

Use only when audit, replay, rebuild or temporal reconstruction is a concrete requirement, and retention, deletion and restore are funded. A current-state store plus an audit or history log is the cheaper default for audit alone.

1. Choose one aggregate or bounded context. Keep a current-state read model for queries and operations.
2. Define event ownership, schema versioning and an append-only store. Make command handling idempotent per aggregate.
3. Build projections and snapshots as needed. Establish rebuild, backup, export and restore before relying on the log.
4. Migrate current state through an initial snapshot or baseline event; verify invariants against the old store.
5. Expand to another aggregate only after rebuild, replay and restore are proven.

- **Rollback:** keep the current-state model or an export so reads survive; derive or restore it if the event store is unavailable. Do not make event sourcing the only copy before restore is tested.
- **Compatibility:** retained event versions must remain replayable; consumers need a schema contract; deletion and redaction must have a defined path.
- **Evidence:** rebuild from the log, replay across every retained version, restore test, projection lag, retention cost, deletion exercise.
- **Stop condition:** if no one can state the replay or reconstruction query, the pattern is not justified.

## Adopt serverless

Use for stateless or event-driven work with spiky or low-utilization traffic, after checking runtime limits, latency, cost and the local path.

1. Extract a stateless handler behind the existing contract.
2. Handle idempotency, timeouts, retries, connection pooling and cold-start behavior explicitly.
3. Add tracing, metrics and a local or CI path that exercises the handler.
4. Route a slice and compare latency, errors and cost with the current path.
5. Keep the container or service fallback until behavior and cost are stable.

- **Rollback:** route back and keep dual deployment during the window; avoid provider-specific queues or storage at the contract boundary where portability is required.
- **Compatibility:** same external contract; verify runtime limits, quotas, concurrency and per-invocation cost at peak.
- **Evidence:** cold-start and peak-load test, throttling behavior, cost model at expected and peak volume, local and CI execution, portability decision.

## Rollback and compatibility review

| Change | Compatible overlap | Rollback mechanism | Irreversible or risky part |
| --- | --- | --- | --- |
| Module boundary | Internal; rolling deploy is enough | Revert code and dependency rule | Split schemas or moved tables |
| Strangler cutover | Old and new paths behind one facade | Route back, reverse-sync or compensate | Writes accepted only by the new path |
| Service split | Both services and a versioned contract | Route back, reverse-sync, reconcile | Data created under the new ownership |
| CQRS projection | Reads can fall back to the write model | Disable projection and route reads back | None if the projection is disposable |
| Event sourcing | Current-state model or export retained | Rebuild from events or restore export | Published events, deletion and schema history |
| Serverless handler | Both deployments behind one route | Route back and keep the old runtime | Provider-specific configuration and queues |
| External contract change | Old and new versions served together | Serve the old version again | Semantic changes to stored data and emitted events |

## Stop conditions

Do not advance to the next step when any of these is true:

- parity or reconciliation is unmeasured;
- rollback has not been exercised on realistic data;
- the write owner during the overlap is ambiguous;
- the on-call owner or cost curve is unassigned;
- consumers are not inventoried;
- the only evidence is a successful build, a deployed skeleton or a diagram.

A migration that cannot stop safely at its current step is a rewrite with extra steps.
