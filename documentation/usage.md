# Using the plugins

Start with a task and an outcome. Task entry points choose the relevant supporting guidance; you do not need to memorize every backend, frontend, testing or operations skill. For a rough idea that should become working software, start with `develop`. For one phase, choose from the lifecycle below.

![Choose tasks by SDLC phase, with develop spanning the cycle and supporting skills across it](images/sdlc-cycle.svg)

The cycle is a map, not a required sequence. Enter where useful, return to design/code when verification exposes a problem, and use [the detailed SDLC map](sdlc.md) for supporting expertise.

## Skills you invoke

The short `/name` notation below describes an activity, not a universal alias. In VS Code, plugin skills use names such as `/development-workflow:test`; other clients expose their own skill picker/names. Check the actual inventory. Plain requests such as “Use test for the current changes” are a fallback in clients supporting explicit skills. `/workflow-help` is this toolkit's help; it does not replace the client's built-in `/help`.

| Where you are | Task | What happens |
| --- | --- | --- |
| Not sure what to use | `workflow-help` | Read-only help, available capabilities, examples and next activity |
| Rough idea to a working result | `develop` | Clarification, design, implementation, tests and review in one engagement |
| Starting/adopting a project | `setup` | Establish useful context, commands and scoped foundations |
| Requirements need definition | `refine` | Repository-aware work package or specific decision blockers |
| Scope agreed; sequencing needed | `plan` | Bounded implementation steps and verification |
| UX/contracts/architecture undecided | `design` | Text/visual behavior design before implementation |
| Defined work ready to build | `implement` | Implement and verify through the feature contribution flow |
| Need behavior evidence | `test` | Select/run appropriate checks and add requested missing coverage |
| PR or diff ready for assessment | `review` | Findings against intended behavior/standards plus relevant checks |
| Want architecture/performance/UX improvement | `improve` | Prioritized discovery, or focused work for a specified objective |
| Security/privacy weakness | `harden` | Scoped assessment/fixes and remaining risks |
| Dependency updates or vulnerability PRs | `dependencies` | Release-note/compatibility/CI review and allowed remediation |
| Preparing or executing delivery | `release` | Readiness by default; execute only a named authorized action/target |

`implement` is the retained pinned upstream skill with local task framing; the other entries above are local. A source-only checkout lacks acquired upstream skills until built. Advanced explicit skills such as `implement-spec`, `grill-me`, `to-spec`, `retro` and `handoff` remain available with their native controls. They are choices, not prerequisites. Interviews and tracker publication are not implicit parts of ordinary work.

Examples (VS Code's documented plugin-qualified notation; adapt through your client's picker):

```text
/development-workflow:refine Add read-only sharing to saved searches
/development-workflow:test the current change, including the persisted journey
/development-workflow:review PR #42 against its agreed behavior
/development-workflow:improve architecture in the reporting module
/development-workflow:workflow-help I am changing an existing application's navigation
```

Bare `improve` returns a short opportunity list; a specific improvement objective can authorize bounded implementation. `review` assesses by default and does not edit source/post/merge. `test` does not authorize deployed load or faults. `dependencies` merges only under an explicit eligible-update policy with current head/checks/protections. `release` without a named execution scope prepares rather than deploys.

## One end-to-end request

Use `develop` for an application, feature, refactor or improvement that begins as a rough idea:

```text
/development-workflow:develop Build a nutritionist/client progress application from this brief. Ask about important product and UX choices, state reversible assumptions, and implement a useful first slice. Prepare a PR; do not merge or deploy.

/development-workflow:develop Improve saved-search sharing in this existing application. Preserve its UI and identity model, define the interactions first, then implement and verify them.
```

The agent inspects existing evidence, asks decision-changing questions and carries accepted answers forward. It makes ordinary reversible choices without constant confirmation. Meaningful UX/backend behavior is defined before dependent code. Then it implements, tests, reviews and reports actual completion evidence within the request. “One-shot” means one end-to-end engagement, with appropriate questions; it does not mean zero interaction or guaranteed production quality. No full planning/design ceremony is needed for a tiny change.

