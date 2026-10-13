# Using the plugins

Choose plugins for the work, then select skills for the task. A **local** skill captures my conventions. An **upstream** skill supplies a specialist technique from another project.

## Generic or stack-specific?

Skills carry standard string labels under `metadata`: `scope`, `invocation`, and `stack` where applicable. These describe intended use; clients may not display the labels or enforce invocation behavior.

| Scope | Meaning | Examples |
| --- | --- | --- |
| Generic | Applies across application stacks. It may still need Git, a browser or another tool. | Project conventions, strategy, requirements, documentation, code review, Humanizer, recovery/capacity/cost principles |
| Stack-specific | Requires matching technology or platform APIs. Check the installed versions and supported coverage. | Next.js/shadcn/Tailwind, FastAPI/SQLAlchemy, Playwright, ADK/LangChain, FastMCP, Bash, Python automation, Kubernetes resources, JVM tuning, GitHub Actions, AKS cost optimization |

For example, `frontend-conventions` has `scope: stack-specific`, `stack: React, Next.js, Tailwind, shadcn`, and `invocation: both`. `project-conventions` is generic and also supports both forms of use. Scope is independent of who invokes the skill and where it came from.

## Skills you invoke

Ask for an outcome or name the skill explicitly. Local skills can start the activities below directly. **User** means an explicit activity; **both** means it can also guide related work already requested. Routine changes do not require a planning workflow.

| Activity | Skill | Source | Scope / invocation |
| --- | --- | --- | --- |
| Start or review project foundations | `project-conventions` | Local | Generic / both; full setup or reorganization requires a request |
| Evaluate a product or business direction | `business-strategy` | Local | Generic / user |
| Analyze product feedback | `learn-from-product-feedback` | Local | Generic / both |
| Explain architecture visually | `architecture-diagraming` | Local | Generic / user |
| Create a presentation | `presentation-building` | Local | Generic / user |
| Review feature security and privacy | `design-secure-features` | Local | Generic / both |
| Design or review delivery pipelines | `build-delivery-pipelines` | Local | Generic / both |
| Review backup, restore and disaster recovery | `protect-and-restore-data` | Local | Generic / both |
| Map services and critical journeys from evidence | `system-mapping` | Local | Generic / both |
| Build an interactive architecture walkthrough | `system-flow-explorer` | Local | Generic / user |
| Define journey SLIs/SLOs and alerts | `reliability-design` | Local | Generic / both |
| Review or implement instrumentation | `observability-operations` | Local | Generic / both |
| Respond to an active incident | `incident-response` | Local | Generic / both; target actions need task authority |
| Write or review an operational runbook | `runbook-engineering` | Local | Generic / both |
| Facilitate or draft an incident review | `postmortem-facilitation` | Local | Generic / both; interviews only on request |
| Verify postmortem actions in deployed behavior | `postmortem-followup` | Local | Generic / both |
| Review deployed vulnerability remediation | `vulnerability-management` | Local | Generic / both |
| Review credentials and rotation | `credential-lifecycle` | Local | Generic / both |
| Review recurring operational upkeep | `operational-housekeeping` | Local | Generic / both; no scheduler installed |
| Plan capacity | `plan-application-capacity` | Local | Generic / both |
| Assess costs | `optimize-application-cost` | Local | Generic / both |
| Evaluate an AI feature | `build-evaluated-ai` | Local | Stack-specific / both |
| Plan or run browser journeys | `test-end-to-end` | Local | Playwright-specific / both |
| Clarify requirements | `grill-me`, `grill-with-docs`, `to-questionnaire` | Upstream: Matt | Generic / user |
| Write an agreed spec | `to-spec` | Upstream: Matt | Generic / user |
| Implement agreed scope | `implement`, `implement-spec` | Upstream: Matt | Generic / user |
| Explore codebase architecture | `improve-codebase-architecture` | Upstream: Matt | Generic / user |
| Learn from a coding session | `retro` | Upstream: Matt | Generic / user |
| Hand work to another session | `handoff` | Upstream: Matt | Generic / user |

Examples:

> Use business-strategy to compare these two product ideas, then learn-from-product-feedback to assess the support notes. Separate evidence from assumptions.

