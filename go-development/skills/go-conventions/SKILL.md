---
name: go-conventions
description: Build, extend or review Go services, libraries and command-line applications.
  Use for modules, package/API boundaries, errors, cancellation, runtime lifecycle
  and meaningful Go verification without requiring a framework.
license: MIT
metadata:
  scope: stack-specific
  invocation: both
  role: support
  stack: Go
  references: references/sources.md
user-invocable: true
---

# Implement the Go contract in the existing project

Read go.mod/go.work, supported toolchain/targets, package boundaries, commands and accepted conventions. Determine whether the change serves a library, service, worker or CLI. Preserve an adequate existing layout and dependencies; a Go task does not require a microservice, framework, DI container or fixed directory shape. Read [source selection](references/sources.md) for researched upstreams and primary implementation references.

## Keep package and dependency boundaries useful

Let domain responsibilities and actual consumers shape packages and interfaces.

- Prefer small consumer-driven interfaces where substitution or external boundaries need them; avoid an interface or constructor pattern for every type.
- Respect zero-value semantics and document ownership/lifecycle where non-obvious.
- Keep application wiring, process policy and side effects explicit; libraries should not unexpectedly start work, terminate the process or select global configuration/logging.

Use the project's module/toolchain policy and reproducible dependency commands. Review direct/transitive changes, supported versions and advisories before adding packages. Standard-library capabilities are a useful starting point, but an accepted maintained framework need not be removed. Configuration and feature flags should express actual operational decisions rather than hide invalid required settings behind permissive defaults.

## Make errors and concurrency part of the contract

### Errors

Return useful errors and preserve inspectable identity/type where callers depend on it. Choose wrapping, public error exposure and logging at the responsible boundary; avoid lost errors or repeated noisy reports. Match errors.Is/As and other APIs to supported Go versions. Expected domain failures and programmer invariants need different handling; recovered panics do not prove the service remains correct.

### Concurrency

Before starting concurrent work, identify who starts it, who can stop it, and who waits for it to finish. Follow every blocking receive, send and external call through success, error and cancellation. If the consumer stops early, the producer still needs a way to unblock and release its resources.

Treat cancellation as a signal that cooperating work must observe. Propagating a context helps only when the blocking operation uses it or has another shutdown path. Decide who closes a channel and when all senders are finished; closing it does not establish that the workers have exited. Bound concurrency according to the work and available resources, and make completion observable to the owner.

- Propagate appropriate context/deadlines through context-aware APIs; cancellation is cooperative and does not undo committed work.
- Choose channels, mutexes or atomics from ownership and contention rather than style alone.
- Read [lifecycle and failure reasoning](references/lifecycle-and-errors.md) when changing concurrent work, network/DB resources or shutdown.

## Verify real behavior

Format with the accepted tooling; run relevant builds, vet/static checks and behavioral tests using the project's commands.

- Use race detection for affected concurrency when the target/toolchain supports it, reporting unavailable coverage.
- Test failure/cancellation and public contracts alongside successful paths.
- Table-driven, property/fuzz, integration and consumer tests are techniques selected for the property; no fixed coverage percentage or test filename scheme establishes correctness.

Read [verification and performance](references/verification-and-performance.md) when choosing test boundaries, diagnosing cost or making performance claims. Match production entrypoint/configuration, shutdown and platform/architecture to the claimed result. A cross-compile does not exercise the target runtime. Seek available service/data/security/delivery expertise for the actual boundaries; its absence does not select another stack or remove required evidence.

Return the affected contract, implementation, actual checks and remaining limits. Tool installation, live dependency access, package publication and deployment remain within the authorized task and environment.
