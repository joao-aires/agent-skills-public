# Agent Plugins

Activity-oriented bundles of skills for consistent application development, business strategy and visual communication. Packages use [Agent Plugins 1.0.0](https://agent-plugins.org/specification): `plugin.json` and `skills/<name>/SKILL.md`, with optional `mcp.json` when a server is useful.

## Bundles

| Plugin | Guidance | Upstream expertise included when built |
| --- | --- | --- |
| `development-workflow` | Project structure, documentation, E2E, delivery | Playwright, GitHub Actions hardening, Superpowers debugging/verification, Sentry review, Trail of Bits testing/review |
| `python-backend` | Python, uv, FastAPI/Uvicorn, SQLAlchemy/Alembic, PostgreSQL, optional FastMCP | Trail of Bits modern-python; Anthropic MCP builder |
| `web-frontend` | Next.js, shadcn, consistent UI/UX, accessibility and performance | Official shadcn; Vercel React practices and composition |
| `ai-development` | Framework choice, Gemini LLM/audio experiments, evaluation and tool boundaries | Official Google ADK and LangChain/LangGraph skills |
| `business-strategy` | Existing strategy and opportunity-analysis skills | Original resources preserved |
| `visual-communication` | Existing architecture-diagram and presentation skills | Original resources preserved |

For a full-stack application, use workflow + backend + frontend; add AI when needed. Load task-relevant skills rather than every skill at once. The new local skills are concise principles: the agent chooses implementation details from the product, existing code and accepted decisions. Upstream guidance contributes expertise without expanding the requested scope or overriding those decisions. Use compatible installed UI/UX skills locally.

## Use

Install a local-only bundle directly from `plugins/<name>` through your client's supported plugin route. To include upstream skills as well:

```bash
python -m pip install -r requirements-validation.txt
python scripts/build_plugins.py --destination /tmp/development-plugins
```

This builds the three full-stack bundles. To choose other bundles, repeat `--plugin`, for example `--plugin ai-development`. Install the resulting directories through your client. The helper only packages skills: it clones pinned sources, copies their complete resources and preserves licenses. It does not install application dependencies, create projects or configure the client. Existing destinations are never overwritten.

[Upstream catalogue](documentation/upstream-sources.md) · [Exact source pins](upstream.lock.json)

MCPs are optional: shadcn for component/registry work, Playwright for browser exploration, and a project's FastMCP server when application tools are needed. Configure them for the actual application and client. No servers or hooks are enabled automatically. Hooks are client-specific extensions; add one only for a concrete recurring need. Skills alone are valid plugins.

## Compatibility and maintenance

The original skills moved from `skills/` into their activity bundles without changing their content. Existing skills-only users can still run `./scripts/sync-skills.sh sync` (`status` and `remove` are also supported). This links local skills only; it does not acquire upstream content or configure MCPs.

```bash
python scripts/validate_plugins.py
python -m unittest discover -s tests -v
```

Keep new guidance concise and project-independent. Local material is MIT; acquired upstream skills retain their own terms. Private installed skills are never redistributed. Native client discovery depends on the client; package validation is not an application test.
