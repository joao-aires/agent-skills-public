---
name: project-conventions
description: Establish or maintain an application repository's structure, stack constraints, scoped AGENTS.md, local setup and delivery conventions. Use when explicitly asked to start, organize or review a project, or when the requested change affects those foundations; keep ordinary feature work within existing conventions.
---

Read [workflow framing](../../WORKFLOW.md) for skill selection and invocation boundaries.


# Establish and maintain project conventions

## Match the requested change

Read the request, existing code and accepted decisions before choosing structure. For a new project, establish a useful first slice. For an existing application, identify which foundation the requested change actually affects and update only that part; do not repeat setup or start a repository-wide reorganization during ordinary feature work. State the smallest useful user journey and its observable acceptance criteria; carry forward answers already agreed. Resolve ambiguity that changes the product or data boundary, and make reversible implementation choices without another planning ceremony. Use the conversation as scope unless a separate spec is useful; require no tickets or tracker.

Prefer Python/FastAPI/PostgreSQL and Next.js/shadcn for new full-stack projects. Add AI or MCP for a concrete capability. Preserve an existing stack and layout unless changing them solves an agreed problem.

## Establish a small, navigable repository

- Put code, migrations, tests, dependencies, application configuration and scoped AGENTS.md under `applications/`. Separate `api/` and `web/` when they represent actual boundaries. Keep provider-required CI entrypoints in their required locations.
- Put product and engineering knowledge under `documentation/`; use `maintain-documentation` to create only useful documents.
- Keep root AGENTS.md focused on purpose, stack, startup/test commands, shared conventions and the requirement to synchronize affected docs with code and decisions. Put component-specific commands and exceptions beside that component. Link authoritative information instead of duplicating it.
- Record compatible dependencies and lockfiles, required configuration and a safe local setup. Make it possible to start and verify the first slice without guessing secrets or commands.
- Add boundaries, services and infrastructure when a concrete requirement justifies them. Prefer domain-oriented code over layers with no present responsibility.

Use the relevant backend/frontend/AI skills and installed upstream expertise; do not assume a reference is installed. Preserve compatible installed UI/UX guidance without redistributing private material. Capture repeated corrections as a short scoped instruction or an executable check, rather than accumulating generic rules.

## Include operating constraints in design

Use `design-secure-features` for changed data flows and authority boundaries. Identify critical latency/concurrency constraints, durable state and meaningful recovery needs early; choose simple hosting that meets them. Bring capacity, cost and data-recovery guidance into design when relevant rather than treating them as production afterthoughts. Use `build-delivery-pipelines` when creating CI/CD. Do not introduce platforms or complete operations frameworks merely because their skills are available.

## Keep foundations aligned as the project evolves

Treat repository structure, dependency/runtime choices, configuration contracts, scoped instructions and delivery commands as maintained project decisions. Update affected commands, lockfiles and authoritative documentation alongside a relevant change. Resolve conflicting instructions at their proper scope; avoid copying the same rules into every component. Use `maintain-documentation` for knowledge upkeep and `build-delivery-pipelines` plus installed GitHub Actions hardening for delivery mechanics; this skill coordinates the project conventions rather than duplicating specialist guidance.

Start a full setup or structural review only when requested. Apply existing conventions during feature work, and suggest a broader change when a concrete problem warrants it rather than silently migrating the application.

## Prove the affected capability

For a saved-search application, start with saving a named filter and reopening it through the UI, API and database. Include ownership enforcement if users have private data. Defer sharing, recommendation agents and a generic workflow engine until requested. Prefer a real useful flow over disconnected mock screens and endpoints.

Finish by showing how to start the application, what journey works, which checks ran and what remains incomplete. Verify the applicable startup, migration and browser/API path; distinguish mocked providers from real integrations. Keep first-slice knowledge and decisions current. Do not describe a scaffold or a successful build alone as a working application.
