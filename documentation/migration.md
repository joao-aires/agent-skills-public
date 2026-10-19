# Migrating existing installations

Existing applications can keep their layout, accepted stack and tracker choices. Update the installed guidance and any explicit skill references using the steps below.

## Update your installation

1. Preserve custom edits and inspect the origin of existing copies or links.
2. Update the checkout, then [build the desired bundles](installation.md#select-additional-bundles) into a new destination. Source directories include local skills only; built bundles also contain upstream resources and notices.
3. Replace affected plugins through your client's supported route, keeping their resources intact. For manually copied skills, replace complete directories.
4. Update saved prompts, project instructions and automation references using the name table below. Inspect and remove obsolete copies/managed links from this checkout; preserve unrelated installations.
5. Check client discovery and try a relevant explicit activity. Building packages alone does not install plugins or configure live tools.

For the legacy skills-only helper, run `./scripts/sync-skills.sh status`, then `./scripts/sync-skills.sh sync`. It repairs unchanged-name links from this checkout's old `skills/` paths in `~/.agents/skills`, including broken links, while preserving unrelated paths. It adds available local skills only. Keep the checkout in place. The helper does not migrate renamed basenames or update copied directories/other checkouts; inspect and clean up those old entries manually.

## Plugin package split

Skill names are unchanged. Plugin identities and ownership change, so replace superseded installations instead of loading old and new copies together. Plugin-qualified saved invocations such as `/development-workflow:test` become `/development:test` where the client supports that syntax. Bare skill selection keeps its name.

| Previous bundle | Replacement choices |
| --- | --- |
| development-workflow | development; optionally backend-development, delivery, documentation and development-tooling for their former contents |
| business-strategy | strategy |
| application-operations | operations; optionally operations-platforms |
| web-frontend | frontend-development; optionally frontend-reactjs-development and frontend-native-development |
| python-backend | backend-python-development |
| ai-development (previous combined bundle) | ai-development for generic methods; optionally ai-python-development, ai-adk-development and ai-langchain-development |
| visual-communication | visualization |

Build the chosen replacements in a fresh destination, preserve custom edits, and use the client's supported update/uninstall path to remove superseded plugin copies. In particular, ai-development keeps its identity but now contains only generic methods: replace its whole directory, because overlay copying would leave stale technical skills. Preserve unrelated plugins and project settings. Check discovery for duplicate skill names before starting model work. This revision does not remove or install anything in a client automatically.

The default build is development alone. Explicit `--plugin` arguments replace that default; `--all` builds all packages. The current [ownership map](maintainers/sources.md#target-plugin-ownership) identifies the precise owner of each local/acquired skill. Product, visual and service methods remain separate from accepted technical defaults; no application stack migration or account connection is implied.

## Original directory layout

The original skills moved into activity plugins with their resources intact:

| Previous directory | Current directory |
| --- | --- |
| `skills/business-strategy/` | [plugins/strategy/skills/business-strategy/](../plugins/strategy/skills/business-strategy/) |
| `skills/business-opportunity-analysis/` | [plugins/strategy/skills/business-opportunity-analysis/](../plugins/strategy/skills/business-opportunity-analysis/) |
| `skills/architecture-diagraming/` | [plugins/visualization/skills/architecture-diagramming/](../plugins/visualization/skills/architecture-diagramming/) |
| `skills/presentation-building/` | [plugins/visualization/skills/presentation-building/](../plugins/visualization/skills/presentation-building/) |

## Local skill naming

Local names use short task activities and recognizable supporting topics. Upstream names remain unchanged; duplicate aliases are not bundled.

| Previous local name | Current name |
| --- | --- |
| `project-bootstrap`, `maintain-project-foundations` | `project-conventions` |
| `build-consistent-frontend` | `frontend-conventions` |
| `build-python-backend` | `backend-conventions` |
| `design-interactions` | `interaction-design` |
| `interface-craft` | `interface-quality` |
| `write-scannable-documentation`, `write-project-documentation` | `documentation-writing` |
| `document-software-architecture` | `architecture-documentation` |
| `test-end-to-end` | `journey-testing` |
| `test-application-performance` | `performance-testing` |
| `test-application-resilience` | `resilience-testing` |
| `build-evaluated-ai` | `ai-development` |
| `build-delivery-pipelines` | `delivery-pipelines` |
| `documentation-conventions` | `documentation-conventions` |
| `design-secure-features` | `security-and-privacy-design` |
| `contribute-code` | `git-contributions` |
| `architecture-diagraming` | `architecture-diagramming` |
| Standalone `backup-recovery` | `protect-and-restore-data` |
| Standalone `cicd-release-management` | `delivery-pipelines` |

The architecture rename corrects spelling. These changes do not require renaming application files or changing test frameworks.

The AI skill now covers application/task design, model/context/tool choices, reusable skills, harness/session integration and protocol selection alongside evaluation and operation. Rebuild the ai-development package and replace the old skill directory; no duplicate alias is shipped. Native invocation controls are unchanged.

## Generic AI methods and technical names

The ai-development package now provides generic ai-development, ai-testing and ai-operations. Detailed evaluation methods, including speech evaluation, moved to `ai-development/skills/ai-testing/references/evaluation-references.md`. Update private links to that resource; the generic testing and operating methods require no Python/evaluator/telemetry package.

The earlier technical profiles have explicit implementation names:

| Previous package/path | Current package/path |
| --- | --- |
| `ai-python-development/skills/ai-testing` | `ai-python-development/skills/ai-deepeval-testing` |
| `ai-python-development/skills/ai-operations` | `ai-python-development/skills/python-ai-observability` |

A request for ai-testing or ai-operations now selects the generic discipline where available; request ai-deepeval-testing or python-ai-observability for those implementations. Rebuild and replace complete affected packages, removing stale technical copies rather than creating duplicate aliases. Native invocation controls remain unchanged.

## Bundle and invocation changes

- MCP builder belongs to ai-python-development. Generic MCP contracts remain in ai-development; MCP-only work does not require an LLM.
- The workflow bundle retains 18 reviewed Matt skills and excludes nine from its earlier broad import. See [selection decisions](maintainers/sources.md#matt-pocock-selection) before removing excluded copies.
- Portable operations guidance is distributed across workflow, Python and operations bundles. `system-flow-explorer`, including its renderer/example/checks, belongs to visualization. Operating, documentation, visualization and technical capabilities are explicit additions to development.
- `develop` handles end-to-end work; focused tasks handle individual activities. `implement` remains the upstream skill with local framing. `interaction-design` belongs to frontend-development.
- Most local supporting skills use `user-invocable: false` in clients honoring it; request tasks or explicitly name supporting guidance where supported. Upstream native controls are preserved. No universal `/help` or task aliases are installed.

The bundles configure no monitoring services, fault injectors, credentials, schedulers, MCP servers or browser/device dependencies. Host tools and permissions remain separate from installing guidance. See [Usage](usage.md) for the current activities.

## Generic methods and selected technical references

Rebuild complete affected bundles after the task-2 content separation. Tooling-conventions now owns selected quality-tool, Compose, workflow/registry and telemetry-backend references formerly under project-conventions, delivery-pipelines and observability-operations. Private links into those resources need updating. Generic journey and AI methods retain their outcomes; concrete driver and versioned protocol details live with technical guidance. The separate AI-skill rename is documented above; other skill names and native invocation controls remain intact.

The package split is implemented. Resource paths now follow the current owner; rebuild complete packages and update private links to the moved skill/resource folders.
