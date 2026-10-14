# Migrating existing installations

Existing applications can keep their layout, accepted stack and tracker choices. Update the installed guidance and any explicit skill references using the steps below.

## Update your installation

1. Preserve custom edits and inspect the origin of existing copies or links.
2. Update the checkout, then [build the desired bundles](../README.md#quick-start) into a new destination. Source directories include local skills only; built bundles also contain upstream resources and notices.
3. Replace affected plugins through your client's supported route, keeping their resources intact. For manually copied skills, replace complete directories.
4. Update saved prompts, project instructions and automation references using the name table below. Inspect and remove obsolete copies/managed links from this checkout; preserve unrelated installations.
5. Check client discovery and try a relevant explicit activity. Building packages alone does not install plugins or configure live tools.

For the legacy skills-only helper, run `./scripts/sync-skills.sh status`, then `./scripts/sync-skills.sh sync`. It repairs unchanged-name links from this checkout's old `skills/` paths in `~/.agents/skills`, including broken links, while preserving unrelated paths. It adds available local skills only. Keep the checkout in place. The helper does not migrate renamed basenames or update copied directories/other checkouts; inspect and clean up those old entries manually.

## Original directory layout

The original skills moved into activity plugins with their resources intact:

| Previous directory | Current directory |
| --- | --- |
| `skills/business-strategy/` | [plugins/business-strategy/skills/business-strategy/](../plugins/business-strategy/skills/business-strategy/) |
| `skills/business-opportunity-analysis/` | [plugins/business-strategy/skills/business-opportunity-analysis/](../plugins/business-strategy/skills/business-opportunity-analysis/) |
| `skills/architecture-diagraming/` | [plugins/visual-communication/skills/architecture-diagramming/](../plugins/visual-communication/skills/architecture-diagramming/) |
| `skills/presentation-building/` | [plugins/visual-communication/skills/presentation-building/](../plugins/visual-communication/skills/presentation-building/) |

## Local skill naming

Local names use short task activities and recognizable supporting topics. Upstream names remain unchanged; duplicate aliases are not bundled.

| Previous local name | Current name |
| --- | --- |
| `project-bootstrap`, `maintain-project-foundations` | `project-conventions` |
| `build-consistent-frontend` | `frontend-conventions` |
| `build-python-backend` | `backend-conventions` |
| `design-interactions` | `interaction-design` |
| `test-end-to-end` | `journey-testing` |
| `test-application-performance` | `performance-testing` |
| `test-application-resilience` | `resilience-testing` |
| `build-delivery-pipelines` | `delivery-pipelines` |
| `maintain-documentation` | `documentation-conventions` |
| `design-secure-features` | `security-and-privacy-design` |
| `contribute-code` | `git-contributions` |
| `architecture-diagraming` | `architecture-diagramming` |
| Standalone `backup-recovery` | `protect-and-restore-data` |
| Standalone `cicd-release-management` | `delivery-pipelines` |

The architecture rename corrects spelling. These changes do not require renaming application files or changing test frameworks.

## Bundle and invocation changes

- MCP builder belongs to `ai-development`, even for MCP-only work. It does not require an LLM.
- The workflow bundle retains 18 reviewed Matt skills and excludes nine from its earlier broad import. See [selection decisions](maintainer-reference.md#matt-pocock-selection) before removing excluded copies.
- Portable operations guidance is distributed across workflow, Python and operations bundles. `system-flow-explorer`, including its renderer/example/checks, belongs to visual communication. Operations and visual communication must be explicitly selected when building beyond the default three bundles.
- `develop` handles end-to-end work; focused tasks handle individual activities. `implement` remains the upstream skill with local framing. `interaction-design` belongs to web-frontend.
- Most local supporting skills use `user-invocable: false` in clients honoring it; request tasks or explicitly name supporting guidance where supported. Upstream native controls are preserved. No universal `/help` or task aliases are installed.

The bundles configure no monitoring services, fault injectors, credentials, schedulers, MCP servers or browser/device dependencies. Host tools and permissions remain separate from installing guidance. See [Usage](usage.md) for the current activities.