`refine` stops at actionable work/unknowns, `design` stops at a design, and `implement` starts from defined work. `develop` owns the full engagement and uses supporting guidance directly; it does not bypass explicit-only skill controls to invoke other task workflows automatically. A task can finish partial/blocked when a material decision or execution capability is missing.

## Define UX before changing screens

Use `design` for design work alone, or `develop`/`improve` when implementation should follow. The web bundle's `interaction-design` skill guides meaningful UI work automatically alongside frontend-conventions.

1. Inventory the affected routes, menus/submenus, dialogs/drawers and role/mobile variants, including shared components and overrides.
2. Define goals, actions, navigation and relevant loading/empty/validation/error/permission/cancel states in text. Add wireframes/wireflows or mockups when they settle layout/visual decisions; do not require all formats.
3. Resolve consequential questions, reuse accepted patterns and state reversible assumptions. Establish a representative pattern, then propagate it through shared components.
4. Reconcile every in-scope surface against implementation and observed behavior. Report unfinished or unverified surfaces; one screenshot or a shared-component build cannot establish global consistency.

```text
/development-workflow:design Unify navigation, nested menus and edit dialogs across this application. Inventory all affected surfaces, specify interaction/state behavior and show wireframes where useful. Do not implement yet.

/development-workflow:improve Apply the agreed global navigation/dialog design across every in-scope surface. Verify desktop/mobile, role variants and focus/cancel/error behavior; report any unfinished coverage.
```

Backend work follows the same principle: establish actor authority, contracts, invariants, state/failure and compatibility before implementation, then account for every affected endpoint/job/tool.

## Evaluate during implementation

`develop` and the implementation guidance use a feedback loop: define observable scenarios, implement a useful increment, run affected checks, operate the real application, inspect diagnostic evidence, then repair and recheck. Broader regression and complete surface coverage precede completion. `test` can run the same evaluation independently.

```mermaid
flowchart TD
    A["Intent and acceptance"] --> B["Interaction and contract design"]
    B --> C["Implement increment"]
    C --> D["Checks and application exploration"]
    D --> E["Results, state and telemetry"]
    E --> F{"Outcome established?"}
    F -->|Defect| C
    F -->|Design uncertainty| B
    F -->|Yes| G["Verified result and remaining gaps"]
```

Use complementary evidence: logic/integration checks for rules and authority, component states for shared behavior, a small critical journey suite, visual/accessibility checks and bounded agent exploration. Keep accepted visual baselines and expected outcomes independent of generated results. Automated accessibility or model judgments do not replace appropriate human evaluation. A repeated unexplained failure is a blocker to diagnose, not a reason to weaken checks or retry indefinitely.

| Application | Driver starting point | Important limits |
| --- | --- | --- |
| Web | Playwright scripts and browser exploration | Semantic locators, isolated data and observable outcomes; screenshots alone do not prove behavior |
| Electron | Compatible Playwright Electron automation (experimental) | Renderer checks do not establish native dialogs, installation or updates |
| Native desktop | Platform-native tooling or maintained Appium driver | Test the named supported OS and packaged application; inspect driver limitations |
| Android/iOS | Maestro, Appium or platform-native tooling | Use the actual emulator/device; check lifecycle/permissions/offline behavior where relevant |

The [journey-testing guidance](../plugins/development-workflow/skills/journey-testing/SKILL.md) explains selection and evidence. A responsive web check is not a native-mobile check. Driver selection does not install every platform or device tool.

```text
Use test to evaluate creating and reopening a client plan, including failed-save recovery, permissions and desktop/mobile navigation. Operate the running application, verify persistence, inspect relevant telemetry and report unverified surfaces.
```

For AI changes, keep versioned cases/scorers in the application and compare quality, failures, latency and usage. Routine deterministic fixtures do not prove live model quality. Live calls require configured credentials and established execution scope; optional Langfuse experiments complement portable application-side evaluation.

## Run services and observability locally

For a new containerizable stack, project-conventions defaults to Docker Compose for application services and actual dependencies, with migrations, representative seed data and readiness checks. Document startup, checks, shutdown and safe reset; isolate project names, ports and test data per worktree/run. Preserve an existing working environment unless changing it is requested. Desktop clients and mobile simulators normally run on the host against those services.

