# Local development runbook

Requires Python 3.12, uv 0.12.19, Node 24, pnpm 10.32.1, Docker Compose and a free local 5432/8000/3000. Choose a local-only POSTGRES_PASSWORD, export DATABASE_URL=postgresql+psycopg://notes:<password>@127.0.0.1:5432/notes, WEB_ORIGIN=http://localhost:3000 and COOKIE_SECURE=false. Never reuse local HTTP settings in public hosting.

Start docker compose up -d --wait database. In applications/api: uv sync --frozen; uv run alembic upgrade head; uv run uvicorn notes.main:app --app-dir src --host 127.0.0.1 --port 8000. In applications/web: pnpm install --frozen-lockfile; pnpm dev. Open http://localhost:3000 and create an account. No default seeded passwords. CI uses isolated PostgreSQL service data and synthetic credentials.

Verification: stop manually started API/web first; run API bash ci/check.sh, then web pnpm exec playwright install chromium and bash ci/check.sh. GitHub CI supplies PostgreSQL and installs browser OS dependencies. Generated OpenAPI must match the committed schema (git diff --exit-code). Alembic check rejects model/DDL drift. docker compose down preserves local DB; down -v destroys it intentionally. No deployment/production readiness is claimed. Restore/backup, auth hardening, monitoring and hosting are project-specific follow-ups.

Optional MCP: uv sync --frozen --group mcp; configure NOTES_API_URL and NOTES_SESSION_TOKEN for an authorized session, PYTHONPATH=src; run uv run --group mcp python -m notes.mcp. Local stdio only; never expose this adapter remotely without server auth. ci/mcp_smoke.py verifies a real client round trip when API and explicit session token exist. Secrets stay outside model/tool arguments.

Render optional client configuration with python applications/tooling/mcp_config.py. It scopes shadcn to applications/web and notes to applications/api. Export NOTES_SESSION_TOKEN through the client secret environment first; the renderer never stores a token. shadcn server startup remains separately unverified where registry network access is unavailable. CI separately executes the notes stdio MCP adapter for two isolated identities.
