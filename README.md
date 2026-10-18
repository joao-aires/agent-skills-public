# Agent Plugins

I use these skill bundles to build and operate applications and explore product ideas. My local skills capture conventions; bundled upstream skills add specialist techniques. Plugins follow the [Agent Plugins standard](https://agent-plugins.org/specification).

Start with **development-workflow**, **python-backend** and **web-frontend** for a full-stack application. You request an activity such as `develop`, `test` or `review`; the agent uses relevant supporting skills within that work. Add **business-strategy** for product discovery/priorities and business direction. Tickets are optional, and existing project decisions take precedence.

## Choose your plugins

| Plugin | Use it for |
| --- | --- |
| [development-workflow](plugins/development-workflow/) | Development activities, project conventions, testing, Git/PRs, delivery and security |
| [python-backend](plugins/python-backend/) | Python, FastAPI, SQLAlchemy, Alembic and PostgreSQL |
| [web-frontend](plugins/web-frontend/) | Web UI/UX, interface quality, UX writing, usability research, Next.js/shadcn, TypeScript/Tauri desktop and iOS/Android clients |
| [ai-development](plugins/ai-development/) | AI features, agents, evaluations and MCP interfaces |
| [application-operations](plugins/application-operations/) | Reliability, observability, incidents, recovery, capacity and cost |
| [business-strategy](plugins/business-strategy/) | Business strategy, product discovery/priorities and feedback |
| [visual-communication](plugins/visual-communication/) | Architecture diagrams, interactive explorers and presentations |

## Quick start

### 1. Build the bundles

With Git and Python 3.10+ available, run in a POSIX shell:

```bash
git clone https://github.com/joao-aires/agent-skills-public.git
cd agent-skills-public
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-validation.txt
python scripts/build_plugins.py --destination ./built-plugins
export AGENT_PLUGINS_DIR="$(pwd)/built-plugins"
```

If you already have a checkout, start there instead of cloning again. The builder acquires pinned upstream skills and their resources for the three full-stack plugins. The destination must be new. [Additional bundles and rebuilds](documentation/usage.md#build-and-load) use the same builder.

### 2. Load them in your client

Open the target application repository or an empty project workspace, rather than developing inside this skills repository.

<details>
<summary>Copilot CLI</summary>

From the application workspace, in the same terminal:

```bash
copilot \
  --plugin-dir "$AGENT_PLUGINS_DIR/development-workflow" \
  --plugin-dir "$AGENT_PLUGINS_DIR/python-backend" \
  --plugin-dir "$AGENT_PLUGINS_DIR/web-frontend"
```

Append `skill list --json` to inspect discovery without starting a model session. In another terminal, set `AGENT_PLUGINS_DIR` to the absolute build directory first. Session-local loading was checked with CLI 1.0.95; see the [CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) for your version.

</details>

<details>
<summary>Antigravity CLI (agy)</summary>

Install the complete built bundles, then inspect discovery:

```bash
agy plugin install "$AGENT_PLUGINS_DIR/development-workflow"
agy plugin install "$AGENT_PLUGINS_DIR/python-backend"
agy plugin install "$AGENT_PLUGINS_DIR/web-frontend"
agy plugin list --json
```

An earlier installation with 56 skills was checked with `agy` 1.3.5. Authenticate through the client's sign-in flow before model work. The [generation-trial specification](documentation/maintainers/evaluations.md#generation-trials) is harness-independent; `agy` is my local runner choice. Installation does not establish execution behavior.

</details>

<details>
<summary>VS Code</summary>

For versions supporting Agent Plugins, merge the individual absolute paths into user settings:

```json
{
  "chat.plugins.enabled": true,
  "chat.pluginLocations": {
    "/absolute/path/built-plugins/development-workflow": true,
    "/absolute/path/built-plugins/python-backend": true,
    "/absolute/path/built-plugins/web-frontend": true
  }
}
```

Open the application workspace and inspect Configure Skills. This route follows [VS Code documentation](https://code.visualstudio.com/docs/agent-customization/agent-plugins#use-local-plugins); it has not been exercised here.

</details>

For another client, use its documented plugin-loading route. Keep each plugin directory and its resources intact. Discovery establishes availability, not that an agent will follow every instruction. Updating an old installation? Read [migration](documentation/migration.md) first.

### 3. Make a first request

Choose the activity explicitly through the client's skill picker or supported invocation syntax. In VS Code, for example: `/development-workflow:develop`. Plain requests below work where explicit skill selection by name is supported.

| Starting point | Example request |
| --- | --- |
| New idea | Use develop to build a saved-search application. Ask about important decisions, state reversible assumptions and implement a useful first slice. Prepare a PR. |
| Existing application | Use develop to add read-only sharing to saved searches. Preserve the existing architecture, UI and private defaults. |
| Assess current work | Use test to verify the changed journey, then review the diff against the agreed behavior. |

The agent should clarify consequential unknowns, define relevant behavior before coding, verify the result and report evidence or gaps. It proceeds within the requested scope; merge and deployment are separate actions. Use `workflow-help` when unsure where to start.

## How the guidance fits together

Request an activity such as develop, design or review. The agent selects relevant disciplines, including product-management, system-design, visual-design and backend-design, then applies the accepted stack's conventions. Product direction starts before development and evolves with feedback. A defined change reuses accepted context. Plugins package these capabilities; they are not sequential process layers. See [ownership and composition](documentation/maintainer-reference.md#capability-architecture) for the boundaries.

## SDLC coverage

![Seven-phase SDLC: planning, requirements analysis, design, implementation, testing, deployment and maintenance; product discovery feeds the cycle, repair returns to implementation, and product feedback informs discovery, supported by a maintained project baseline, shared methods and matching stack expertise](documentation/images/sdlc-cycle.svg)

`develop` spans the useful cycle. Enter at the activity the work needs, repeat implementation and verification as evidence demands, and reopen affected decisions when product or operational learning changes the context. Project foundations and relevant specialist guidance support the work throughout. The arrows show relationships, not required task invocations or permission to release or deploy.

[Compare typical starting points](documentation/sdlc.md#different-starting-points), [choose an activity](documentation/usage.md#skills-you-invoke) or explore the [linked skill map](documentation/sdlc.md).

## Documentation

| Guide | Question it answers |
| --- | --- |
| [Usage](documentation/usage.md) | What should I invoke, provide and expect? |
| [SDLC coverage](documentation/sdlc.md) | Which skills support each phase and area? |
| [Migration](documentation/migration.md) | How do I update an existing installation? |
| [Maintainer reference](documentation/maintainer-reference.md) | How do I change, validate and evaluate the collection? |

The bundles contain guidance and resources, without generated applications, configured MCP servers or hooks. Client tools and application dependencies are configured separately.

## Contributing

Keep guidance concise and project-independent. Run `python scripts/validate_plugins.py`, `python scripts/check_collection.py` and `python -m unittest discover -s tests -v` after changes. Local material is MIT; upstream resources retain their own licenses. See [AGENTS.md](AGENTS.md) and the [maintainer checks](documentation/maintainer-reference.md#maintaining-the-collection).
