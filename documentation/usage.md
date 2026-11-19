# Using the plugins

[Install the bundles](installation.md) before using this guide. Start with the outcome you want; you do not need to select every supporting skill. The [SDLC overview](../README.md#sdlc-coverage) shows where activities fit, and the [skill map](sdlc.md) links to deeper expertise. [Engineering artifacts and workspaces](artifact-workflow.md) explain the artifact model, planes, homes, contracts, quality bar, filesystem/provider choices and diagram lifecycle.

[Choose an activity](#skills-you-invoke) · [Focused examples](#focused-examples) · [UI/UX work](#uiux-expertise-for-people-and-agents) · [Automation](#scheduled-and-event-triggered-tasks)

## Skills you invoke

Select the activity through the client's supported invocation:

| Client | Example after discovery |
| --- | --- |
| Claude Code | `/sdlc:test` |
| Codex | Select `test` in the skill picker, then describe the change |
| OpenCode V2 | `@test` followed by the behavior to verify |

The [installation guide](installation.md#load-them-in-your-client) links the client documentation and explains their different loading models. Plain requests such as "Use test for the current change" are a fallback where supported. `activity-system` describes this collection and its help mode and does not replace the client's built-in help.

| Where you are | Task | Expected result |
| --- | --- | --- |
| Unsure what to use | `activity-system` | Relevant capabilities, examples and next activity |
| Rough idea to working software | `develop` | Clarification, design, implementation, tests and review |
| Starting or adopting a project | `setup` | Useful foundations, context and working commands |
| Outcome, first slice or feasibility is open | `plan` | Scoped decision and next action, with a linked brief, roadmap or actionable ticket when warranted |
| Requirements need definition | `refine` | Functional and relevant quality constraints, observable acceptance or concrete questions; requirements-engineering supports substantial analysis |
| Scope agreed and only a breakdown is requested | Ask for implementation preparation | Bounded steps and verification |
| Architecture, UX or contracts undecided | `design` | System/platform decisions and interaction contracts before implementation |
| Defined work ready to build | `implement` | Implemented and verified change |
| Need evidence of behavior | `test` | Checks, results and coverage gaps |
| PR or diff ready for assessment | review composition (`code-review` + `test` + artifact assurance) | Findings against intended behavior, design, tests and artifact consistency |
| Want improvements | `improve` | Prioritized opportunities, or a specified improvement |
| Reported defect with repair requested | `fix` | Reproduced or evidenced defect, focused repair and verification |
| Security/privacy weakness | `harden` | Scoped assessment, fixes and remaining risks |
| Dependencies need attention | `run-dependency-maintenance` | Compatibility, release-note and CI review; permitted remediation |
| Preparing delivery | `release` | Readiness, or a named authorized delivery action |

`plan`, `refine` and `design` stop at their respective outcomes. `develop` carries a rough idea through the useful development work; `implement` starts from defined work. Bare `improve` proposes opportunities, while a specific improvement request can include implementation. Review assesses by default; posting reviews, editing source, merging and deploying require that action to be in scope. A routine test request does not authorize deployed load or faults.

`implement` is a local activity that starts from defined work. Optional explicit workflows include `grill-me`, `grill-with-docs`, `to-questionnaire`, `write-spec` and `retro`. `handoff` lives in the `documentation` bundle. Use them when their particular method helps; interviews, specs and trackers are not prerequisites. [Upstream selection](maintainers/sources.md#matt-pocock-selection) explains which upstream methods remain and why.

## Product decisions and specialist methods

Select strategy for product-management, business direction and product feedback. Ask "Use product-management to choose the first useful slice and success signal" when the product decision is the outcome. Ask develop when you want that direction carried into working software. Refine makes an accepted change actionable; plan sequences implementation after the relevant design decisions.

Frontend-development provides one integrated interface-design method for information architecture, interaction, visual craft and critique, plus design research, independent UX writing and usability research. The package ships several optional design methods: `ui-ux-pro-max` for candidate styles and UX rules, `impeccable` for rendered critique and refinement, and `design-research` for product and precedent research. Choose by the decision; no single method is mandatory. `design-research` asks once about optional Mobbin or Refero access and continues with repository evidence, user references, public product research and local prototypes when those services are unavailable. For consequential UI work, expect at least three materially different directions, a request for feedback and a recorded decision before implementation. Creative, subject-specific art direction is conditionally available inside interface-design when choices are open; ordinary changes preserve the existing system. Application-specific specialists contribute archetype patterns and domain semantics, while the accepted frontend platform constrains and implements the design. Backend-development provides service design across stacks, with dedicated REST, GraphQL, event-driven, distributed-systems and architecture-pattern methods.

The ai-development package supplies four generic skills: ai-development for application patterns, architecture and capability/protocol decisions; ai-testing for testing/evaluation strategy, cases and evidence; ai-evaluation for the program-level evaluation lifecycle, datasets, gates, production sampling and reporting; and ai-operations for task signals, quality monitoring, provider/resource limits and recovery. Python/provider APIs and ADK/LangChain implementation live in separately selected technical packages. Ai-python-development includes ai-deepeval-testing for a selected DeepEval evaluation runner, with a playbook for datasets, metrics, CI and local reporting, and python-ai-observability for Python OpenTelemetry instrumentation. Quality criteria and operating outcomes stay generic, and no hosted backend is required. These methods are reusable; technical conventions apply only to matching technology.

For an existing accepted product, start with the affected work. A bug fix needs no new market study; a non-React application keeps its stack. The activity system recommends relevant activities without executing them, and missing optional guidance does not block the activity: use project evidence, general expertise and appropriate primary sources while retaining acceptance and verification standards. Missing tools or an execution target remain precise limits. See [composition and fallback](architecture.md#compose-without-optional-dependencies).

The operations-platforms package adds platform-specific methods only when the accepted stack calls for them: kubernetes-resource-engineering for object semantics, kubernetes-troubleshooting for live-cluster diagnosis, infra-delivery for infrastructure and GitOps delivery, aws-platform for AWS service decisions, infra-jvm-optimization for JVM tuning and aks-cost-optimization for AKS. Kubernetes troubleshooting does not design manifests, and aws-platform does not reproduce every service. Application configuration lives in sdlc and covers source precedence, typed validation, secrets and reload.

Repository instruction maintenance is local to `project-conventions`. Use its [maintenance method](../plugins/sdlc/skills/project-conventions/references/repository-instructions.md) for AGENTS.md/CLAUDE.md audits, scope, durable session learnings and removal of stale guidance. It absorbed the useful Sentry repository-instruction authoring rules without adopting its line targets or sample attribution policy. Client-specific filenames and discovery still require the client's documented behavior.

## SaaS, security, governance and data expertise

Use the relevant sdlc capability, or add a product/technical package when its deeper methods help. These requests can end at design or assessment; they do not require a complete application engagement.

| Need | Example request | Useful boundary |
| --- | --- | --- |
| Requirements and quality attributes | Use refine with requirements-engineering to write the ECR requirement set, then design to answer it. | Functional, non-functional and design requirements per affected area, with IDs and acceptance evidence. |
| SaaS behavior and administration | Use saas-design to define organization membership, subscription/entitlement changes and offboarding for the accepted product. | Customer commitments and transitions; framework/provider implementation remains contextual. |
| Supporting services | Use saas-supporting-services to choose analytics, email, search, queues or notifications from the requirement, not a vendor list. | Build/managed/self-hosted/defer comparison, integration contract and evidence limits. |
| Billing and entitlements | Use saas-billing to define plans, entitlements, provider events, reconciliation and dunning. | Stripe for web; ask about Superwall for mobile. No durable prices or fees. |
| Organization identity | Use saas-identity-and-access for roles, invitations, SSO/SCIM, machine identity and support access. | Organization authority; general authentication remains with design-security. |
| Requirements synthesis | Use write-spec when a conversation already contains the decision and needs to become ECR spec content. | No re-interview, story catalogue or tracker requirement; refine owns readiness. |
| Production readiness | Use run-production-readiness-review to assess whether a service can be depended on for a scoped launch. | Readiness evidence and limits; release still owns the authorized action. |
| System documentation | Use guide-system-documentation to discover, record and review the current architecture set. | Current versus proposed stays explicit; C4/sequence guides own view detail. |
| Infrastructure delivery | Use infra-delivery for IaC choice, GitOps reconciliation, drift and delivery recovery. | Owns infrastructure as code; Kubernetes semantics and AWS services stay with their owners. |
| AWS services | Use aws-platform for the common IAM, network, compute, data, operations and cost decisions. | Reference-only reuse of upstream AWS material; verify current prices, quotas and docs. |
| Customer/operator dashboard | Use saas-dashboard-design to shape the operations queue and billing administration using the existing design system. | Tasks, context, data meaning and interface states before dependent implementation. |
| Identity and resource authority | Use design-security to compare identity options and define session, tenant/resource permission and revocation behavior. | Preserve accepted providers; no account setup or credential change is implied. |
| Applicable obligations and readiness | Use run-compliance-assessment for the supplied service and evidence, stopping at an assessment. | Actual applicability, controls, evidence and unresolved judgments; no certification or external submission. |
| Data design or workload bottleneck | Use database-design or database-performance for the affected workload; apply PostgreSQL expertise only for that engine. | Invariants, compatibility and measured evidence; an unavailable database remains an execution limit. |
| PostgreSQL upgrades | Use postgresql-operations for major, minor or managed upgrade planning and rehearsal. | Version and provider constraints; no in-place downgrade. |
| Capacity and cost planning | Use design-system for capacity and cost plans; use analyze-capacity-cost for measured saturation, FinOps allocation, forecasting and optimization. | Plans and targets belong to design/ECR; provider mechanics belong to provider guidance. No invented rates. |
| TypeScript or Go implementation | Use matching language guidance for the existing library, service or client and its real consumers. | Loading a language package does not select a framework or runtime migration. |

The [skill map](sdlc-reference.md#skills-by-area) records owners and applicability. Missing optional expertise preserves the requested outcome and acceptance standard using project evidence, general expertise and appropriate primary sources; it does not authorize installation or justify a weaker result.

## One end-to-end request

```text
Use develop to build a nutritionist/client progress application from this brief. Ask about consequential product and design choices, state reversible assumptions and implement a useful first slice. Prepare a PR; do not merge or deploy.
```

The agent inspects context, preserves existing answers and asks questions that materially change the outcome. It makes ordinary reversible choices without repeated confirmation. "One-shot" means one end-to-end engagement with appropriate questions, not zero interaction or guaranteed production readiness.

Provide the outcome, relevant repository/context, constraints and desired stopping point. Screenshots, reference repositories, schemas and architecture notes can help. A conversation or local document is sufficient; a ticket is optional.

## Focused examples

| Need | Request |
| --- | --- |
| Compare design directions | Use design to compare three materially different saved-search directions for the web client and API, with wireframes, a contract sketch and the seam decision. |
| Research interface precedent | Use design-research to compare how shipped products handle subscription cancellation, then use interface-design to turn the findings into three directions. |
| Explain a concept | Use explain to teach a new maintainer why two concurrent edits can lose an update, with a worked interleaving and a comprehension check. |
| Produce an artifact | Use guide-architecture-views to turn this proposed architecture into context, container and one failure sequence. |
| Define a feature | Use refine to define read-only saved-search sharing from this brief and the existing code. |
| Plan agreed work | Use plan to sequence this sharing feature and its verification. |
| Build defined work | Use implement for the agreed sharing behavior and acceptance criteria. |
| Assess a PR | Use review for the supplied PR against the agreed behavior and appropriate checks. |
| Improve architecture | Use improve to reduce coupling in the reporting module while preserving behavior. |
| Maintain dependencies | Use `run-dependency-maintenance` to assess the update PRs, release notes and checks; prepare fixes where needed. |
| Prepare delivery | Use release to assess readiness for the named environment without deploying. |
| Get help | Use activity-system: I am changing an existing application's navigation. |

### Compare directions before deciding

```text
Use design to compare three materially different ways to add saved searches across the web client and API. Show the UI states and the contract or sequence for each, decide the error and pagination seam, and record the recommendation. Do not implement yet.
```

Expect three options that differ in responsibility or behavior, a linked artifact for each affected type, and one seam decision. A design request stops at the decision. For a backend-only change, the frontend is explicitly not affected; for a UI-only change, do not invent backend design work.

Read [software types](../plugins/sdlc/skills/artifact-system/references/software-types.md), the [option set](../plugins/sdlc/skills/design/references/option-set.md) and the [design proposal contract](../plugins/sdlc/skills/artifact-system/references/contracts/design-proposal.md).

### Define UX before changing screens

```text
Use design to unify navigation, nested menus and edit dialogs across this application. Specify the interactions and show wireframes where useful. Do not implement yet.
```

Then ask `improve` or `develop` to implement the agreed direction. Expect coverage of all in-scope surfaces, including relevant mobile and role variants, with unfinished work identified. [Interface design](../plugins/frontend-development/skills/interface-design/SKILL.md) owns the integrated UX/UI method; [design research](../plugins/frontend-development/skills/design-research/SKILL.md) supplies precedent and option evidence. Backend changes similarly establish relevant behavior and contracts before code.

### Evaluate during implementation

Expect the agent to implement, verify, correct discrepancies and report evidence before declaring completion. Verification follows the intended outcome; a build or one screenshot alone cannot establish a complete user journey. Missing execution or coverage remains explicit. See [change verification](../plugins/sdlc/skills/test/SKILL.md) and [testing-journey](../plugins/frontend-development/skills/testing-journey/SKILL.md) for methods.

### Run services and observability locally

Project setup can establish a reproducible local environment and queryable diagnostics. Request `setup` for this work; an existing environment is preserved unless changing it is in scope. Details belong to [project conventions](../plugins/sdlc/skills/project-conventions/SKILL.md) and [observability design](../plugins/sdlc/skills/design-system/references/observability-and-monitoring.md).

## Skills agents use during your work

Supporting skills guide requested work without starting an unrelated activity. Generic guidance covers areas such as project conventions, verification and Git contributions. Stack-specific guidance applies to technologies such as Next.js or FastAPI. You can name guidance explicitly; the [area catalogue](sdlc-reference.md#skills-by-area) shows applicability and upstream specialists.

Most local supporting skills are hidden from slash menus in clients honoring that setting, while remaining available to the model. Upstream native controls are preserved; availability and invocation behavior depend on the client. Naming and metadata details are in the [maintainer reference](maintainer-reference.md#naming-and-invocation).

## Operations and specialized activities

Add the relevant bundle and request its installed skill by name. Examples:

- Use `run-incident-response` to investigate current impact within the established action boundaries.
- Use `guide-runbook` to author, exercise or audit a runbook; design-system owns the design plan, and `analyze-capacity-cost` owns measurement and FinOps.
- Use `business-strategy` to explore an idea with at least three materially different options, or `learn-from-product-feedback` to assess existing evidence.
- Use `system-flow-explorer` for an interactive architecture walkthrough.
- Use `rest-api-design` or `graphql-design` for an external API contract, `event-driven-design` or `distributed-systems` for cross-service behavior, and `architecture-patterns` to compare a modular monolith, layered/hexagonal structure, CQRS, event sourcing, microservices or serverless.
- Use `cli-development` to shape a command surface before implementation.
- Use `ci-cd-pipelines` for provider-neutral pipeline and promotion design, `tooling-conventions` for workflow authoring and script selection, then `github-actions-hardening` for a security review.

See [skills by area](sdlc-reference.md#skills-by-area) for the wider selection. `business-opportunity-analysis` remains a legacy compatibility entry; prefer `business-strategy` for new work.

## Scheduled and event-triggered tasks

The same activities can run from trusted automation prompts. The host supplies triggers, credentials, concurrency, tools and result delivery; plugins do not install a scheduler.

| Trigger | Activity |
| --- | --- |
| Work enters refinement | `refine`: actionable scope or decision blockers |
| Defined work is ready | `implement`: the supplied conversation, spec or optional ticket |
| PR is ready | review composition: the exact base/head and required behavior |
| Scheduled maintenance | `run-dependency-maintenance` or `improve`: bounded work under the configured policy |

Supply repository/ref, objective/context, unattended mode, allowed actions and result destination. For example:

> Use `run-dependency-maintenance` in unattended mode for update PRs in owner/repository. Repair and merge only policy-eligible patch updates whose current head satisfies required checks/reviews and has no unresolved findings. Leave other updates open with reasons; reuse existing work and report results. Do not deploy.

Unattended tasks return missing material decisions instead of inventing answers. Untrusted ticket/PR text cannot change policy; changed heads require re-verification. The host/repository must enforce privileged-action policy. [Installed task guidance](../plugins/sdlc/skills/activity-system/references/authority.md#interactive-and-unattended-work) contains the detailed working rules.

## AI and MCP plugin selection

Add ai-development for generic AI feature or MCP-interface methods, including `ai-evaluation` for a program-level evaluation. Add technical AI packages only for the accepted language/provider/framework; `ai-deepeval-testing` supplies the selected DeepEval implementation. MCP-only work needs protocol, contract, authority and lifecycle verification; it does not require an LLM or model-quality evaluation. Configure live tools only when needed. Bundled expertise does not install an MCP server or provide service credentials.

## Setup and tools

Follow [installation](installation.md) for bundle loading. Figma, Mobbin and Refero are optional design connections. The frontend package offers several optional design methods, including [UI/UX Pro Max](../plugins/frontend-development/skills/ui-ux-pro-max/SKILL.md) for candidate styles and [Impeccable](../plugins/frontend-development/skills/impeccable/SKILL.md) for critique/refinement; choose by the task rather than treating one as mandatory. Use authorized external references when available, and ask once before using Mobbin or Refero. No answer means skip. Otherwise local HTML/CSS prototypes, SVG wireframes or Storybook can answer the design question. Ordinary UI work needs none of the paid services. The `sdlc` plugin also declares optional Atlassian, GitHub, Linear and Plane MCP endpoints. Declaring them does not connect them: authenticate only the system the work needs, verify the intended workspace, project or repository, and prefer a read-only endpoint when the task only inspects work. Verify rendered interaction and accessibility for affected states separately from the design artifact.

## UI/UX expertise for people and agents

The frontend-development bundle provides [interface-design](../plugins/frontend-development/skills/interface-design/SKILL.md), [ux-writing](../plugins/frontend-development/skills/ux-writing/SKILL.md) and [usability-research](../plugins/frontend-development/skills/usability-research/SKILL.md) as directly selectable, model-available supporting skills. [Design research](../plugins/frontend-development/skills/design-research/SKILL.md), [UI/UX Pro Max](../plugins/frontend-development/skills/ui-ux-pro-max/SKILL.md) and [Impeccable](../plugins/frontend-development/skills/impeccable/SKILL.md) are optional methods selected by the decision; none is a mandatory baseline. Client picker/discovery behavior still needs verification. The same guidance supports design, develop, improve and review when relevant; no separate user and agent copies are maintained.

Ask for a scoped result: "Review this dialog without changing it", "Improve and apply the error messages in this flow", or "Prepare a usability study for onboarding". A bare review/improvement assessment stays read-only. A specified repair can include implementation and rechecking. A research guide is a plan until actual observations exist. Ordinary UI development needs no compulsory study or Figma connection.

Interface-design owns information architecture, interactions, visual direction, cross-view consistency, critique and component/token audits; frontend conventions implement the accepted direction for the selected React stack. UX-writing owns task language, and usability-research owns studies and participant evidence synthesis. Existing test/journey guidance verifies implementation and Storybook states where adopted.

## Explain and maintain project knowledge

Use [explain](../plugins/documentation/skills/explain/SKILL.md) for a conversational explanation that builds a usable mental model. Use [technical-writing](../plugins/documentation/skills/technical-writing/SKILL.md) to write or review a durable product/engineering document, reference or procedure; its references cover common document types, formatting, concept explanation and review. Use [guide-system-documentation](../plugins/sdlc/skills/guide-system-documentation/SKILL.md) to explain structure, runtime/lifecycle behavior, interfaces, deployment and current versus target state from evidence. Use [skill-authoring](../plugins/documentation/skills/skill-authoring/SKILL.md) to create or revise a skill in this collection. All are directly selectable and model-available support; actual client discovery remains client-dependent.

The [artifact system](../plugins/sdlc/skills/artifact-system/SKILL.md) owns the artifact model, contracts, planes, homes, quality bar and assurance. [Project conventions](../plugins/sdlc/skills/project-conventions/SKILL.md) and `setup` establish the repository artifact home map; `develop`, implementation and release read or update it. Before adding a persistent project document, inspect the existing map and related authorities, then decide whether to update a canonical page or create a distinct one with appropriate navigation. Design-system owns architectural decisions; writing guidance explains them. Existing formats and proportional scope remain authoritative; a routine edit needs no new tracker, document tree or full system audit.

For new visual directions, [creative interface design](creative-interface.md) explains discovery, a shared brief, bundled method selection and rendered acceptance. Existing-product repairs reuse accepted decisions without a questionnaire.
