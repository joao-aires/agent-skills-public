---
name: project-bootstrap
description: Organize a new or existing application around a useful first slice, scoped AGENTS.md instructions, documentation and verification. Use only when the user explicitly asks to start or organize a project.
---

Read [workflow framing](../../WORKFLOW.md) for skill selection and invocation boundaries.


# Organize an application

## Choose the first outcome

Read the request, existing code and accepted decisions before choosing structure. State the smallest useful user journey and its observable acceptance criteria; carry forward answers already agreed. Resolve ambiguity that changes the product or data boundary, and make reversible implementation choices without another planning ceremony. Use the conversation as scope unless a separate spec is useful; require no tickets or tracker.

Prefer Python/FastAPI/PostgreSQL and Next.js/shadcn for new full-stack projects. Add AI or MCP for a concrete capability. Preserve an existing stack and layout unless changing them solves an agreed problem.

## Establish a small, navigable repository

- Put code, migrations, tests, dependencies, application configuration and scoped AGENTS.md under `applications/`. Separate `api/` and `web/` when they represent actual boundaries. Keep provider-required CI entrypoints in their required locations.
- Put product and engineering knowledge under `documentation/`; use `maintain-documentation` to create only useful documents.
- Keep root AGENTS.md focused on purpose, stack, startup/test commands, shared conventions and the requirement to synchronize affected docs with code and decisions. Put component-specific commands and exceptions beside that component. Link authoritative information instead of duplicating it.
- Record compatible dependencies and lockfiles, required configuration and a safe local setup. Make it possible to start and verify the first slice without guessing secrets or commands.
- Add boundaries, services and infrastructure when a concrete requirement justifies them. Prefer domain-oriented code over layers with no present responsibility.

Use the relevant backend/frontend/AI skills and installed upstream expertise; do not assume a reference is installed. Preserve compatible installed UI/UX guidance without redistributing private material. Capture repeated corrections as a short scoped instruction or an executable check, rather than accumulating generic rules.

## Build and prove a vertical slice

For a saved-search application, start with saving a named filter and reopening it through the UI, API and database. Include ownership enforcement if users have private data. Defer sharing, recommendation agents and a generic workflow engine until requested. Prefer a real useful flow over disconnected mock screens and endpoints.

Finish by showing how to start the application, what journey works, which checks ran and what remains incomplete. Verify the applicable startup, migration and browser/API path; distinguish mocked providers from real integrations. Keep first-slice knowledge and decisions current. Do not describe a scaffold or a successful build alone as a working application.
