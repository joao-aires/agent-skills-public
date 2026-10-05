# Verification strategy

Ruff/mypy and TypeScript guard source quality; API tests exercise actual PostgreSQL auth/state; Alembic upgrade/check guard migration/ORM alignment; OpenAPI regeneration guards API docs; Playwright verifies integrated production frontend. Optional live AI and actual MCP have separate evidence. Structural checker is never application correctness proof.
