# Capability expansion roadmap

Maintainer plan for the next capability additions. The [source catalogue](sources.md) remains the record of acquired material; this page records what is intentionally local, what may be acquired, and where the boundary sits.

## Decision rules

| Situation | Decision |
| --- | --- |
| Same intent, missing depth, examples or presentation | Expand the existing skill or reference. Do not add a parallel skill. |
| Distinct intent, stopping point, evidence or authority | Add a skill. |
| Distinct install audience and at least three cohesive skills | Add a plugin. |
| Vendor or tool with a large operational model | One method plus vendor references. Add a dedicated tool skill only when the operational model is the method. |
| New durable artifact | Add one contract, one guide and a registry entry. Otherwise reuse an existing artifact. |
| Upstream skill | Acquire unchanged only when it fits the model. Otherwise cite it as a reviewed source and write local original guidance. |

A new plugin needs an install decision that a user can make independently. A new skill needs a stopping point that differs from every existing skill. A new artifact needs a contract that differs from every existing contract.

Phase 1 and the application-type work are implemented in this branch and validated locally. Later phases remain planned; the private blog/content pack is separate.

## Public and private split

The public collection keeps reusable methods, provider references and evidence-backed guidance. The private `joao-aires/agent-skills-personal` repository keeps personal voice, personal diagram style, private stack choices and private examples.

| Area | Home |
| --- | --- |
| Explain, documentation craft, README guidance | Public |
| UI research, option review, Mobbin/Refero integration | Public |
| AI evaluation and DeepEval | Public |
| CI/CD authoring | Public |
| Application types, architecture, SRE, infrastructure, cloud, SaaS | Public |
| Engineering-blog craft and public source patterns | Private content pack |
| Personal blog voice, diagram style and examples | Private |

Private skills reference public skills by name. They do not copy them.

## Capability map

| Area | Existing home | Change | Status |
| --- | --- | --- | --- |
| Intuitive explanation | `documentation` | New `explain` method | Implemented |
| Documentation craft | `documentation` | Expand `technical-writing` with document-type, formatting, concept and review references | Implemented |
| README | `sdlc` | Expand `guide-readme` and `repository-readme` for open-source adoption | Implemented |
| UI research | `frontend-development` | New `design-research`; strengthen option review; optional Mobbin/Refero MCPs | Implemented |
| AI evaluation | `ai-development` | New `ai-evaluation` activity; deepen `ai-testing` and `ai-deepeval-testing` | Implemented |
| CI/CD authoring | `development-tooling` | Expand workflow authoring and script-selection references | Implemented |
| Strategy options | `strategy` | Require materially different strategies and an opportunity-cost comparison | Implemented |
| REST API | `backend-development` | New method | Implemented |
| GraphQL | `backend-development` | New method | Implemented |
| Event-driven/Kafka | `backend-development` | New method | Implemented |
| Distributed systems | `backend-development` | New method | Implemented |
| CLI | `development-tooling` | New method | Implemented |
| Reliability | `sdlc` | New activity for SLOs, error budgets and alert policy | Phase 3 |
| Production readiness | `sdlc` | New activity using assurance evidence | Phase 3 |
| Kubernetes troubleshooting | `operations-platforms` | Acquire/adapt the distinct upstream method | Phase 3 |
| Datadog | `operations-platforms` | New tool method | Phase 3 |
| FinOps | `sdlc` | Expand `capacity-and-cost` | Phase 3 |
| Disaster recovery | `sdlc` | Expand `data-recovery` into service/regional recovery | Phase 3 |
| PostgreSQL upgrades | `database-postgresql-development` | New method | Phase 3 |
| GitOps | `operations-platforms` | New method for Argo CD and Flux | Phase 4 |
| Application configuration | `development-tooling` | New method for config and secrets | Phase 4 |
| Kubernetes config repositories | `operations-platforms` | New method for config-repo conventions | Phase 4 |
| Crossplane | `operations-platforms` | New provider method | Phase 4 |
| AWS | `cloud-platforms` | New plugin and provider method | Phase 4 |
| OpenStack | `cloud-platforms` | New provider method | Phase 4 |
| SaaS service integration | `saas-development` | New method plus vendor references | Phase 5 |
| SaaS billing | `saas-development` | New method; Stripe web, Superwall mobile on request | Phase 5 |
| SaaS identity and access | `saas-development` | New method | Phase 5 |
| Multi-tenancy | `saas-development` | Deepen `saas-design` | Phase 5 |
| SaaS compliance | `sdlc` + `saas-development` | Extend `compliance-readiness` with CCPA and SaaS evidence | Phase 5 |
| Blog/content | Private repository | New private content pack | Implemented in private repo |

