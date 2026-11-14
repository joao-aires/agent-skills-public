# Metadata contract

Metadata is the repo-wide classification layer for skills, packs and the artifacts/activities they own. It exists for discovery, maintenance and generated inventories; it is not an execution router or a permission system.

## Skill metadata

Every local skill declares the following in `SKILL.md` frontmatter. Acquired skills receive the same labels from `agent-depot.json` at build time; their source bytes are not edited.

| Field | Allowed values | Meaning |
| --- | --- | --- |
| `kind` | `system`, `activity`, `method`, `workflow`, `reference` | The skill's conceptual role. |
| `pack` | `sdlc`, `technical`, `craft`, `product` | The installable capability pack the skill belongs to. |
| `domain` | `development`, `delivery`, `operations`, `security`, `governance`, `product`, `saas`, `frontend`, `backend`, `database`, `ai`, `tooling`, `platform`, `documentation`, `visualization`, `browser-extension`, `native`, `go`, `typescript` | The lifecycle stage or capability area. |
| `phase` | `planning`, `requirements`, `design`, `implementation`, `verification`, `release`, `maintenance`, `cross-phase` | The primary SDLC phase. Use `cross-phase` for systems, assurance and methods that genuinely span the lifecycle. |
| `origin` | `local`, `upstream` | Authored here or acquired and pinned. |
| `scope` | `generic`, `stack-specific` | Applicability across stacks. |
| `invocation` | `user`, `agent`, `both` | Preferred invocation surface. Native client controls still govern actual availability. |
| `role` | `task`, `support` | Packaging role: requested activity versus supporting capability. |

`kind` and `role` are different. `role` is the task/support packaging label; `kind` is the conceptual layer. `phase` is a single primary phase, not a list; the activity catalog and transitions carry multi-phase behavior.

## Pack types

| Pack | Contains | Examples |
| --- | --- | --- |
| `sdlc` | The full lifecycle: development, delivery, operations, security and governance | `activity-system`, `release`, `incident-response`, `compliance-readiness` |
| `technical` | Stack and platform implementation expertise | Frontend, backend, database, AI, language, tooling and platform packs |
| `craft` | Cross-type presentation and authoring craft | Documentation, visualization |
| `product` | Product direction and commercial design | Strategy, SaaS design |

A pack is an install/update boundary. It is not an execution sequence.

## Sources of truth

| Concern | Owner |
| --- | --- |
| Artifact types, planes, homes, contracts, quality and assurance | `plugins/sdlc/skills/artifact-system/` |
| Activity selection, stopping points, transitions and authority | `plugins/sdlc/skills/activity-system/` |
| Local skill classification | Each `SKILL.md` frontmatter |
| Acquired skill classification and pins | `agent-depot.json` and `agent-depot.lock.json` |
| Generated maintainer view | `python scripts/skill_inventory.py` |
| Package ownership and counts | `documentation/maintainers/sources.md` |

Do not duplicate artifact types, homes, phases or evidence rules in every skill. Skill metadata classifies the skill; the artifact and activity catalogs own the detailed model.

## Validation and generation

| Check | Command |
| --- | --- |
| Skill metadata, packs and containment | `python scripts/validate_plugins.py` |
| Maintained links and names | `python scripts/check_collection.py` |
| Generated skill inventory | `python scripts/skill_inventory.py` |
| Scenario definitions | `python scripts/validate_evaluations.py` |

Local skills require the full classification. Acquired labels are validated from `agent-depot.json`; do not add them by editing upstream files.

## Adding or moving a skill

1. Choose its `kind`, `pack`, `domain` and primary `phase`.
2. Declare the fields in the local `SKILL.md` frontmatter.
3. Link the owning artifact contract or activity reference rather than duplicating it.
4. Update the package README/catalog if the pack's responsibilities change.
5. Run the validation and inventory commands above.

Moving a skill between packs changes its `pack`, `domain` and destination. Update local links, `agent-depot.json`/lock destinations for acquired skills, package counts, migration notes and the generated inventory together.
