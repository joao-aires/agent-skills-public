# SDLC coverage

Use the [SDLC overview](../README.md#sdlc-coverage) to orient yourself and the [task menu](usage.md#skills-you-invoke) to start work. This reference links the expertise behind those activities. `develop` spans the useful lifecycle; individual tasks let you enter at any phase. Phases describe outcomes, **not required agent invocations or stage-gate approvals**. For new applications, [new-application flow](../plugins/development/skills/develop/references/new-application-flow.md) defines the dependent decisions; `setup` alone does not establish the full lifecycle.

![Seven-outcome software lifecycle after product direction: requirements engineering, solution design, implementation planning, implementation, verification, release, and maintenance; shared methods and matching technical expertise apply across phases](images/sdlc-cycle.svg)

## Read the lifecycle map

Product direction answers **what is worth solving and why**. Its [product-management](../plugins/strategy/skills/product-management/SKILL.md), [business-strategy](../plugins/strategy/skills/business-strategy/SKILL.md) and [learn-from-product-feedback](../plugins/strategy/skills/learn-from-product-feedback/SKILL.md) activities sit outside the seven engineering phases. Accepted objectives feed requirements; production and product evidence can reopen affected decisions.

The engineering sequence is **requirements → solution design → implementation planning → implementation → verification → release → maintenance**. Its arrows show useful decision dependencies, not seven separate meetings, commands or documents. Work enters at the missing outcome: an existing bug rarely needs product discovery, while a significant rearchitecture may revisit requirements and design several times. `develop` owns the authorized end-to-end engagement when selected; explicit-only phase entry points are not silently invoked as substeps.

| Part of the diagram | How it contributes |
| --- | --- |
| Product direction | Select users, problems, value, priorities and success signals; learn from delivered value |
| Engineering lifecycle | Establish and deliver required behavior, design, implementation, evidence, release and long-lived operational health |
| Project baseline | Reuse accepted decisions, existing contracts, instructions and evidence; update their canonical owners as they change |
| Shared methods | Research, documentation, security and review provide conditional expertise across phases |
| Technical/domain expertise | Choose by actual engineering concern and accepted stack rather than assuming Python, React or a particular framework |

Green labels identify entry-point skills or directly requested activities; dashed warm labels identify specialist support. Some expertise can also be requested directly. These are explanatory examples, not a fixed dependency graph. An agent must still respect user scope, runtime access, credentials and separate authorization for deployment or production actions.

## User-facing entry points

| Need or missing outcome | Appropriate entry point |
| --- | --- |
| Business direction and product priority | `business-strategy`, `product-management` |
| Engineering requirements and acceptance | [refine](../plugins/development/skills/refine/SKILL.md), supported by [requirements-engineering](../plugins/development/skills/requirements-engineering/SKILL.md) when substantive |
| Architecture, user experience or interface contracts | `design`, with `system-design`, `interface-design` or `backend-design` expertise when applicable |
| Agreed implementation needs dependency ordering | `plan` |
| Build an already-defined change | `implement` |
| Rough idea through implementation, tests and review | `develop` |
| Behavior checks and source assessment | `test`, `review`; review also applies earlier |
| Delivery readiness or named authorized deployment | `release` |
| Live incident or restoration | [incident-response](../plugins/operations/skills/incident-response/SKILL.md), recovery expertise as applicable |
| Proactive operation, maintenance and improvement | `improve`, `dependencies`, [observability-operations](../plugins/operations/skills/observability-operations/SKILL.md), and other targeted operating skills |
| Project foundation or activity selection | `setup`, `workflow-help` |

### Which entry point should you use?

| Starting situation | Typical work and stopping points |
| --- | --- |
| Company product request | Product direction establishes priority → `refine` defines behavior and quality constraints → `design` settles consequential solution choices → `plan` sequences implementation when useful → `implement`, `test`, `review`, `release` as authorized |
| Company refactor / rearchitecture | Inspect current behavior and maintenance pain → `refine` the preserved contracts, migration constraints and expected outcome → `design` alternatives and migration boundary → `plan` compatible increments, rollback and checks → authorized implementation |
| Local agent-assisted feature or new app | Select `develop` for an authorized end-to-end slice; it establishes the missing decisions directly with relevant supporting expertise. Select `refine`, `design`, `plan` or `implement` individually when a bounded artifact or stopping point is desired |
| Known bug or narrow change | Reproduce/diagnose → implement and verify the affected behavior. No required planning or new specification ceremony |
| Incident, recovery or operational drift | Start with the matching operations activity; follow causal evidence and actual operating policy. Turn confirmed learning into a requirement/design/improvement only when warranted |
| Exploration, security review or architecture question | Request research, `harden`, `review`, design or specialist expertise; stop at the requested analysis rather than beginning implementation |

A company's portfolio planning, roadmap prioritization or sprint scheduling is **not** the `plan` implementation skill. `plan` converts sufficiently accepted requirements/design into actionable increments, dependencies and tests. It can iterate when implementation discovers a new constraint. The end-to-end `develop` activity does not need to invoke each explicit-only task skill by name to accomplish those outcomes.

## Standard engineering artifacts and workspace handoffs

Every **performed** SDLC phase leaves a structured, reviewable result in an Engineering Change Record (ECR). The ECR is a **seven-section, evolving document** in an authorized workspace **parallel to application code**. The workspace may be a local folder, separate Git repository or optionally a connected issue/document provider; **no issue-tracking software is required**. Section expectations and readiness checks are standardized by [engineering-artifacts](../plugins/development/skills/engineering-artifacts/SKILL.md), while [engineering-workspace](../plugins/development/skills/engineering-workspace/SKILL.md) handles discovery, identity, revision and authorized persistence. External provider access is never assumed.

![Seven phases hand off to their ECR artifacts through evidence-based assurance assessments; separate canonical application knowledge and issue/PR views remain independently owned](images/sdlc-artifact-flow.svg)

The labels on the **seven direct phase-to-artifact arrows** indicate a relevant assurance assessment, not a mandatory human approval or a new phase command. Requirements quality, design consistency and plan coverage check whether decisions and dependencies agree; implementation alignment and convergence compare actual source/tests with accepted behavior; release readiness and operational feedback use actual target evidence. A handoff is **ready**, **ready with limitations** or **blocked** relative to the next dependent action. The ECR's structural checker can verify Markdown shape only; semantic and convergence checks remain evidence-based engineering assessments, not executable workflow enforcement.

| Phase / producer | ECR section or linked artifact | Consumer / handoff |
| --- | --- | --- |
| Product direction / refine | Problem, scope, requirements, acceptance; PRD linked rather than duplicated | Design consumes accepted user outcomes and quality constraints |
| Solution design | Proposed future-state C4 / user journey / technical sequence, RFC/decision and alternatives when applicable | Plan consumes accepted design and unresolved compatibility/authority choices |
| Implementation planning | Ordered slices, tests, migrations, rollback, dependencies | Implementation consumes executable increments and current app contracts |
| Implementation | Revision, affected code, deviations, updated canonical docs where warranted | Verification compares real behavior with acceptance and target designs |
| Verification / review | Actual tests, findings, current revision and gaps | Release uses explicit readiness, not a generic green build |
| Release | Artifact/target, approval and rollout/recovery evidence, actual state | Maintenance consumes observed target health; merged is not deployed |
| Maintenance | Operational findings, incidents, signals and remediation | Relevant new requirements/design feedback with references |

The ECR is **not the current architecture**. Current C4 and critical sequence views remain in the application's stable-branch documentation. Target diagrams are proposed in the ECR/RFC against a known base revision, then reconciled with verified implementation in the application repository. A local fix may justify "diagrams unaffected" without fabricating diagrams. Issues summarize intended work/acceptance for coordinators and implementers; PRs explain actual changes, design variance and evidence for reviewers. Both are optional views of the authoritative record, not competing specifications.

Read [engineering artifact workflow](artifact-workflow.md) for the document structure, filesystem versus external workspace configuration, PRD/RFC/ADR ownership, example flows and audience rules. The same standard applies to an end-to-end `develop` request without invoking explicit-only phase skills as substeps. When the ECR cannot be persisted, return a structured **unpersisted** outcome rather than inventing a saved document.

## Different starting points

![Six representative paths for a new product, existing feature, bug, assessment, operations or specialist question, with contextual methods and bounded outcomes](images/sdlc-use-cases.svg)

The same capability collection serves full applications and bounded changes. Reuse accepted context and reopen only affected decisions. A new product needs enough outcome, feasibility, requirements and design evidence before irreversible commitments; a bug fix starts with reproduction. Operational incidents begin with response and recovery, not a product-planning ritual.

Direct strategy, design, documentation and specialist requests can end at their own useful results. People and trusted automation can request the same activities; the host supplies triggering, tools, credentials, limits and action scope. Implementation and verification iterate; an actual deployment or recovery is not established by a passing unit test.

## Before and around the cycle

- Product discovery and direction: [product-management](../plugins/strategy/skills/product-management/SKILL.md) owns user problems, priorities, useful scope and success signals; business-strategy owns viability and positioning. These decisions sit outside the seven engineering outcomes and may be reopened by evidence.
- Foundations: `setup` uses [project-conventions](../plugins/development/skills/project-conventions/SKILL.md) and relevant [delivery-pipelines](../plugins/delivery/skills/delivery-pipelines/SKILL.md). Establish foundations after sufficient product and architecture decisions for a new project; maintain them as conditions change.
- Feedback: [learn-from-product-feedback](../plugins/strategy/skills/learn-from-product-feedback/SKILL.md) informs product direction; incident learning addresses reliability and may also expose missing requirements or design protections.
- Changes to consequential decisions: follow [the shared decision policy](../plugins/development/WORKFLOW.md#resolve-consequential-findings) and continue independent authorized work. Do not invent acceptance or account permissions.

## Skills by phase

### 1. Requirements engineering

Start with [refine](../plugins/development/skills/refine/SKILL.md). For new systems, significant changes, rearchitecture or uncertain requirements, use its supporting [requirements-engineering](../plugins/development/skills/requirements-engineering/SKILL.md) method to elicit needs, define functional and measurable quality constraints, validate conflicts and link acceptance to evidence. Preserve accepted product intent; product-management is not repeated as a development phase. Requirements may be ready for solution design before implementation architecture is decided.

### 2. Solution design

Use [design](../plugins/development/skills/design/SKILL.md) with [system-design](../plugins/development/skills/system-design/SKILL.md) for consequential system choices. For UI work compose [interface-design](../plugins/frontend-development/skills/interface-design/SKILL.md) with relevant domain patterns and selected platform constraints **from the outset**. Use [backend-design](../plugins/backend-development/skills/backend-design/SKILL.md) for service behavior, authority, state and API contracts. Preserve current-versus-target status, meaningful alternatives, and verification consequences. No comprehensive design document is required for a trivial local fix.

### 3. Implementation planning

Start with [plan](../plugins/development/skills/plan/SKILL.md) when sequencing is useful. Derive bounded increments, dependencies, tests, compatibility and rollout/recovery implications from agreed requirements and relevant solution choices. Implementation planning happens **after those decisions when they are material**, not as a mandatory early product planning phase.

### 4. Implementation

Start with the bundled upstream `implement` when explicitly selected, or use `develop` for the broader end-to-end engagement. Use [git-contributions](../plugins/development/skills/git-contributions/SKILL.md) for the objective worktree, plus matching frontend/backend/AI/database/native-client and operating expertise. Carry tests and affected documentation with the change.

### 5. Verification & testing

Start with [test](../plugins/development/skills/test/SKILL.md), and use [deliver-reliable-changes](../plugins/development/skills/deliver-reliable-changes/SKILL.md), [journey-testing](../plugins/development/skills/journey-testing/SKILL.md), performance/resilience and other specialist methods where relevant. `review` may apply in any phase. Observe real behavior, repair failures and recheck without weakening acceptance.

### 6. Release & deployment

Start with [release](../plugins/development/skills/release/SKILL.md). [Delivery pipelines](../plugins/delivery/skills/delivery-pipelines/SKILL.md) supports artifacts, CI, publication, promotion, rollout and recovery; actual remote actions require named authorization and target verification.

### 7. Maintenance

Maintenance is one lifecycle outcome with four complementary responsibilities: **respond & restore**, **reliability & signals**, **learn & prevent**, and **maintain & evolve**. Operations activities are direct ways of achieving those outcomes; they are **not just substeps** of `improve` or `dependencies`. React to incidents with [incident-response](../plugins/operations/skills/incident-response/SKILL.md) and appropriate recovery, runbook, [postmortem facilitation](../plugins/operations/skills/postmortem-facilitation/SKILL.md) and [follow-up](../plugins/operations/skills/postmortem-followup/SKILL.md). Proactively manage [reliability and SLOs](../plugins/operations/skills/reliability-design/SKILL.md), [observability](../plugins/operations/skills/observability-operations/SKILL.md), [operational housekeeping](../plugins/operations/skills/operational-housekeeping/SKILL.md), capacity, cost, vulnerability and credentials. `improve` and `dependencies` complement those responsibilities. Reliability and operations expertise also informs requirements, design, implementation and testing before a release.

## UI/UX methods across activities

[Interface design](../plugins/frontend-development/skills/interface-design/SKILL.md) defines and reviews structure, behavior and visual direction for the intended experience; [UX writing](../plugins/frontend-development/skills/ux-writing/SKILL.md) connects language to real actions and states; [usability research](../plugins/frontend-development/skills/usability-research/SKILL.md) prepares studies or analyzes supplied observations. These skills are directly requestable and model-available support for relevant design, development, improvement and review. Interface-design owns visual direction, flows, cross-view consistency and critique; technical conventions own the selected implementation; journey-testing retains executable verification. No study or design tool is compulsory for every UI change.

## Across phases

[Documentation writing](../plugins/documentation/skills/documentation-writing/SKILL.md) guides authoring and reader review. [Architecture documentation](../plugins/documentation/skills/architecture-documentation/SKILL.md) explains structural/runtime/interface/deployment views with source evidence. They complement documentation-conventions and system-design rather than replacing their ownership.

Research, explicit clarification, prose editing, documentation, Git contributions, security and operating constraints can support any relevant phase. `review` is not confined to a final gate. Design and verification can recur during implementation; a phase label does not restrict when guidance is useful.

[reliability-design](../plugins/operations/skills/reliability-design/SKILL.md) connects outcomes and SLIs/SLOs to design and operation. [observability-operations](../plugins/operations/skills/observability-operations/SKILL.md) supplies signal implementation; [documentation-conventions](../plugins/documentation/skills/documentation-conventions/SKILL.md) keeps affected knowledge current. Upstream research, Humanizer and clarification techniques are listed below. [grill-me](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/grill-me) and other explicit workflows still require a request.

## Skills by area

Generic means reusable across stacks; stack-specific means select it only for matching technology. Some areas combine both. Supporting and directly requested specialist activities are both included; role and applicability are different dimensions. To extend the collection, follow [adding stack support](maintainers/adding-stack-support.md).

<details>
<summary>Expand the area catalogue and upstream techniques</summary>

| Area | Local applicability | Local guidance | Upstream techniques or contextual tools |
| --- | --- | --- | --- |
| Database engineering | Generic | [database-design](../plugins/database-development/skills/database-design/SKILL.md), [database-performance](../plugins/database-development/skills/database-performance/SKILL.md) | Data contracts, consistency, schema evolution and evidence-led performance methods. |
| PostgreSQL implementation | Stack-specific | [postgresql-development](../plugins/database-postgresql-development/skills/postgresql-development/SKILL.md), [postgresql-operations](../plugins/database-postgresql-development/skills/postgresql-operations/SKILL.md), [postgresql-performance](../plugins/database-postgresql-development/skills/postgresql-performance/SKILL.md) | PostgreSQL development, diagnostics and operating mechanics. |
| Security engineering | Generic | [security-and-privacy-design](../plugins/security/skills/security-and-privacy-design/SKILL.md), [security-auth-development](../plugins/security/skills/security-auth-development/SKILL.md) | Identity/access and security/privacy design with contextual implementation selection. |
| SaaS applications | Generic | [saas-dashboard-design](../plugins/saas-development/skills/saas-dashboard-design/SKILL.md), [saas-design](../plugins/saas-development/skills/saas-design/SKILL.md), [saas-readiness](../plugins/saas-development/skills/saas-readiness/SKILL.md) | Tenant/customer and commercial lifecycle, SaaS dashboard design and scoped readiness. |
| Governance and assurance | Generic | [compliance-design](../plugins/governance/skills/compliance-design/SKILL.md), [gdpr-readiness](../plugins/governance/skills/gdpr-readiness/SKILL.md), [soc2-readiness](../plugins/governance/skills/soc2-readiness/SKILL.md) | Applicability, accountable controls and GDPR/SOC 2 readiness evidence. |
| TypeScript implementation | Stack-specific | [typescript-conventions](../plugins/typescript-development/skills/typescript-conventions/SKILL.md) | Runtime/module/package contracts and TypeScript implementation verification without React. |
| Go implementation | Stack-specific | [go-conventions](../plugins/go-development/skills/go-conventions/SKILL.md) | Go module/package, lifecycle, error and verification contracts for services, libraries and CLIs. |
| Product direction | Generic | [product-management](../plugins/strategy/skills/product-management/SKILL.md) | Existing research and feedback; no tracker required |
| Business strategy | Generic | [business-strategy](../plugins/strategy/skills/business-strategy/SKILL.md) | Preserved strategy references |
| Project foundations | Generic | [project-conventions](../plugins/development/skills/project-conventions/SKILL.md) for affected structure, commands and constraints | None required |
| Documentation | Generic | [documentation-conventions](../plugins/documentation/skills/documentation-conventions/SKILL.md) | [writing-for-agents](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/writing-for-agents) for agent instructions |
| Prose editing | No local skill | Follow the document's author and technical claims | [humanizer](https://github.com/blader/humanizer/tree/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8) |
| Frontend development | Generic + stack-specific | [frontend-conventions](../plugins/frontend-reactjs-development/skills/frontend-conventions/SKILL.md), [interface-design](../plugins/frontend-development/skills/interface-design/SKILL.md) for unified UX design and full-surface coverage | Built-in visual craft in interface-design; official shadcn, Tailwind design system, Vercel React/composition for matching implementations |
| Browser extensions | Stack-specific | [browser-extension-development](../plugins/browser-extension-development/skills/browser-extension-development/SKILL.md), [browser-extension-security](../plugins/browser-extension-development/skills/browser-extension-security/SKILL.md), [browser-extension-ui](../plugins/browser-extension-development/skills/browser-extension-ui/SKILL.md), [browser-extension-testing](../plugins/browser-extension-development/skills/browser-extension-testing/SKILL.md), [browser-extension-delivery](../plugins/browser-extension-development/skills/browser-extension-delivery/SKILL.md) | Chrome/MV3 and current compatible framework, driver and store contracts |
| Desktop and mobile clients | Stack-specific | [native-client-development](../plugins/frontend-native-development/skills/native-client-development/SKILL.md) for TypeScript/Tauri and informed iOS/Android choices | Current Tauri/Expo/React Native/platform documentation |
| Backend development | Generic + stack-specific | [backend-design](../plugins/backend-development/skills/backend-design/SKILL.md), [backend-conventions](../plugins/backend-python-development/skills/backend-conventions/SKILL.md) | [modern-python](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/modern-python/skills/modern-python) |
| AI development | Generic + stack-specific | [ai-development](../plugins/ai-development/skills/ai-development/SKILL.md), [ai-conventions](../plugins/ai-python-development/skills/ai-conventions/SKILL.md) (local, not an upstream skill) | Chosen model/provider, harness and protocol SDK guidance; Google ADK or LangChain/LangGraph only when selected |
| AI testing and evaluation | Generic | [ai-testing](../plugins/ai-development/skills/ai-testing/SKILL.md) owns levels, cases, graders, acceptance and evidence | Matching evaluator/driver implementation when selected |
| AI operating behavior | Generic | [ai-operations](../plugins/ai-development/skills/ai-operations/SKILL.md) owns AI-specific task/quality signals, limits, drift and recovery | Generic service operations and matching implementation expertise as relevant |
| AI evaluation implementation | Stack-specific | [ai-deepeval-testing](../plugins/ai-python-development/skills/ai-deepeval-testing/SKILL.md) for a selected Python DeepEval runner; generic AI testing owns conceptual levels/criteria | DeepEval APIs and CI; deterministic service/protocol tests remain separate |
| AI observability implementation | Stack-specific | [python-ai-observability](../plugins/ai-python-development/skills/python-ai-observability/SKILL.md) for Python OpenTelemetry; generic AI operations and service operations own signal/target decisions | Compatible provider/framework instrumentation and chosen exporter/backend |
| MCP interfaces | Generic + stack-specific | MCP section of [ai-development](../plugins/ai-development/skills/ai-development/SKILL.md), [ai-conventions](../plugins/ai-python-development/skills/ai-conventions/SKILL.md); reuse authorized application services | [mcp-builder](https://github.com/anthropics/skills/tree/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/mcp-builder), in ai-python-development for an accepted Python MCP implementation |
| Selected development tools | Stack-specific | [tooling-conventions](../plugins/development-tooling/skills/tooling-conventions/SKILL.md) for accepted CI/container/checker, telemetry-backend and web-driver mechanics | Existing provider/tool documentation and installed matching specialists |
| Testing | Generic | [deliver-reliable-changes](../plugins/development/skills/deliver-reliable-changes/SKILL.md), [journey-testing](../plugins/development/skills/journey-testing/SKILL.md) for web/desktop/mobile journeys | [tdd](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/tdd), [property-based-testing](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/property-based-testing/skills/property-based-testing), [playwright-cli](https://github.com/microsoft/playwright-cli/tree/b85c7a736bb473bf55b584e54a09ffa698d6d871/skills/playwright-cli) |
| Failure testing | Generic | [resilience-testing](../plugins/development/skills/resilience-testing/SKILL.md) for scoped fixtures and controlled experiments | Project-native test tools; optional isolated fault proxy |
| Performance testing | Stack-specific | [performance-testing](../plugins/development-tooling/skills/performance-testing/SKILL.md) for local, CI-runner and deployed non-production k6 checks | Official k6 references; no cloud account required |
| Code review | No local skill | Requested behavior and project standards | [code-review](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/code-review); [differential-review](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/differential-review/skills/differential-review) for security-sensitive diffs |
| Debugging | No local skill | Preserve the affected scope and regression evidence | [diagnosing-bugs](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/diagnosing-bugs) |
| Research | No local skill | Record decision-changing findings where the project keeps them | [research](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/research) |
| Architecture and domain design | Generic | [system-design](../plugins/development/skills/system-design/SKILL.md) | [codebase-design](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/codebase-design), [domain-modeling](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/domain-modeling), [prototype](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/prototype) when exploration is requested |
| Git contributions | Generic | [git-contributions](../plugins/development/skills/git-contributions/SKILL.md) | No separate PR template required |
| Delivery | Generic | [delivery-pipelines](../plugins/delivery/skills/delivery-pipelines/SKILL.md) | [github-actions-hardening](https://github.com/github/awesome-copilot/tree/143a3d976b3c1603cc8932984d5e1f28501cb5fc/skills/github-actions-hardening) for GitHub Actions |
| Security and privacy | Generic | [security-and-privacy-design](../plugins/security/skills/security-and-privacy-design/SKILL.md) | [differential-review](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/differential-review/skills/differential-review), [supply-chain-risk-auditor](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor) within supported coverage |
| Data recovery | Generic | [protect-and-restore-data](../plugins/operations/skills/protect-and-restore-data/SKILL.md) | Current platform/database references |
| Capacity | Generic | [plan-application-capacity](../plugins/operations/skills/plan-application-capacity/SKILL.md) | Current platform references |
| Cost | Generic | [optimize-application-cost](../plugins/operations/skills/optimize-application-cost/SKILL.md) | [aks-cost-optimization](https://github.com/Azure/AKS-Skills/tree/20bf35201a79b324d2ca3e00e5c82020ff362024/skills/aks-cost-optimization) only for Azure AKS |
| System discovery | Generic | [system-mapping](../plugins/development/skills/system-mapping/SKILL.md) for evidence, topology and journeys | No particular platform required |
| Interactive architecture | Generic | [system-flow-explorer](../plugins/visualization/skills/system-flow-explorer/SKILL.md) on request; evidence-backed HTML and JSON | Bundled offline renderer; optional existing Playwright for browser checks |
| Shell automation | Stack-specific | [bash-engineering](../plugins/development-tooling/skills/bash-engineering/SKILL.md) | Bash-specific; no new task framework required |
| Python automation | Stack-specific | [python-automation-engineering](../plugins/backend-python-development/skills/python-automation-engineering/SKILL.md) for CLI/API jobs | [modern-python](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/modern-python/skills/modern-python) where useful; separate from FastAPI service conventions |
| Reliability | Generic | [reliability-design](../plugins/operations/skills/reliability-design/SKILL.md) for outcomes, SLIs/SLOs, budgets and alerts | Current first-party references; optional Datadog/Terraform example |
| Observability | Generic | [observability-operations](../plugins/operations/skills/observability-operations/SKILL.md) for signal contracts and pipeline verification | Use the project's libraries/collectors |
| Incident response | Generic | [incident-response](../plugins/operations/skills/incident-response/SKILL.md) for current impact and independently verified recovery | Existing authorized tools and service evidence |
| Runbooks | Generic | [runbook-engineering](../plugins/operations/skills/runbook-engineering/SKILL.md) for branching diagnostics, actions and verification | The service's actual procedures |
| Incident learning | Generic | [postmortem-facilitation](../plugins/operations/skills/postmortem-facilitation/SKILL.md), [postmortem-followup](../plugins/operations/skills/postmortem-followup/SKILL.md) | Evidence-led review and deployed completion checks |
| Vulnerability remediation | Generic | [vulnerability-management](../plugins/operations/skills/vulnerability-management/SKILL.md) | Existing scanners, vendor advisories and deployed artifact evidence |
| Credentials | Generic | [credential-lifecycle](../plugins/operations/skills/credential-lifecycle/SKILL.md) | Actual identity provider/store; never expose secret values |
| Kubernetes resources | Stack-specific | [kubernetes-resource-engineering](../plugins/operations-platforms/skills/kubernetes-resource-engineering/SKILL.md) | Current cluster/operator/Helm/Kustomize documentation |
| JVM performance | Stack-specific | [infra-jvm-optimization](../plugins/operations-platforms/skills/infra-jvm-optimization/SKILL.md) only for Java/JVM workloads | Installed runtime and platform guidance |
| Operational upkeep | Generic | [operational-housekeeping](../plugins/operations/skills/operational-housekeeping/SKILL.md) | Reuse project records; targeted reviews remain targeted |
| Product feedback | Generic | [learn-from-product-feedback](../plugins/strategy/skills/learn-from-product-feedback/SKILL.md) | Existing evidence; no analytics vendor required |

</details>

For the complete acquired set, licenses and precise source pins, use the [upstream catalogue](maintainers/sources.md#upstream-catalogue) and [artifact declarations](../agent-depot.json). Kubernetes, JVM and AKS skills apply only to those platforms. Reference-only techniques are not necessarily installed.

## Coverage and limits

The skills describe ways of working across the lifecycle; installing them does not establish application correctness, production readiness or compliance. Tooling, credentials, devices and platform-specific procedures must exist in the target environment. Package and discovery checks are recorded separately from application evidence in the [maintainer reference](maintainers/evaluations.md#recorded-evidence-and-limits).

Specialist methods and diagrams live with their skills: [change evaluation](../plugins/development/skills/deliver-reliable-changes/SKILL.md), [journey testing](../plugins/development/skills/journey-testing/SKILL.md), [performance](../plugins/development-tooling/skills/performance-testing/SKILL.md), [resilience](../plugins/development/skills/resilience-testing/SKILL.md) and [observability](../plugins/operations/skills/observability-operations/SKILL.md).