## Phase plan

| Phase | Public work | Private work |
| --- | --- | --- |
| 0 | This roadmap, source decisions, artifact decisions, evaluation matrix | Content-pack scaffold, `skills/` layout, sync and validator |
| 1 | `explain`, documentation references, README expansion, `design-research`, UI options, `ai-evaluation`, DeepEval references, CI/CD references, strategy options | Engineering-blog source matrix and provisional voice profile |
| 2 | REST, GraphQL, event-driven/Kafka, distributed systems, CLI | Blog ideation and writing methods |
| 3 | Reliability, production readiness, Kubernetes troubleshooting, Datadog, FinOps, disaster recovery, database upgrades | Blog visuals and publishing checklist |
| 4 | GitOps, application configuration, Kubernetes config repositories, Crossplane, AWS, OpenStack | Blog evaluation scenarios |
| 5 | SaaS service integration, billing, identity/access, multi-tenancy, compliance | |
| 6 | Consolidation, counts, generated maps, independent review | Private content release |

## Source strategy

| Source | Use | Decision |
| --- | --- | --- |
| [nik-kale/sre-skills](https://github.com/nik-kale/sre-skills) | Kubernetes troubleshooting; production readiness | Acquire/adapt only distinct material. Keep local incident response, observability and runbook guidance, which are deeper. |
| [wshobson/agents](https://github.com/wshobson/agents) | API design, GitOps, Stripe, Terraform, SLO implementation | Evaluate and adapt. MIT, but several skills are generic or action-heavy. |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | AWS, CLI, PostgreSQL, cost review | Prefer as reference. Many skills assume GitHub issues, AWS CLI or MCP and should not be acquired raw. |
| [Mobbin MCP](https://mobbin.com/mcp) | Real product screens, flows and sections | Optional paid MCP; local `design-research` method remains authoritative. |
| [Refero MCP](https://refero.design/mcp) | Styles, screens and flows from shipped products | Optional paid MCP; local `design-research` method remains authoritative. |
| [DeepEval skills](https://github.com/confident-ai/deepeval/tree/main/skills) | Metric and CI patterns | Review; do not adopt mandatory hosted reporting, synthetic generation or fixed iteration defaults. |

Every acquisition needs a pinned commit, license check, source review, metadata labels and no upstream byte edits.

## Optional MCP policy

Declare optional MCP servers only in the plugin that owns their use. A skill asks once whether the user wants and can use the service. No answer means no use. The task must complete without the service.

Current optional candidates:

| Plugin | Server | Endpoint | Constraint |
| --- | --- | --- | --- |
| `frontend-development` | Figma | `https://mcp.figma.com/mcp` | Existing |
| `frontend-development` | Mobbin | `https://api.mobbin.com/mcp` | OAuth; paid plans |
| `frontend-development` | Refero | `https://api.refero.design/mcp` | OAuth or bearer; paid plan |
| `sdlc` | Plane | `https://mcp.plane.so/http/mcp` | OAuth |
| `sdlc` | Linear | `https://mcp.linear.app/mcp` | OAuth |
| `sdlc` | Atlassian | `https://mcp.atlassian.com/v2/mcp` | OAuth 2.1 |
| `sdlc` | GitHub | `https://api.githubcopilot.com/mcp/` | OAuth or PAT; `default,projects` toolset header |

## Evaluation requirements

Every new skill or material expansion needs:

- a description that triggers the intended requests and avoids the nearest existing skill;
- positive cases for the intended outcome;
- negative controls for the nearest duplicate or unsafe behavior;
- artifact and evidence checks where the skill claims them;
- authority checks for writes, publication and deployment;
- a recorded limitation when the behavior is defined but not executed.

Add cases to the existing scenario specification rather than creating a second eval system.

## Open decisions

- Keep `backend-development` as the home for REST, GraphQL, event-driven and distributed methods until it exceeds a coherent pack; split only if installation granularity becomes a real problem.
- Keep SRE activities in `sdlc`; do not create a separate SRE plugin. Tool-specific methods belong in `operations-platforms` or `cloud-platforms`.
- Keep blog/content in the private repository. Public `technical-writing`, `humanizer` and `visualization` remain dependencies.
- Do not add a second README skill. Expand `guide-readme`.
- Do not add a second documentation skill. Expand `technical-writing`.
- Do not create one skill per SaaS vendor. Use one method plus vendor references.
- Do not add Azure or GCP until requested; start with AWS and OpenStack.
- Ask about Superwall only for mobile billing. Web defaults to Stripe.
