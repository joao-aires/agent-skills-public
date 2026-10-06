# Agent Plugins

Reusable bundles of skills for application development, business strategy and visual communication. Our concise Markdown skills describe preferred outcomes and conventions; selected upstream skills provide specialist techniques. The agent chooses implementation details from the request, existing code and accepted decisions.

Packages use [Agent Plugins 1.0.0](https://agent-plugins.org/specification): `plugin.json` and `skills/<name>/SKILL.md`. These are guidance bundles, with no generated application or required project template. Tickets, trackers and elaborate planning workflows are optional.

[Usage guide and example prompts](documentation/usage.md) · [Workflow selection](plugins/development-workflow/WORKFLOW.md) · [Upstream catalogue](documentation/upstream-sources.md)

## What the pieces do

| Piece | Role | Example |
| --- | --- | --- |
| Plugin | Bundles skills related to an activity | `web-frontend` |
| Local skill | Defines our preferred approach | Reuse shadcn components and existing design tokens |
| Upstream skill | Supplies implementation or workflow expertise | Vercel React practices, Matt Pocock's TDD |
| Project `AGENTS.md` | Records the application's commands, conventions and accepted decisions | Keep documentation synchronized with code |
| MCP server | Optionally gives the agent live tools | Browse a shadcn registry or interact with a browser |

Installing a plugin makes skills available; it does not require running every skill. No MCP servers or hooks are configured in the current bundles.

## Bundles

| Plugin | Guidance | Upstream expertise included when built |
| --- | --- | --- |
| `development-workflow` | Project structure, documentation, E2E, delivery, Git contribution flow | Matt Pocock engineering/productivity skills, Playwright, GitHub Actions hardening, Trail of Bits testing/review |
| `python-backend` | Python, uv, FastAPI/Uvicorn, SQLAlchemy/Alembic, PostgreSQL, optional FastMCP | Trail of Bits modern-python; Anthropic MCP builder |
| `web-frontend` | Next.js, shadcn, consistent UI/UX, accessibility and performance | Official shadcn; Vercel React practices and composition |
| `ai-development` | Framework choice, Gemini LLM/audio experiments, evaluation and tool boundaries | Official Google ADK and LangChain/LangGraph skills |
| `business-strategy` | Existing strategy and opportunity-analysis skills | Original resources preserved |
| `visual-communication` | Existing architecture-diagram and presentation skills | Original resources preserved |

For a full-stack application, use workflow + backend + frontend; add AI when needed. Load task-relevant skills rather than every skill at once. The new local skills are concise principles: the agent chooses implementation details from the product, existing code and accepted decisions. Upstream guidance contributes expertise without expanding the requested scope or overriding those decisions. Use compatible installed UI/UX skills locally.

Local development skills include decision rules, examples and proportionate completion criteria: a real persisted journey, resource ownership, deliberate migrations, consistent rendered UI and explicit AI evaluation boundaries. These guide the agent toward observable outcomes while leaving implementation choices open. See [skill evaluation evidence and limits](documentation/skill-evaluation.md).

## Invocation and workflow selection

Our `project-bootstrap` starts only on an explicit request. The seven other local development skills are agent-invoked when relevant and can also be invoked manually. `contribute-with-git` applies by default to feature development and Git/PR work: use a feature worktree, Conventional Commits, optional issue references and concise PR descriptions. Automatic selection helps perform the requested work without expanding its scope.

Matt's released engineering and productivity skills join `development-workflow`, including `implement`, `implement-spec`, their testing/review dependencies, and setup. Preserve his user/agent distinction: user-invoked orchestration is a deliberate choice; agent-invoked guidance is task-matched. See the concise [workflow map](plugins/development-workflow/WORKFLOW.md) for available activities, documentation paths and setup boundaries. No workflow is mandatory for every change. Implementation and review work directly from your request or a Markdown spec/plan; tickets and trackers are optional, including for `implement-spec`.

Native `disable-model-invocation` frontmatter and Codex `agents/openai.yaml` are preserved; our user-invoked project skill supplies both. These are client-specific controls, not a universal Agent Plugins invocation mechanism. Clients without support must rely on the documented explicit-request boundary. Packaging verifies metadata, not runtime discovery in every client.

## Quick start

From the repository root, with Python and Git available, build the full-stack bundles with their upstream skills:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-validation.txt
python scripts/build_plugins.py --destination ./built-plugins
```

This produces `built-plugins/development-workflow`, `built-plugins/python-backend` and `built-plugins/web-frontend`. Install those individual directories through your client's supported plugin route, then open the application repository in that client. Packaging is separate from client installation; no universal client install command is supplied here. The activation command above is for a POSIX shell.

For example, once those plugins are available:

> Use project-bootstrap to start a small Next.js/shadcn and FastAPI/PostgreSQL application for saving named searches. Apply the installed workflow, backend and frontend guidance. Build one useful vertical slice, keep documentation current, and test saving and reopening a search. Use this conversation as the scope; no tickets or tracker.

For an existing application:

> Add deletion of a user's saved searches. Preserve the existing architecture and UI conventions. Verify ownership enforcement and the browser journey, update affected documentation, and report the checks you ran.

See the [usage guide](documentation/usage.md) for AI bundles, planning, debugging, review and optional tools.

## Source checkout versus built plugins

| Form | Contents | Use |
| --- | --- | --- |
| `plugins/<name>` | Local skills and plugin guidance | Install when only our principles are needed |
| `built-plugins/<name>` | Local guidance plus actual pinned upstream skills and resources | Install when upstream expertise is also wanted |

The helper clones the sources listed in [upstream.lock.json](upstream.lock.json), checks directory hashes, copies complete resources and preserves licenses. Existing destinations are never overwritten; choose a new destination for another build. It does not install application dependencies, create projects or configure clients. Upstream updates require changing the reviewed pins and rebuilding.

## Optional tools

MCPs are optional: shadcn for component/registry work, Playwright for browser exploration, and a project's FastMCP server when application tools are needed. Configure them for the actual application and client. No servers or hooks are enabled automatically. Hooks are client-specific extensions; add one only for a concrete recurring need. Skills alone are valid plugins.

## Compatibility and maintenance

The original skills moved from `skills/` into their activity bundles without changing their content. Existing skills-only users can still run `./scripts/sync-skills.sh sync` (`status` and `remove` are also supported). This links local skills only; it does not acquire upstream content or configure MCPs.

```bash
python scripts/validate_plugins.py
python -m unittest discover -s tests -v
```

Keep new guidance concise and project-independent. Local material is MIT; acquired upstream skills retain their own terms. Private installed skills are never redistributed. Native client discovery depends on the client; package validation is not an application test.

| Repository path | Purpose |
| --- | --- |
| `plugins/` | Plugin manifests, local skills and supporting resources |
| `documentation/` | Usage guide and upstream catalogue |
| `upstream.lock.json` | Reviewed upstream acquisition pins |
| `scripts/` | Build, validation and skills-only compatibility helpers |
| `schemas/`, `tests/` | Package schemas and helper regression checks |
| `AGENTS.md` | Instructions for maintaining this repository |