Offer observability through an easy-to-start profile or companion stack. Prefer a resource-appropriate self-hosted SigNoz installation for a new unified local view; retain an accepted alternative. Add Langfuse when AI datasets/experiments justify its dependencies. No Compose scaffold or vendor service is bundled here: the agent authors and verifies the target application's configuration.

```mermaid
flowchart TD
    A["Application OTel instrumentation"] --> B["OTLP and Collector"]
    B --> C["SigNoz"]
    B --> D["Datadog"]
    B --> E["Metrics, logs and trace backends"]
```

Keep instrumentation vendor-neutral: OTel APIs/compatible libraries, standard conventions and configuration-driven export. Collector routing/credentials and backend queries/dashboards stay separate from business code. Prometheus handles metrics; a Grafana stack also needs log/trace data sources. OTLP portability does not guarantee identical proprietary features or portable dashboards. Verify actual generation and ingestion with a representative success/error journey. Provide queryable diagnostics for agents as well as dashboards for people, with sensitive data excluded.

See [project-conventions](../plugins/development-workflow/skills/project-conventions/SKILL.md), [observability-operations](../plugins/application-operations/skills/observability-operations/SKILL.md) and [build-evaluated-ai](../plugins/ai-development/skills/build-evaluated-ai/SKILL.md). Fast checks need not start the entire telemetry stack; checks that depend on diagnostic ingestion should enable and verify it.

## Operations and specialized activities

Add the relevant bundle and request the skill directly by its installed name. These remain independently useful:

| Need | Bundle / entry points |
| --- | --- |
| Incident, runbook and learning | application-operations: incident-response, runbook-engineering, postmortem-facilitation, postmortem-followup |
| Reliability/signals | application-operations: reliability-design, observability-operations |
| Recovery/capacity/cost/upkeep | application-operations: protect-and-restore-data, plan-application-capacity, optimize-application-cost, operational-housekeeping |
| Security maintenance | dependencies/harden plus operations vulnerability-management and credential-lifecycle |
| Strategy and feedback | business-strategy: business-strategy, learn-from-product-feedback |
| Architecture walkthroughs/presentations | visual-communication: architecture-diagramming, system-flow-explorer, presentation-building |

For example, ask incident-response to investigate the current impact using existing action boundaries, or protect-and-restore-data to review isolated PostgreSQL restoration without deploying. An interview, incident publication, live restore or message requires its activity to be in scope. Business-opportunity-analysis remains a legacy compatibility entry; use business-strategy for new work.

## Scheduled and event-triggered tasks

The same task can start from a trusted automation prompt. The host configures cron/webhooks, credentials, permissions, concurrency and result delivery; these plugins do not install that infrastructure or a schedule.

| Trigger | Task and expected result |
| --- | --- |
| Ticket enters refinement | refine the supplied context; return actionable work or decision blockers |
| Agreed work becomes ready | implement the conversation/spec/optional tracker item |
| PR becomes ready for review | review the exact base/head and required behavior/checks |
| Scheduled update maintenance | dependencies under an explicit patch/PR/merge policy |
| Scheduled architecture/performance assessment | improve to return evidence-backed opportunities; create work records only if authorized |

Supply repository/ref or PR, objective/context, interactive/unattended mode, allowed actions and result destination in ordinary instructions. Example:

> Use dependencies in unattended mode for update PRs in owner/repository. Review release notes, conflicts and relevant tests. Repair and merge only policy-eligible patch updates whose exact current head passes required checks/reviews and has no unresolved findings; leave other updates open with reasons. Reuse existing work and return per-PR results. Do not deploy.

A tracker transition or untrusted PR body does not grant authority. Unattended tasks return precise missing decisions instead of asking an absent person or inventing requirements. Reruns reconcile partial effects and existing records; changed PR heads require new verification. The host/repository enforces privileged-action policy—skill prose alone does not provide a secure auto-merge mechanism.

## Generic or stack-specific? Task or support?

