# Agent Plugins

I use these skill bundles to build and operate applications and explore product ideas. My local skills capture conventions; bundled upstream skills add specialist techniques. Plugins follow the [Agent Plugins standard](https://agent-plugins.org/specification).

Start with **development** for stack-independent development activities. Add product, interface, backend, AI, delivery or operations methods when useful, and select technical expertise explicitly. Existing project decisions take precedence; tickets are optional.

## Choose your plugins

| Capability | Plugins | Installation choice |
| --- | --- | --- |
| Workflow | [development](plugins/development/), [strategy](plugins/strategy/), [operations](plugins/operations/) | SDLC work; business/product direction; running-system work |
| Application disciplines | [frontend-development](plugins/frontend-development/), [backend-development](plugins/backend-development/), [ai-development](plugins/ai-development/), [delivery](plugins/delivery/) | Interface methods; service behavior; evaluated AI/protocols; CI/release/deployment methods |
| Supporting capabilities | [documentation](plugins/documentation/), [visualization](plugins/visualization/) | Writing and architecture explanation; diagrams, presentations and explorers |
| Backend/client implementation | [backend-python-development](plugins/backend-python-development/), [frontend-reactjs-development](plugins/frontend-reactjs-development/), [frontend-native-development](plugins/frontend-native-development/) | Accepted Python; React; Tauri/Expo/native implementation |
| AI implementation | [ai-python-development](plugins/ai-python-development/), [ai-adk-development](plugins/ai-adk-development/), [ai-langchain-development](plugins/ai-langchain-development/) | Python/provider/MCP APIs; ADK; LangChain/LangGraph |
| Selected tools/platforms | [development-tooling](plugins/development-tooling/), [operations-platforms](plugins/operations-platforms/) | Bash/testing/CI/container/diagnostics tools; JVM/Kubernetes/AKS |

The first nine plugins are generic. The other eight provide technical expertise only for matching accepted choices. No plugin requires installing another; an activity retains its outcome when optional guidance is absent.

## Quick start

<a id="1-build-the-bundles"></a>
<a id="2-load-them-in-your-client"></a>

1. [Build complete bundles and load them in your client](documentation/installation.md). The default build includes development only. Add other bundles for the work you need.
2. Open the application repository or an empty project workspace and confirm discovery. Keep plugin resources intact; application dependencies and live tools are configured separately.
3. Choose an activity and state the outcome and stopping point.

<a id="3-make-a-first-request"></a>

### Make a first request

Choose the activity explicitly: `/development:develop` in Claude Code, `develop` through Codex's skill picker, or `@develop` in OpenCode V2. See [client setup and compatibility](documentation/installation.md#load-them-in-your-client) first. Plain requests below work where explicit skill selection by name is supported.

| Starting point | Example request |
| --- | --- |
| New idea | Use develop to build a saved-search application. Ask about important decisions, state reversible assumptions and implement a useful first slice. Prepare a PR. |
| Existing application | Use develop to add read-only sharing to saved searches. Preserve the existing architecture, UI and private defaults. |
| Assess current work | Use test to verify the changed journey, then review the diff against the agreed behavior. |

The agent should clarify consequential unknowns, define relevant behavior before coding, verify the result and report evidence or gaps. It proceeds within the requested scope; merge and deployment are separate actions. Use `workflow-help` when unsure where to start.

## How the guidance fits together

Request the activity and stopping point. The agent seeks relevant expertise by capability and applies technical guidance only to the accepted stack. Specialists improve the work when available; without them, the activity still owns its outcome and uses project evidence, general expertise and appropriate primary sources. Missing execution tools remain a distinct verification limit.

Plugins package capabilities; they are not dependency layers. Read [architecture and composition](documentation/architecture.md) for selection, fallback and the independent package boundaries.

## SDLC coverage

![Seven-phase SDLC: planning, requirements analysis, design, implementation, testing, deployment and maintenance; product discovery feeds the cycle, repair returns to implementation, and product feedback informs discovery, supported by a maintained project baseline, shared methods and matching stack expertise](documentation/images/sdlc-cycle.svg)

`develop` spans the useful cycle. Enter at the activity the work needs, repeat implementation and verification as evidence demands, and reopen affected decisions when product or operational learning changes the context. Project foundations and relevant specialist guidance support the work throughout. The arrows show relationships, not required task invocations or permission to release or deploy.

[Compare typical starting points](documentation/sdlc.md#different-starting-points), [choose an activity](documentation/usage.md#skills-you-invoke) or explore the [linked skill map](documentation/sdlc.md).

## Documentation

| Guide | Question it answers |
| --- | --- |
| [Installation](documentation/installation.md) | How do I build, load and check the bundles? |
| [Usage](documentation/usage.md) | What should I invoke, provide and expect? |
| [Architecture](documentation/architecture.md) | How do skills compose, and what happens when expertise is absent? |
| [SDLC coverage](documentation/sdlc.md) | Which skills support each phase and area? |
| [Migration](documentation/migration.md) | How do I update an existing installation? |
| [Maintainer reference](documentation/maintainer-reference.md) | How do I change, validate and evaluate the collection? |

The bundles contain guidance and resources, without generated applications, configured MCP servers or hooks. Client tools and application dependencies are configured separately.

## Contributing

Keep guidance concise and project-independent. Run `python scripts/validate_plugins.py`, `python scripts/check_collection.py` and `python -m unittest discover -s tests -v` after changes. Local material is MIT; upstream resources retain their own licenses. See [AGENTS.md](AGENTS.md), the [maintainer checks](documentation/maintainer-reference.md#maintaining-the-collection) and [adding support for a tech stack](documentation/maintainers/adding-stack-support.md).
