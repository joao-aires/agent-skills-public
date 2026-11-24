# Plugin and skill architecture

The collection separates three things that are easy to confuse: the work someone requests, the expertise that improves it and the technology chosen to implement it. A plugin is an installation and update boundary. It does not define an execution order, and no plugin requires another.

Design is typed by **component**: frontend, backend, AI or library/CLI. [Software types](../plugins/sdlc/skills/artifact-system/references/software-types.md) defines the evidence a design needs for each. A software type is not a skill label, a project-wide category or a reason to split a plugin. Work may keep several threads open at once. [Engagement state](../plugins/sdlc/skills/activity-system/references/engagement-state.md) records the focus, parallel threads and reopens.

The repository builds 21 independently selectable plugins: 9 generic capability packages and 12 technical packages, containing 167 skills. `sdlc` is the default build and bundles no technical skills. Each plugin declares its pack once in `plugin.json`. Its skills inherit that pack. The [ownership map](maintainers/sources.md#plugin-ownership) assigns every skill. Distribution uses complete built plugins.

## Kinds of guidance

| Layer | What it owns | Example |
| --- | --- | --- |
| Requested activity | Outcome, action scope, stopping point and completion evidence | Design a service without implementing it; implement and verify an accepted feature |
| Reusable method | Reasoning about a particular concern | Product priorities, service contracts, interaction behavior, reliability or delivery recovery |
| Technical guidance | Realizing accepted decisions with compatible implementation detail | A chosen runtime, framework, CI provider, database, protocol SDK or platform driver |
| Artifact guide | Structure, conventions, examples and review for one artifact type | A guide for an ECR, design proposal or runbook |
| Supporting capability | Independently useful help during relevant work | Documentation, research, diagrams and explanation |

These are responsibilities, not a pipeline. An existing feature reuses accepted product and architecture decisions. A specialist question can end at its own result. The [SDLC map](sdlc.md) explains how outcomes relate. It does not require every skill to run.

A skill's task/support role, generic/stack-specific applicability and user/agent invocation are independent dimensions. The [metadata contract](metadata.md) records them. Native client controls govern discovery and invocation where supported. Neither metadata nor installing a plugin grants authority to act externally. Generic skills can compare technologies without selecting a default stack. Technical guidance applies to accepted technology, not merely because it is installed.

## Select and compose by capability

Workflow instructions describe the expertise a decision needs. They do not maintain lists of optional specialist names, plugin identifiers or external file paths. Descriptions are the portable selection surface, and the client's inventory is what an agent can actually discover. Without inventory access, proceed from available project guidance rather than claiming a specialist was discovered.

The operational rules live with the activity system's [composition](../plugins/sdlc/skills/activity-system/references/composition.md) reference: selecting by capability, composing domain, interface and technical judgment, falling back when expertise is absent, and resolving conflicts with project or environment constraints. The model below is what those rules implement. The reference is what to follow while working.

A user can still explicitly select a known skill. Help may name observed activities, and documentation may catalogue their owners. That is different from hardcoding optional specialist identities into workflow routing.

## Relationships between capabilities

Four abstractions, and a separate set of three moves.

| Abstraction | What it is | Where it lives |
| --- | --- | --- |
| Capability | A skill, activity, method, guide, workflow or system; a plugin is an install boundary | `SKILL.md` and its metadata |
| Work | A phase, thread, outcome or stopping point | The activity, the ECR and [engagement state](../plugins/sdlc/skills/activity-system/references/engagement-state.md) |
| Record | An artifact, decision or evidence | The [artifact system](../plugins/sdlc/skills/artifact-system/SKILL.md) |
| Constraint | Authority, scope or exclusion | Metadata and prose in the owning skill |

A capability reaches another by one of three moves:

- **Route** — the agent selects it from its description, or a person invokes it, optionally through a thin router alias. Two entry mechanisms, one move.
- **Compose** — the activity consults supporting expertise and keeps its outcome. Declared in `## Composition` by need and area, with the fallback stated.
- **Hand off** — ownership of the work moves, carrying the records and revisions the next owner needs. Declared at the phase boundary, not between skills. Delegation is the same move inside a phase: the activity keeps accountability while a bounded unit of work changes hands. [Delegation](../plugins/sdlc/skills/activity-system/references/delegation.md) owns the envelope.

Authority gates a move. It is not a move. Exclusion is the nearest-neighbour boundary — what the capability is not for — and constrains selection. An artifact is a record, never the relationship itself.

Declare only what exists. A composition name resolves inside its own package. Optional expertise elsewhere is described by capability area, not by name. A handoff names its records, and a router satisfies the rules in the [metadata contract](metadata.md#router-skills). None of this is a runtime resolver. Descriptions remain the selection surface, and the declared graph is an audit view, not an execution plan.

## Package resources and knowledge

Each plugin carries the files its own skills require: instructions, conditional references, scripts, assets, licenses and acquired dependency groups. Ordinary technical dependencies of an accepted application still exist. Independence here concerns optional guidance from other plugins. Preserve reviewed upstream pins and native controls when packaging.

Give shared rules an owner within each bundle. Keep enough reasoning locally to perform the stated capability, with concise framing where several skills need it. Link conditional technical detail when it applies. Avoid copying a specialist method into a workflow or adding a resolver to encode optional relationships. Once selected, conclusions flow through the task context and existing project notes. No handoff schema or extra tracker is required.

Writing craft follows the consumer rather than the lifecycle stage: `technical-writing` shapes human-facing documents, `writing-for-agents` shapes agent-facing instructions and skills, and `skill-authoring` owns the repository's skill contract. They share the `documentation` bundle, while artifact contracts, status, evidence and placement stay with the artifact system.

Authored companion skills and package framing own the collection's additional expectations around an acquired method. Keep upstream snapshots unchanged and do not add collection expectations through build-time instruction rewrites. Existing declared output adaptations remain part of the packaging contract and need their own compatibility review. Preserving source bytes does not make the output identical to upstream.

The [stack-extension guide](maintainers/adding-stack-support.md) explains the contribution mechanics. [Upstream maintenance](maintainers/upstreams.md) records how acquired skills are pinned, verified and updated.

## Evidence and limits

Metadata, link, containment, inventory and resource checks establish packaging integrity. They do not establish that an agent discovers the right expertise, uses it well or produces a working application. Behavioral coverage is incomplete.

Evaluation should exercise matching specialists present, absent and partially available, plus an existing different stack, a client without discovery and a genuinely unavailable execution target. Judge preserved outcomes, scope and evidence rather than particular skill names or read counts. See [evaluation procedures and limits](../evals/README.md#recorded-evidence-and-limits).
