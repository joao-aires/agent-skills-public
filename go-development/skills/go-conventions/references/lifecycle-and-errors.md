# Lifecycle and failure reasoning in Go

Read for concurrent work, resource-owning components, clients or service shutdown. Verify APIs against the project's Go version and chosen libraries.

## Establish ownership before coordination

Identify the owner of each goroutine and resource: who starts it, who can stop it and who observes completion. Prefer a synchronous API when the caller can introduce concurrency itself. When the component owns background work, expose a lifecycle that lets its caller wait for shutdown rather than assuming a cancellation signal means work has ended.

Follow each blocking point through early termination. A sender needs a path when its receiver stops; a receiver needs a path when no more input will arrive; an external call needs a supported timeout or cancellation mechanism. A cancellation branch elsewhere does not make an unguarded send cancellable. Decide who closes a channel and how that owner knows no sender remains.

Bound fan-out, queue/pool sizes and retry/deadline budgets from the workload and service commitments. A concurrency bound should account for the resources each operation holds, not just the number of goroutines that can be started. Use context-aware HTTP/database calls and release request-scoped resources on all relevant paths.

Pass context per operation where it represents that call's lifetime. If work legitimately outlives a request, give it an explicit service-owned bounded lifecycle and decide whether it must survive process loss. Detaching cancellation alone does not make a durable job. If a timeout leaves an external result uncertain, preserve the logical operation identity and reconcile before repeating a consequential effect.

| Coordination need | Candidate |
| --- | --- |
| Coordinated shared invariants | Mutex |
| Suitably independent state | Atomics |
| Communication or ownership transfer that clarifies the contract | Channels |

Document actual concurrency guarantees, including whether returned mutable values remain shared. Test closed channels, cancellation while blocked, concurrent shutdown and partial startup where permitted; preserve a sample lifecycle's preconditions.

## Shut down against the actual server contract

Stop admitting relevant work, drain within a bounded budget, release owned clients/resources and wait for tracked workers according to the deployment. In net/http, use the supported Shutdown behavior and account separately for hijacked/long-lived connections and application workers. Give draining an appropriate context rather than reusing an already-cancelled request. Define what unfinished accepted work does after restart; liveness/readiness and graceful shutdown are distinct.

## Preserve useful error semantics

Wrap errors when adding meaningful context or exposing an inspectable cause is part of the API. Preserve stable expected conditions using errors.Is/As or a documented domain result; do not make callers parse private messages. Translate internal details at user/security boundaries without losing useful operator evidence. Decide who records an error and with what severity; duplicate logging and swallowed failures both hinder diagnosis.

A panic recovery boundary can contain a failure but cannot assume partially changed state is valid. Decide whether to stop, restart or recover from actual invariants. Keep secrets and sensitive payloads out of error messages and logs.

Primary references: [context and structs](https://go.dev/blog/context-and-structs), [context](https://pkg.go.dev/context), [net/http shutdown](https://pkg.go.dev/net/http#Server.Shutdown), [database/sql](https://pkg.go.dev/database/sql), [errors](https://pkg.go.dev/errors) and [memory model](https://go.dev/ref/mem).