Local names distinguish short task activities (`develop`, `test`, `review`) from supporting topics (`interaction-design`, `journey-testing`, `frontend-conventions`). Established operations names remain recognizable. Names use lowercase kebab-case; qualification should disambiguate rather than repeat the plugin. `workflow-help` and `dependencies` are deliberate readable exceptions to verb-led task names. Preserve upstream names and native controls. See [migration](migration.md#local-skill-naming) for renamed local skills.

String metadata labels describe intended use: `scope` is generic/stack-specific, `stack` names matching technologies, `role` is task/support, and `invocation` is user/agent/both. Roles describe purpose, not permission. A trusted automation can explicitly invoke a user-labeled task. Native controls and client behavior determine discovery; labels alone do not enforce it.

New task entry points are user-invocable and explicit-only. Most local supporting guidance is hidden from supporting clients' slash menus but remains relevant model context. Packaging hides upstream support entries only when upstream has no explicit visibility setting; native controls/resources are preserved and adaptations recorded. Optional fields/visibility vary by client; do not infer model compliance or enforcement from discovery. Supporting skills can still be named in an explicit plain-language request where supported.

## Skills agents use during your work

Agents select these when needed to carry out the request. You can also name local guidance explicitly. An upstream skill marked **agent** supplies support rather than starting an unrequested interview or orchestration workflow. Native client invocation controls remain intact.

| Area | Local guidance | Upstream specialists |
| --- | --- | --- |
| Project foundations | `project-conventions` for affected structure, commands and constraints | None required |
| Documentation | `documentation-conventions` | `writing-for-agents` for agent instructions |
| Prose editing | Follow the document's author and technical claims | `humanizer` |
| Frontend development | `frontend-conventions`, `interaction-design` for prior UX design and full-surface coverage | Official shadcn, Tailwind design system, Vercel React/composition |
| Backend development | `backend-conventions` | `modern-python` |
| AI development | `build-evaluated-ai` (local, not an upstream skill) | Chosen Google ADK or LangChain/LangGraph skills |
| MCP interfaces | MCP section of `build-evaluated-ai`; reuse authorized application services | `mcp-builder`, in `ai-development`; prefer standalone Python FastMCP |
| Testing | `deliver-reliable-changes`, `journey-testing` for web/desktop/mobile journeys | `tdd`, `property-based-testing`, `playwright-cli` |
| Failure testing | `resilience-testing` for scoped fixtures and controlled experiments | Project-native test tools; optional isolated fault proxy |
| Performance testing | `performance-testing` for local, CI-runner and deployed non-production k6 checks | Official k6 references; no cloud account required |
| Code review | Requested behavior and project standards | `code-review`; `differential-review` for security-sensitive diffs |
| Debugging | Preserve the affected scope and regression evidence | `diagnosing-bugs` |
| Research | Record decision-changing findings where the project keeps them | `research` |
| Architecture and domain design | Relevant frontend/backend conventions | `codebase-design`, `domain-modeling`, `prototype` when exploration is requested |
| Git contributions | `git-contributions` | No separate PR template required |
| Delivery | `delivery-pipelines` | `github-actions-hardening` for GitHub Actions |
| Security and privacy | `security-and-privacy-design` | `differential-review`, `supply-chain-risk-auditor` within supported coverage |
| Data recovery | `protect-and-restore-data` | Current platform/database references |
| Capacity | `plan-application-capacity` | Current platform references |
| Cost | `optimize-application-cost` | `aks-cost-optimization` only for Azure AKS |
| System discovery | `system-mapping` for evidence, topology and journeys | No particular platform required |
| Interactive architecture | `system-flow-explorer` on request; evidence-backed HTML and JSON | Bundled offline renderer; optional existing Playwright for browser checks |
| Shell automation | `bash-engineering` | Bash-specific; no new task framework required |
| Python automation | `python-automation-engineering` for CLI/API jobs | `modern-python` where useful; separate from FastAPI service conventions |
| Reliability | `reliability-design` for outcomes, SLIs/SLOs, budgets and alerts | Current first-party references; optional Datadog/Terraform example |
| Observability | `observability-operations` for signal contracts and pipeline verification | Use the project's libraries/collectors |
| Incident response | `incident-response` for current impact and independently verified recovery | Existing authorized tools and service evidence |
| Runbooks | `runbook-engineering` for branching diagnostics, actions and verification | The service's actual procedures |
| Incident learning | `postmortem-facilitation`, `postmortem-followup` | Evidence-led review and deployed completion checks |
| Vulnerability remediation | `vulnerability-management` | Existing scanners, vendor advisories and deployed artifact evidence |
| Credentials | `credential-lifecycle` | Actual identity provider/store; never expose secret values |
| Kubernetes resources | `kubernetes-resource-engineering` | Current cluster/operator/Helm/Kustomize documentation |
| JVM performance | `infra-jvm-optimization` only for Java/JVM workloads | Installed runtime and platform guidance |
| Operational upkeep | `operational-housekeeping` | Reuse project records; targeted reviews remain targeted |
| Product feedback | `learn-from-product-feedback` | Existing evidence; no analytics vendor required |

Examples:

> Add saved-search deletion. Use backend-conventions for ownership and transactions, frontend-conventions for the interaction, journey-testing for the persisted journey, and git-contributions for the feature worktree and concise PR. No tracker; do not merge.

> Edit this PR description with humanizer. Keep the facts, commands and links intact and use my singular voice.

For new projects, I prefer `applications/` for implementation and `documentation/` for knowledge, with short scoped `AGENTS.md` instructions. Keep existing layouts and accepted choices. Screenshots, reference repositories, schemas and architecture notes can supply context.

## AI and MCP plugin selection

`ai-development` contains model/agent guidance and MCP implementation expertise. An MCP-only server does not require an LLM, transcription, an agent framework or model-quality evaluation. Test its protocol, contracts, authority and lifecycle. For AI features, select the framework actually needed and separate application fixtures from live model evaluation.

## Build and load

The [quick start](../README.md#quick-start) installs build dependencies and packages the three full-stack bundles. To include AI, explicitly select all four:

```bash
python scripts/build_plugins.py \
  --plugin development-workflow \
  --plugin python-backend \
  --plugin web-frontend \
  --plugin ai-development \
  --destination ./built-plugins-with-ai
```

Explicit `--plugin` arguments replace the default selection. Other bundle names work the same way. Build destinations must be new; to update an installation, rebuild and replace it using your client's supported route.

| Directory | Contents |
| --- | --- |
| `plugins/<name>` | Local guidance and supporting resources |
| `built-plugins/<name>` | Local guidance plus complete pinned upstream skills and license/source notices |

Load each plugin directory with its resources and supporting files intact. The builder checks source pins and copies the resources. Application dependencies and client setup are separate; packaging does not execute upstream scripts.

### Client setup and discovery checks

For **Copilot CLI**, session-local loading was tested with version 1.0.95. From the application workspace:

```bash
copilot \
  --plugin-dir /absolute/path/built-plugins/development-workflow \
  --plugin-dir /absolute/path/built-plugins/python-backend \
  --plugin-dir /absolute/path/built-plugins/web-frontend
```

Append `skill list --json` to check discovery without starting a model session. Direct `copilot plugin install` also worked, but that version warns it is deprecated, and a reinstall test dropped an unrelated inventory entry. Session-local loading avoids that persistent-installation route. Consult the [CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) for your version.

For **VS Code** versions supporting Agent Plugins, merge the individual paths into user settings:

```json
{
  "chat.plugins.enabled": true,
  "chat.pluginLocations": {
    "/absolute/path/built-plugins/development-workflow": true,
    "/absolute/path/built-plugins/python-backend": true,
    "/absolute/path/built-plugins/web-frontend": true
  }
}
```

Open the application workspace and check Configure Skills. This route follows [official documentation](https://code.visualstudio.com/docs/agent-customization/agent-plugins#use-local-plugins); it was not exercised here. For other clients, use their documented route. Discovery confirms availability, not model compliance.

## Optional tools and verification

MCP servers expose tools; skills explain how to use or build them. Configure servers for the actual client and application. The Playwright skill does not install Playwright MCP, and the MCP builder does not create a running server during plugin installation. These bundles configure no servers or hooks.

Ask which checks ran and what they cover: rendered UI, real persistence, ownership denial, mocked providers and live AI quality, as applicable. Package validation alone says nothing about the application's quality. See the [SDLC map](sdlc.md) for coverage and the [migration guide](migration.md) for older installations.
