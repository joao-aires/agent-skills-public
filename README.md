# Agent Plugins

I use these Markdown skill bundles to build and operate applications and explore product ideas. The local skills capture my conventions; upstream skills add specialist techniques. Each bundle follows the [Agent Plugins standard](https://agent-plugins.org/specification): `plugin.json` plus `skills/<name>/SKILL.md`.

For a full-stack application, start with `development-workflow`, `python-backend` and `web-frontend`. Add other bundles as needed.

## Choose your plugins

| Plugin | What it contributes | Included upstream expertise |
| --- | --- | --- |
| [development-workflow](plugins/development-workflow/) | Project conventions, documentation, Git/PRs, testing, CI/CD and security | Matt Pocock, Humanizer, Playwright, GitHub Actions hardening, Trail of Bits |
| [python-backend](plugins/python-backend/) | FastAPI, SQLAlchemy/Alembic, PostgreSQL and optional standalone FastMCP | Modern Python, MCP builder |
| [web-frontend](plugins/web-frontend/) | Next.js, Tailwind v4, shadcn, consistent UI/UX and accessibility | Official shadcn, Tailwind design system, Vercel React/composition |
| [ai-development](plugins/ai-development/) | Model/framework choice, transcription, evaluation and tool boundaries | Google ADK, LangChain/LangGraph |
| [application-operations](plugins/application-operations/) | Recovery, capacity and cost | AKS cost optimization, for Azure AKS only |
| [business-strategy](plugins/business-strategy/) | Strategy, opportunity analysis and product feedback | Original skills and resources |
| [visual-communication](plugins/visual-communication/) | Architecture diagrams and presentations | Original skills and resources |

## Quick start

From this repository, with Python and Git available:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-validation.txt
python scripts/build_plugins.py --destination ./built-plugins
```

The command builds the three full-stack plugins with pinned upstream skills. Load each plugin directory in your client and open the application repository. See [installation and example prompts](documentation/usage.md) for client commands and additional bundles. The activation command above is for a POSIX shell.

> Use project-conventions, frontend-conventions and backend-conventions to build a saved-search application. Implement saving and reopening a search, verify ownership and persistence, and keep affected documentation current. Use this conversation as scope; no tracker is needed.

`frontend-conventions` and `backend-conventions` also accept screenshots, URLs, reference repositories and architecture notes. Use their defaults for new projects and preserve accepted choices in existing ones.

## How guidance works

- **Skills you invoke:** start a deliberate activity, such as `grill-me`, `to-spec`, `implement-spec` or a full project setup.
- **Skills agents use:** guide requested work, such as frontend/backend conventions, testing, documentation and Git contributions. You can also ask for them by name.

See [user-invoked activities](documentation/usage.md#skills-you-invoke) and [agent-used guidance](documentation/usage.md#skills-agents-use-during-your-work) for examples. Actual discovery and invocation depend on the client.

Follow project instructions and accepted decisions when using upstream techniques. Tickets are optional. The bundles provide skills without application templates, configured MCP servers or hooks; add live tools when a task needs them.

## SDLC coverage

![Project foundations, discovery, seven-phase SDLC cycle, product feedback and cross-cutting skills](documentation/images/sdlc-cycle.svg)

The cycle covers planning, requirements analysis, design, implementation, testing, deployment and maintenance. Discovery and product feedback inform it; project foundations and cross-cutting guidance support it. See the [linked skill mapping and coverage gaps](documentation/sdlc.md).

## More detail

- [Usage](documentation/usage.md): loading plugins, invocation and example requests.
- [Workflow selection](plugins/development-workflow/WORKFLOW.md): choosing engineering activities.
- [Upstream catalogue](documentation/upstream-sources.md): included skills, licenses and adaptations.
- [Research notes](documentation/conventions-research.md) and [evaluation evidence](documentation/skill-evaluation.md): provenance and validation limits.

Updating an older installation? The original four skills moved under `plugins/`; the development entry points are now `project-conventions`, `frontend-conventions` and `backend-conventions`. See [migration instructions](documentation/migration.md) before replacing old copies or links.

## Contributing

Keep guidance concise and project-independent. After changes, run:

```bash
python scripts/validate_plugins.py
python -m unittest discover -s tests -v
```

Local material is MIT; upstream resources retain their own licenses. See [AGENTS.md](AGENTS.md) for repository instructions.
