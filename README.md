# Agent Plugins

I use these skill bundles to build and operate applications and explore product ideas. My local skills capture conventions; bundled upstream skills add specialist techniques. Plugins follow the [Agent Plugins standard](https://agent-plugins.org/specification).

Start with **sdlc** for the full software lifecycle. Add product, interface, backend, AI or technical methods when useful; delivery, operations, security and governance are included in sdlc. Existing project decisions take precedence; tickets are optional.

## Choose your plugins

| Capability | Plugins | Installation choice |
| --- | --- | --- |
| Workflow | [sdlc](plugins/sdlc/), [strategy](plugins/strategy/) | Full SDLC work; business/product direction |
| Application disciplines | [frontend-development](plugins/frontend-development/), [backend-development](plugins/backend-development/), [ai-development](plugins/ai-development/) | Interface methods; service behavior; AI design/testing/operations |
| Supporting capabilities | [documentation](plugins/documentation/), [visualization](plugins/visualization/) | Writing and architecture explanation; diagrams, presentations and explorers |
| Backend/client implementation | [backend-python-development](plugins/backend-python-development/), [frontend-reactjs-development](plugins/frontend-reactjs-development/), [frontend-native-development](plugins/frontend-native-development/) | Accepted Python; React; Tauri/Expo/native implementation |
| Browser extensions | [browser-extension-development](plugins/browser-extension-development/) | Chrome/MV3 architecture, permissions, extension UI, runtime testing and store delivery. |
| AI implementation | [ai-python-development](plugins/ai-python-development/), [ai-adk-development](plugins/ai-adk-development/), [ai-langchain-development](plugins/ai-langchain-development/) | Python/provider/MCP APIs; ADK; LangChain/LangGraph |
| Selected tools/platforms | [development-tooling](plugins/development-tooling/), [operations-platforms](plugins/operations-platforms/) | Bash/testing/CI/container/diagnostics tools; JVM/Kubernetes/AKS |
| Database engineering | [database-development](plugins/database-development/) | Data contracts, consistency, schema evolution and evidence-led performance methods. |
| PostgreSQL implementation | [database-postgresql-development](plugins/database-postgresql-development/) | PostgreSQL development, diagnostics and operating mechanics. |
| Security engineering | [sdlc](plugins/sdlc/) | Identity/access and security/privacy design inside the lifecycle. |
| SaaS applications | [saas-development](plugins/saas-development/) | Tenant/customer and commercial lifecycle, SaaS dashboard design and scoped readiness. |
| Governance and assurance | [sdlc](plugins/sdlc/) | Applicability, accountable controls and GDPR/SOC 2 readiness evidence inside the lifecycle. |
| TypeScript implementation | [typescript-development](plugins/typescript-development/) | Runtime/module/package contracts and TypeScript implementation verification without React. |
| Go implementation | [go-development](plugins/go-development/) | Go module/package, lifecycle, error and verification contracts for services, libraries and CLIs. |

The collection has 9 generic plugins and 12 technical plugins. Technical expertise applies only to matching accepted choices. No plugin requires installing another; an activity retains its outcome when optional guidance is absent.

## Quick start

<a id="1-build-the-bundles"></a>
<a id="2-load-them-in-your-client"></a>

Install the published **sdlc** bundle, then add other capabilities as needed. The generated `claude-marketplace` branch contains complete bundles and catalogs for both clients.

**Claude Code**

```bash
claude plugin marketplace add joao-aires/agent-skills-public#claude-marketplace
claude plugin install sdlc@agent-skills-public
```

**Codex**

```bash
codex plugin marketplace add joao-aires/agent-skills-public --ref claude-marketplace
```

Open the plugin browser in a supported Codex client, install sdlc from Agent Skills Public, then start a new session. Open the application repository and confirm discovery before beginning work.

[Installation and updates](documentation/installation.md) covers local builds, ChatGPT desktop, OpenCode, Pi, VS Code and other clients. It also explains marketplace refresh versus installed-plugin updates. If published output is unavailable, use the local-build route.

<a id="3-make-a-first-request"></a>

### Make a first request

Choose the activity explicitly: `/sdlc:develop` in Claude Code, or `develop` through Codex's skill picker. See [client setup and compatibility](documentation/installation.md#load-them-in-your-client) first. Plain requests below work where explicit skill selection by name is supported.

| Starting point | Example request |
| --- | --- |
| New idea | Use develop to build a saved-search application. Ask about important decisions, state reversible assumptions and implement a useful first slice. Prepare a PR. |
| Existing application | Use develop to add read-only sharing to saved searches. Preserve the existing architecture, UI and private defaults. |
| Assess current work | Use test to verify the changed journey, then review the diff against the agreed behavior. |

The agent should clarify consequential unknowns, define relevant behavior before coding, verify the result and report evidence or gaps. It proceeds within the requested scope; merge and deployment are separate actions. Use the `activity-system` help mode when unsure where to start.

## How the guidance fits together

Request the activity and stopping point. The agent seeks relevant expertise by capability and applies technical guidance only to the accepted stack. Specialists improve the work when available; without them, the activity still owns its outcome and uses project evidence, general expertise and appropriate primary sources. Missing execution tools remain a distinct verification limit.

Plugins package capabilities; they are not dependency layers. Read [architecture and composition](documentation/architecture.md) for selection, fallback and the independent package boundaries.

## SDLC coverage

The [engineering artifacts and workspaces guide](documentation/artifact-workflow.md) shows how to record an engineering change, share a standalone research result and hand off work through an issue or PR. It links the artifact model, planes, homes, contracts, shared quality bar, workspace choices and proposed versus implemented diagram guidance. The [artifact system design note](plugins/sdlc/README.md) explains why code, tests, docs and change records are all artifacts with distinct authority, homes and evidence.


![Seven SDLC phases from project planning through maintenance, with feedback and shared expertise](documentation/images/sdlc-cycle.svg)

`develop` spans the useful cycle. Enter at the activity the work needs, repeat implementation and verification as evidence demands, and reopen affected decisions when product or operational learning changes the context. Project foundations and relevant specialist guidance support the work throughout. The arrows show outcome dependencies and feedback, not required task invocations or permission to release or deploy. Start with `plan` when deciding what to pursue, `refine` for requirements, or `develop` when you want an authorized end-to-end result; implementation preparation follows the relevant design decisions.

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

For new visual products or expressive web experiences, see [creative interface design](documentation/creative-interface.md): bundled design methods, discovery and feedback, implementation mechanisms and evidence-based acceptance.
