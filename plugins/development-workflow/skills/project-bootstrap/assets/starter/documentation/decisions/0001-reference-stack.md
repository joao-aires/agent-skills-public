# ADR 0001: reference slice

Status: accepted for development reference.

Use requested Next.js/shadcn and FastAPI/SQLAlchemy/Alembic/Postgres stack. Use opaque DB sessions with Argon2, HttpOnly/SameSite cookies and trusted-origin enforcement; secure cookies default true, explicitly false on local HTTP only. Next proxies requests so the browser sees one origin. Do not add an AI framework until a product use case requires it; direct Gemini smoke scripts evaluate the shared output boundary. Optional read-only stdio MCP delegates authorization to the same API.

Consequences: this proves auth/isolation without external credentials. It is not production identity management: add abuse limits, email verification/recovery and provider/session lifecycle decisions before public deployment.
