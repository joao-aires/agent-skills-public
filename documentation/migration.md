# Migrating existing installations

The original four skills retain their content and resources. Their locations changed; the architecture skill also has a spelling correction:

| Previous directory | New directory |
| --- | --- |
| `skills/business-strategy/` | [plugins/business-strategy/skills/business-strategy/](../plugins/business-strategy/skills/business-strategy/) |
| `skills/business-opportunity-analysis/` | [plugins/business-strategy/skills/business-opportunity-analysis/](../plugins/business-strategy/skills/business-opportunity-analysis/) |
| `skills/architecture-diagraming/` | [plugins/visual-communication/skills/architecture-diagramming/](../plugins/visual-communication/skills/architecture-diagramming/) |
| `skills/presentation-building/` | [plugins/visual-communication/skills/presentation-building/](../plugins/visual-communication/skills/presentation-building/) |

After updating your checkout to the plugin version, choose the route matching your installation:

- **Linked with my helper:** run `./scripts/sync-skills.sh status`, then `./scripts/sync-skills.sh sync`. This repairs unchanged-name links to the old `skills/` paths in `~/.agents/skills` from this same checkout, including broken links. For architecture-diagraming, follow the rename cleanup below. It preserves unrelated files/links and adds the available local skills. To select one skill, use `./scripts/sync-skills.sh sync business-strategy`. Keep the checkout in place; this route links local skills only.
- **Copied or linked manually:** update the source paths above and replace the complete skill directory, including resources. Preserve your custom edits and check for duplicate installations. The helper does not update copied directories or links from another checkout.
- **Moving to plugins:** install the relevant individual plugin directories through your client's supported route. Use the [build instructions](usage.md#build-and-load) for bundles containing upstream skills. Retire duplicate old installations after verifying the new ones; packaging alone does not install plugins or configure MCPs.

If you used an earlier development version, `project-bootstrap` and its interim name `maintain-project-foundations` are now `project-conventions`. Update saved prompt references and replace the old installed entry; a legacy helper link to that renamed skill needs manual cleanup after checking its target. You can keep your application layout and work without a tracker.

## Renamed frontend/backend skills

The frontend/backend entry points are now `frontend-conventions` and `backend-conventions` (previously `build-consistent-frontend` and `build-python-backend`). No `apply` prefix or suffix is used. Update explicit prompts and project `AGENTS.md` links, rebuild, then replace the affected plugin installation through your client. For skill-only symlink installs, inspect and remove only the old managed links before synchronizing the new names; do not delete unrelated skills. Old aliases are not bundled.

## Curated upstream set and MCP placement

MCP builder now belongs to `ai-development`; add that plugin for MCP work, even when no LLM is needed. The workflow bundle retains 18 of Matt's skills and excludes nine from its earlier broad import; see [the review](maintainer-reference.md#matt-pocock-selection). Rebuild and replace the affected bundles as usual. Remove excluded skill copies only after inspecting their origin; unrelated installations are unchanged.

## Operations guidance and interactive architecture

The portable operations collection is now integrated by activity: general system mapping and Bash work in `development-workflow`, Python automation in `python-backend`, and service operations in `application-operations`. Backup and release material enrich the existing `protect-and-restore-data` and `delivery-pipelines` entry points. If importing the standalone collection previously, update `backup-recovery` and `cicd-release-management` references to those canonical names and inspect duplicate copies before removal. The source-notes companion and factory framework are not bundled.

`system-flow-explorer` belongs to `visual-communication`, including its renderer, model example and tests. Rebuild and replace the selected bundles with resources intact. The default three-plugin build does not include operations or visual communication; select those explicitly. No monitoring service, credentials, scheduler or browser dependency is installed by this update.

The workflow bundle also adds `resilience-testing`. Rebuild and replace it with supporting references intact. This exposes guidance for controlled failure tests; it does not install an injector, schedule chaos experiments or authorize deployed faults. Existing skill names remain unchanged.

## Task entry points and design-first work

Rebuild/replace workflow and relevant stack bundles to obtain the task menu and interaction-design guidance. Local specialist renames are listed below. Most local supporting skills now use `user-invocable: false` to reduce picker clutter in supporting clients; request the task or name supporting guidance in plain language where supported. Upstream explicit controls remain intact. No automatic rename/alias for `/help`, `/test` or other client commands is installed.

`implement` remains the pinned upstream entry point with local task framing; no duplicate local implement skill is added. `develop` handles rough-idea-to-implementation work, while `refine`, `design` and other tasks handle focused stages. Design-interactions is bundled with web-frontend and guides meaningful UI changes before implementation, without requiring an approval per screen. Automation triggers and permissions remain configured in the host.


## Local skill naming

Task entry points use short activities such as `develop`, `design`, `test` and `review`. Supporting guidance uses recognizable topics such as `interaction-design` or `performance-testing`. Explicit operations keep established names such as `incident-response`. Upstream names remain unchanged.

| Previous local name | Current name |
| --- | --- |
| `design-interactions` | `interaction-design` |
| `test-end-to-end` | `journey-testing` |
| `test-application-performance` | `performance-testing` |
| `test-application-resilience` | `resilience-testing` |
| `build-delivery-pipelines` | `delivery-pipelines` |
| `maintain-documentation` | `documentation-conventions` |
| `design-secure-features` | `security-and-privacy-design` |
| `contribute-code` | `git-contributions` |
| `architecture-diagraming` | `architecture-diagramming` |

Update saved prompts, project instructions and automation references, then rebuild and replace affected installations through the client's supported route. Inspect and remove old managed links or copies only after confirming their origin; the sync helper does not migrate renamed basenames. No duplicate aliases are bundled. Existing application repositories do not need to rename their own files or adopt a new test framework just because a skill was renamed.