> Use protect-and-restore-data to review recovery for my PostgreSQL application on its actual hosting platform. Identify RPO/RTO assumptions and isolated restore checks; do not deploy from this review.

> Use implement-spec for the scope agreed here. No tracker. Use the relevant frontend/backend conventions, verify the affected behavior, and report actual checks.

`business-opportunity-analysis` remains a legacy compatibility entry point; use `business-strategy` for new work. The [review of Matt's skills](maintainer-reference.md#matt-pocock-selection) explains which 18 are retained and why nine were removed. Tracker setup, ticket creation and a separate teaching workspace are not bundled prerequisites.

## Skills agents use during your work

Agents select these when needed to carry out the request. You can also name local guidance explicitly. An upstream skill marked **agent** supplies support rather than starting an unrequested interview or orchestration workflow. Native client invocation controls remain intact.

| Area | Local guidance | Upstream specialists |
| --- | --- | --- |
| Project foundations | `project-conventions` for affected structure, commands and constraints | None required |
| Documentation | `maintain-documentation` | `writing-for-agents` for agent instructions |
| Prose editing | Follow the document's author and technical claims | `humanizer` |
| Frontend development | `frontend-conventions` | Official shadcn, Tailwind design system, Vercel React/composition |
| Backend development | `backend-conventions` | `modern-python` |
| AI development | `build-evaluated-ai` (local, not an upstream skill) | Chosen Google ADK or LangChain/LangGraph skills |
| MCP interfaces | MCP section of `build-evaluated-ai`; reuse authorized application services | `mcp-builder`, in `ai-development`; prefer standalone Python FastMCP |
| Testing | `deliver-reliable-changes`, `test-end-to-end` for browser journeys | `tdd`, `property-based-testing`, `playwright-cli` |
| Code review | Requested behavior and project standards | `code-review`; `differential-review` for security-sensitive diffs |
| Debugging | Preserve the affected scope and regression evidence | `diagnosing-bugs` |
| Research | Record decision-changing findings where the project keeps them | `research` |
| Architecture and domain design | Relevant frontend/backend conventions | `codebase-design`, `domain-modeling`, `prototype` when exploration is requested |
| Git contributions | `contribute-code` | No separate PR template required |
| Delivery | `build-delivery-pipelines` | `github-actions-hardening` for GitHub Actions |
| Security and privacy | `design-secure-features` | `differential-review`, `supply-chain-risk-auditor` within supported coverage |
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

> Add saved-search deletion. Use backend-conventions for ownership and transactions, frontend-conventions for the interaction, test-end-to-end for the persisted journey, and contribute-code for the feature worktree and concise PR. No tracker; do not merge.

> Edit this PR description with humanizer. Keep the facts, commands and links intact and use my singular voice.

For new projects, I prefer `applications/` for implementation and `documentation/` for knowledge, with short scoped `AGENTS.md` instructions. Keep existing layouts and accepted choices. Screenshots, reference repositories, schemas and architecture notes can supply context.

## Operations and architecture examples

Add `application-operations` when operating a service or changing its reliability and recovery contracts. Its [selection guide](../plugins/application-operations/OPERATIONS.md) distinguishes policy, signals, response and follow-up. These are local skills adapted from the supplied portable collection, not newly acquired upstream packages. Match stack-specific skills to the actual runtime.

> Map the checkout journey with system-mapping, define its completion and latency indicators with reliability-design, and instrument the accepted contract with observability-operations. Use existing tooling and mark assumptions and unverified signals.

> Investigate this active incident with incident-response. Preserve the current action boundaries; distinguish mitigation from verified customer recovery. Draft a postmortem after stabilization without starting an interview or publishing it.

> Use system-flow-explorer to build an offline walkthrough of this API's success and failure paths. Cite repository evidence, distinguish proposed parts, and deliver the HTML and source JSON. Do not change the application.

> Review these Kubernetes manifests with kubernetes-resource-engineering and plan-application-capacity. This service runs Python: do not apply JVM settings. Report proposed changes and checks; do not deploy.

The explorer's JSON contract serves that artifact only. It is not a repository architecture schema. Read-only inventories and static diagrams can use system-mapping or architecture-diagraming without the renderer.

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
