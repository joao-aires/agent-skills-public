# SDLC coverage

Use the [SDLC overview](../README.md#sdlc-coverage) to orient yourself and the [task menu](usage.md#skills-you-invoke) to start work. This reference links the expertise behind those activities. `develop` spans the useful lifecycle; individual tasks let you enter at any phase. Phases are a map, not required handoffs. For a new application, [new-application flow](../plugins/development-workflow/skills/develop/references/new-application-flow.md) defines the decision outcomes develop must establish before dependent work; setup alone does not establish the lifecycle.

The circular overview names SDLC phases and their outcomes. Separate labels marked **Skill** identify user-facing skills; each card first explains its purpose in plain language. Plugins are installation bundles, and supporting disciplines are linked below. A skill may support more than one phase. `plan` is detailed implementation planning after the relevant requirements and design decisions.

The top panel is the **project baseline**: accepted decisions, working conventions and reproducible foundations. Read it as input to relevant work and update it when decisions change. It is maintained project context, not an extra phase before discovery.

The lower panel separates **shared methods** from **technical expertise for the accepted stack**. Shared methods contribute across discovery, development and feedback. Stack guidance informs feasibility and requirements and applies through design, implementation, testing, delivery and maintenance; it is not confined to coding. Rails point into the three parts of the flow to show this support. Labels marked Guidance name supporting skills and Records name project inputs. The groups are representative, not a checklist to load in full.

## User-facing entry points

| Need or phase | Entry point |
| --- | --- |
| Business direction | business-strategy |
| Product discovery, priorities and success | product-management |
| Requirements and scope | refine |
| System, experience or contract design | design; focused visual-design or backend-design when installed |
| Implementation sequencing | plan |
| Implementation | implement; develop for the broader engagement |
| Verification and assessment | test; review across phases |
| Delivery | release |
| Maintenance and learning | improve, dependencies, relevant operations; learn-from-product-feedback |
| Foundations or choosing an activity | setup / workflow-help |

Some disciplines are directly selectable and also support requested work. Entry points may span phases; they do not imply a mandatory invocation chain.

## Different starting points

![Six representative paths for a new product, existing feature, bug, assessment, operations or specialist question, with contextual methods and bounded outcomes](images/sdlc-use-cases.svg)

The same cycle supports a whole product and a small change. A new product needs enough refinement, feasibility and design evidence before dependent implementation; an existing feature reuses accepted context and revisits only affected decisions. Bug repair starts with reproduction and diagnosis. A scoped review returns findings and gaps; fixes require the corresponding request. Operations can enter through an incident, recovery exercise, capacity question or routine upkeep, with outcomes verified in the named environment.

Direct strategy, design, documentation and other specialist requests can end at their own useful result. They need no full development engagement. Representative task names in the map describe supported entry points, not universal client commands or automatic invocation of explicit-only workflows. People and trusted automation can request the same activities; the host supplies triggering, credentials, tools, limits and allowed actions.

Implementation and verification form a repeated loop inside the broader SDLC. Product feedback, incident learning and test evidence can reopen the relevant requirement, design or increment. Local checks, real-platform behavior and deployed outcomes establish different claims; a finished diagram, successful build or passing component test cannot establish them all. Follow the [shared consequential-decision policy](../plugins/development-workflow/WORKFLOW.md#resolve-consequential-findings) when new evidence requires a user choice, and continue independent work within the existing scope.

## Before and around the cycle

- Product discovery and direction: [product-management](../plugins/business-strategy/skills/product-management/SKILL.md) owns user problems, priorities, useful scope and success signals. [Business strategy](../plugins/business-strategy/skills/business-strategy/SKILL.md) owns business direction, competitive position and value capture. These decisions begin before development and evolve with evidence.
- Project foundations: `setup` uses [project-conventions](../plugins/development-workflow/skills/project-conventions/SKILL.md) and relevant [delivery-pipelines](../plugins/development-workflow/skills/delivery-pipelines/SKILL.md) guidance. Establish them after sufficient product and architecture decisions for a new project, then maintain affected parts as it evolves.
- Product feedback: [learn-from-product-feedback](../plugins/business-strategy/skills/learn-from-product-feedback/SKILL.md) examines delivered value and feeds discovery and future work. Incident learning addresses reliability and is a separate feedback source.

## Skills by phase

Product discovery and refinement establish the outcome. System design makes architectural decisions before dependent implementation planning; revisit it for features that change consequential boundaries. Phases can recur and do not require separate task invocations.

### 1. Planning

Establish the goals, feasibility, constraints and rough scope needed to decide whether and how to proceed. Product-management supplies product priorities and evidence for this decision; business-strategy supports unresolved business choices. Revisit the initial plan as requirements and design become clearer; detailed implementation planning follows the decisions it depends on.

### 2. Requirements analysis

Start with [refine](../plugins/development-workflow/skills/refine/SKILL.md). Establish actor authority, scope, observable acceptance and material unknowns. Reuse accepted product direction; product-management supports unresolved product priorities without replacing engineering requirements.

### 3. Design

#### Architecture and system design

Use [design](../plugins/development-workflow/skills/design/SKILL.md) with [system-design](../plugins/development-workflow/skills/system-design/SKILL.md). Compare consequential architecture/platform options against the product and operating constraints, map boundaries and critical flows, and carry the decisions into setup and feature plans. Reuse installed codebase-design/domain-modeling where applicable.

#### Interaction, visual and contract design

Use [design](../plugins/development-workflow/skills/design/SKILL.md), [visual-design](../plugins/web-frontend/skills/visual-design/SKILL.md), [interaction-design](../plugins/web-frontend/skills/interaction-design/SKILL.md) and [backend-design](../plugins/development-workflow/skills/backend-design/SKILL.md), then relevant technical guidance. Derive contextual visual direction and define surfaces, behavior, authority and failure contracts from the requirements before dependent implementation.

#### Implementation planning and foundations

Start with [plan](../plugins/development-workflow/skills/plan/SKILL.md). Produce bounded dependency-ordered increments, tests and delivery/recovery consequences from the accepted system and experience design. Reconcile earlier rough plans after material decisions; establish complete applicable project foundations.

### 4. Implementation

Start with bundled upstream implement. Use [git-contributions](../plugins/development-workflow/skills/git-contributions/SKILL.md) for the actual objective worktree and applicable frontend/backend/AI/native-client guidance. Keep source, configuration, tests and docs in that objective.

### 5. Testing

Start with [test](../plugins/development-workflow/skills/test/SKILL.md). Use [deliver-reliable-changes](../plugins/development-workflow/skills/deliver-reliable-changes/SKILL.md), [journey-testing](../plugins/development-workflow/skills/journey-testing/SKILL.md), and performance/resilience methods when relevant. Commit meaningful tests, inspect failures, repair and recheck the real behavior.

### 6. Deployment

Start with [release](../plugins/development-workflow/skills/release/SKILL.md). Use [delivery-pipelines](../plugins/development-workflow/skills/delivery-pipelines/SKILL.md) for CI, artifacts, registry publication, promotion and recovery. Setup authors applicable delivery foundations; live release/deployment requires a named authorized action.

### 7. Maintenance

Start with improve/dependencies or the requested operations activity. Use relevant upkeep, vulnerability, credential, capacity/cost and data-recovery guidance. Feed product evidence and incident learning into the next refinement/design decision.

## UI/UX methods across activities

[Interface quality](../plugins/web-frontend/skills/interface-quality/SKILL.md) assesses and refines the intended experience; [UX writing](../plugins/web-frontend/skills/ux-writing/SKILL.md) connects language to real actions and states; [usability research](../plugins/web-frontend/skills/usability-research/SKILL.md) prepares studies or analyzes supplied observations. They are both directly requestable and model-available support for relevant design, development, improvement and review. Visual-design owns direction, interaction-design owns flows and technical conventions own the selected implementation; journey-testing retains executable verification. No study or design tool is compulsory for every UI change.

## Across phases

[Documentation writing](../plugins/development-workflow/skills/documentation-writing/SKILL.md) guides authoring and reader review. [Architecture documentation](../plugins/development-workflow/skills/architecture-documentation/SKILL.md) explains structural/runtime/interface/deployment views with source evidence. They complement documentation-conventions and system-design rather than replacing their ownership.

Research, explicit clarification, prose editing, documentation, Git contributions, security and operating constraints can support any relevant phase. `review` is not confined to a final gate. Design and verification can recur during implementation; a phase label does not restrict when guidance is useful.

[reliability-design](../plugins/application-operations/skills/reliability-design/SKILL.md) connects outcomes and SLIs/SLOs to design and operation. [observability-operations](../plugins/application-operations/skills/observability-operations/SKILL.md) supplies signal implementation; [documentation-conventions](../plugins/development-workflow/skills/documentation-conventions/SKILL.md) keeps affected knowledge current. Upstream research, Humanizer and clarification techniques are listed below. [grill-me](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/grill-me) and other explicit workflows still require a request.

## Skills by area

Generic means reusable across stacks; stack-specific means select it only for matching technology. Some areas combine both. Supporting and directly requested specialist activities are both included; role and applicability are different dimensions.

<details>
<summary>Expand the area catalogue and upstream techniques</summary>

| Area | Local applicability | Local guidance | Upstream techniques or contextual tools |
| --- | --- | --- | --- |
| Product direction | Generic | [product-management](../plugins/business-strategy/skills/product-management/SKILL.md) | Existing research and feedback; no tracker required |
| Business strategy | Generic | [business-strategy](../plugins/business-strategy/skills/business-strategy/SKILL.md) | Preserved strategy references |
| Project foundations | Generic | [project-conventions](../plugins/development-workflow/skills/project-conventions/SKILL.md) for affected structure, commands and constraints | None required |
| Documentation | Generic | [documentation-conventions](../plugins/development-workflow/skills/documentation-conventions/SKILL.md) | [writing-for-agents](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/writing-for-agents) for agent instructions |
| Prose editing | No local skill | Follow the document's author and technical claims | [humanizer](https://github.com/blader/humanizer/tree/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8) |
| Frontend development | Generic + stack-specific | [frontend-conventions](../plugins/web-frontend/skills/frontend-conventions/SKILL.md), [visual-design](../plugins/web-frontend/skills/visual-design/SKILL.md), [interaction-design](../plugins/web-frontend/skills/interaction-design/SKILL.md) for prior UX design and full-surface coverage | Official shadcn, Tailwind design system, Vercel React/composition |
| Desktop and mobile clients | Stack-specific | [native-client-development](../plugins/web-frontend/skills/native-client-development/SKILL.md) for TypeScript/Tauri and informed iOS/Android choices | Current Tauri/Expo/React Native/platform documentation |
| Backend development | Generic + stack-specific | [backend-design](../plugins/development-workflow/skills/backend-design/SKILL.md), [backend-conventions](../plugins/python-backend/skills/backend-conventions/SKILL.md) | [modern-python](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/modern-python/skills/modern-python) |
| AI development | Generic + stack-specific | [build-evaluated-ai](../plugins/ai-development/skills/build-evaluated-ai/SKILL.md), [ai-conventions](../plugins/ai-development/skills/ai-conventions/SKILL.md) (local, not an upstream skill) | Chosen Google ADK or LangChain/LangGraph skills |
| MCP interfaces | Generic + stack-specific | MCP section of [build-evaluated-ai](../plugins/ai-development/skills/build-evaluated-ai/SKILL.md), [ai-conventions](../plugins/ai-development/skills/ai-conventions/SKILL.md); reuse authorized application services | [mcp-builder](https://github.com/anthropics/skills/tree/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/mcp-builder), in `ai-development`; prefer standalone Python FastMCP |
| Testing | Generic | [deliver-reliable-changes](../plugins/development-workflow/skills/deliver-reliable-changes/SKILL.md), [journey-testing](../plugins/development-workflow/skills/journey-testing/SKILL.md) for web/desktop/mobile journeys | [tdd](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/tdd), [property-based-testing](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/property-based-testing/skills/property-based-testing), [playwright-cli](https://github.com/microsoft/playwright-cli/tree/b85c7a736bb473bf55b584e54a09ffa698d6d871/skills/playwright-cli) |
| Failure testing | Generic | [resilience-testing](../plugins/development-workflow/skills/resilience-testing/SKILL.md) for scoped fixtures and controlled experiments | Project-native test tools; optional isolated fault proxy |
| Performance testing | Stack-specific | [performance-testing](../plugins/development-workflow/skills/performance-testing/SKILL.md) for local, CI-runner and deployed non-production k6 checks | Official k6 references; no cloud account required |
| Code review | No local skill | Requested behavior and project standards | [code-review](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/code-review); [differential-review](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/differential-review/skills/differential-review) for security-sensitive diffs |
| Debugging | No local skill | Preserve the affected scope and regression evidence | [diagnosing-bugs](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/diagnosing-bugs) |
| Research | No local skill | Record decision-changing findings where the project keeps them | [research](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/research) |
| Architecture and domain design | Generic | [system-design](../plugins/development-workflow/skills/system-design/SKILL.md) | [codebase-design](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/codebase-design), [domain-modeling](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/domain-modeling), [prototype](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/prototype) when exploration is requested |
| Git contributions | Generic | [git-contributions](../plugins/development-workflow/skills/git-contributions/SKILL.md) | No separate PR template required |
| Delivery | Generic | [delivery-pipelines](../plugins/development-workflow/skills/delivery-pipelines/SKILL.md) | [github-actions-hardening](https://github.com/github/awesome-copilot/tree/143a3d976b3c1603cc8932984d5e1f28501cb5fc/skills/github-actions-hardening) for GitHub Actions |
| Security and privacy | Generic | [security-and-privacy-design](../plugins/development-workflow/skills/security-and-privacy-design/SKILL.md) | [differential-review](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/differential-review/skills/differential-review), [supply-chain-risk-auditor](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor) within supported coverage |
| Data recovery | Generic | [protect-and-restore-data](../plugins/application-operations/skills/protect-and-restore-data/SKILL.md) | Current platform/database references |
| Capacity | Generic | [plan-application-capacity](../plugins/application-operations/skills/plan-application-capacity/SKILL.md) | Current platform references |
| Cost | Generic | [optimize-application-cost](../plugins/application-operations/skills/optimize-application-cost/SKILL.md) | [aks-cost-optimization](https://github.com/Azure/AKS-Skills/tree/20bf35201a79b324d2ca3e00e5c82020ff362024/skills/aks-cost-optimization) only for Azure AKS |
| System discovery | Generic | [system-mapping](../plugins/development-workflow/skills/system-mapping/SKILL.md) for evidence, topology and journeys | No particular platform required |
| Interactive architecture | Generic | [system-flow-explorer](../plugins/visual-communication/skills/system-flow-explorer/SKILL.md) on request; evidence-backed HTML and JSON | Bundled offline renderer; optional existing Playwright for browser checks |
| Shell automation | Stack-specific | [bash-engineering](../plugins/development-workflow/skills/bash-engineering/SKILL.md) | Bash-specific; no new task framework required |
| Python automation | Stack-specific | [python-automation-engineering](../plugins/python-backend/skills/python-automation-engineering/SKILL.md) for CLI/API jobs | [modern-python](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/modern-python/skills/modern-python) where useful; separate from FastAPI service conventions |
| Reliability | Generic | [reliability-design](../plugins/application-operations/skills/reliability-design/SKILL.md) for outcomes, SLIs/SLOs, budgets and alerts | Current first-party references; optional Datadog/Terraform example |
| Observability | Generic | [observability-operations](../plugins/application-operations/skills/observability-operations/SKILL.md) for signal contracts and pipeline verification | Use the project's libraries/collectors |
| Incident response | Generic | [incident-response](../plugins/application-operations/skills/incident-response/SKILL.md) for current impact and independently verified recovery | Existing authorized tools and service evidence |
| Runbooks | Generic | [runbook-engineering](../plugins/application-operations/skills/runbook-engineering/SKILL.md) for branching diagnostics, actions and verification | The service's actual procedures |
| Incident learning | Generic | [postmortem-facilitation](../plugins/application-operations/skills/postmortem-facilitation/SKILL.md), [postmortem-followup](../plugins/application-operations/skills/postmortem-followup/SKILL.md) | Evidence-led review and deployed completion checks |
| Vulnerability remediation | Generic | [vulnerability-management](../plugins/application-operations/skills/vulnerability-management/SKILL.md) | Existing scanners, vendor advisories and deployed artifact evidence |
| Credentials | Generic | [credential-lifecycle](../plugins/application-operations/skills/credential-lifecycle/SKILL.md) | Actual identity provider/store; never expose secret values |
| Kubernetes resources | Stack-specific | [kubernetes-resource-engineering](../plugins/application-operations/skills/kubernetes-resource-engineering/SKILL.md) | Current cluster/operator/Helm/Kustomize documentation |
| JVM performance | Stack-specific | [infra-jvm-optimization](../plugins/application-operations/skills/infra-jvm-optimization/SKILL.md) only for Java/JVM workloads | Installed runtime and platform guidance |
| Operational upkeep | Generic | [operational-housekeeping](../plugins/application-operations/skills/operational-housekeeping/SKILL.md) | Reuse project records; targeted reviews remain targeted |
| Product feedback | Generic | [learn-from-product-feedback](../plugins/business-strategy/skills/learn-from-product-feedback/SKILL.md) | Existing evidence; no analytics vendor required |

</details>

For the complete acquired set, licenses and precise source pins, use the [upstream catalogue](maintainers/sources.md#upstream-catalogue) and [lockfile](../upstream.lock.json). Kubernetes, JVM and AKS skills apply only to those platforms. Reference-only techniques are not necessarily installed.

## Coverage and limits

The skills describe ways of working across the lifecycle; installing them does not establish application correctness, production readiness or compliance. Tooling, credentials, devices and platform-specific procedures must exist in the target environment. Package and discovery checks are recorded separately from application evidence in the [maintainer reference](maintainers/evaluations.md#recorded-evidence-and-limits).

Specialist methods and diagrams live with their skills: [change evaluation](../plugins/development-workflow/skills/deliver-reliable-changes/SKILL.md), [journey testing](../plugins/development-workflow/skills/journey-testing/SKILL.md), [performance](../plugins/development-workflow/skills/performance-testing/SKILL.md), [resilience](../plugins/development-workflow/skills/resilience-testing/SKILL.md) and [observability](../plugins/application-operations/skills/observability-operations/SKILL.md).
