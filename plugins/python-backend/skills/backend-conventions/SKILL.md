---
name: backend-conventions
description: Build, extend or review Python/FastAPI systems with SQLAlchemy, Alembic, contextual persistence, auth, API contracts, jobs and optional AI/FastMCP. Use for backend architecture, endpoints, migrations, transactions, integrations and verification; accept reference systems and preserve established project constraints.
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

## Organize behavior and contracts

Keep application code, migrations, tests and runtime configuration within the application's boundary. Group routes, schemas, behavior and persistence by domain where useful. Share genuinely cross-cutting auth, database and configuration concerns. Routes translate HTTP and delegate substantive behavior; services/repositories exist for real responsibilities, not a layer quota. Inject authentication, sessions and integrations. Manage shared clients through lifespan and close them cleanly. Validate configuration at startup, inject secrets through the deployment environment, and provide proportionate health/readiness checks with graceful shutdown.

Separate public input/output schemas from ORM models. Allowlist mutable fields; never mass-assign ownership, roles or internal state. Publish coherent OpenAPI with stable operation IDs and generate frontend types where useful. Use resource-oriented URLs, correct HTTP status semantics, bounded pagination and allowlisted filters/sorts. Return predictable errors and useful field validation; retain FastAPI's validation shape unless deliberately mapping a documented alternative. Include correlation IDs without leaking internals.

Use timezone-aware UTC timestamps at persistence boundaries, explicit units, and Decimal or integer minor units for money. Version APIs at actual compatibility boundaries rather than reflexively versioning every route.

## Treat identity and authority as separate concerns

Reuse the established identity provider or maintained library. For new externally authenticated applications, prefer OIDC authorization code with PKCE and an appropriate server/session boundary. Choose secure cookies/BFF or bearer tokens for the actual client; do not invent an identity system by default. Cookies need HttpOnly, Secure and deliberate SameSite settings, plus CSRF protection for authenticated mutations. Restrict CORS; CORS is not CSRF protection. Avoid long-lived browser tokens in local storage.

Validate token signature with an explicit algorithm allowlist, trusted issuer/key source, audience and expiry; define session/token revocation as required. If local passwords are needed, use Argon2 through a maintained implementation such as pwdlib, verification/recovery and abuse controls. PyJWT handles tokens, not the whole identity lifecycle.

Derive identity and verified tenant membership from authentication. Enforce ownership/permissions on reads, lists, writes, jobs, exports and tool calls. Never trust caller-supplied owner/tenant fields alone. Apply a consistent 403/404 policy without leaking resource existence. Prompts, hidden UI controls and object IDs do not grant authority.

## Make persistence and migrations intentional

Prefer PostgreSQL for shared relational production data. SQLite fits appropriate local/single-writer contexts; other databases require workload or platform justification. Add Redis for a real cache, queue or coordination need, with expiry/ownership semantics; use object storage for uploads with explicit size/type/access limits. Preserve suitable existing database choices.

Use one session per request, job or concurrent task; never share an AsyncSession across concurrent tasks or keep a global mutable session. The operation owns its transaction: related changes commit together and roll back on failure. Helpers do not commit opportunistically. Serialize required data while the session is available; avoid implicit lazy I/O, inspect N+1 queries and load relationships deliberately.

Enforce uniqueness and invariants with database constraints. Handle races through conditional updates, appropriate locking or isolation, not check-then-insert alone. Review Alembic output manually, especially renames, defaults, backfills, indexes and destructive changes. Apply migrations once through a controlled delivery job rather than racing application replicas. Use expand/contract for live compatibility; test upgrades and plan code rollback separately from data recovery. Keep schema/decision documentation aligned.

## Bound integrations, concurrency and AI

Set explicit timeouts, payload limits and cancellation behavior. Retry with bounded backoff only when operations are safe/idempotent; verify and deduplicate webhooks. Restrict user-configurable fetch/webhook destinations to prevent SSRF, and bound upload access and resource consumption. Budget database pools across all replicas/workers with reserved headroom, bound queue/concurrent work and apply backpressure. Investigate tail latency, query plans and slow dependencies before increasing workers. Keep slow external calls outside long transactions; remote calls and database commits are not automatically atomic. FastAPI BackgroundTasks suits best-effort work, not critical durable delivery.

For AI, begin with a direct provider adapter if sufficient; use LangChain/LangGraph or Google ADK when orchestration requires it, without installing both by default. Pair with `build-evaluated-ai` when available. Enforce authorization outside prompts, validate structured outputs, constrain tool authority and bound tokens, audio size/duration, time and retries. Gemini can support experiments, but verify current model availability, quotas and pricing rather than assuming every LLM/STT path is free. Separate deterministic fixtures from live-provider evaluations and include failure/fallback behavior.

Prefer Python with the standalone `fastmcp` package where an MCP interface is needed: install with `uv add fastmcp`, import `from fastmcp import FastMCP`, and pin a tested compatible version for production. Use typed narrow tools, authenticated transport and the same application authorization/business services. The MCP SDK's `from mcp.server.fastmcp import FastMCP` is a different implementation/API surface: do not mix its examples, imports, Context or auth/transport options with standalone FastMCP. Use version-matched standalone docs to adapt upstream examples; inspect lifecycle, auth and transport behavior rather than blindly changing imports. The MCP builder's TypeScript recommendation does not override this Python preference. Preserve an existing SDK-based server until a migration is in scope. Do not expose unrestricted database or shell access as a convenience tool.

## Verify observable behavior

Test domain behavior, API contracts, cross-user/tenant denial, transaction rollback, races/idempotency where relevant and migrations against the chosen database. SQLite tests do not establish PostgreSQL behavior. Isolate fixtures and exercise lifespan/startup when affected. Useful checks include reopening persisted data, rejecting unauthorized parent/child access, rolling back partial writes and ensuring duplicate jobs do not duplicate outcomes.

Use the development workflow's relevant E2E/security/delivery guidance and operations skills for recovery/capacity/cost needs. Keep secrets and sensitive data out of logs, while retaining useful correlation diagnostics. Report actual checks and remaining gaps without treating a passing suite as production readiness.

Routine decisions are inline here. Use bundled modern-python/MCP-builder skills and the AI plugin's official framework skills for specialist work. Consult [sources and exceptions](references/sources-and-exceptions.md) for unfamiliar auth, driver, migration or platform details; verify current APIs when versions matter.
