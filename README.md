# Agent Plugins

I use these skill bundles to build and operate applications and explore product ideas. My local skills capture conventions; bundled upstream skills add specialist techniques. Plugins follow the [Agent Plugins standard](https://agent-plugins.org/specification).

Start with **development-workflow**, **python-backend** and **web-frontend** for a Python/React application. Keep an existing application's stack and select the matching expertise. You request an activity such as `develop`, `test` or `review`; the agent uses relevant supporting skills within that work. Add **business-strategy** for product discovery/priorities and business direction. Tickets are optional, and existing project decisions take precedence.

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

<a id="1-build-the-bundles"></a>
<a id="2-load-them-in-your-client"></a>

1. [Build complete bundles and load them in your client](documentation/installation.md). The default build includes development-workflow, python-backend and web-frontend. Add other bundles for the work you need.
2. Open the application repository or an empty project workspace and confirm discovery. Keep plugin resources intact; application dependencies and live tools are configured separately.
3. Choose an activity and state the outcome and stopping point.

<a id="3-make-a-first-request"></a>

### Make a first request

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
| [Installation](documentation/installation.md) | How do I build, load and check the bundles? |
| [Usage](documentation/usage.md) | What should I invoke, provide and expect? |
| [SDLC coverage](documentation/sdlc.md) | Which skills support each phase and area? |
| [Migration](documentation/migration.md) | How do I update an existing installation? |
| [Maintainer reference](documentation/maintainer-reference.md) | How do I change, validate and evaluate the collection? |

The bundles contain guidance and resources, without generated applications, configured MCP servers or hooks. Client tools and application dependencies are configured separately.

## Contributing

Keep guidance concise and project-independent. Run `python scripts/validate_plugins.py`, `python scripts/check_collection.py` and `python -m unittest discover -s tests -v` after changes. Local material is MIT; upstream resources retain their own licenses. See [AGENTS.md](AGENTS.md), the [maintainer checks](documentation/maintainer-reference.md#maintaining-the-collection) and [adding support for a tech stack](documentation/maintainers/adding-stack-support.md).
