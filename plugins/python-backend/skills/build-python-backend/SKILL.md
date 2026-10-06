---
name: build-python-backend
description: Guide Python backend development with FastAPI, Uvicorn, SQLAlchemy, Alembic, PostgreSQL and optional FastMCP.
---

# Build a Python backend

- Prefer Python with uv, FastAPI/Uvicorn, Pydantic, SQLAlchemy and Alembic over PostgreSQL for new applications. Use compatible maintained versions and lock dependencies; preserve an existing stack unless a change is justified.
- Keep routes focused on HTTP concerns and organize code around the domain. Share business logic across HTTP, AI and MCP adapters where useful, without imposing layers on simple features.
- Make database session and transaction ownership clear. Be deliberate about sync/async code; avoid blocking work inside async handlers.
- Validate inputs and enforce authorization at the resource boundary. Keep secrets in configuration, avoid sensitive logs and use bounded external calls.
- Review migrations for data, constraints, indexes and deployment compatibility. Verify relevant persistence behavior against PostgreSQL and keep OpenAPI/data-model documentation current.
- Add FastMCP only when tools are needed. Expose narrow, typed capabilities with explicit authorization, reuse application logic and choose transport for the actual client/deployment needs.
- Use focused tests for domain behavior and integration tests for contracts, migrations and authorization. Use available modern-python guidance and first-party stack documentation for implementation details.

Choose the simplest structure that makes the application easy to change and operate.
