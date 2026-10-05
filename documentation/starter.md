# Runnable reference starter

Generate a new/empty project:

```bash
python plugins/development-workflow/skills/project-bootstrap/scripts/scaffold.py /path/to/project --starter
```

The application is bundled inside project-bootstrap assets, keeping the plugin self-contained. Default scaffolding remains documentation/governance only. The starter copies code and frozen locks; it neither installs dependencies nor starts services. Read the generated runbook, set local DB configuration, run setup, then dev. The same API/web scripts run in generated-project CI and the repository's generated-starter CI.

The reference is a private Project Notes journey using Next.js/shadcn → FastAPI/Uvicorn → SQLAlchemy/Alembic/Postgres. It includes Argon2 passwords, opaque expiring/revocable sessions, secure-by-default cookies, trusted-Origin checks and owner-filtered queries. Playwright proves browser persistence after reload/relogin and second-account denial; API tests add revoked-session, invalid-login/input and origin checks. OpenAPI and frontend types are generated and drift-checked; migrations are explicit and ORM drift-checked.

Optional extras: `uv sync --frozen --group ai` enables bounded explicit Gemini LLM/audio smoke checks. `--group mcp` enables a local read-only FastMCP adapter that delegates to the same authenticated API; CI checks two isolated session identities over actual stdio. A project helper renders opt-in client configuration for notes and pinned shadcn MCP. No live Gemini or native client invocation is inferred from config or deterministic tests. ADK/LangChain remain selectable specialist packages when an application needs a framework; neither is added unnecessarily to this simple reference slice.

Compatibility decisions: Node 24, Python 3.12, frozen uv/pnpm locks; Next production build uses webpack. ESLint 10 uses official @eslint/compat for legacy rule APIs in Next's current React/accessibility plugins, preserving enabled checks. Source TypeScript is strict; standard skipLibCheck avoids third-party declaration incompatibilities. Official shadcn components are copied from a pinned source commit with MIT notice and import-adaptation provenance because the registry endpoint was unavailable in this workspace. Existing private design skills stay local and are selected through the inventory/routing helper.

Readiness: development reference, never production identity infrastructure. Public signup needs abuse limits, email verification/recovery and hosting/session lifecycle decisions. Deployment/restore/monitoring choices remain project-specific. Local production-build/lint/type evidence and GitHub actual-database/browser/MCP evidence are reported in the PR; live Gemini/audio and actual user coding-client discovery remain separate gates.
