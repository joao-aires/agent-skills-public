# Upstream skills

The packaging helper copies these selected skill directories at the reviewed commit/tree pins in `upstream.lock.json`, with their complete resources and notices. Source checkouts contain our local guidance; built bundles also contain these upstream skills. Installation does not launch tools or install application frameworks. Select the relevant skill for the task.

| Bundle | Source | Selected skills |
| --- | --- | --- |
| web-frontend | [Vercel](https://github.com/vercel-labs/agent-skills) | React best practices, composition patterns |
| web-frontend | [shadcn](https://github.com/shadcn-ui/ui/tree/main/skills/shadcn) | Official shadcn |
| development-workflow | [Matt Pocock](https://github.com/mattpocock/skills) | Released engineering + productivity skills, including their complete local resources and invocation metadata |
| development-workflow | [Microsoft Playwright](https://github.com/microsoft/playwright-cli) | playwright-cli |
| development-workflow | [GitHub awesome-copilot](https://github.com/github/awesome-copilot/tree/main/skills/github-actions-hardening) | GitHub Actions hardening |
| development-workflow | [Trail of Bits](https://github.com/trailofbits/skills) | property-based-testing, differential-review |
| python-backend | [Trail of Bits](https://github.com/trailofbits/skills/tree/main/plugins/modern-python) | modern-python |
| python-backend | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) | mcp-builder |
| ai-development | [Google ADK](https://github.com/google/adk-python/tree/main/.agents/skills) | adk-agent-builder, adk-architecture |
| ai-development | [LangChain](https://github.com/langchain-ai/langchain-skills) | langchain-fundamentals, langchain-dependencies, langgraph-fundamentals, langgraph-persistence |

Matt's debugging/review skills replace the overlapping Superpowers/Sentry selections. All released engineering/productivity directories are pinned together so internal skill calls remain available; miscellaneous, deprecated and in-progress skills are excluded. Built Matt Markdown gets a pointer to the local workflow guide plus `docs/agents/` → `documentation/engineering/` and `docs/adr/` → `documentation/decisions/adr/` substitutions. Ticket preferences are defined in the plugin workflow guide, which takes precedence over upstream ticket prerequisites; upstream ticket instructions are not patched. Acquisition notices record these adaptations; existing project paths remain authoritative. No scripts or setup are executed during packaging.

These sources are selected for provenance and fit, not a universal popularity ranking. Use the AI skills for the chosen framework, and security/property-based reviews where useful; having a skill available does not make its workflow mandatory for every change. Keep the local stack and accepted design decisions authoritative.

Trail of Bits guidance is CC-BY-SA-4.0; other selected sources are MIT or Apache-2.0 as recorded at their exact pins. Built bundles carry mixed-license notices. Source pinning does not freeze live documentation or commands embedded in upstream guidance.

## Additional references

- [Git worktrees](https://git-scm.com/docs/git-worktree), [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) and [GitHub CLI PR creation](https://cli.github.com/manual/gh_pr_create): contribution mechanics used by the local `contribute-code` skill; no additional MCP server is required.
- [Next.js agent guidance](https://github.com/vercel/next.js/tree/canary/skills): use documentation matching the application's chosen release.
- [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) and [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design): optional design guidance, constrained by existing tokens and direction. Reuse installed skills without copying private content.
- [Vercel web-design-guidelines](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines): reference only; the reviewed source did not declare a redistribution license and fetched floating guidance.
- [FastAPI](https://fastapi.tiangolo.com/), [Uvicorn](https://www.uvicorn.org/), [uv](https://docs.astral.sh/uv/), [SQLAlchemy](https://docs.sqlalchemy.org/en/20/), [Alembic](https://alembic.sqlalchemy.org/), [PostgreSQL](https://www.postgresql.org/docs/) and [FastMCP](https://gofastmcp.com/): first-party implementation documentation; no unified official skill for this entire backend stack is claimed.
- [Gemini audio](https://ai.google.dev/gemini-api/docs/audio), [pricing](https://ai.google.dev/gemini-api/docs/pricing) and [quotas](https://ai.google.dev/gemini-api/docs/rate-limits): verify the actual model and account before live tests.
- [C4](https://c4model.com/), [arc42](https://arc42.org/overview/), [MADR](https://adr.github.io/madr/) and [AGENTS.md](https://agents.md/): lightweight structures for project knowledge and scoped instructions.
- [shadcn MCP](https://ui.shadcn.com/docs/mcp) and [Playwright MCP](https://github.com/microsoft/playwright-mcp): optional live tools configured in the chosen client. Hooks use [client-specific extensions](https://agent-plugins.org/specification#8-client-extensions), not a portable hooks field.
