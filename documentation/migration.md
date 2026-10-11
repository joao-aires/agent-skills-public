# Migrating existing installations


The original four skills retain their names, content and resources. Their locations changed:

| Previous directory | New directory |
| --- | --- |
| `skills/business-strategy/` | [plugins/business-strategy/skills/business-strategy/](../plugins/business-strategy/skills/business-strategy/) |
| `skills/business-opportunity-analysis/` | [plugins/business-strategy/skills/business-opportunity-analysis/](../plugins/business-strategy/skills/business-opportunity-analysis/) |
| `skills/architecture-diagraming/` | [plugins/visual-communication/skills/architecture-diagraming/](../plugins/visual-communication/skills/architecture-diagraming/) |
| `skills/presentation-building/` | [plugins/visual-communication/skills/presentation-building/](../plugins/visual-communication/skills/presentation-building/) |

After updating your checkout to the plugin version, choose the route matching your installation:

- **Linked with our helper:** run `./scripts/sync-skills.sh status`, then `./scripts/sync-skills.sh sync`. This repairs links to the old `skills/` paths in `~/.agents/skills` from this same checkout, including broken links. It preserves unrelated files/links and adds the available local skills. To select one skill, use `./scripts/sync-skills.sh sync business-strategy`. Keep the checkout in place; this route links local skills only.
- **Copied or linked manually:** update the source paths above and replace the complete skill directory, including resources. Preserve your custom edits and check for duplicate installations. The helper does not update copied directories or links from another checkout.
- **Moving to plugins:** install the relevant individual plugin directories through your client's supported route. Use the [build instructions](usage.md#build-and-load) for bundles containing upstream skills. Retire duplicate old installations after verifying the new ones; packaging alone does not install plugins or configure MCPs.

If you tried an earlier version of this PR, `project-bootstrap` and its interim name `maintain-project-foundations` are now `project-conventions`. Update saved prompt references and replace the old installed entry; a legacy helper link to that renamed skill needs manual cleanup after checking its target. No application repository migration or new tracker is required.

## Renamed frontend/backend skills


The frontend/backend entry points are now `frontend-conventions` and `backend-conventions` (previously `build-consistent-frontend` and `build-python-backend`). No `apply` prefix or suffix is used. Update explicit prompts and project `AGENTS.md` links, rebuild, then replace the affected plugin installation through your client. For skill-only symlink installs, inspect and remove only the old managed links before synchronizing the new names; do not delete unrelated skills. Old aliases are not bundled.
