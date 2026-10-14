---
name: backend-conventions
description: Build, extend or review Python/FastAPI systems with SQLAlchemy, Alembic,
  contextual persistence, auth, API contracts, jobs and optional AI/FastMCP. Use for
  backend architecture, endpoints, migrations, transactions, integrations and verification;
  accept reference systems and preserve established project constraints.
metadata:
  scope: stack-specific
  invocation: both
  stack: Python, FastAPI, SQLAlchemy, Alembic, PostgreSQL
  role: support
user-invocable: false
---

# Backend conventions

## Establish the system's shape

Read the request, `AGENTS.md`, architecture and existing code. Accept reference repositories, API examples, schemas, architecture decisions or platform constraints. Extract applicable boundaries and behaviors rather than copying an entire system. Preserve accepted choices; record meaningful deviations in existing architecture/project notes without requiring a new profile format.

For new services, prefer a supported Python, uv with a committed lockfile, FastAPI/Uvicorn, Pydantic v2 and settings, SQLAlchemy 2, Alembic, PostgreSQL, Ruff, pytest and HTTPX. Match installed APIs and dependency versions. Upstream tooling suggestions are defaults for compatible new projects, not permission to replace an existing type checker, hook runner, package manager or application layout. Use async end-to-end where suitable drivers and concurrency needs justify it; an intentional synchronous stack is valid. Do not run blocking I/O inside async handlers or mistake async/thread pools for a CPU scaling strategy.

| System type | Starting approach |
| --- | --- |
| Application API | One deployable service with clear domain boundaries; add services only for an actual independent responsibility. |
| Durable background work | Worker/queue when work must survive process loss; define status, retries, cancellation and recovery according to the task. |
| Event-driven integration | Idempotent consumers and explicit delivery assumptions; use an outbox when database changes and delivery intent must be atomic. Do not promise exactly-once delivery. |
| AI or MCP interface | Narrow authorized adapters over application services; introduce a framework only for capabilities the system needs. |

## Define behavior before implementation

For meaningful new behavior or cross-cutting changes, establish the actor/use case, observable input/output, ownership/permissions, invariants and state transitions before writing handlers/models. Include validation/error semantics, transactions, idempotency, async cancellation/recovery and compatibility where affected. Use concise text, examples or a state/sequence view in existing context; no compulsory design document for routine fixes. Resolve consequential product/authority choices and make explicit reversible assumptions. Inventory affected endpoints, jobs, tools and consumers for global changes, reuse coherent domain behavior and reconcile implementation/tests against every affected entry point. A route-by-route patch without common behavior is not a complete cross-cutting change.

## Organize behavior and contracts

Keep application code, migrations, tests and runtime configuration within the application's boundary. Group routes, schemas, behavior and persistence by domain where useful. Share genuinely cross-cutting auth, database and configuration concerns. Routes translate HTTP and delegate substantive behavior; services/repositories exist for real responsibilities, not a layer quota. Inject authentication, sessions and integrations. Manage shared clients through lifespan and close them cleanly. Validate configuration at startup, inject secrets through the deployment environment, and provide proportionate health/readiness checks with graceful shutdown.

Separate public input/output schemas from ORM models. Allowlist mutable fields; never mass-assign ownership, roles or internal state. Publish coherent OpenAPI with stable operation IDs and generate frontend types where useful. Use resource-oriented URLs, correct HTTP status semantics, bounded pagination and allowlisted filters/sorts. Return predictable errors and useful field validation; retain FastAPI's validation shape unless deliberately mapping a documented alternative. Include correlation IDs without leaking internals.

Use timezone-aware UTC timestamps at persistence boundaries, explicit units, and Decimal or integer minor units for money. Version APIs at actual compatibility boundaries rather than reflexively versioning every route.

## Treat identity and authority as separate concerns

Reuse the established identity provider or maintained library. For new externally authenticated applications, prefer OIDC authorization code with PKCE and an appropriate server/session boundary. Choose secure cookies/BFF or bearer tokens for the actual client; do not invent an identity system by default. Cookies need HttpOnly, Secure and deliberate SameSite settings, plus CSRF protection for authenticated mutations. Restrict CORS; CORS is not CSRF protection. Avoid long-lived browser tokens in local storage.

