# Plugin and skill architecture

The collection separates three things that are easy to confuse: the work someone requests, the expertise that improves it and the technology chosen to implement it. A plugin is an installation and update boundary. It does not define an execution order, and no plugin requires another.

Design is typed by **component**: frontend, backend, AI or library/CLI. [Software types](../plugins/sdlc/skills/artifact-system/references/software-types.md) defines the evidence a design needs for each. A software type is not a skill label, a project-wide category or a reason to split a plugin. Work may keep several threads open at once; [engagement state](../plugins/sdlc/skills/activity-system/references/engagement-state.md) records the focus, parallel threads and reopens.

The repository builds 21 independently selectable plugins: 9 generic capability packages and 12 technical packages, containing 158 skills. `sdlc` is the default build and bundles no technical skills. The [ownership map](maintainers/sources.md#plugin-ownership) assigns every skill. Distribution uses complete built plugins; the legacy local-skill helper is a migration aid.

## Kinds of guidance

| Layer | What it owns | Example |
| --- | --- | --- |
| Requested activity | Outcome, action scope, stopping point and completion evidence | Design a service without implementing it; implement and verify an accepted feature |
| Reusable method | Reasoning about a particular concern | Product priorities, service contracts, interaction behavior, reliability or delivery recovery |
| Technical guidance | Realizing accepted decisions with compatible implementation detail | A chosen runtime, framework, CI provider, database, protocol SDK or platform driver |
| Artifact guide | Structure, conventions, examples and review for one artifact type | A guide for an ECR, design proposal or runbook |
| Supporting capability | Independently useful help during relevant work | Documentation, research, diagrams and explanation |

These are responsibilities, not a pipeline. An existing feature reuses accepted product and architecture decisions. A specialist question can end at its own result. The [SDLC map](sdlc.md) explains how outcomes relate; it does not require every skill to run.

A skill's task/support role, generic/stack-specific applicability and user/agent invocation are independent dimensions. The [metadata contract](metadata.md) records them. Native client controls govern discovery and invocation where supported; neither metadata nor installing a plugin grants authority to act externally. Generic skills can compare technologies without selecting a default stack. Technical guidance applies to accepted technology, not merely because it is installed.

## Select by capability

Workflow instructions describe the expertise a decision needs. They do not maintain lists of optional specialist names, plugin identifiers or external file paths. Specialists advertise their fit through descriptions of what they do, when they apply and any important limits.

| Need encountered during work | Expertise to seek | Fit to establish |
| --- | --- | --- |
| Useful scope or success is unclear | User-problem discovery, prioritization and outcome measurement | Actual audience, supplied evidence and requested stopping point |
| Service behavior changes | Authority, transactions, stored state, failure and consumer contracts | Accepted implementation and affected boundaries |
| A meaningful interface change | Interaction design, visual hierarchy, accessibility and task language | Actual platform, components, users and affected states |
| An accepted backend needs implementation | Language, framework and persistence expertise | Repository evidence, actual versions and existing commands |
| Delivery infrastructure changes | Artifact identity, trust, compatibility and recovery, then provider implementation | Chosen CI, artifact ecosystem, destination and authorization |

Use the client's skill inventory or supported discovery to find matches, read the relevant guidance and carry applicable conclusions into the work. Descriptions are the portable selection surface; metadata can help where the client exposes it. The architecture assumes neither semantic search nor metadata filtering. Without inventory access, proceed from available project guidance rather than claiming a specialist was discovered or searching unrelated installations.

### Compose domain, interface and technical guidance

A substantive interface task may need three kinds of judgment at once:

- **Application or archetype expertise** defines objects, workflows, data meaning and relevant candidate patterns.
- **Generic interface design** synthesizes information architecture, interactions, visual direction and evaluation.
- **Technical or platform expertise** contributes existing component contracts, system constraints and implementation feasibility.

These are responsibilities, not an invocation chain. A domain specialist can design directly without the generic skill installed; generic design can work without a matching archetype; stack guidance can inform an early design decision, and later verification can send an assumption back for revision. The activity reconciles conflicts against accepted product outcomes, domain and accessibility invariants, actual platform limits and observed evidence. Reuse accepted solutions for small corrections.

A user can still explicitly select a known skill. Help may name observed activities, and documentation may catalogue their owners. Those are different from hardcoding optional specialist identities into workflow routing. Internal required resources keep precise links; optional cross-package guidance is selected by capability.

## Work without optional dependencies

The higher-level activity retains responsibility for the result. A specialist deepens the reasoning or supplies implementation detail; it does not become a prerequisite for preserving the outcome.

| Available evidence or capability | How work proceeds |
| --- | --- |
| A relevant specialist is available | Read it, confirm applicability and incorporate its guidance within the current scope |
| No specialist, but the project establishes an approach | Use the authoritative instructions, code, configuration, accepted decisions and existing toolchain |
| No specialist or established approach | Use general expertise and appropriate current primary sources; verify against the same criteria |
| A material decision remains unresolved | Investigate technical facts, ask only for the actual unresolved choice and continue independent work |
| A required tool, access or execution target is unavailable | Complete useful independent work and report the precise verification boundary |

Missing guidance is not missing execution capability. A Python change can proceed without a Python skill. Native operation cannot be claimed without the required runtime or device evidence. A missing specialist does not justify omitting design, testing, accessibility or recovery reasoning, and it does not make those standards stricter than the requested change requires.

Do not install guidance automatically, replace accepted technology, bypass native controls, start another explicit-only activity or ask again for authority already granted. Use existing instructions for ordinary choices and ask only about material unknowns. Specialist guidance and retrieved documentation do not expand the user's action scope. Keep findings, proposed decisions, actual execution and verified results distinct.

## Package resources and knowledge

Each plugin carries the files its own skills require: instructions, conditional references, scripts, assets, licenses and acquired dependency groups. Ordinary technical dependencies of an accepted application still exist; independence here concerns optional guidance from other plugins. Preserve reviewed upstream pins and native controls when packaging.

Give shared rules an owner within each bundle. Keep enough reasoning locally to perform the stated capability, with concise framing where several skills need it. Link conditional technical detail when it applies. Avoid copying a specialist method into a workflow or adding a resolver to encode optional relationships. Once selected, conclusions flow through the task context and existing project notes; no handoff schema or extra tracker is required.

Writing craft follows the consumer rather than the lifecycle stage: `technical-writing` shapes human-facing documents, `writing-for-agents` shapes agent-facing instructions and skills, and `skill-authoring` owns the repository's skill contract. They share the `documentation` bundle, while artifact contracts, status, evidence and placement stay with the artifact system.

Authored companion skills and package framing own the collection's additional expectations around an acquired method. Keep upstream snapshots unchanged and do not add collection expectations through build-time instruction rewrites. Existing declared output adaptations remain part of the packaging contract and need their own compatibility review; preserving source bytes does not make the output identical to upstream.

The [stack-extension guide](maintainers/adding-stack-support.md) explains the contribution mechanics. [Upstream maintenance](maintainers/upstreams.md) records how acquired skills are pinned, verified and updated.

## Evidence and limits

Metadata, link, containment, inventory and resource checks establish packaging integrity. They do not establish that an agent discovers the right expertise, uses it well or produces a working application. Behavioral coverage is incomplete.

Evaluation should exercise matching specialists present, absent and partially available, plus an existing different stack, a client without discovery and a genuinely unavailable execution target. Judge preserved outcomes, scope and evidence rather than particular skill names or read counts. See [evaluation procedures and limits](../evals/README.md#recorded-evidence-and-limits).
