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

Every new or revised skill also follows [own the capability, disclose the detail, link the authority](../maintainer-reference.md#own-the-capability-disclose-the-detail-link-the-authority): own the judgment and procedure, disclose branch detail, execute deterministic work, link volatile external detail, and keep optional cross-plugin composition conditional.

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
| Skill authoring | `documentation` | New method for creating and revising skills | Implemented |
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
| Backend architecture patterns | `backend-development` | New method for pattern selection and migration | Implemented |
| CI/CD pipeline design | `development-tooling` | New provider-neutral method; release remains the activity | Implemented |
| Reliability and quality attributes | `sdlc` | Extend `system-design` with a quality-attribute dimension model and design references; no separate reliability activity | Implemented |
| Production readiness | `sdlc` | New activity using assurance evidence | Implemented |
| Kubernetes troubleshooting | `operations-platforms` | New local diagnostic method; no upstream acquisition | Implemented |
| FinOps | `sdlc` | Expand `capacity-and-cost` with FinOps and SaaS attribution references | Implemented |
| Disaster recovery | `sdlc` | Expand the `system-design` reliability reference with continuity and DR design; `data-recovery` keeps restore evidence | Implemented |
| PostgreSQL upgrades | `database-postgresql-development` | Expand `postgresql-operations` with major and managed upgrade references | Implemented |
| Requirements and quality attributes | `sdlc` | Extend the ECR contract, `guide-ecr`, `requirements-engineering` and `system-design`; no new artifact | Implemented |
| Infrastructure delivery | `operations-platforms` | New method owning IaC, GitOps and Kubernetes configuration; Crossplane is a reference | Implemented |
| Application configuration | `sdlc` | New method for configuration precedence, secrets and reload | Implemented |
| AWS | `operations-platforms` | New provider method in the existing plugin; reference-only reuse of upstream AWS material | Implemented |
| Supabase PostgreSQL | `database-postgresql-development` | Pinned acquisition of `supabase-postgres-best-practices` | Implemented |
| SaaS supporting services | `saas-development` | New requirement-first selection and integration method | Implemented |
| SaaS billing | `saas-development` | New method; Stripe web, Superwall mobile on request | Implemented |
| SaaS identity and access | `saas-development` | New method for organization, enterprise and machine identity | Implemented |
| Multi-tenancy | `saas-development` | Deepen `saas-design` with isolation, residency and tenant recovery | Implemented |
| SaaS compliance | `sdlc` | Extend `compliance-readiness` with CCPA and SaaS evidence | Implemented |
| Blog/content | Private repository | New private content pack | Implemented in private repo |

## Phase plan

| Phase | Public work | Private work |
| --- | --- | --- |
| 0 | This roadmap, source decisions, artifact decisions, evaluation matrix | Content-pack scaffold, `skills/` layout, sync and validator |
| 1 | `explain`, documentation references, README expansion, `design-research`, UI options, `ai-evaluation`, DeepEval references, CI/CD references, strategy options | Engineering-blog source matrix and provisional voice profile |
| 2 | REST, GraphQL, event-driven/Kafka, distributed systems, CLI | Blog ideation and writing methods |
| 3 | Quality attributes and DR in `system-design`, production readiness, Kubernetes troubleshooting, FinOps, PostgreSQL upgrades | Blog visuals and publishing checklist |
| 4 | Infrastructure delivery, application configuration, AWS, Supabase PostgreSQL | Blog evaluation scenarios |
| 5 | SaaS supporting services, billing, identity/access, multi-tenancy, CCPA and SaaS evidence | |
| 6 | Consolidation, counts, generated maps, independent review | Private content release |

## Source strategy

| Source | Use | Decision |
| --- | --- | --- |
| [nik-kale/sre-skills](https://github.com/nik-kale/sre-skills) | Kubernetes troubleshooting; production readiness | Do not acquire. Small, single-day history, no maintenance trail, and heavy overlap with the local operations owners. Use only as a checklist reference if a specific structure is useful. |
| [wshobson/agents](https://github.com/wshobson/agents) | API design, GitOps, Stripe, Terraform, SLO implementation | Reference and compare. MIT, but several skills are generic or action-heavy; do not acquire raw. |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | AWS, CLI, PostgreSQL, cost review | Reference. Many skills assume GitHub issues, AWS CLI or MCP and should not be acquired raw. |
| [Confluent agent skills](https://github.com/confluentinc/agent-skills) | Kafka subset | Evaluate for a pinned acquisition after license, resource and behavioral review. Keep generic event reasoning local. |
| [Supabase agent skills](https://github.com/supabase/agent-skills) | Limited database/provider material | Acquired one artifact, `supabase-postgres-best-practices`, at a pinned commit. The rest of the repository is not acquired. |
| [Mobbin MCP](https://mobbin.com/mcp) | Real product screens, flows and sections | Optional paid MCP; local `design-research` method remains authoritative. |
| [Refero MCP](https://refero.design/mcp) | Styles, screens and flows from shipped products | Optional paid MCP; local `design-research` method remains authoritative. |
| [DeepEval skills](https://github.com/confident-ai/deepeval/tree/main/skills) | Metric and CI patterns | Review; do not adopt mandatory hosted reporting, synthetic generation or fixed iteration defaults. |

Every acquisition needs a pinned commit, license check, source review, metadata labels and no upstream byte edits.

### Research conclusions

The 2026-11-16 source review checked 188 URLs with official documentation and specifications. Prices, plan limits, quotas and vendor performance claims remain unverified and need re-checking at use time.

| Area | Current baseline | Decision |
| --- | --- | --- |
| REST | RFC 9110/9111/9112/9113; RFC 9457; OpenAPI 3.1.1 baseline, 3.2.1 current | Write local method; reference standards. |
| GraphQL | September 2025 specification; Relay connections; Apollo guidance | Write local method; Apollo is one implementation. |
| Kafka/events | Kafka 4.4; AsyncAPI 3.1; CloudEvents 1.0.2; Confluent Schema Registry | Write local method; evaluate Confluent Kafka subset only. |
| SRE | Google SRE; OpenSLO; Prometheus; Kubernetes docs | Write local activities; do not acquire `nik-kale/sre-skills`. |
| AWS | Well-Architected, IAM, VPC, ECS/EKS, RDS/Aurora, S3, SQS/SNS, CloudWatch, Backup, Route 53, WAF, Secrets Manager | Write local provider guidance; reference official docs. Reuse `awesome-copilot` and `wshobson/agents` AWS material as references, not acquired skills. |
| OpenStack | 2026.2 Hibiscus; core service docs; Kolla/OpenStack-Ansible | Not added; version-fragmented and outside the current common 80%. |
| Datadog | Monitors, APM, logs, SLOs, usage/cost, API/CLI | Not added; generic observability already owns signal selection and provider details are volatile. |
| FinOps | FinOps Framework; FOCUS 1.4; AWS CUR/tagging; unit economics | Extend `capacity-and-cost`; do not create a parallel FinOps plugin. |
| Disaster recovery | AWS DR whitepaper; Google DR planning; PostgreSQL backup/PITR | Extend `data-recovery`; avoid a second DR owner. |
| PostgreSQL upgrades | PostgreSQL 18.7 stable; 19 RC2; pg_upgrade; logical replication; managed-service constraints | Add focused PostgreSQL upgrade method; keep generic database strategy separate. |
| SaaS vendors | Official vendor docs for Stripe, PostHog, Resend, Sentry, Cloudflare, Hetzner, Supabase, Superwall, Zernio | Vendor notes inside capability methods; prices and plan gates need re-checking. |

Highest duplication risks are SLO/incident/DR in `sdlc`, PostgreSQL upgrades in `database-postgresql-development`, AI evaluation in `ai-development`, and SaaS lifecycle in `saas-development`. Extend those owners rather than creating parallel skills.

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
- Keep SRE activities in `sdlc`; do not create a separate SRE plugin. Tool-specific methods belong in `operations-platforms`.
- Keep blog/content in the private repository. Public `technical-writing`, `humanizer` and `visualization` remain dependencies.
- Do not add a second README skill. Expand `guide-readme`.
- Do not add a second documentation skill. Expand `technical-writing`.
- Do not create one skill per SaaS vendor. Use one method plus vendor references.
- Do not add Azure or GCP until requested; AWS lives in `operations-platforms`. OpenStack, Datadog and a separate `cloud-platforms` plugin are not part of this phase.
- `infra-delivery` owns infrastructure as code; do not add a separate `infrastructure-as-code` skill. Crossplane is one reference under that method.
- Quality attributes are a requirements dimension and a `system-design` reference set, not a profile, lifecycle or separate reliability skill.
- Ask about Superwall only for mobile billing. Web defaults to Stripe.
