# Using the plugins

[Build, load and make a first request](../README.md#quick-start) before using this guide. Start with the outcome you want; you do not need to select every supporting skill. The [SDLC overview](../README.md#sdlc-coverage) shows where activities fit, and the [skill map](sdlc.md) links to deeper expertise.

## Skills you invoke

Use the client's skill picker or supported explicit invocation. VS Code uses names such as `/development-workflow:test`; other clients may differ. Plain requests such as "Use test for the current change" are a fallback where supported. `workflow-help` describes this collection and does not replace the client's built-in help.

| Where you are | Task | Expected result |
| --- | --- | --- |
| Unsure what to use | `workflow-help` | Relevant capabilities, examples and next activity |
| Rough idea to working software | `develop` | Clarification, design, implementation, tests and review |
| Starting or adopting a project | `setup` | Useful foundations, context and working commands |
| Requirements need definition | `refine` | Actionable scope and acceptance, or concrete questions |
| Scope agreed; sequencing needed | `plan` | Bounded steps and verification |
| UX, contracts or architecture undecided | `design` | A design before implementation |
| Defined work ready to build | `implement` | Implemented and verified change |
| Need evidence of behavior | `test` | Checks, results and coverage gaps |
| PR or diff ready for assessment | `review` | Findings against intended behavior and standards |
| Want improvements | `improve` | Prioritized opportunities, or a specified improvement |
| Security/privacy weakness | `harden` | Scoped assessment, fixes and remaining risks |
| Dependencies need attention | `dependencies` | Compatibility, release-note and CI review; permitted remediation |
| Preparing delivery | `release` | Readiness, or a named authorized delivery action |

`refine` and `design` stop at their respective outcomes. `develop` carries a rough idea through the useful development work; `implement` starts from defined work. Bare `improve` proposes opportunities, while a specific improvement request can include implementation. `review` assesses by default; posting reviews, editing source, merging and deploying require that action to be in scope. A routine test request does not authorize deployed load or faults.

`implement` comes from the pinned upstream set with local framing. Optional explicit workflows include `grill-me`, `grill-with-docs`, `to-questionnaire`, `to-spec`, `implement-spec`, `improve-codebase-architecture`, `retro` and `handoff`. Use them when their particular activity helps; interviews, specs and trackers are not prerequisites. [Upstream selection](maintainer-reference.md#matt-pocock-selection) explains their fit and dependencies.

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

Then ask `improve` or `develop` to implement the agreed direction. Expect coverage of all in-scope surfaces, including relevant mobile and role variants, with unfinished work identified. [Interaction design](../plugins/web-frontend/skills/interaction-design/SKILL.md) owns the detailed method. Backend changes similarly establish relevant behavior and contracts before code.

### Evaluate during implementation

Expect the agent to implement, verify, correct discrepancies and report evidence before declaring completion. Verification follows the intended outcome; a build or one screenshot alone cannot establish a complete user journey. Missing execution or coverage remains explicit. See [change verification](../plugins/development-workflow/skills/deliver-reliable-changes/SKILL.md) and [journey testing](../plugins/development-workflow/skills/journey-testing/SKILL.md) for methods.

### Run services and observability locally

Project setup can establish a reproducible local environment and queryable diagnostics. Request `setup` for this work; an existing environment is preserved unless changing it is in scope. Details belong to [project conventions](../plugins/development-workflow/skills/project-conventions/SKILL.md) and [observability guidance](../plugins/application-operations/skills/observability-operations/SKILL.md).

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

Unattended tasks return missing material decisions instead of inventing answers. Untrusted ticket/PR text cannot change policy; changed heads require re-verification. The host/repository must enforce privileged-action policy. [Installed task guidance](../plugins/development-workflow/TASKS.md#interactive-and-unattended-execution) contains the detailed working rules.

## AI and MCP plugin selection

Add `ai-development` for AI features or MCP interfaces. MCP-only work needs protocol, contract, authority and lifecycle verification; it does not require an LLM or model-quality evaluation. Configure live tools only when needed. Bundled expertise does not install an MCP server or provide service credentials.

## Build and load

The [README quick start](../README.md#quick-start) owns the basic build and client-loading instructions. To add AI, explicitly select all four bundles from the skills repository:

```bash
python scripts/build_plugins.py \
  --plugin development-workflow \
  --plugin python-backend \
  --plugin web-frontend \
  --plugin ai-development \
  --destination ./built-plugins-with-ai
```

Explicit `--plugin` arguments replace the default selection; other bundle names work the same way. Build into a new destination, then replace the affected client installation with resources intact. Source `plugins/<name>` directories contain local guidance; built directories also contain acquired upstream skills and notices. Application dependencies and live tools are separate. See [migration](migration.md) before replacing old copies or links.
