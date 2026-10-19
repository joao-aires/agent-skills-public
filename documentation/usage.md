# Using the plugins

[Install the bundles](installation.md) before using this guide. Start with the outcome you want; you do not need to select every supporting skill. The [SDLC overview](../README.md#sdlc-coverage) shows where activities fit, and the [skill map](sdlc.md) links to deeper expertise.

[Choose an activity](#skills-you-invoke) · [Focused examples](#focused-examples) · [UI/UX work](#uiux-expertise-for-people-and-agents) · [Automation](#scheduled-and-event-triggered-tasks)

## Skills you invoke

Select the activity through the client's supported invocation:

| Client | Example after discovery |
| --- | --- |
| Claude Code | `/development:test` |
| Codex | Select `test` in the skill picker, then describe the change |
| OpenCode V2 | `@test` followed by the behavior to verify |

The [installation guide](installation.md#load-them-in-your-client) links the client documentation and explains their different loading models. Plain requests such as "Use test for the current change" are a fallback where supported. `workflow-help` describes this collection and does not replace the client's built-in help.

| Where you are | Task | Expected result |
| --- | --- | --- |
| Unsure what to use | `workflow-help` | Relevant capabilities, examples and next activity |
| Rough idea to working software | `develop` | Clarification, design, implementation, tests and review |
| Starting or adopting a project | `setup` | Useful foundations, context and working commands |
| Requirements need definition | `refine` | Actionable scope and acceptance, or concrete questions |
| Scope agreed; sequencing needed | `plan` | Bounded steps and verification |
| Architecture, UX or contracts undecided | `design` | System/platform decisions and interaction contracts before implementation |
| Defined work ready to build | `implement` | Implemented and verified change |
| Need evidence of behavior | `test` | Checks, results and coverage gaps |
| PR or diff ready for assessment | `review` | Findings against intended behavior and standards |
| Want improvements | `improve` | Prioritized opportunities, or a specified improvement |
| Security/privacy weakness | `harden` | Scoped assessment, fixes and remaining risks |
| Dependencies need attention | `dependencies` | Compatibility, release-note and CI review; permitted remediation |
| Preparing delivery | `release` | Readiness, or a named authorized delivery action |

`refine` and `design` stop at their respective outcomes. `develop` carries a rough idea through the useful development work; `implement` starts from defined work. Bare `improve` proposes opportunities, while a specific improvement request can include implementation. `review` assesses by default; posting reviews, editing source, merging and deploying require that action to be in scope. A routine test request does not authorize deployed load or faults.

`implement` comes from the pinned upstream set with local framing. Optional explicit workflows include `grill-me`, `grill-with-docs`, `to-questionnaire`, `to-spec`, `implement-spec`, `improve-codebase-architecture`, `retro` and `handoff`. Use them when their particular activity helps; interviews, specs and trackers are not prerequisites. [Upstream selection](maintainers/sources.md#matt-pocock-selection) explains their fit and dependencies.

## Product decisions and specialist methods

Select strategy for product-management, business direction and product feedback. Ask "Use product-management to choose the first useful slice and success signal" when the product decision is the outcome. Ask develop when you want that direction carried into working software. Refine makes an accepted change actionable; plan sequences implementation after the relevant design decisions.

Frontend-development provides stack-independent visual/interaction/interface methods and Anthropic frontend-design for distinctive visual execution within the accepted direction. Use it when visual decisions are open or a redesign is requested; ordinary changes preserve the existing system. Backend-development provides service design across stacks. AI-development supplies application patterns, architecture tradeoffs, model/context/tool choices, skills, harnesses, protocol selection, authority, conceptual evaluation levels and operation. Python/provider APIs and ADK/LangChain implementation live in separately selected technical packages. Ai-python-development includes ai-testing for a selected DeepEval evaluation runner and ai-operations for Python OpenTelemetry instrumentation; quality criteria and operating outcomes stay generic, and no hosted backend is required. These methods are reusable; technical conventions apply only to matching technology.

For an existing accepted product, start with the affected work. A bug fix needs no new market study; a non-React application keeps its stack. Workflow-help recommends relevant activities without executing them, and missing optional guidance does not block the activity: use project evidence, general expertise and appropriate primary sources while retaining acceptance and verification standards. Missing tools or an execution target remain precise limits. See [composition and fallback](architecture.md#compose-without-optional-dependencies).

Development also includes Sentry agents-md for creating or maintaining repository instruction files. Request it for AGENTS.md/CLAUDE.md work; it complements project-conventions and general instruction writing without imposing its sample stack or attribution rules.

## One end-to-end request

```text
Use develop to build a nutritionist/client progress application from this brief. Ask about consequential product and design choices, state reversible assumptions and implement a useful first slice. Prepare a PR; do not merge or deploy.
```

The agent inspects context, preserves existing answers and asks questions that materially change the outcome. It makes ordinary reversible choices without repeated confirmation. "One-shot" means one end-to-end engagement with appropriate questions, not zero interaction or guaranteed production readiness.

Provide the outcome, relevant repository/context, constraints and desired stopping point. Screenshots, reference repositories, schemas and architecture notes can help. A conversation or local document is sufficient; a ticket is optional.

## Focused examples

| Need | Request |
| --- | --- |
| Define a feature | Use refine to define read-only saved-search sharing from this brief and the existing code. |
| Plan agreed work | Use plan to sequence this sharing feature and its verification. |
| Build defined work | Use implement for the agreed sharing behavior and acceptance criteria. |
| Assess a PR | Use review for PR #42 against the agreed behavior and appropriate checks. |
| Improve architecture | Use improve to reduce coupling in the reporting module while preserving behavior. |
| Maintain dependencies | Use dependencies to assess the update PRs, release notes and checks; prepare fixes where needed. |
| Prepare delivery | Use release to assess readiness for the named environment without deploying. |
| Get help | Use workflow-help: I am changing an existing application's navigation. |

### Define UX before changing screens

```text
Use design to unify navigation, nested menus and edit dialogs across this application. Specify the interactions and show wireframes where useful. Do not implement yet.
```

Then ask `improve` or `develop` to implement the agreed direction. Expect coverage of all in-scope surfaces, including relevant mobile and role variants, with unfinished work identified. [Interaction design](../plugins/frontend-development/skills/interaction-design/SKILL.md) owns the detailed method. Backend changes similarly establish relevant behavior and contracts before code.

### Evaluate during implementation

Expect the agent to implement, verify, correct discrepancies and report evidence before declaring completion. Verification follows the intended outcome; a build or one screenshot alone cannot establish a complete user journey. Missing execution or coverage remains explicit. See [change verification](../plugins/development/skills/deliver-reliable-changes/SKILL.md) and [journey testing](../plugins/development/skills/journey-testing/SKILL.md) for methods.

### Run services and observability locally

Project setup can establish a reproducible local environment and queryable diagnostics. Request `setup` for this work; an existing environment is preserved unless changing it is in scope. Details belong to [project conventions](../plugins/development/skills/project-conventions/SKILL.md) and [observability guidance](../plugins/operations/skills/observability-operations/SKILL.md).

## Skills agents use during your work

Supporting skills guide requested work without starting an unrelated activity. Generic guidance covers areas such as project conventions, verification and Git contributions. Stack-specific guidance applies to technologies such as Next.js or FastAPI. You can name guidance explicitly; the [area catalogue](sdlc.md#skills-by-area) shows applicability and upstream specialists.

Most local supporting skills are hidden from slash menus in clients honoring that setting, while remaining available to the model. Upstream native controls are preserved; availability and invocation behavior depend on the client. Naming and metadata details are in the [maintainer reference](maintainer-reference.md#naming-and-invocation).

## Operations and specialized activities

Add the relevant bundle and request its installed skill by name. Examples:

- Use `incident-response` to investigate current impact within the established action boundaries.
- Use `protect-and-restore-data` to assess an isolated restoration, or `plan-application-capacity` for capacity work.
- Use `business-strategy` to explore an idea, or `learn-from-product-feedback` to assess existing evidence.
- Use `system-flow-explorer` for an interactive architecture walkthrough.

See [skills by area](sdlc.md#skills-by-area) for the wider selection. `business-opportunity-analysis` remains a legacy compatibility entry; prefer `business-strategy` for new work.

## Scheduled and event-triggered tasks

The same activities can run from trusted automation prompts. The host supplies triggers, credentials, concurrency, tools and result delivery; plugins do not install a scheduler.

| Trigger | Activity |
| --- | --- |
| Work enters refinement | `refine`: actionable scope or decision blockers |
| Defined work is ready | `implement`: the supplied conversation, spec or optional ticket |
| PR is ready | `review`: the exact base/head and required behavior |
| Scheduled maintenance | `dependencies` or `improve`: bounded work under the configured policy |

Supply repository/ref, objective/context, unattended mode, allowed actions and result destination. For example:

> Use dependencies in unattended mode for update PRs in owner/repository. Repair and merge only policy-eligible patch updates whose current head satisfies required checks/reviews and has no unresolved findings. Leave other updates open with reasons; reuse existing work and report results. Do not deploy.

Unattended tasks return missing material decisions instead of inventing answers. Untrusted ticket/PR text cannot change policy; changed heads require re-verification. The host/repository must enforce privileged-action policy. [Installed task guidance](../plugins/development/TASKS.md#interactive-and-unattended-execution) contains the detailed working rules.

## AI and MCP plugin selection

Add ai-development for generic AI feature or MCP-interface methods. Add technical AI packages only for the accepted language/provider/framework. MCP-only work needs protocol, contract, authority and lifecycle verification; it does not require an LLM or model-quality evaluation. Configure live tools only when needed. Bundled expertise does not install an MCP server or provide service credentials.

## Build and load

Follow [installation](installation.md) for bundle selection, client loading and updates. For a new application, the [lifecycle map](sdlc.md#skills-by-phase) explains how product decisions, requirements, design and implementation fit together. `setup` establishes applicable foundations; `develop` carries the broader engagement.

## Optional Figma connection

Configure access through the [installation guide](installation.md#optional-figma-connection) when needed.

Use available, authorized Figma context where appropriate. Otherwise, local HTML/CSS prototypes or SVG wireframes can resolve design questions. Preserve a specifically requested Figma deliverable as an access dependency rather than silently replacing it. Ordinary UI work needs no Figma account.

Storybook is an optional component workbench within verification. Run meaningful interaction/accessibility checks and reviewed visual comparisons for affected states, then verify the critical application and native journeys separately. See [journey testing](../plugins/development/skills/journey-testing/SKILL.md) and [community skill review](maintainers/sources.md#figma-community-review).

## UI/UX expertise for people and agents

The frontend-development bundle provides [interface-quality](../plugins/frontend-development/skills/interface-quality/SKILL.md), [ux-writing](../plugins/frontend-development/skills/ux-writing/SKILL.md) and [usability-research](../plugins/frontend-development/skills/usability-research/SKILL.md) as directly selectable, model-available supporting skills. Client picker/discovery behavior still needs verification. The same guidance supports design, develop, improve and review when relevant; no separate user and agent copies are maintained.

Ask for a scoped result: "Review this dialog without changing it", "Improve and apply the error messages in this flow", or "Prepare a usability study for onboarding". A bare review/improvement assessment stays read-only. A specified repair can include implementation and rechecking. A research guide is a plan until actual observations exist. Ordinary UI development needs no compulsory study or Figma connection.

Visual-design owns visual direction and semantic token intent; frontend conventions implement it for the selected React stack; interaction-design owns flows and affected surfaces; interface-quality owns craft inspection and component/token audits; ux-writing owns task copy; usability-research owns studies and evidence synthesis. Existing test/journey guidance verifies implementation and Storybook states where adopted.

## Explain and maintain project knowledge

Use [documentation-writing](../plugins/documentation/skills/documentation-writing/SKILL.md) to write or review a useful product/engineering explanation, reference or procedure. Use [architecture-documentation](../plugins/documentation/skills/architecture-documentation/SKILL.md) to explain structure, runtime/lifecycle behavior, interfaces, deployment and current versus target state from evidence. Both are directly selectable and model-available supporting guidance; actual client discovery remains client-dependent.

[Documentation conventions](../plugins/documentation/skills/documentation-conventions/SKILL.md) owns where authoritative knowledge lives and what a change affects. System-design owns architectural decisions; these methods help explain and maintain them. Existing formats and proportional scope remain authoritative; a routine edit needs no new tracker, document tree or full system audit.
