# Metadata contract

Metadata is the repo-wide classification layer for skills, packs and the artifacts/activities they own. It exists for discovery, maintenance and generated inventories; it is not an execution router or a permission system.

## Skill metadata

Every local skill declares the following in `SKILL.md` frontmatter. Acquired skills receive the same labels from `agent-depot.json` at build time; their source bytes are not edited.

| Field | Allowed values | Meaning |
| --- | --- | --- |
| `kind` | `system`, `activity`, `method`, `workflow`, `guide`, `reference` | The skill's conceptual role. |
| `pack` | `sdlc`, `technical`, `craft`, `product` | The installable capability pack the skill belongs to. |
| `domain` | `development`, `design`, `delivery`, `operations`, `security`, `governance`, `product`, `saas`, `frontend`, `backend`, `database`, `ai`, `tooling`, `platform`, `documentation`, `visualization`, `browser-extension`, `native`, `go`, `typescript` | The lifecycle stage or capability area. |
| `phase` | `planning`, `requirements`, `design`, `implementation`, `verification`, `release`, `maintenance`, `cross-phase` | The primary SDLC phase. Use `cross-phase` for systems, assurance and methods that genuinely span the lifecycle. |
| `origin` | `local`, `upstream` | Authored here or acquired and pinned. |
| `scope` | `generic`, `stack-specific` | Applicability across stacks. |
| `invocation` | `user`, `agent`, `both` | Preferred invocation surface. Native client controls still govern actual availability. |
| `role` | `task`, `support` | Packaging role: requested activity versus supporting capability. |

`kind` and `role` are different. `role` is the task/support packaging label; `kind` is the conceptual layer. `phase` is a single primary phase, not a list; the activity catalog and transitions carry multi-phase behavior.

### Kinds in use

| Kind | Owns | Examples |
| --- | --- | --- |
| `system` | A shared model or router other skills compose: vocabulary, catalogs, stopping points and authority | `artifact-system`, `activity-system` |
| `activity` | A requested engagement with an intent, output, stopping point and transitions | `design`, `implement`, `release`, `test` |
| `method` | Reusable expertise that deepens work without starting another activity: judgment, tradeoffs and evidence | `design-system`, `requirements-engineering`, `tdd` |
| `workflow` | An ordered sequence inside or around an activity, usually requested explicitly | `git-contributions`, `write-spec`, `retro` |
| `guide` | Artifact-shaped craft for one artifact type: structure, conventions, examples, common failures and review questions | `guide-adr`, `guide-runbook`, `guide-prd` |
| `reference` | Stable lookup detail loaded for one branch or a deeper question; no current skill is classified this way | — |

The distinctions that matter most:

- **Activity versus method.** An activity changes what the requester has afterward and owns a stopping point. A method deepens a concern inside that engagement without starting another activity.
- **Method versus workflow.** A method supplies judgment and tradeoffs. A workflow supplies an ordered sequence, often for a named operation such as contributing a change.
- **Method versus guide.** A method owns a subject and how to reason about it. A guide owns how to shape one artifact well. Artifact guides are `kind: guide`; their matching contract still owns lifecycle, authority, maturity, evidence and handoff.
- **Guide versus reference.** A guide is prescriptive craft that tells the writer what good looks like. A reference is lookup material consulted for a detail.
- **System versus everything else.** A system owns shared vocabulary and rules that other skills compose; it should not be selected as if it were a single engagement.

The [artifact guide registry](../plugins/sdlc/skills/artifact-system/references/guide-registry.md) pairs each artifact guide with its contract. `kind: guide` does not change the skill's `role`, `invocation` or native client controls.

### Invocation controls are not the same as our labels

`user-invocable`, `disable-model-invocation` and our `invocation` label answer different questions. A skill can be agent-usable even when it is not directly user-invocable.

| Control | What it means | Blocks agent use? |
| --- | --- | --- |
| `user-invocable` (native) | A user can invoke the skill directly, e.g. as `/name` | **No**. It only controls the direct user command surface. |
| `disable-model-invocation` (native) | The model must not select or auto-invoke the skill | **Yes**, unless the user explicitly requests it or the task instructs the agent to read it. |
| `invocation` (ours) | Preferred discovery surface: `user`, `agent` or `both` | **No**. It is a label, not a permission. |
| `role` (ours) | Packaging role: `task` or `support` | **No**. |

So `user-invocable: false` means “not a direct slash command,” not “hidden from the agent.” An agent can still read and apply the skill. `disable-model-invocation: true` is the actual auto-invocation gate.


**Software type is not skill metadata.** A skill such as `design` is reusable across frontend, backend, AI and library/CLI work. The type belongs to the component and is recorded in the change, engagement thread or component inventory. Do not add a `software_type` field to `SKILL.md` or to acquired labels. Read [software types](../plugins/sdlc/skills/artifact-system/references/software-types.md) for the four types and the type-versus-constraint rules.

## Pack types

| Pack | Contains | Examples |
| --- | --- | --- |
| `sdlc` | The full lifecycle: development, delivery, operations, security and governance | `activity-system`, `release`, `run-incident-response`, `run-compliance-assessment` |
| `technical` | Stack and platform implementation expertise | Frontend, backend, database, AI, language, tooling and platform packs |
| `craft` | Cross-type presentation and authoring craft | Documentation, visualization |
| `product` | Product direction and commercial design | Strategy, SaaS design |

A pack is an install/update boundary. It is not an execution sequence.

## Sources of truth

| Concern | Owner |
| --- | --- |
| Artifact types, planes, homes, contracts, quality and assurance | `plugins/sdlc/skills/artifact-system/` |
| Software types and required design evidence | `plugins/sdlc/skills/artifact-system/references/software-types.md` |
| Activity selection, stopping points, transitions and authority | `plugins/sdlc/skills/activity-system/` |
| Engagement focus, threads and reopens | `plugins/sdlc/skills/activity-system/references/engagement-state.md` |
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
