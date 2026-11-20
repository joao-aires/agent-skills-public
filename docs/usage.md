# Using the plugins

[Install the bundles](installation.md) before using this guide. Start from the result you need; you do not have to select every supporting skill. [Architecture](architecture.md) explains how guidance composes, [SDLC coverage](sdlc.md) shows where activities fit, and [Engineering artifacts and workspaces](artifact-workflow.md) explains how durable work is recorded.

## Invoke an activity

Use the client's supported selection route. The [installation guide](installation.md#load-them-in-your-client) explains the different loading models.

| Client | Example |
| --- | --- |
| Claude Code | `/sdlc:test` |
| Codex | Select `test` in the skill picker, then describe the change |
| OpenCode V2 | `@test` followed by the behavior to verify |

A plain request such as "Use test for the current change" works where selection by name is supported. `activity-system` explains this collection and its help mode; it does not replace the client's built-in help.

| Situation | Activity | Expected result |
| --- | --- | --- |
| You do not know where to start | `activity-system` | Relevant capabilities, examples and a next activity |
| A rough idea needs to become working software | `develop` | Clarification, design, implementation, tests and review |
| A project needs foundations and context | `setup` | Useful foundations, working commands and an artifact home map |
| The outcome, first slice or feasibility is open | `plan` | A scoped decision and next action, with a linked brief or roadmap when useful |
| Requirements need definition | `refine` | Behavior, applicable quality constraints and observable acceptance |
| Scope is agreed and only a breakdown is requested | Ask for implementation preparation | Bounded increments and their verification |
| Architecture, UX or a contract is undecided | `design` | Materially different options and one recorded decision |
| Defined work is ready to build | `implement` | An implemented and verified change |
| You need evidence of behavior | `test` | Checks, results and coverage gaps |
| Shipped behavior needs interpretation | `run-product-feedback-analysis` | Evidence-backed analysis and a recommended next decision |
| A PR or diff needs assessment | `code-review` + `test` + artifact assurance | Findings against intended behavior, design, tests and artifacts |
| You want improvements | `improve` | Prioritized opportunities, or a specified improvement |
| A defect needs repair | `fix` | Reproduction, focused repair and verification |
| Security or privacy needs attention | `harden` | Scoped assessment, fixes and remaining risk |
| Dependencies need attention | `run-dependency-maintenance` | Compatibility review and permitted remediation |
| Delivery needs preparation | `release` | Readiness assessment, or a named authorized action |

`plan`, `refine` and `design` stop at their own outcomes. `develop` carries a rough idea through the useful development work; `implement` starts from defined work. Bare `improve` proposes opportunities, while a specified improvement can include implementation. Review assesses by default; posting a review, editing source, merging and deploying each need that action in scope.

