# Upstream source catalogue

Reviewed 2026-10-05. Selected components are now acquired by `scripts/install_profile.py` using immutable commits and Git tree identities in `upstream.lock.json`. See [installation](installation.md) for packages, notices and runtime limits. Sources absent from the lock remain reference-only.

| Area | Source | Qualification |
| --- | --- | --- |
| React performance, composition, UX review | https://github.com/vercel-labs/agent-skills | First-party Vercel: React practices, composition, web-design-guidelines |
| Next.js | https://github.com/vercel/next.js/tree/canary/skills | Current source; match stable chosen framework release, do not adopt canary as an application dependency |
| shadcn skill | https://ui.shadcn.com/docs/skills | Official; reads actual project configuration |
| shadcn MCP | https://ui.shadcn.com/docs/mcp | Official; configure application path/components.json |
| UI/UX Pro Max | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | Community; constrain to established tokens and patterns |
| Visual exploration | https://github.com/anthropics/skills/tree/main/skills/frontend-design | First-party Anthropic; optional, avoid style drift during cleanup |
| ADK | https://github.com/google/adk-python/tree/main/.agents/skills | First-party agent-builder/architecture skills; review transitive resources |
| LangChain/LangGraph | https://github.com/langchain-ai/langchain-skills | First-party fundamentals/persistence/evaluation; override provider defaults with Gemini |
| Backend template | https://github.com/fastapi/full-stack-fastapi-template | Official reference; SQLModel/Vite defaults differ from requested SQLAlchemy/Next.js |
| FastAPI/Uvicorn/uv | https://fastapi.tiangolo.com/ ; https://www.uvicorn.org/ ; https://docs.astral.sh/uv/ | Official runtime/reference documentation |
| SQLAlchemy/Alembic/PostgreSQL | https://docs.sqlalchemy.org/en/20/ ; https://alembic.sqlalchemy.org/en/latest/ ; https://www.postgresql.org/docs/ | Official persistence documentation |
| FastMCP | https://gofastmcp.com/llms.txt | Official index; no unified backend skill asserted |
| Gemini | https://ai.google.dev/gemini-api/docs/audio ; https://ai.google.dev/gemini-api/docs/pricing ; https://ai.google.dev/gemini-api/docs/rate-limits | Verify selected LLM/audio model and free-tier quota |
| Architecture/ADRs | https://arc42.org/overview/ ; https://c4model.com/diagrams ; https://adr.github.io/madr/ | Recognised structures adapted into lean local templates |

Record source commit/release, selected skills, license, scripts/network behavior and actual install route in project-profile.json. The standard is not a universal dependency installer. Do not redistribute private skills.

Official documented skills CLI examples: `pnpm dlx skills add shadcn/ui`; `npx skills add vercel-labs/agent-skills`; `npx skills add vercel/next.js`. These are upstream alternatives. This repository uses its pinned builder rather than these floating commands.

## Wider development workflow sources

These recommendations are based on first-party provenance, applicability and inspectable workflow—not a claim of universal popularity or benchmark superiority. Selected rows are acquired into built packages; the source checkout retains recipes rather than vendored trees.

| Source / component | Provenance | Priority / fit | Integration limits |
| --- | --- | --- | --- |
| https://github.com/microsoft/playwright-cli | Microsoft/Playwright maintainers | Core browser exploration, test authoring and failure investigation | Use committed Playwright Test suites for CI; CLI exploration alone is not an E2E gate |
| https://playwright.dev/docs/test-agents | Official Playwright planner/generator/healer definitions | Core E2E authoring | Agents are client definitions, not all SKILL.md; healer must preserve accepted assertions |
| https://github.com/anthropics/skills/tree/main/skills/webapp-testing | Anthropic | Alternative helper for local browser work | Avoid overlapping orchestration if Playwright tooling already covers the task |
| https://github.com/trailofbits/skills/tree/main/plugins/modern-python | Trail of Bits | Core Python tooling: uv/Ruff/pytest | Exact backend conventions remain local |
| https://github.com/obra/superpowers/tree/main/skills/systematic-debugging | Superpowers community | Core failure diagnosis | Selectively load; local user instructions and accepted scope apply |
| https://github.com/obra/superpowers/tree/main/skills/verification-before-completion | Superpowers community | Core evidence-based completion | Keep relevant verification fresh; avoid redundant reruns when nothing changed |
| https://github.com/github/awesome-copilot/tree/main/skills/github-actions-hardening | GitHub-hosted community | Pipeline authoring/review | Portable skill; review exact references/version |
| https://github.com/github/awesome-copilot/blob/main/instructions/github-actions-ci-cd-best-practices.instructions.md | GitHub-hosted community | Pipeline design | Instruction file, not a portable skill on its own |
| https://github.com/getsentry/skills/tree/main/skills/code-review | Sentry engineering | Conditional targeted code review | Adapt Sentry-specific conventions; Sentry service is not a mandatory app dependency |
| https://github.com/trailofbits/skills/tree/main/plugins/property-based-testing | Trail of Bits | Conditional domain invariants/calculations/state | High value for financial/model-heavy apps, not blanket coverage bureaucracy |
| https://github.com/trailofbits/skills/tree/main/plugins/insecure-defaults | Trail of Bits | Conditional security-sensitive changes | Audit depth/resource use may be inappropriate for trivial changes |
| https://github.com/trailofbits/skills/tree/main/plugins/differential-review | Trail of Bits | Conditional security review of significant diffs | Select narrowly; not a replacement for auth/integration tests |
| https://github.com/anthropics/skills/tree/main/skills/mcp-builder | Anthropic | MCP tool/API authoring | Maintain requested FastMCP/Python direction and deterministic policy boundaries |
| https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring | Anthropic | Substantive PRD/spec/decision drafting and reader clarity | Do not force collaborative interview steps on routine synchronization |
| https://agents.md/ | Open format reference | Core scoped repository instructions | Not a skill or enforcement engine |

Trail of Bits publishes CC-BY-SA-4.0 guidance. Linking to it does not relicense this repository; acquired components preserve their applicable notices/terms. Check all other sources' licenses at the exact pinned version too.
