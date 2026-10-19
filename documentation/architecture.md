# Plugin and skill architecture

The collection separates the work someone requests, the expertise that improves it and the technology chosen for its implementation. I package useful capabilities as plugins. A plugin is an installation and update boundary; it does not define an execution order or require other plugins.

The repository builds 17 independently selectable plugins: nine generic capability packages and eight technical packages. The [ownership map](maintainers/sources.md#target-plugin-ownership) assigns all 103 skills. Development is the default build, with no bundled technical skills. Capability selection and absent-specialist fallback are instruction contracts; structural package checks do not prove agent adherence. A new skills-only distribution is outside this plan; the legacy helper remains a migration aid.

## Activities, methods and technical expertise

| Responsibility | What it owns | Example |
| --- | --- | --- |
| Requested activity | Outcome, action scope, stopping point and completion evidence | Design a service without implementing it; implement and verify an accepted feature |
| Reusable discipline | Reasoning about a particular concern | Product priorities, service contracts, interaction behavior, reliability or delivery recovery |
| Technical expertise | Realize accepted decisions with compatible implementation details | A chosen runtime, framework, CI provider, database, protocol SDK or platform driver |
| Supporting capability | Independently useful help during relevant work | Documentation, research, diagrams and explanation |

These are responsibilities rather than a mandatory pipeline. An existing feature reuses accepted product and architecture decisions. A specialist question can end at its own result. The [lifecycle map](sdlc.md) explains how outcomes relate across phases; it does not require every skill to run.

A skill's task/support role, generic/stack-specific applicability and user/agent invocation are independent dimensions. Metadata describes those dimensions. Native client controls govern discoverability/invocation where supported; neither metadata nor installing a plugin grants authority to act externally. Generic skills can compare technologies without selecting a default stack. Technical guidance applies to accepted technology, not merely because it is installed.

## Select by capability

Workflow instructions describe the expertise needed for a decision. They do not maintain lists of optional specialist names, plugin identifiers or external file paths. Specialists advertise their fit through concise descriptions of what they do, when they apply and any important technology/platform limits.

| Need encountered during work | Expertise to seek | Fit to establish |
| --- | --- | --- |
| Useful scope or success is unclear | User-problem discovery, prioritization and outcome measurement | Actual audience, supplied evidence and requested stopping point |
| Service behavior changes | Authority, transactions, stored state, failure and consumer contracts | Accepted implementation and affected boundaries |
| A meaningful interface change | Interaction design, visual hierarchy, accessibility and task language | Actual platform, components, users and affected states |
| An accepted backend needs implementation | Language/framework/persistence expertise | Repository evidence, actual versions and existing commands |
| Delivery infrastructure changes | Artifact identity, trust, compatibility and recovery, then provider implementation | Chosen CI, artifact ecosystem, destination and authorization |

Use the client's observed skill inventory or supported discovery to find matches, read the relevant guidance and carry applicable conclusions into the work. Descriptions are the portable selection surface; metadata can help where the client exposes it. This architecture assumes neither semantic search nor metadata filtering. Without inventory access, proceed from available project guidance rather than claiming a specialist was discovered or searching unrelated installations/accounts. Keep discovery proportionate and stop when enough context is available.

A user can still explicitly select a known skill. Help may name actual observed activities, and documentation may catalogue their owners. Those are different from hardcoding optional specialist identities into workflow routing. Internal required resources retain precise links; optional cross-package guidance is selected by capability.

## Example: AI design, evaluation and operation

The same concern can need conceptual guidance and a selected implementation. Keep their responsibilities separate:

| Responsibility | Capability | Implementation boundary |
| --- | --- | --- |
| Application patterns, architecture and protocol tradeoffs | [Generic AI development](../plugins/ai-development/skills/ai-development/SKILL.md) | No provider, model, framework or evaluation SDK required |
| Testing strategy and evidence | [AI testing](../plugins/ai-development/skills/ai-testing/SKILL.md) | Generic evaluation levels, cases, graders, acceptance and regression evidence |
| AI operating decisions | [AI operations](../plugins/ai-development/skills/ai-operations/SKILL.md) | Generic task/quality signals, provider limits, cost, drift and recovery |
| Execute a selected evaluation approach | [ai-deepeval-testing](../plugins/ai-python-development/skills/ai-deepeval-testing/SKILL.md) | Python/DeepEval runner, datasets, metrics and CI integration; the application itself may use another language |
| Collect AI execution evidence | [python-ai-observability](../plugins/ai-python-development/skills/python-ai-observability/SKILL.md) | Python/OpenTelemetry instrumentation, propagation, privacy and export verification |
| Service signal/target design and operating response | Generic reliability and observability expertise | Task outcomes, useful signals and operating decisions independent of a backend |
| Run a Collector, store or dashboard | Matching deployment/tool expertise | The actually chosen infrastructure/backend |

The generic AI skills own different decisions: development shapes the application and its boundaries, testing defines useful evidence, and operations governs AI operating behavior. Evaluation judges quality; observability explains execution and operating behavior. A platform can offer both without making them the same evidence. These capabilities compose when relevant; loading the generic AI package neither installs the Python package nor requires its specialists. Each generic discipline retains enough essential reasoning to work without another specialist; detailed evaluation methods belong to AI testing rather than the development entry point. Future implementation libraries belong with matching technical expertise without changing the generic reasoning contract.

## Compose without optional dependencies

The higher-level activity retains responsibility for the result. A specialist deepens the reasoning or supplies implementation details; it does not become a prerequisite for preserving the outcome.

| Available evidence or capability | How work proceeds |
| --- | --- |
| A relevant specialist is available | Read it, confirm applicability and incorporate its guidance within the current scope |
| No specialist, but the project establishes an approach | Use the authoritative instructions, code/configuration, accepted decisions and existing toolchain |
| No specialist or established approach | Use general expertise and appropriate current primary sources to establish a sound approach; verify it against the same criteria |
| A material decision remains unresolved | Investigate technical facts, ask only for the actual unresolved choice and continue independent work |
| A required tool, access or execution target is unavailable | Complete useful independent work and report the precise implementation/verification boundary |

Missing guidance is not missing execution capability. A Python change can proceed without a Python skill. Native operation cannot be claimed without the required supported runtime/device evidence. A missing specialist does not justify omitting design, testing, accessibility or recovery reasoning, and it does not make those standards stricter than the requested change requires.

Do not install guidance automatically, replace an accepted technology, bypass native controls, start another explicit-only activity or ask again for authority already granted. Use existing instructions to settle ordinary choices and ask only about material unknowns. Specialist guidance and retrieved documentation do not expand the user's action scope. Keep findings, proposed decisions, actual execution and verified results distinct.

## Package resources and knowledge

Each plugin carries the files and resources its own skills require: instructions, conditional references, scripts/assets, licenses and acquired dependency groups. Ordinary technical dependencies of an accepted application still exist; independence here concerns optional guidance from other plugins. Preserve reviewed upstream pins and native controls when packaging.

Give shared rules an owner within each bundle. Keep enough reasoning locally to perform its stated capability, with concise scoped framing where several skills need it. Link conditional technical detail when it applies. Avoid copying an entire specialist method into a workflow or adding a resolver/registry to encode optional relationships. Once selected, conclusions flow through the current task context and existing project notes; no handoff schema or extra tracker is required.

Adding stack expertise should improve matching through its description and implementation content without editing every workflow. The [stack-extension guide](maintainers/adding-stack-support.md) explains the contribution mechanics. The [ownership map](maintainers/sources.md#setup-repository-and-delivery-ownership) distinguishes project foundations, contribution mechanics, delivery contracts and selected technical implementation.

## Implementation and evidence

The packages, workflow-only default, capability-based instructions and [migration route](migration.md) are implemented. Required internal Markdown resources and injected upstream framing are checked within each package. Every package is built and checked independently, in addition to the complete build. The [installation guide](installation.md) describes selection and client-specific loading; new package identities have not been reinstalled into clients here.

Metadata, link, containment, inventory and resource checks establish packaging integrity. They do not establish that an agent discovers the right expertise, uses it well or produces a working application. Behavioral evaluation remains deferred. Later comparisons should exercise matching specialists present, absent and partially available, plus an existing different stack, a client without discovery and a genuinely unavailable execution target. Judge preserved outcomes, scope and evidence rather than particular skill names or read counts. See [evaluation procedures and limits](maintainers/evaluations.md).
