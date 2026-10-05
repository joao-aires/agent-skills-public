# Python API

Use uv, FastAPI/Uvicorn, Pydantic, SQLAlchemy, Alembic, and PostgreSQL. Read the build-python-backend skill when available. Keep src/, tests/, migrations/, container and ci/ files here. Routes/MCP tools delegate to domain services; use explicit request/use-case transaction boundaries. Do not substitute SQLModel or SQLite for the approved persistence stack. Add FastMCP or an AI framework only when enabled in project-profile.json and needed by the product.

Update documentation/architecture/, product requirements and operations guidance when behavior changes. Review migrations and generated API/data contracts; test persistence with PostgreSQL. Configure real commands in project-profile.json.

Use real integration evidence and the E2E contract in documentation/verification/e2e.md. Keep setup and verification commands reproducible locally and in CI.