`implement` is a local activity that starts from defined work. Optional explicit workflows include `grill-me`, `grill-with-docs`, `to-questionnaire`, `write-spec` and `retro`. `handoff` and agent-instruction craft live in the `documentation` bundle. Use them when their particular method helps; interviews, specs and trackers are not prerequisites. [Upstream selection](maintainers/sources.md#matt-pocock-selection) explains which upstream methods remain and why.

## Choose a path

Each path is a composition, not a compulsory pipeline. Stop at the requested outcome.

| Starting point | Typical path | Main artifacts |
| --- | --- | --- |
| New application | `setup` → `plan` → `refine` → `design` → `implement` → `test` → review → `release` when authorized | ECR, design proposal when a choice is open, README, code and tests |
| Existing feature | Inspect the current system → `refine` → `design` if consequential → `implement` → `test` → review | Compact or full ECR, design proposal, PR |
| Bug fix | Reproduce → `fix` → `test` → review | Compact ECR or commit/PR note, regression test |
| Idea to implementation | `plan` → `refine` → `design` → `implement` → `test` → review | Product brief or PRD, design proposal, ECR, README, tests |

Read [software types](../plugins/sdlc/skills/artifact-system/references/software-types.md) and the matching type file when the work affects a design. For review, use the [code-review](../plugins/sdlc/skills/code-review/SKILL.md) skill for the diff, [test](../plugins/sdlc/skills/test/SKILL.md) for verification evidence, [artifact assurance](../plugins/sdlc/skills/artifact-system/references/assurance.md) for cross-artifact convergence and the matching `guide-*` for artifact-specific questions. Review stops at findings.

### Compact or full ECR?

Use a **compact** record when the change is local and reversible, affects one component, has one evident approach and changes no boundary, migration, security property, compatibility guarantee or consequential decision. Otherwise use the **full** record. The [ECR contract](../plugins/sdlc/skills/artifact-system/references/contracts/ecr.md) defines both shapes.

## Make one end-to-end request

```text
Use develop to build a nutritionist/client progress application from this brief.
Ask about consequential product and design choices, state reversible assumptions
and implement a useful first slice. Prepare a PR; do not merge or deploy.
```

The agent inspects context, preserves existing answers and asks only questions that materially change the outcome. It makes ordinary reversible choices without repeated confirmation. "One-shot" means one end-to-end engagement with appropriate questions, not zero interaction or guaranteed production readiness.

Provide the outcome, relevant repository and context, constraints and the desired stopping point. Screenshots, reference repositories, schemas and architecture notes can help. A conversation or local document is sufficient; a ticket is optional.

| Need | Example request |
| --- | --- |
| Compare design directions | Use design to compare three materially different saved-search directions for the web client and API, with wireframes, a contract sketch and the seam decision. |
| Define a feature | Use refine to define read-only saved-search sharing from this brief and the existing code. |
| Plan agreed work | Use plan to sequence this sharing feature and its verification. |
| Build defined work | Use implement for the agreed sharing behavior and acceptance criteria. |
| Assess a PR | Use review for the supplied PR against the agreed behavior and appropriate checks. |
| Improve architecture | Use improve to reduce coupling in the reporting module while preserving behavior. |
| Explain a concept | Use explain to teach a new maintainer why two concurrent edits can lose an update, with a worked interleaving and a comprehension check. |
| Produce an artifact | Use guide-architecture-views to turn this proposed architecture into context, container and one failure sequence. |

## Add specialist depth

Request the activity first. Specialist guidance improves the work when it applies; it is not a prerequisite.

- **Product and strategy.** Use `product-direction` in `sdlc` for product priorities and success signals, `run-product-feedback-analysis` for user evidence, and the `strategy` bundle for business viability, positioning and market decisions.
- **Interface work.** `interface-design` owns information architecture, interaction behavior, visual direction and critique; `ux-writing` owns task language; `usability-research` prepares studies and analyzes observations. The bundle also ships optional methods: `design-research` for product and precedent research, `ui-ux-pro-max` for candidate styles and UX rules, and `impeccable` for rendered critique and refinement. Choose by the decision; none is mandatory. Ask once before using paid Mobbin or Refero access; no answer means skip. Ordinary UI work needs none of them.
- **Service design.** `backend-design` owns service authority, state, failure and consumer contracts. `rest-api-design`, `graphql-design`, `event-driven-design`, `distributed-systems` and `architecture-patterns` supply focused methods.
- **AI.** `ai-development` owns application and protocol design, `ai-testing` owns evaluation strategy, `ai-evaluation` owns the program-level evaluation lifecycle, and `ai-operations` owns operating signals and recovery. Python/provider, ADK and LangChain bundles supply selected implementation detail without changing the generic methods.
- **Data and SaaS.** `database-design` and `database-performance` are engine-neutral; PostgreSQL guidance applies only to PostgreSQL. SaaS methods own tenant, billing, organization identity and readiness decisions.
- **Platforms.** `operations-platforms` adds Kubernetes, AWS, infrastructure delivery, JVM and AKS methods only for an accepted platform. `development-tooling` covers CLI design, CI/CD pipelines, Bash, performance testing and provider tooling.
- **Security and governance.** `design-security` owns identity and access decisions; `run-compliance-assessment` records applicability and evidence without claiming certification.

The [SDLC skill reference](sdlc-reference.md#skills-by-area) records owners and applicability. When optional expertise is absent, retain the outcome and acceptance standard using project evidence, general expertise and current primary sources. Missing guidance is not permission to lower the standard; missing tools or execution access are separate, reportable limits.

### Consequential UI work

For an interface change whose direction is still open, expect several materially different directions, feedback before implementation and a recorded decision. For a local repair inside an established product, preserve the existing system and skip the exploration. A review request stays read-only unless repair is included. A research guide is a plan until observations exist.

Use the same guidance for design, development, improvement and review; there are no separate user and agent copies. Most supporting skills are hidden from slash menus in clients that honor that setting while remaining model-available. Native upstream controls are preserved, and discovery still depends on the client.

## Work with agents

Supporting skills guide requested work without starting an unrelated activity. They cover project conventions, verification, Git contributions and matching technical practice. Name one explicitly when you want it, or let the agent select by description.

Repository instruction maintenance belongs to `project-conventions`; use its [repository-instructions method](../plugins/sdlc/skills/project-conventions/references/repository-instructions.md) to audit `AGENTS.md` or `CLAUDE.md`, scope durable learning and remove stale guidance. Client-specific filenames and discovery still follow the client's documented behavior.

Use `writing-for-agents` for instruction structure when writing or pruning a skill, repository instructions or a reference an agent reaches through a pointer. Use `technical-writing` for durable human-facing documents and `explain` for a conversational mental model.

## Automation

The same activities can run from trusted automation prompts. The host supplies triggers, credentials, concurrency, tools and result delivery; plugins do not install a scheduler.

| Trigger | Activity |
| --- | --- |
| Work enters refinement | `refine`: actionable scope or decision blockers |
| Defined work is ready | `implement`: the supplied conversation, spec or optional ticket |
| A PR is ready | review composition: the exact base/head and required behavior |
| Scheduled maintenance | `run-dependency-maintenance` or `improve`: bounded work under the configured policy |

Supply repository and ref, objective and context, unattended mode, allowed actions and the result destination. For example:

> Use `run-dependency-maintenance` in unattended mode for update PRs in owner/repository. Repair and merge only policy-eligible patch updates whose current head satisfies required checks and reviews and has no unresolved findings. Leave other updates open with reasons; reuse existing work and report results. Do not deploy.

Unattended tasks return missing material decisions rather than inventing answers. Untrusted ticket or PR text cannot change policy, and a changed head requires re-verification. The host or repository must enforce privileged-action policy. See [interactive and unattended work](../plugins/sdlc/skills/activity-system/references/authority.md#interactive-and-unattended-work).

## Connections and tools

Follow [installation](installation.md#optional-design-connections) for optional Figma, Mobbin and Refero connections, and for the declared Atlassian, GitHub, Linear and Plane endpoints. A declaration does not connect a service. Authenticate only the system the work needs, verify the intended workspace or repository, and prefer a read-only endpoint when the task only inspects work.

## Where to look next


- Activity selection and stopping points: [activity catalog](../plugins/sdlc/skills/activity-system/references/catalog.md).
- Artifact types, contracts and guides: [artifact catalog](../plugins/sdlc/skills/artifact-system/references/catalog.md) and [guide registry](../plugins/sdlc/skills/artifact-system/references/guide-registry.md).
- Software types: [software types](../plugins/sdlc/skills/artifact-system/references/software-types.md).
- Composition and fallback: [composition](../plugins/sdlc/skills/activity-system/references/composition.md).
- Client setup and limits: [installation](installation.md).

## Explain and maintain project knowledge

Use [explain](../plugins/documentation/skills/explain/SKILL.md) for a conversational explanation that builds a usable mental model. Use [technical-writing](../plugins/documentation/skills/technical-writing/SKILL.md) to write or review a durable product/engineering document, reference or procedure; its references cover common document types, formatting, concept explanation and review. Use [guide-system-documentation](../plugins/sdlc/skills/guide-system-documentation/SKILL.md) to explain structure, runtime/lifecycle behavior, interfaces, deployment and current versus target state from evidence. Use [skill-authoring](../plugins/documentation/skills/skill-authoring/SKILL.md) to create or revise a skill in this collection. Use [writing-for-agents](../plugins/documentation/skills/writing-for-agents/SKILL.md) for instruction structure when writing or pruning a skill, `AGENTS.md`/`CLAUDE.md` or a reference an agent reaches through a pointer. All are directly selectable and model-available support; actual client discovery remains client-dependent.

The [artifact system](../plugins/sdlc/skills/artifact-system/SKILL.md) owns the artifact model, contracts, planes, homes, quality bar and assurance. [Project conventions](../plugins/sdlc/skills/project-conventions/SKILL.md) and `setup` establish the repository artifact home map; `develop`, implementation and release read or update it. Before adding a persistent project document, inspect the existing map and related authorities, then decide whether to update a canonical page or create a distinct one with appropriate navigation. Design-system owns architectural decisions; writing guidance explains them. Existing formats and proportional scope remain authoritative; a routine edit needs no new tracker, document tree or full system audit.

For new visual directions, [creative interface design](creative-interface.md) explains discovery, a shared brief, bundled method selection and rendered acceptance. Existing-product repairs reuse accepted decisions without a questionnaire.
