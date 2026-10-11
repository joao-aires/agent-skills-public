# Upstream skills

Built plugins include the sources below at the commit/tree pins in [upstream.lock.json](../upstream.lock.json), with complete resources and license notices. Local-only checkouts do not contain acquired upstream skills. Sources are selected for provenance and fit; see [conventions research](conventions-research.md) for adoption evidence and exclusions.

| Bundle | Source | Selected skills |
| --- | --- | --- |
| web-frontend | [Vercel](https://github.com/vercel-labs/agent-skills) | React best practices, composition patterns |
| web-frontend | [shadcn](https://github.com/shadcn-ui/ui/tree/main/skills/shadcn) | Official shadcn |
| web-frontend | [Wshobson](https://github.com/wshobson/agents/tree/46891e7e60da0e52baf1050b7b6391b64e84c6d9/plugins/frontend-mobile-development/skills/tailwind-design-system) | Tailwind design system (v4; preserve existing project versions) |
| development-workflow | [Matt Pocock](https://github.com/mattpocock/skills) | Released engineering + productivity skills, including their complete local resources and invocation metadata |
| development-workflow | [Microsoft Playwright](https://github.com/microsoft/playwright-cli) | playwright-cli |
| development-workflow | [GitHub awesome-copilot](https://github.com/github/awesome-copilot/tree/main/skills/github-actions-hardening) | GitHub Actions hardening |
| development-workflow | [Trail of Bits](https://github.com/trailofbits/skills) | property-based-testing, differential-review, supply-chain-risk-auditor |
| application-operations | [Microsoft Azure AKS-Skills](https://github.com/Azure/AKS-Skills/tree/20bf35201a79b324d2ca3e00e5c82020ff362024/skills/aks-cost-optimization) | aks-cost-optimization with its six references; applies only to AKS |
| python-backend | [Trail of Bits](https://github.com/trailofbits/skills/tree/main/plugins/modern-python) | modern-python |
| python-backend | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) | mcp-builder |
| ai-development | [Google ADK](https://github.com/google/adk-python/tree/main/.agents/skills) | adk-agent-builder, adk-architecture |
| ai-development | [LangChain](https://github.com/langchain-ai/langchain-skills) | langchain-fundamentals, langchain-dependencies, langgraph-fundamentals, langgraph-persistence |

## How they fit our conventions

- Local guidance and accepted project choices govern implementation. Frontend sources receive a `frontend-conventions` pointer; backend sources receive a `backend-conventions` pointer, including Python/standalone FastMCP preference and the SDK distinction.
- Matt's released engineering/productivity skills are acquired as a complete dependency group; deprecated, experimental and miscellaneous skills are excluded. They retain their invocation metadata and receive a pointer to [workflow framing](../plugins/development-workflow/WORKFLOW.md). Tickets are optional; setup runs only on request.
- Matt's built documentation paths map `docs/agents/` to `documentation/engineering/` and `docs/adr/` to `documentation/decisions/adr/`. Existing project paths remain authoritative. PR attribution is preserved as standard string metadata.
- `differential-review` uses its included adversarial methodology rather than dispatching an unavailable registered agent. `supply-chain-risk-auditor` retains its scripts/lockfile; its pinned parser does not cover pnpm/yarn, so missing coverage is not a clean audit.
- AKS cost guidance applies only to Azure AKS. General operations skills select the actual cloud/service and its current first-party documentation; they do not import an operator runtime or assume one platform.

Adaptations are recorded in the lockfile and built notices. Packaging checks hashes and copies resources without executing scripts. Embedded live documentation and commands are not frozen by source pinning. Trail of Bits skills are CC-BY-SA-4.0; other included sources are MIT or Apache-2.0 as recorded at their pins. Built bundles carry mixed-license notices; private installed material is not redistributed.

## Additional references

- [Git worktrees](https://git-scm.com/docs/git-worktree), [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) and [GitHub CLI PR creation](https://cli.github.com/manual/gh_pr_create): contribution mechanics used by the local `contribute-code` skill; no additional MCP server is required.
- [Next.js agent guidance](https://github.com/vercel/next.js/tree/canary/skills): use documentation matching the application's chosen release.
- [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) and [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design): optional design guidance, constrained by existing tokens and direction. Reuse installed skills without copying private content.
- [Vercel web-design-guidelines](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines): reference only; the reviewed source did not declare a redistribution license and fetched floating guidance.
- [FastAPI](https://fastapi.tiangolo.com/), [Uvicorn](https://www.uvicorn.org/), [uv](https://docs.astral.sh/uv/), [SQLAlchemy](https://docs.sqlalchemy.org/en/20/), [Alembic](https://alembic.sqlalchemy.org/), [PostgreSQL](https://www.postgresql.org/docs/) and [FastMCP](https://gofastmcp.com/): first-party implementation documentation; no unified official skill for this entire backend stack is claimed.
- [Gemini audio](https://ai.google.dev/gemini-api/docs/audio), [pricing](https://ai.google.dev/gemini-api/docs/pricing) and [quotas](https://ai.google.dev/gemini-api/docs/rate-limits): verify the actual model and account before live tests.
- [C4](https://c4model.com/), [arc42](https://arc42.org/overview/), [MADR](https://adr.github.io/madr/) and [AGENTS.md](https://agents.md/): lightweight structures for project knowledge and scoped instructions.
- [shadcn MCP](https://ui.shadcn.com/docs/mcp) and [Playwright MCP](https://github.com/microsoft/playwright-mcp): optional live tools configured in the chosen client. Hooks use [client-specific extensions](https://agent-plugins.org/specification#8-client-extensions), not a portable hooks field.

## Reference-only selections

[Amplitude analyze-feedback](https://github.com/amplitude/builder-skills/tree/51838c2d85560466d1bbc174ea0e645bb9c44ea9/analytics-skills/skills/analyze-feedback) depends on Amplitude MCP and had no explicit redistribution license at the reviewed pin. It is not acquired or configured; our feedback guide works with existing evidence. Vercel web-design-guidelines is also reference-only for its undeclared redistribution license and floating guideline fetch.

The operations skills link to PostgreSQL, Kubernetes, CloudNativePG, Velero and cloud-provider docs for contextual implementation. Security guidance uses OWASP and applicable authoritative privacy rules; it does not establish compliance. The [SDLC mapping](sdlc.md) follows a seven-phase split; different models may group planning and analysis together.
