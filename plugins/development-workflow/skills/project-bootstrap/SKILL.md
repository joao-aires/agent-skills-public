---
name: project-bootstrap
description: Guide the structure and first implementation of a new application, or organize an existing repository, without imposing a starter template.
---

# Organize an application

- Start with the user's problem, a small useful outcome and clear non-goals. Build a working vertical slice early; add architecture as the product needs it.
- Put application code, migrations, tests, dependencies, application-specific CI/CD and scoped AGENTS.md under `applications/`. Use `api/` and `web/` when those boundaries make sense. Keep provider-required workflow entrypoints where the provider expects them.
- Put product and engineering knowledge under `documentation/`. Use the documentation skill for a lean structure; create documents when there is something useful to record.
- Keep root AGENTS.md short: project purpose, stack, commands and shared conventions. Put local exceptions beside the code. State that documentation must stay synchronized with implementation and decisions.
- Prefer Python/FastAPI/PostgreSQL and Next.js/shadcn for new full-stack projects. Add AI or MCP only for a concrete need. Adapt existing applications deliberately rather than rewriting them to match a preferred layout.
- Use only the skills relevant to the current task. Reuse available upstream expertise and compatible installed UI/UX guidance; do not assume a linked skill is installed or copy private skills into this repository.
- Capture recurring corrections as a brief scoped instruction or a useful check. Keep instructions specific to this project, without duplicating general programming knowledge.
- Make local startup and verification straightforward. Choose compatible dependencies, commit lockfiles and record consequential tradeoffs. Avoid speculative services, layers and abstractions.

Treat these as defaults. Let product requirements and existing decisions determine the implementation.