Validate token signature with an explicit algorithm allowlist, trusted issuer/key source, audience and expiry; define session/token revocation as required. If local passwords are needed, use Argon2 through a maintained implementation such as pwdlib, verification/recovery and abuse controls. PyJWT handles tokens, not the whole identity lifecycle.

Derive identity and verified tenant membership from authentication. Enforce ownership/permissions on reads, lists, writes, jobs, exports and tool calls. Never trust caller-supplied owner/tenant fields alone. Sharing a filter or parent resource must not implicitly grant access to underlying records the recipient cannot otherwise read. Apply a consistent 403/404 policy without leaking resource existence. Prompts, hidden UI controls and object IDs do not grant authority.

## Make persistence and migrations intentional

Prefer PostgreSQL for shared relational production data. SQLite fits appropriate local/single-writer contexts; other databases require workload or platform justification. Add Redis for a real cache, queue or coordination need, with expiry/ownership semantics; use object storage for uploads with explicit size/type/access limits. Preserve suitable existing database choices.

Use one session per request, job or concurrent task; never share an AsyncSession across concurrent tasks or keep a global mutable session. The operation owns its transaction: related changes commit together and roll back on failure. Helpers do not commit opportunistically. Serialize required data while the session is available; avoid implicit lazy I/O, inspect N+1 queries and load relationships deliberately.

Enforce uniqueness and invariants with database constraints. Handle races through conditional updates, appropriate locking or isolation, not check-then-insert alone.

## Evolve production data safely

Inspect existing data, volume, active writers, API/event consumers and overlapping application versions before changing schema. Review Alembic output manually, especially renames, defaults, indexes and destructive changes. Apply migrations once through a controlled delivery job; application replicas must not race them.

Use expand, compatible deployment, bounded backfill, verification and later contract removal when live compatibility requires it. For a new required ownership field, introduce a compatible representation, populate existing rows from defensible mappings, report ambiguous rows, then enforce the invariant. Never fabricate ownership to satisfy a constraint. Remove old fields/paths only after their consumers and rollback needs are resolved.

Assess lock acquisition, scans/rewrites, disk/WAL growth and replication lag for the actual PostgreSQL version and operation. Bound lock waits and backfill rate/transactions; define stop conditions. Choose concurrent indexes or staged constraint validation when supported and justified, checking transaction restrictions and failed-operation cleanup. Make backfills resumable and idempotent, preserving concurrent edits with suitable conditions; review samples, totals and business invariants before enforcing constraints.

Exercise upgrades from the previous schema with representative populated data and compatible old/new code where relevant. A tiny local database does not establish large-table timing or lock safety. Separate application rollback, data repair and backup restoration; document irreversible steps and recovery evidence. Keep schema/operating notes current and live execution within task authority. See [sources and exceptions](references/sources-and-exceptions.md) for platform-specific details.

## Bound integrations and concurrency

Set explicit timeouts, payload limits and cancellation behavior. Retry with bounded backoff only when operations are safe/idempotent; verify and deduplicate webhooks. Restrict user-configurable fetch/webhook destinations to prevent SSRF, and bound upload access and resource consumption. Budget database pools across all replicas/workers with reserved headroom, bound queue/concurrent work and apply backpressure. Investigate tail latency, query plans and slow dependencies before increasing workers. Keep slow external calls outside long transactions; remote calls and database commits are not automatically atomic. FastAPI BackgroundTasks suits best-effort work, not critical durable delivery.

## Make durable work recoverable

For work that must survive process loss, persist accepted intent and a stable logical identity before reporting acceptance. Use the project's worker/queue or durable job mechanism; best-effort in-process tasks need not become a distributed system. Define queued/running/succeeded/failed and cancellation/deadline behavior as needed. Accepted work without a terminal record remains visible and requires recovery.

Assume retries and duplicate delivery can occur. Make the business effect idempotent through persisted keys/constraints or supported provider keys; an in-memory set is not restart-safe deduplication. Acknowledge work only after durable progress according to the actual queue's semantics. An expired worker lease does not prove the old worker stopped; prevent overlapping owners from committing conflicting effects when that risk exists. Preserve actor/tenant authority in worker execution.

