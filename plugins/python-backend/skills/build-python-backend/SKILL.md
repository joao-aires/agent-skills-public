---
name: build-python-backend
description: Build or review Python APIs and persistence with uv, FastAPI/Uvicorn, SQLAlchemy, Alembic and PostgreSQL. Use for endpoints, domain behavior, transactions, migrations, authorization, backend tests and optional FastMCP tools.
---

# Build a Python backend

## Choose a coherent baseline

Prefer uv, FastAPI/Uvicorn, Pydantic, SQLAlchemy/Alembic and PostgreSQL for new applications. Preserve an existing stack unless changing it solves an agreed problem. Lock compatible dependencies; use installed `modern-python` guidance and first-party documentation matching the chosen versions. Do not assume a skill exists for the entire stack.

Organize around domain responsibilities. Keep routes concerned with HTTP input, authentication and response mapping; share domain behavior with AI/MCP adapters where useful. Introduce a service/repository boundary when it has a real responsibility, rather than wrapping every operation in layers.

## Make contracts and ownership explicit

- Validate request and response contracts and distinguish malformed input, absent/unauthorized resources, conflicts and provider failures. Follow one error convention without leaking internals or resource existence contrary to project policy.
- Derive user/tenant identity from authenticated context, not a caller-supplied owner ID. Enforce ownership on reads, lists and mutations; UI restrictions are insufficient.
- Use database constraints for invariants that must survive concurrent requests: required relationships, uniqueness and valid values. Choose indexes from actual query patterns rather than speculative optimization.
- Make session lifetime and transaction ownership clear. Treat dependent writes as one unit, roll back failures and avoid accidental partial commits. Choose sync/async deliberately; avoid blocking I/O inside async handlers and sharing a session across concurrent tasks.
- Bound external calls and avoid keeping a database transaction open while waiting for a slow provider where practical. Design retries/idempotency around duplicate side effects when required; do not assume a database commit and remote action are atomic.

For a user-owned saved search, set ownership from the session and scope fetch/delete by authenticated identity. Test user B requesting user A's resource ID directly. For a feature that writes a parent and dependent records, inject a failure between writes and confirm no partial state survives.

## Evolve persistence safely

Review Alembic migrations as code: defaults, nullability, constraints, indexes, backfills, locks and old/new application compatibility where deployment requires it. For existing data, prefer a staged change when adding a new constraint; avoid treating a destructive downgrade as guaranteed recovery. Apply relevant migrations against PostgreSQL, not only an SQLite substitute. Keep the data model/OpenAPI and migration/recovery notes aligned.

Keep secrets in configuration and sensitive data out of logs. Provide actionable errors and useful diagnostics without inventing an observability platform for a small app.

## Add tools only for a need

Use FastMCP when application capabilities must be exposed as tools; use installed `mcp-builder` expertise for protocol/server details. Reuse authorized application logic, expose narrow typed capabilities and choose transport for the actual client/deployment. Treat model/tool arguments as untrusted input; do not let an MCP adapter bypass ownership or transaction rules.

## Establish completion

Run focused domain tests and applicable API/PostgreSQL integration checks for contracts, migrations, rollback and authorization. Verify startup/configuration when affected. Report commands, results and gaps; distinguish stubbed providers from live integration. Use the workflow bundle's documentation/E2E/delivery guidance when installed, and preserve the accepted request as scope without a tracker prerequisite.
