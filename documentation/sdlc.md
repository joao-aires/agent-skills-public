# SDLC coverage

Use the [SDLC overview](../README.md#sdlc-coverage) to orient yourself and the [task menu](usage.md#skills-you-invoke) to start work. This reference links the expertise behind those activities. `develop` spans the useful lifecycle; individual tasks let you enter at any phase. Phases are a map, not required handoffs.

## Before and around the cycle

- Product discovery: [business-strategy](../plugins/business-strategy/skills/business-strategy/SKILL.md) helps choose a useful problem.
- Project foundations: `setup` uses [project-conventions](../plugins/development-workflow/skills/project-conventions/SKILL.md) and relevant [delivery-pipelines](../plugins/development-workflow/skills/delivery-pipelines/SKILL.md) guidance. Establish them for a new project, then maintain affected parts as it evolves.
- Product feedback: [learn-from-product-feedback](../plugins/business-strategy/skills/learn-from-product-feedback/SKILL.md) examines delivered value and feeds discovery and future work. Incident learning addresses reliability and is a separate feedback source.

## Skills by phase

### 1. Planning

Start with [plan](../plugins/development-workflow/skills/plan/SKILL.md). Supporting guidance: [project-conventions](../plugins/development-workflow/skills/project-conventions/SKILL.md), [reliability-design](../plugins/application-operations/skills/reliability-design/SKILL.md).

Expected outcome: Agreed scope, constraints and a useful next increment.

### 2. Requirements analysis

Start with [refine](../plugins/development-workflow/skills/refine/SKILL.md). Supporting guidance: [reliability-design](../plugins/application-operations/skills/reliability-design/SKILL.md), [security-and-privacy-design](../plugins/development-workflow/skills/security-and-privacy-design/SKILL.md).

Expected outcome: Observable acceptance and unresolved material decisions.

### 3. Design

Start with [design](../plugins/development-workflow/skills/design/SKILL.md). Supporting guidance: [interaction-design](../plugins/web-frontend/skills/interaction-design/SKILL.md), [frontend-conventions](../plugins/web-frontend/skills/frontend-conventions/SKILL.md), [backend-conventions](../plugins/python-backend/skills/backend-conventions/SKILL.md), [security-and-privacy-design](../plugins/development-workflow/skills/security-and-privacy-design/SKILL.md), [system-mapping](../plugins/development-workflow/skills/system-mapping/SKILL.md).

Expected outcome: Relevant interactions, contracts and consequential decisions before code.

### 4. Implementation

Start with [implement](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/implement) (bundled upstream). Supporting guidance: [frontend-conventions](../plugins/web-frontend/skills/frontend-conventions/SKILL.md), [backend-conventions](../plugins/python-backend/skills/backend-conventions/SKILL.md), [build-evaluated-ai](../plugins/ai-development/skills/build-evaluated-ai/SKILL.md), [git-contributions](../plugins/development-workflow/skills/git-contributions/SKILL.md).

Expected outcome: A scoped change following the accepted project and design.

### 5. Testing

Start with [test](../plugins/development-workflow/skills/test/SKILL.md). Supporting guidance: [deliver-reliable-changes](../plugins/development-workflow/skills/deliver-reliable-changes/SKILL.md), [journey-testing](../plugins/development-workflow/skills/journey-testing/SKILL.md), [performance-testing](../plugins/development-workflow/skills/performance-testing/SKILL.md), [resilience-testing](../plugins/development-workflow/skills/resilience-testing/SKILL.md).

Expected outcome: Evidence for the intended behavior, with actual boundaries and gaps.

### 6. Deployment

Start with [release](../plugins/development-workflow/skills/release/SKILL.md). Supporting guidance: [delivery-pipelines](../plugins/development-workflow/skills/delivery-pipelines/SKILL.md), [runbook-engineering](../plugins/application-operations/skills/runbook-engineering/SKILL.md), [observability-operations](../plugins/application-operations/skills/observability-operations/SKILL.md).

Expected outcome: Readiness, or verification/recovery for a named authorized delivery action.

### 7. Maintenance

Start with [improve](../plugins/development-workflow/skills/improve/SKILL.md) / [dependencies](../plugins/development-workflow/skills/dependencies/SKILL.md). Supporting guidance: [operational-housekeeping](../plugins/application-operations/skills/operational-housekeeping/SKILL.md), [vulnerability-management](../plugins/application-operations/skills/vulnerability-management/SKILL.md), [protect-and-restore-data](../plugins/application-operations/skills/protect-and-restore-data/SKILL.md), [plan-application-capacity](../plugins/application-operations/skills/plan-application-capacity/SKILL.md), [optimize-application-cost](../plugins/application-operations/skills/optimize-application-cost/SKILL.md).

Expected outcome: Evidence-backed improvements and scoped maintenance.

## Across phases

Research, explicit clarification, prose editing, documentation, Git contributions, security and operating constraints can support any relevant phase. `review` is not confined to a final gate. Design and verification can recur during implementation; a phase label does not restrict when guidance is useful.

[reliability-design](../plugins/application-operations/skills/reliability-design/SKILL.md) connects outcomes and SLIs/SLOs to design and operation. [observability-operations](../plugins/application-operations/skills/observability-operations/SKILL.md) supplies signal implementation; [documentation-conventions](../plugins/development-workflow/skills/documentation-conventions/SKILL.md) keeps affected knowledge current. Upstream research, Humanizer and clarification techniques are listed below. [grill-me](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/grill-me) and other explicit workflows still require a request.

## Skills by area

Generic means reusable across stacks; stack-specific means select it only for matching technology. Some areas combine both. Supporting and directly requested specialist activities are both included; role and applicability are different dimensions.

<details>
<summary>Expand the area catalogue and upstream techniques</summary>

| Area | Local applicability | Local guidance | Upstream techniques or contextual tools |
| --- | --- | --- | --- |
| Project foundations | Generic | [project-conventions](../plugins/development-workflow/skills/project-conventions/SKILL.md) for affected structure, commands and constraints | None required |
| Documentation | Generic | [documentation-conventions](../plugins/development-workflow/skills/documentation-conventions/SKILL.md) | [writing-for-agents](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/writing-for-agents) for agent instructions |
| Prose editing | No local skill | Follow the document's author and technical claims | [humanizer](https://github.com/blader/humanizer/tree/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8) |
| Frontend development | Generic + stack-specific | [frontend-conventions](../plugins/web-frontend/skills/frontend-conventions/SKILL.md), [interaction-design](../plugins/web-frontend/skills/interaction-design/SKILL.md) for prior UX design and full-surface coverage | Official shadcn, Tailwind design system, Vercel React/composition |
| Backend development | Stack-specific | [backend-conventions](../plugins/python-backend/skills/backend-conventions/SKILL.md) | [modern-python](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/modern-python/skills/modern-python) |
| AI development | Stack-specific | [build-evaluated-ai](../plugins/ai-development/skills/build-evaluated-ai/SKILL.md) (local, not an upstream skill) | Chosen Google ADK or LangChain/LangGraph skills |
| MCP interfaces | Stack-specific | MCP section of [build-evaluated-ai](../plugins/ai-development/skills/build-evaluated-ai/SKILL.md); reuse authorized application services | [mcp-builder](https://github.com/anthropics/skills/tree/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/mcp-builder), in `ai-development`; prefer standalone Python FastMCP |
| Testing | Generic | [deliver-reliable-changes](../plugins/development-workflow/skills/deliver-reliable-changes/SKILL.md), [journey-testing](../plugins/development-workflow/skills/journey-testing/SKILL.md) for web/desktop/mobile journeys | [tdd](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/tdd), [property-based-testing](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/property-based-testing/skills/property-based-testing), [playwright-cli](https://github.com/microsoft/playwright-cli/tree/b85c7a736bb473bf55b584e54a09ffa698d6d871/skills/playwright-cli) |
| Failure testing | Generic | [resilience-testing](../plugins/development-workflow/skills/resilience-testing/SKILL.md) for scoped fixtures and controlled experiments | Project-native test tools; optional isolated fault proxy |
| Performance testing | Stack-specific | [performance-testing](../plugins/development-workflow/skills/performance-testing/SKILL.md) for local, CI-runner and deployed non-production k6 checks | Official k6 references; no cloud account required |
| Code review | No local skill | Requested behavior and project standards | [code-review](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/code-review); [differential-review](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/differential-review/skills/differential-review) for security-sensitive diffs |
| Debugging | No local skill | Preserve the affected scope and regression evidence | [diagnosing-bugs](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/diagnosing-bugs) |
| Research | No local skill | Record decision-changing findings where the project keeps them | [research](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/research) |
| Architecture and domain design | No local skill | Relevant frontend/backend conventions | [codebase-design](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/codebase-design), [domain-modeling](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/domain-modeling), [prototype](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/prototype) when exploration is requested |
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