Retry transient failures with bounded attempts/backoff and a total deadline; reject permanent invalid/auth failures appropriately. A timeout after a remote write is ambiguous: reconcile provider state before repeating the effect. Keep durable progress so a crash after saving a report does not regenerate it or resend its notification blindly. Use an outbox when domain changes and delivery intent must commit atomically; dispatch still needs duplicate handling, not an exactly-once claim.

Keep exhausted/poison work discoverable with reasons, an owner and a controlled replay path. Define cancellation races, external-effect compensation where possible, and manual reconciliation where not. Verify duplicates, restart after partial completion, lost acknowledgments and deadlines with controlled fixtures. Track queue age, stuck work and recovery through the operations guidance when available. Do not add a particular broker or workflow framework without a concrete requirement.

## AI and MCP interfaces

For AI, begin with a direct provider adapter if sufficient; use LangChain/LangGraph or Google ADK when orchestration requires it, without installing both by default. Pair with `build-evaluated-ai` when available. Enforce authorization outside prompts, validate structured outputs, constrain tool authority and bound tokens, audio size/duration, time and retries. Gemini can support experiments, but verify current model availability, quotas and pricing rather than assuming every LLM/STT path is free. Separate deterministic fixtures from live-provider evaluations and include failure/fallback behavior.

For an MCP interface, add the AI plugin and use its standalone FastMCP guidance plus `mcp-builder`. Reuse authorized application services and transaction boundaries; an MCP adapter must not bypass them.

## Deploy FastAPI deliberately

Choose worker processes and replicas from measured concurrency, CPU work and memory; account for each process's clients/pools and large in-memory state. Budget connections across API workers, background workers, rollout surge and migrations. Do not share live pooled connections across process forks; initialize/dispose them through the runtime's supported lifecycle. Keep blocking I/O out of async paths and bound external/pool waits.

Test the built runtime's actual entrypoint and configuration, without development reload. Configure trusted proxy/forwarded headers, request limits and TLS termination for the real hosting boundary. Keep startup validation separate from the once-only migration job. Make readiness reflect ability to serve and liveness avoid restart loops caused solely by a dependency outage. During shutdown stop admission, drain bounded in-flight work, close clients and let durable jobs recover according to their delivery contract. Verify these behaviors in the target platform; a local startup check alone does not prove a rollout.

## Verify observable behavior

Test domain behavior, API contracts, cross-user/tenant denial, transaction rollback, races/idempotency where relevant and migrations against the chosen database. SQLite tests do not establish PostgreSQL behavior. Isolate fixtures and exercise lifespan/startup when affected. Useful checks include reopening persisted data, rejecting unauthorized parent/child access, rolling back partial writes and ensuring duplicate jobs do not duplicate outcomes.

Use the development workflow's relevant E2E/security/delivery guidance and operations skills for recovery/capacity/cost needs. Keep secrets and sensitive data out of logs, while retaining useful correlation diagnostics. Report actual checks and remaining gaps without treating a passing suite as production readiness.

Routine decisions are inline here. Use bundled modern-python for Python tooling and the AI plugin's MCP/framework skills when those interfaces are needed. Consult [sources and exceptions](references/sources-and-exceptions.md) for unfamiliar auth, driver, migration or platform details; verify current APIs when versions matter.

## Preserve API and event consumers

For changed interfaces, identify actual consumers and supported versions: browser clients, jobs, webhooks, MCP tools and event readers. Compare schemas and behavior, including omitted/null fields, enum values, status/error semantics, authorization, ordering/pagination and event meaning. A type-compatible change can still break a consumer; even an added field may break a strict reader. Keep stable operation/event identities and regenerate affected typed clients deliberately.

Use provider validation against OpenAPI plus representative consumer/producer examples and behavior checks. For independently deployed consumers, use consumer-driven contracts when useful; Pact is optional. Fixtures must represent supported real usage and remain aligned with provider verification. Test relevant old/new combinations and retained queued events where applicable. Document intentional breaks and migration/deprecation scope before removing support; do not require a broker or contract-testing platform for a single application.
