# Sources and compatibility

[Maintainer guide](../maintainer-reference.md) · [Catalogue](#upstream-catalogue) · [Adaptations](#adaptations) · [Matt selection](#matt-pocock-selection) · [Application references](#application-references) · [Capability architecture](#product-and-capability-architecture) · [Documentation methods](#documentation-methods) · [Plugin ownership](#plugin-ownership)

## Upstream catalogue

For authoring principles and rule ownership, see [keeping guidance focused](../maintainer-reference.md#keep-guidance-focused).

The [manifest](../../agent-depot.json) declares repositories, accepted artifact commits, destinations and consumer packaging metadata within each artifact. The [Depot lockfile](../../agent-depot.lock.json) records file integrity and provenance. Checkouts contain complete, unmodified acquired skills in their plugin folders. Build bundles to apply the collection’s adaptations and generate notices before loading them in a client. I select sources for provenance, maintenance, licensing and fit with these workflows. Popularity is supporting evidence, not proof of correctness.

| Plugin | Source | Selected skills |
| --- | --- | --- |
| ai-adk-development | [google/adk-python](https://github.com/google/adk-python) | adk-agent-builder, adk-architecture |
| ai-langchain-development | [langchain-ai/langchain-skills](https://github.com/langchain-ai/langchain-skills) | langchain-fundamentals, langgraph-fundamentals, langgraph-persistence, langchain-dependencies |
| ai-python-development | [anthropics/skills](https://github.com/anthropics/skills) | mcp-builder |
| backend-python-development | [trailofbits/skills](https://github.com/trailofbits/skills) | modern-python |
| development | [mattpocock/skills](https://github.com/mattpocock/skills) | code-review, codebase-design, diagnosing-bugs, domain-modeling, grill-with-docs, implement, implement-spec, improve-codebase-architecture, prototype, research, retro, tdd, to-spec, grill-me, grilling, handoff, to-questionnaire, writing-for-agents |
| development | [getsentry/skills](https://github.com/getsentry/skills) | agents-md |
| development | [trailofbits/skills](https://github.com/trailofbits/skills) | property-based-testing, differential-review |
| development-tooling | [github/awesome-copilot](https://github.com/github/awesome-copilot) | github-actions-hardening |
| development-tooling | [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | playwright-cli |
| development-tooling | [trailofbits/skills](https://github.com/trailofbits/skills) | supply-chain-risk-auditor |
| documentation | [blader/humanizer](https://github.com/blader/humanizer) | humanizer |
| frontend-development | [anthropics/skills](https://github.com/anthropics/skills) | frontend-design |
| frontend-reactjs-development | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | shadcn |
| frontend-reactjs-development | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | vercel-composition-patterns, vercel-react-best-practices |
| frontend-reactjs-development | [wshobson/agents](https://github.com/wshobson/agents) | tailwind-design-system |
| operations-platforms | [Azure/AKS-Skills](https://github.com/Azure/AKS-Skills) | aks-cost-optimization |

## Adaptations

| Area | Packaged behavior or limitation |
| --- | --- |
| Frontend and Python | Pointers to local conventions; accepted project choices take precedence. Tailwind v4 is the new-project default; existing versions need no automatic migration. shadcn guidance applies to compatible installed primitives. |
| MCP and AI | Local framing prefers Python/standalone FastMCP for new servers and distinguishes it from MCP SDK examples. Existing choices remain authoritative; MCP-only work needs no LLM evaluation. |
| Matt workflows | Preserve dependency groups, resources and native controls. Add [workflow framing](../../plugins/development/WORKFLOW.md); tickets remain optional and setup is explicit. Map `docs/agents/` to `documentation/engineering/` and `docs/adr/` to `documentation/decisions/adr/`, respecting existing paths. |
| Targeted Matt changes | Remove stale setup prerequisites from three skills; give implement-spec a tracker-neutral description. Implement receives pointers to task, contribution and verification guidance without replacing its body. |
| Review and supply chain | differential-review uses its included method without an unavailable registered agent. The pinned supply-chain parser does not cover pnpm/yarn; missing coverage is not a clean audit. |
| AKS cost | Azure AKS only, with its six references. Other platforms use contextual first-party guidance. |
| Repository instructions | agents-md retains its complete source directory; local framing treats size/format targets as heuristics, sample commands/attribution as examples and host instruction precedence as authoritative. |
| Visual craft | frontend-design preserves its body and license; local framing applies accepted visual direction, project scope and platform conventions before aesthetic suggestions. |
| Visibility and labels | Preserve explicit upstream controls; set support visibility only when absent. Scope/stack/role/invocation labels describe use, not permissions. |

Agent Depot acquires accepted artifact commits and records file identities without executing upstream scripts. Built `UPSTREAM.json`, `UPSTREAM-NOTICES.json` and license files record provenance. Trail of Bits material is CC-BY-SA-4.0; other acquired sources are MIT or Apache-2.0 as recorded at their pins. Bundles have mixed-license notices. Embedded live links/commands can still change despite source pinning. Private installed content is never redistributed.

## Matt Pocock selection

The selection below covers 27 upstream skills at [the pinned revision](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d) and includes 18 in development, with their dependencies. Exclusions keep the bundle focused; they do not judge upstream quality.

| Skill | Decision | Reason or constraint |
| --- | --- | --- |
| ask-matt | Remove | Routes only Matt's catalogue and assumes his full flow; the plugin usage guide covers the wider collection. |
| setup-matt-pocock-skills | Remove | Configures trackers, labels and domain files, not plugin installation. Project conventions already cover relevant setup. |
| triage | Remove | Depends on a tracker state machine and labels; outside this bundle's default workflow. |
| to-tickets | Remove | Publishes a tracker-specific task graph; local specs/plans provide scope without tickets. |
| wayfinder | Remove | Requires a map of decision tickets and a large tracker workflow. |
| teach | Remove | Turns the application directory into a separate learning workspace with lessons, resources and learning records. |
| wait-what | Remove | A conversational clarification shortcut; ordinary instructions can request a clearer explanation. |
| wizard | Remove | Generates a scripted human provisioning procedure; adds machinery beyond the default contribution workflow. |
| pr | Remove | Its mandatory visual/evidence/merge-danger template overlaps and conflicts with the concise local contribution guide. |
| grill-me | Keep | Explicit interview without persistent domain docs; calls grilling. |
| grill-with-docs | Keep | Explicit interview with glossary/decisions; calls grilling and domain-modeling. |
| grilling | Keep | Shared interview primitive, only within requested clarification. |
| domain-modeling | Keep | Sharpens domain language and records consequential decisions. |
| to-questionnaire | Keep | Drafts stakeholder questions when facts are held elsewhere; does not authorize sending them. |
| to-spec | Keep, adapt | Synthesizes agreed scope; remove stale setup prerequisite and use local docs unless tracker publication is requested. |
| implement | Keep | Focused execution using TDD where appropriate and code review. |
| implement-spec | Keep, adapt | Dependency-ordered implementation; use local plan slices, supported worktrees/subagents and no tracker prerequisite. |
| tdd | Keep | Behavior-focused testing; apply proportionately at established test boundaries. |
| code-review | Keep, adapt | Separates standards from requested behavior; no tracker setup needed to review conversation/spec scope. |
| diagnosing-bugs | Keep | Reproduction, hypothesis tests, regression evidence and cleanup. |
| research | Keep | Primary-source research; delegation is optional when unsupported. |
| prototype | Keep | Resolves an explicit design uncertainty; prototype branches/artifacts remain scoped to that exploration. |
| codebase-design | Keep | Module/interface design technique; project vocabulary takes precedence over its terminology preferences. |
| improve-codebase-architecture | Keep | Explicit architectural exploration using codebase-design, grilling and domain-modeling. |
| retro | Keep | Improves the agent environment after a requested session review; calls writing-for-agents. |
| handoff | Keep | Portable context for another session, avoiding duplication and redacting secrets. |
| writing-for-agents | Keep | Instruction structure, pointers and progressive disclosure; complements Humanizer's prose editing. |

## Application references

The review on 2026-10-11 covered manifests, official template code and published guidance, not complete architecture audits. No application code, assets or unlicensed skill content was copied. Reviewed source revisions and compatibility limits are recorded below.

| Source | Reviewed revision | Evidence and limits |
| --- | --- | --- |
| [Dub](https://github.com/dubinc/dub) | `bc7eeb882ead4652ed375545db81bb79b72137e8` | Next.js/React, Tailwind v3, Radix, table/form primitives. Evidence that mature applications need not migrate to v4 to follow coherent conventions. |
| [Cal.diy](https://github.com/calcom/cal.diy) (~48.9k stars; redirect from cal.com) | `54343aa685ae8f33159d2f485ec4a57bad5c574a` | Next.js, Tailwind v4 and reusable UI packages. Reference only; do not transplant scheduling-specific architecture. |
| [Supabase Studio](https://github.com/supabase/supabase/tree/master/apps/studio) | `8617532ae1a41571d5d557cd24c6f5f2565d9230` | Tailwind/Radix, tables/forms and multiple framework paths. Repository adoption does not measure Studio usage; not a prescription for its backend scale. |
| [FastAPI full-stack template](https://github.com/fastapi/full-stack-fastapi-template) | `7257e606cb94eada1dca40173e2b7f99dd549bc6` | First-party auth, sessions and full-stack integration. Uses SQLModel and Vite; my SQLAlchemy/Next.js defaults remain explicit. |
| [FastAPI best practices](https://github.com/zhanymkanov/fastapi-best-practices) | `5e00aa6095521f0d00e4eec2ef0afa44cd566af4` | Domain organization, blocking/async distinctions and production cautions. Community reference, not a package; no redistribution license assumed. |

Implementation details and exceptions live beside [frontend conventions](../../plugins/frontend-reactjs-development/skills/frontend-conventions/references/sources-and-exceptions.md) and [backend conventions](../../plugins/backend-python-development/skills/backend-conventions/references/sources-and-exceptions.md). First-party stack documentation supplies backend details; no unified official FastAPI/SQLAlchemy/Alembic skill is claimed. The target of avoiding reference lookup in 90 to 95% of routine uses remains unmeasured.

## Reference-only and excluded sources

| Source | Decision |
| --- | --- |
| [Vercel web-design-guidelines](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) | Reference only: no declared redistribution license at review and a floating guideline fetch. |
| [Amplitude analyze-feedback](https://github.com/amplitude/builder-skills/tree/51838c2d85560466d1bbc174ea0e645bb9c44ea9/analytics-skills/skills/analyze-feedback) | Reference only: Amplitude MCP dependency and no explicit redistribution license at the reviewed pin. No MCP is configured; the local feedback skill works with existing evidence. |
| Jezweb tailwind-v4-shadcn | Not acquired: directory absent at reviewed repository HEAD `1260fa7439b36b18dbf16648ccc7fb44783f6c23`; published setup was Vite-specific. |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Optional installed expertise, constrained by accepted UI direction. No private material is copied. |

Optional [shadcn MCP](https://ui.shadcn.com/docs/mcp) and [Playwright MCP](https://github.com/microsoft/playwright-mcp) require client setup. Hooks use [client extensions](https://agent-plugins.org/specification#8-client-extensions), not a portable hooks field. SigNoz is a replaceable local OTel preference; its [community support is best-effort](https://signoz.io/support/). Provider versions, resources and edition limits require contextual checks; operating/security guidance does not establish compliance.

## Repository-instruction and visual-craft selection

[getsentry/skills agents-md](https://github.com/getsentry/skills/tree/f57ada2d0b640406ea7e25b11d636c530e77c58b/skills/agents-md) adds focused repository-instruction authoring to development. Its inspect-first method, exact command/path checks, scoped instructions and reference-backed editing complement project foundations and general instruction writing. The reviewed source is Apache-2.0; acquisition preserves SKILL.md, SPEC.md and SOURCES.md. GitHub's create-agentsmd was also reviewed; its comprehensive section/template approach adds less to this collection's concise, conditional guidance. Sentry's sample package manager and attribution blocks do not become project policy, and shortening must preserve required information. Use it for instruction-file work rather than every documentation change.

[Anthropic frontend-design](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design) adds visual execution craft to frontend-development without choosing a framework. The claude-code plugin copy references an absent LICENSE.txt; that repository's root terms do not establish a redistribution grant. The reviewed anthropics/skills copy has identical skill text and an included Apache-2.0 LICENSE.txt, so that is the acquired source. Visual-design owns early component-system/appearance foundations, direction and handoff, interaction-design owns behavior, frontend-design supplies subject-grounded composition/typography/craft, and interface-quality owns rendered critique. Plain Tailwind, Tailwind with shadcn/ui, HeroUI or another accepted system can implement those foundations when compatible; this does not create a package dependency or authorize a migration. Use craft guidance for new visual decisions or requested redesigns; preserve accepted tokens/components and avoid adding a new style or approval ceremony to routine changes. Deterministic accessibility, interactions and persisted behavior need their own verification.

The [skills directory](https://www.skills.sh/getsentry/skills/agents-md) reports meaningful adoption for agents-md, and [frontend-design](https://www.skills.sh/anthropics/skills/frontend-design) is widely installed. Adoption supports discovery; source review and applicable evidence determine fit. Neither acquisition establishes behavioral improvement; those trials remain deferred.

## AI development, testing and operations segmentation

The generic ai-development package contains three independently useful disciplines. Ai-development owns application patterns, architecture tradeoffs, model/context/tool choices, skills/harness integration and protocols. Ai-testing owns conceptual evaluation levels, cases, measures, acceptance and regression evidence, including the retained detailed quality/speech reference. Ai-operations owns AI-specific task and quality signals, provider/resource limits, cost, drift, configuration changes and recovery. Development keeps concise pointers to those owners; it no longer duplicates detailed evaluation or operating methods. None requires an evaluator SDK, instrumentation library or vendor.

Ai-deepeval-testing owns the selected Python/DeepEval test-case, dataset, metric and script/pytest-style CI integration. Python-ai-observability owns Python OpenTelemetry provider/instrumentor/exporter integration, context propagation, privacy controls and received-signal verification. AI-conventions retains provider and FastMCP implementation. These three local technical skills share ai-python-development with the acquired mcp-builder, for four skills in total. A Python evaluation runner need not imply a Python application. Generic service reliability and incident procedures remain with relevant operating expertise, and Collector/backend deployment remains with matching platform/tool guidance. Optional specialists are selected by capability; missing expertise does not remove essential reasoning or lower acceptance.

The [DeepEval evaluation guide](https://deepeval.com/docs/evaluation-introduction), [metrics](https://deepeval.com/docs/metrics-introduction) and [CI instructions](https://deepeval.com/docs/evaluation-unit-testing-in-ci-cd) informed the original testing skill. The official [DeepEval skills](https://github.com/confident-ai/deepeval/tree/main/skills) were reviewed but not acquired: their mandatory intake/synthetic-data generation, hosted-service preference and fixed iteration defaults do not fit this collection's scope and composition principles. API documentation remains the implementation authority; no hosted account or generation loop is imposed.

The Python observability skill uses [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/), [exporters](https://opentelemetry.io/docs/languages/python/exporters/) and the selected [GenAI conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/). These are technical integration choices, not a generic monitoring-vendor preference. Traces describe execution; evaluations assess quality, even when a platform offers both. No SDK/backend or live evaluation was installed or exercised for this guidance change.

## Operations and visualization provenance

The supplied portable operations guidance is local material under this repository's license. Private source-note companions, inventories, incident identities, internal skills, factory runtime and fixed schedules are excluded. Public primary references remain with the skills.

| Current package | Material |
| --- | --- |
| development | System mapping and shared development methods |
| backend-python-development | Python automation engineering |
| operations | Reliability, observability, incidents, runbooks, postmortems, recovery, capacity, cost, vulnerabilities, credentials and upkeep |
| operations-platforms | JVM, Kubernetes and AKS expertise |
| delivery and development-tooling | Delivery methods and selected implementation tools |
| visualization | The supplied system-flow-explorer with its renderer, validator, examples and checks; diagram and presentation resources |

Platform boundaries and native invocation controls remain explicit. Numerical examples are contextual. The [SDLC map](../sdlc.md) owns phase and capability coverage.

## System and client design choices

I retain the pinned Matt codebase-design and domain-modeling techniques for interfaces and domain concepts. I reviewed [wshobson architecture-patterns](https://github.com/wshobson/agents/blob/main/plugins/backend-development/skills/architecture-patterns/SKILL.md), a widely installed backend-pattern skill, but keep it reference-only: its prescribed Clean/Hexagonal/DDD structures are narrower than product-led system decisions. My local system-design skill coordinates outcomes, alternatives, boundaries, operating constraints and delivery across new products and feature changes; it does not copy the upstream body or change existing source pins.

My desktop default is TypeScript + Tauri. My initial mobile recommendation is React Native + Expo for a TypeScript team, compared with Flutter, Kotlin Multiplatform and native UI when constraints warrant. The [platform selection reference](../../plugins/frontend-native-development/skills/native-client-development/references/platform-selection.md) contains first-party sources and actual native verification boundaries. AI interfaces can use complementary [AG-UI/A2UI contracts](../../plugins/ai-development/skills/ai-development/references/interaction-protocols.md); protocol/renderer versions and framework adapters must be checked together.

## Figma community review

I reviewed the supplied Community entries on 2026-10-16. These are external references, not bundled skills or evidence of tool compatibility. The [official catalogue](https://www.figma.com/community/ai-skills?resource_type=skills) includes workflows for Figma's own agent; a familiar skill name does not establish compatibility with a coding-agent MCP client.

| Candidate | Fit and material limits | Current decision |
| --- | --- | --- |
| [better-interface](https://www.figma.com/community/skill/61238/better-interface) | Broad craft review with concrete runtime evidence; the Community version also writes annotation cards and prescribes exact motion values. [The author's MIT repository](https://github.com/jakubkrehel/skills) has a different orchestration version with six required domain owners. | Reference-only: the Community and GitHub versions differ, and the GitHub version requires a six-skill group. |
| [usability-test-guide](https://www.figma.com/community/skill/71690/usability-test-guide) | Neha Kodi's selected-frame moderated discussion guide, with goal-based tasks and neutral probes; writes a guide frame. It prepares research rather than conducting it. | Reference-only: redistribution rights are unestablished, and the workflow requires a compatible Figma host. |
| [analyze-components](https://www.figma.com/community/skill/61009/analyze-components) | Component/style/variable inventory, canvas audit document and repairs, including orphan/instance changes. Long host-specific script/layout guidance. | Targeted design-system maintenance only; separate inspection from authorized repair and verify instance/binding preservation. Not a read-only audit by default. |
| [spacing-audit](https://www.figma.com/community/skill/70410/spacing-audit) | Audits and adjusts a prescribed 4/8pt scale. Preserves token bindings and asks before changing a deliberate alternative scale. | Optional focused review; accepted project tokens/density remain authoritative. Not a universal new spacing standard. |
| [balise-ux-writing](https://www.figma.com/community/skill/64048/balise-ux-writing) | Scoped review/rewrite/generate/harmonize modes, preserves product meaning and avoids invented claims. [The author's repository](https://github.com/mrstev3n/balise-skills) declares Apache-2.0; Community and repository versions need comparison at a reviewed pin. | Reference-only: the separately licensed author repository has its own resources and host adapters. |
| [superfuture-design-review](https://www.figma.com/community/skill/65434/superfuture-design-review) | Prioritized broad critique; its frontmatter is named design-review and it overlaps better-interface. Numeric craft preferences need contextual interpretation. | Alternative review reference, without a requirement for a second critique of every screen. |
| [desktop-to-mobile](https://www.figma.com/community/skill/72495/desktop-to-mobile) | Creates a separate 390px mobile frame and menu states, with prescribed stacking/type/navigation transformations. Preserves original frame and existing variants where possible. | Optional responsive exploration; it does not produce or validate native iOS/Android behavior, tablet coverage or arbitrary widths. |

Several entries display the [Community Free Resource License](https://www.figma.com/community-free-resource-license/), which restricts use to the Figma platform and does not grant the redistribution/adaptation rights needed here. I keep those as links; no Community instructions or scripts are bundled. The usability guide's rendered page did not establish a redistribution license. Separately licensed author repositories require their own revision, dependency, resource and behavioral review before acquisition. Source review does not authorize account connections or canvas mutation.

Figma's [official MCP guide](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/) owns endpoint and client support. The frontend-development declaration does not establish authenticated client/file access. Official Figma skills are available from [mcp-server-guide](https://github.com/figma/mcp-server-guide); the reviewed tree did not expose a root license, so those skills are reference-only.

## Local UI/UX capability owners

Interface-quality, ux-writing and usability-research are original local guidance under this repository's license. Their responsibilities include evidence-based inspection, contextual design, scoped copy changes, component/token preservation, neutral research tasks and honest observation status. These local methods do not copy Community skill text, scripts or private installed content.

The Community candidates above remain references. The MIT better-interface repository delegates to a six-skill group and differs from the canvas-writing Community version; acquiring that group would add overlapping ownership and dependency/control adaptation. The Apache-2.0 Balise source remains reference-only. I chose focused local owners with shared user/agent access and host-independent evidence boundaries, retaining Figma as an optional surface. This is a scope decision, not a claim that local guidance outperforms those sources. A controlled behavioral comparison has not run.

## Documentation methods

I use documentation-writing for authoring quality and architecture-documentation for useful structural, runtime, interface and deployment explanations. Documentation-conventions owns authoritative records and upkeep; system-design owns design choices. These are original local skills; no upstream resources or invocation controls are imported.

The source review compares [Anthropic doc-coauthoring](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/doc-coauthoring/SKILL.md) and [GitHub documentation-writer](https://github.com/github/awesome-copilot/blob/8bc0f5715b2ddc7901a62fddf144ded30d56de8b/skills/documentation-writer/SKILL.md). Context gathering, reader questions, accuracy and terminology fit; mandatory collaboration/outline approvals do not fit routine authorized upkeep. Diátaxis and Google technical writing inform the authoring method; C4, arc42 and OpenAPI inform architecture coverage. References remain with the skills and do not establish complete standards conformance.

### Skill-writing references

The [Anthropic skills collection](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills) provides several useful forms of instruction, rather than one template to reproduce:

| Reference | Useful authoring quality |
| --- | --- |
| [frontend-design](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design/SKILL.md) | Connects choices in composition, typography and content to the subject and brief. |
| [mcp-builder](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/mcp-builder/SKILL.md) | Describes a technical method and routes implementation detail to relevant resources. |
| [webapp-testing](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/webapp-testing/SKILL.md) | Makes the path from inspection to action concrete and exposes reusable execution helpers. |
| [doc-coauthoring](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/doc-coauthoring/SKILL.md) | Explains what each stage achieves and checks whether a reader can use the result. |

These references inform original authoring; this review does not acquire more upstream skills or change existing pins. Adopt a writing technique when it clarifies the local method, while retaining the collection's scope, optional composition and proportional execution. Client-specific tools, rigid collaboration counts and technical defaults need their own applicability assessment. Readability and meaningful depth require author judgment and reader feedback; resemblance to an upstream format does not establish effectiveness.

## Product and capability architecture

The [ownership catalogue](#plugin-ownership) identifies each skill's package. Structural independence has repository/build checks; behavioral adherence remains unverified.

I separate the requested activity, reusable discipline and technical implementation. Activities own the engagement and stopping point; disciplines own decisions and evidence; technical conventions apply those decisions to an accepted stack. Role, applicability and invocation remain independent metadata dimensions. Plugins stay as useful delivery bundles rather than becoming one package per conceptual layer.

| Decision | Ownership and boundary |
| --- | --- |
| Business direction | Business-strategy retains its original strategic model and resources. |
| Product direction | Product-management owns problem evidence, priorities, useful scope, success signals and sequencing. Product-feedback owns evidence synthesis; refine owns engineering requirements. |
| System and service design | System-design owns architectural boundaries; backend-design owns service authority, state, failure and consumer contracts. Python conventions retain concrete runtime/persistence mechanics. |
| Interface design | Visual-design owns product-derived direction and token intent; interaction-design owns flows and coverage; interface-quality owns critique. React and native conventions implement these decisions with compatible primitives. |
| AI design, testing and operations | Ai-development owns application/capability/protocol design; ai-testing owns evaluation strategy/evidence; ai-operations owns AI operating outcomes. Ai-conventions, ai-deepeval-testing and python-ai-observability supply selected Python implementations. Framework and backend deployment expertise remain separate. |
| Navigation | Workflow-help recommends activities; develop coordinates an explicitly requested engagement. TASKS.md describes needed expertise and matches available descriptions, preserving fallback when specialists are absent. No global router or dependency engine is added. |

I reviewed Anthropic's product-brainstorming and roadmap-update skills at [33eeda1](https://github.com/anthropics/knowledge-work-plugins/tree/33eeda1e8fd856455b05479d13a0f85b5f803744/product-management/skills), under its [Apache-2.0 license](https://github.com/anthropics/knowledge-work-plugins/blob/33eeda1e8fd856455b05479d13a0f85b5f803744/LICENSE). They offer problem exploration, assumption testing, outcome-oriented roadmaps and dependency reasoning. Their larger workflow includes fixed ideation counts, connected-tool assumptions and suggested follow-ups that do not fit every bounded development request.

I also reviewed prioritize-features and identify-assumptions-new at [phuryn/pm-skills 07b34f6](https://github.com/phuryn/pm-skills/tree/07b34f64ee828df08953f505b7f747aef85ae7c6/pm-product-discovery/skills), under its [MIT license](https://github.com/phuryn/pm-skills/blob/07b34f64ee828df08953f505b7f747aef85ae7c6/LICENSE). They connect impact, effort, uncertainty and product risk, but prescribe a top-five result or a fixed eight-category treatment and introduce additional skill/framework dependencies. I keep these as reviewed references rather than import their orchestrations or scoring conventions. This is a scope and composition decision, not a demonstrated quality ranking.

Product-management is original local guidance. It uses the accepted product outcomes and existing evidence/decision principles, with optional frameworks and no required research format, tracker, scoring formula or commercial study. Acquired resources retain reviewed pins, licenses and native controls, with scoped adaptations recorded in notices. The same principle guides the visual/backend/AI ownership split: preserve useful technical invariants and explicit preferences without repeating an entire product process in each stack.

Independently installable bundles retain concise essential defaults and discover optional methods through the observed inventory. Missing guidance does not select another stack, authorize installation or eliminate required outcomes. I preserve the seven-phase lifecycle, project foundations, implementation/verification loop and consequential-decision policy. Repository checks do not establish improved routing or application outcomes; see [evaluation status](evaluations.md#current-status).

<a id="target-plugin-ownership"></a>

## Database guidance sources

Database methods are original and engine-independent. The three original PostgreSQL skills retain reviewed Neon, Supabase and Microsoft skill references through string metadata and a [package-local source reference](../../plugins/database-postgresql-development/references/sources.md). No PostgreSQL skills are acquired, and no database MCP server is declared. Primary version-matched PostgreSQL documentation controls implementation.

## Identity and access sources

Original identity/access guidance uses inspected Keycloak, Better Auth, Ory Kratos and OpenFGA paths plus current protocol/OWASP references. The [package source review](../../plugins/security/skills/security-auth-development/references/sources.md) records revisions, applicability and limitations. No identity framework or external connection is installed. Security/privacy design moves to security; development retains essential reasoning and capability-based selection.

## SaaS research sources

The original SaaS methods use selected public Next.js SaaS starter and Wasp Open SaaS schema, administration, dashboard and payment paths. The [package source review](../../plugins/saas-development/references/sources.md) pins inspected revisions and separates useful concerns from starter simplifications. No application code, visual theme or framework choice is imported. Dashboard methods remain generic; the actual component framework is selected separately.

## Governance source approach

The original governance skills connect applicability, system/control decisions and evidence. [Official source references](../../plugins/governance/references/sources.md) identify when to consult GDPR/EDPB and AICPA material. Regulations and restricted criteria are not copied, and no vendor checklist or project template establishes compliance or an attestation outcome.

## TypeScript source selection

[TypeScript conventions source notes](../../plugins/typescript-development/skills/typescript-conventions/references/sources.md) record the reviewed Jeffallan, Wshobson and Microsoft candidates. No upstream fills the cross-runtime foundation without scope mismatch; the original skill retains a narrow boundary and first-party conditional references. Advanced-type tutorials and compiler-maintenance workflows are not acquired. Existing client packages remain independently useful.

## Go source selection

The [Go source review](../../plugins/go-development/skills/go-conventions/references/sources.md) records inspected Samber, madflojo, cxuu and JetBrains candidates. Their topic coverage informs an original concise foundation, but mandatory orchestration/tool installation, broad house rules or linked-group scope do not fit unchanged acquisition. No Go upstream skill or setup script is imported. Conditional primary references cover the accepted toolchain.

## Browser-extension source selection

The [browser-extension source review](../../plugins/browser-extension-development/references/sources.md) records the pinned Quang collection and primary Chrome, WXT, CRXJS and browser-driver contracts. Five original technical skills cover architecture/lifecycle, permissions/security, extension UI, runtime testing and store delivery. They preserve existing workflows, design systems and accepted stacks. The upstream's twelve skills are source references rather than acquired snapshots: correcting their framework, testing and authority examples would require extensive adaptations. No new Agent Depot artifacts, client installation or publisher connection is introduced. Chrome/MV3 is the supported guidance scope; other browsers and store/runtime behavior need their own evidence.

## Plugin ownership

The collection has 25 independent packages and 122 skills: 83 local and 39 acquired. Development is the default build; 13 generic packages contain no stack-specific skills, and 12 technical packages are explicitly selected. Artifact commit pins, original resource groups and native invocation controls are preserved. Acquisition destinations follow the owners below; Humanizer uses documentation-local composition framing and the Python MCP wrapper uses Python-local conventions.

A plugin represents a useful installation choice. Workflow, application discipline and supporting capability describe its purpose; generic versus technical describes its applicability. These groups do not impose an execution order or dependencies. Installing a technical package makes expertise available without accepting its technology for a project. Keep accepted choices, select matching guidance from actual inventory and retain useful outcomes when optional specialists are absent.

### Package boundaries

The collection has 13 generic capability packages and 12 optional technical packages. I group specialist tools and operating platforms into two explicit optional packages rather than create a plugin for every tool. Split a package only when independent installation is useful.

| Plugin | Applicability | Skills | Responsibility |
| --- | --- | --- | --- |
| `strategy` | Generic | 4 | Business direction, product priorities and evidence-based feedback. |
| `development` | Generic | 40 | SDLC engagements, project foundations, contribution flow and verification; usable without stack packages. |
| `operations` | Generic | 12 | Service reliability, signals, incidents, recovery, capacity and security upkeep. |
| `frontend-development` | Generic | 6 | Experience and interface methods across web, desktop and mobile. |
| `backend-development` | Generic | 1 | Service authority, state, failure, durable work and consumer contracts. |
| `ai-development` | Generic | 3 | AI application/architecture and protocol design; testing/evaluation methods; AI-specific operating decisions and evidence. |
| `delivery` | Generic | 1 | CI/release/deployment methods, immutable artifacts, promotion, compatibility and recovery. |
| `documentation` | Generic support | 4 | Writing, architecture explanation, knowledge organization and prose editing. |
| `visualization` | Generic support | 3 | Diagrams, presentations and interactive system explanation; preserve executable resources. |
| `backend-python-development` | Technical | 3 | Python/FastAPI/persistence and Python automation; no backend service required for CLI work. |
| `frontend-reactjs-development` | Technical | 5 | React/Next.js/shadcn/Tailwind and their actual component APIs. |
| `browser-extension-development` | Technical | 5 | Chrome/MV3 execution contexts, permissions, extension surfaces, runtime verification and controlled store delivery. |
| `frontend-native-development` | Technical | 1 | TypeScript/Tauri and React Native/Expo, platform lifecycle, packaging and native drivers. |
| `ai-adk-development` | Technical | 2 | Google ADK; preserve the paired architecture/builder skills. |
| `ai-langchain-development` | Technical | 4 | LangChain/LangGraph and dependencies/persistence as a complete group. |
| `ai-python-development` | Technical | 4 | Python provider/FastMCP adapters, DeepEval evaluation suites and OpenTelemetry AI instrumentation; no required agent framework or hosted backend. |
| `development-tooling` | Technical | 6 | Optional Bash, browser/load testing, delivery/configuration tooling and lockfile audit implementations. |
| `operations-platforms` | Technical | 3 | Optional JVM, Kubernetes and AKS expertise; match each skill independently to the actual platform. |
| `database-development` | Generic | 2 | Data contracts, consistency, schema evolution and evidence-led performance methods. |
| `database-postgresql-development` | Technical | 3 | PostgreSQL development, diagnostics and operating mechanics. |
| `saas-development` | Generic | 3 | Tenant/customer and commercial lifecycle, SaaS dashboard design and scoped readiness. |
| `governance` | Generic | 3 | Applicability, accountable controls and GDPR/SOC 2 readiness evidence. |
| `typescript-development` | Technical | 1 | Runtime/module/package contracts and TypeScript implementation verification without React. |
| `go-development` | Technical | 1 | Go module/package, lifecycle, error and verification contracts for services, libraries and CLIs. |

Generic means no required language, framework, provider or platform selection. Comparing technologies, naming optional standards and explaining compatibility remain useful. Concrete implementation and preferred-tool setup belong to technical guidance. Classification must follow the body and its references, not just the metadata label.

### Setup, repository and delivery ownership

| Decision or work | Owner | Boundary |
| --- | --- | --- |
| Requested project setup/adoption | setup in development | Coordinates the agreed foundation work; does not replace product/architecture decisions or authorize feature implementation. |
| Repository structure, configuration contract, local commands, onboarding and applicable checks | project-conventions in development | Owns the foundation outcomes; accepted layout and tooling take precedence. |
| Worktree, branch, staging, commit and PR mechanics | git-contributions in development | Keeps the objective reviewable; does not own runtime/package setup. |
| Product-to-design-to-implementation engagement | develop in development | Establishes needed outcomes within scope; optional discipline packages deepen the method. |
| CI, versioned artifacts, release/deployment compatibility, promotion and recovery | delivery-pipelines in delivery | Owns provider-neutral delivery decisions and evidence; an unknown target remains an unresolved boundary. |
| Explicit release/readiness engagement | release in development | Coordinates the requested action and stopping point; delivery expertise is optional, not an automatic installation. |
| Python/React/native/AI build, package and configuration mechanics | Matching technical package | Implements accepted decisions with compatible APIs and tools. |
| GitHub Actions, Docker/Compose, registry and checker configuration | development-tooling | Supplies selected implementation details; no implied provider adoption or publication. |
| Signal/recovery requirements, incidents and restoration exercises | operations | Owns running-system outcomes; platform and telemetry-backend configuration is optional technical expertise. |
| Authoritative knowledge and source-backed explanation | documentation | Keeps useful knowledge current; setup and delivery retain their own required outcomes. |

A workflow-only setup still establishes applicable onboarding, reproducible commands, meaningful checks and artifact/delivery/recovery expectations. It uses available project facts and tools without promising specialist depth. Missing optional guidance neither deletes these outcomes nor requires installation. Methods are selected by needed capability against observed descriptions, with no cross-plugin filesystem links or automatic explicit-only task invocations.

### Method and implementation responsibilities

| Concern | Generic owner | Technical expertise |
| --- | --- | --- |
| Project foundations | development: foundation outcomes, isolation/readiness and check selection | Accepted language/framework; selected local-service, hook/checker and diagnostics tools |
| Delivery | delivery: artifact identity, trust, promotion and recovery | Selected CI, registry, packaging and deployment implementation |
| AI | ai-development: application design, testing/evaluation and AI operations | Accepted provider/framework, evaluator, instrumentation, protocol SDK and renderer |
| Client experience | frontend-development: visual/interaction decisions and interface evidence | Accepted web/native framework, component primitives and drivers |
| Observability | operations and generic AI operations: meaningful signals, privacy and failure boundaries | Runtime instrumentation, Collector/backend deployment and actual export configuration |
| Application verification | development: journey, workload, fault and completion evidence | Compatible test tools, platform drivers and execution targets |

Concrete preferences belong in explicitly selected technical guidance or project instructions. Conditional interoperability standards do not choose an application stack; implementation must match accepted protocols and installed versions.

### Skill catalogue

Each row has one owner. Local links lead to source; upstream links lead to the exact acquired revision. Preserve every skill's complete resources, licenses, native controls and scope. The dispositions record the separation of method outcomes from technical implementation; each package is checked independently.

<details>
<summary>All 122 skills and their current owners</summary>

| Skill | Origin | Plugin |
| --- | --- | --- |
| [business-opportunity-analysis](../../plugins/strategy/skills/business-opportunity-analysis/SKILL.md) | Local | `strategy` |
| [business-strategy](../../plugins/strategy/skills/business-strategy/SKILL.md) | Local | `strategy` |
| [learn-from-product-feedback](../../plugins/strategy/skills/learn-from-product-feedback/SKILL.md) | Local | `strategy` |
| [product-management](../../plugins/strategy/skills/product-management/SKILL.md) | Local | `strategy` |
| [agents-md](https://github.com/getsentry/skills/tree/f57ada2d0b640406ea7e25b11d636c530e77c58b/skills/agents-md) | Upstream | `development` |
| [code-review](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/code-review) | Upstream | `development` |
| [codebase-design](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/codebase-design) | Upstream | `development` |
| [deliver-reliable-changes](../../plugins/development/skills/deliver-reliable-changes/SKILL.md) | Local | `development` |
| [dependencies](../../plugins/development/skills/dependencies/SKILL.md) | Local | `development` |
| [design](../../plugins/development/skills/design/SKILL.md) | Local | `development` |
| [develop](../../plugins/development/skills/develop/SKILL.md) | Local | `development` |
| [diagnosing-bugs](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/diagnosing-bugs) | Upstream | `development` |
| [differential-review](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/differential-review/skills/differential-review) | Upstream | `development` |
| [domain-modeling](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/domain-modeling) | Upstream | `development` |
| [git-contributions](../../plugins/development/skills/git-contributions/SKILL.md) | Local | `development` |
| [grill-me](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/grill-me) | Upstream | `development` |
| [grill-with-docs](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/grill-with-docs) | Upstream | `development` |
| [grilling](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/grilling) | Upstream | `development` |
| [handoff](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/handoff) | Upstream | `development` |
| [harden](../../plugins/development/skills/harden/SKILL.md) | Local | `development` |
| [implement](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/implement) | Upstream | `development` |
| [implement-spec](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/implement-spec) | Upstream | `development` |
| [improve](../../plugins/development/skills/improve/SKILL.md) | Local | `development` |
| [improve-codebase-architecture](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/improve-codebase-architecture) | Upstream | `development` |
| [journey-testing](../../plugins/development/skills/journey-testing/SKILL.md) | Local | `development` |
| [plan](../../plugins/development/skills/plan/SKILL.md) | Local | `development` |
| [project-conventions](../../plugins/development/skills/project-conventions/SKILL.md) | Local | `development` |
| [property-based-testing](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/property-based-testing/skills/property-based-testing) | Upstream | `development` |
| [prototype](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/prototype) | Upstream | `development` |
| [refine](../../plugins/development/skills/refine/SKILL.md) | Local | `development` |
| [release](../../plugins/development/skills/release/SKILL.md) | Local | `development` |
| [research](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/research) | Upstream | `development` |
| [resilience-testing](../../plugins/development/skills/resilience-testing/SKILL.md) | Local | `development` |
| [retro](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/retro) | Upstream | `development` |
| [review](../../plugins/development/skills/review/SKILL.md) | Local | `development` |
| [security-and-privacy-design](../../plugins/security/skills/security-and-privacy-design/SKILL.md) | Local | `security` |
| [setup](../../plugins/development/skills/setup/SKILL.md) | Local | `development` |
| [system-design](../../plugins/development/skills/system-design/SKILL.md) | Local | `development` |
| [system-mapping](../../plugins/development/skills/system-mapping/SKILL.md) | Local | `development` |
| [tdd](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/tdd) | Upstream | `development` |
| [test](../../plugins/development/skills/test/SKILL.md) | Local | `development` |
| [to-questionnaire](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/to-questionnaire) | Upstream | `development` |
| [to-spec](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/to-spec) | Upstream | `development` |
| [workflow-help](../../plugins/development/skills/workflow-help/SKILL.md) | Local | `development` |
| [writing-for-agents](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/writing-for-agents) | Upstream | `development` |
| [credential-lifecycle](../../plugins/operations/skills/credential-lifecycle/SKILL.md) | Local | `operations` |
| [incident-response](../../plugins/operations/skills/incident-response/SKILL.md) | Local | `operations` |
| [observability-operations](../../plugins/operations/skills/observability-operations/SKILL.md) | Local | `operations` |
| [operational-housekeeping](../../plugins/operations/skills/operational-housekeeping/SKILL.md) | Local | `operations` |
| [optimize-application-cost](../../plugins/operations/skills/optimize-application-cost/SKILL.md) | Local | `operations` |
| [plan-application-capacity](../../plugins/operations/skills/plan-application-capacity/SKILL.md) | Local | `operations` |
| [postmortem-facilitation](../../plugins/operations/skills/postmortem-facilitation/SKILL.md) | Local | `operations` |
| [postmortem-followup](../../plugins/operations/skills/postmortem-followup/SKILL.md) | Local | `operations` |
| [protect-and-restore-data](../../plugins/operations/skills/protect-and-restore-data/SKILL.md) | Local | `operations` |
| [reliability-design](../../plugins/operations/skills/reliability-design/SKILL.md) | Local | `operations` |
| [runbook-engineering](../../plugins/operations/skills/runbook-engineering/SKILL.md) | Local | `operations` |
| [vulnerability-management](../../plugins/operations/skills/vulnerability-management/SKILL.md) | Local | `operations` |
| [interaction-design](../../plugins/frontend-development/skills/interaction-design/SKILL.md) | Local | `frontend-development` |
| [interface-quality](../../plugins/frontend-development/skills/interface-quality/SKILL.md) | Local | `frontend-development` |
| [usability-research](../../plugins/frontend-development/skills/usability-research/SKILL.md) | Local | `frontend-development` |
| [ux-writing](../../plugins/frontend-development/skills/ux-writing/SKILL.md) | Local | `frontend-development` |
| [frontend-design](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design) | Upstream | `frontend-development` |
| [visual-design](../../plugins/frontend-development/skills/visual-design/SKILL.md) | Local | `frontend-development` |
| [backend-design](../../plugins/backend-development/skills/backend-design/SKILL.md) | Local | `backend-development` |
| [ai-development](../../plugins/ai-development/skills/ai-development/SKILL.md) | Local | `ai-development` |
| [ai-testing](../../plugins/ai-development/skills/ai-testing/SKILL.md) | Local | `ai-development` |
| [ai-operations](../../plugins/ai-development/skills/ai-operations/SKILL.md) | Local | `ai-development` |
| [delivery-pipelines](../../plugins/delivery/skills/delivery-pipelines/SKILL.md) | Local | `delivery` |
| [architecture-documentation](../../plugins/documentation/skills/architecture-documentation/SKILL.md) | Local | `documentation` |
| [documentation-conventions](../../plugins/documentation/skills/documentation-conventions/SKILL.md) | Local | `documentation` |
| [documentation-writing](../../plugins/documentation/skills/documentation-writing/SKILL.md) | Local | `documentation` |
| [humanizer](https://github.com/blader/humanizer/tree/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8) | Upstream | `documentation` |
| [architecture-diagramming](../../plugins/visualization/skills/architecture-diagramming/SKILL.md) | Local | `visualization` |
| [presentation-building](../../plugins/visualization/skills/presentation-building/SKILL.md) | Local | `visualization` |
| [system-flow-explorer](../../plugins/visualization/skills/system-flow-explorer/SKILL.md) | Local | `visualization` |
| [backend-conventions](../../plugins/backend-python-development/skills/backend-conventions/SKILL.md) | Local | `backend-python-development` |
| [modern-python](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/modern-python/skills/modern-python) | Upstream | `backend-python-development` |
| [python-automation-engineering](../../plugins/backend-python-development/skills/python-automation-engineering/SKILL.md) | Local | `backend-python-development` |
| [frontend-conventions](../../plugins/frontend-reactjs-development/skills/frontend-conventions/SKILL.md) | Local | `frontend-reactjs-development` |
| [shadcn](https://github.com/shadcn-ui/ui/tree/6b600cf1ff42f8a746747ea587e52af3ee224643/skills/shadcn) | Upstream | `frontend-reactjs-development` |
| [tailwind-design-system](https://github.com/wshobson/agents/tree/46891e7e60da0e52baf1050b7b6391b64e84c6d9/plugins/frontend-mobile-development/skills/tailwind-design-system) | Upstream | `frontend-reactjs-development` |
| [vercel-composition-patterns](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns) | Upstream | `frontend-reactjs-development` |
| [vercel-react-best-practices](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices) | Upstream | `frontend-reactjs-development` |
| [browser-extension-development](../../plugins/browser-extension-development/skills/browser-extension-development/SKILL.md) | Local | `browser-extension-development` |
| [browser-extension-security](../../plugins/browser-extension-development/skills/browser-extension-security/SKILL.md) | Local | `browser-extension-development` |
| [browser-extension-ui](../../plugins/browser-extension-development/skills/browser-extension-ui/SKILL.md) | Local | `browser-extension-development` |
| [browser-extension-testing](../../plugins/browser-extension-development/skills/browser-extension-testing/SKILL.md) | Local | `browser-extension-development` |
| [browser-extension-delivery](../../plugins/browser-extension-development/skills/browser-extension-delivery/SKILL.md) | Local | `browser-extension-development` |
| [native-client-development](../../plugins/frontend-native-development/skills/native-client-development/SKILL.md) | Local | `browser-extension-development` | Technical | 5 | Chrome/MV3 execution contexts, permissions, extension surfaces, runtime verification and controlled store delivery. |
| `frontend-native-development` |
| [adk-agent-builder](https://github.com/google/adk-python/tree/6be386d8939c4898aa2c0fc8a1f7cb34e7df7904/.agents/skills/adk-agent-builder) | Upstream | `ai-adk-development` |
| [adk-architecture](https://github.com/google/adk-python/tree/6be386d8939c4898aa2c0fc8a1f7cb34e7df7904/.agents/skills/adk-architecture) | Upstream | `ai-adk-development` |
| [langchain-dependencies](https://github.com/langchain-ai/langchain-skills/tree/16a992f09ab3ccfb642dd4f08d350d833d1990bf/config/skills/langchain-dependencies) | Upstream | `ai-langchain-development` |
| [langchain-fundamentals](https://github.com/langchain-ai/langchain-skills/tree/16a992f09ab3ccfb642dd4f08d350d833d1990bf/config/skills/langchain-fundamentals) | Upstream | `ai-langchain-development` |
| [langgraph-fundamentals](https://github.com/langchain-ai/langchain-skills/tree/16a992f09ab3ccfb642dd4f08d350d833d1990bf/config/skills/langgraph-fundamentals) | Upstream | `ai-langchain-development` |
| [langgraph-persistence](https://github.com/langchain-ai/langchain-skills/tree/16a992f09ab3ccfb642dd4f08d350d833d1990bf/config/skills/langgraph-persistence) | Upstream | `ai-langchain-development` |
| [ai-deepeval-testing](../../plugins/ai-python-development/skills/ai-deepeval-testing/SKILL.md) | Local | `ai-python-development` |
| [python-ai-observability](../../plugins/ai-python-development/skills/python-ai-observability/SKILL.md) | Local | `ai-python-development` |
| [ai-conventions](../../plugins/ai-python-development/skills/ai-conventions/SKILL.md) | Local | `ai-python-development` |
| [mcp-builder](https://github.com/anthropics/skills/tree/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/mcp-builder) | Upstream | `ai-python-development` |
| [bash-engineering](../../plugins/development-tooling/skills/bash-engineering/SKILL.md) | Local | `development-tooling` |
| [github-actions-hardening](https://github.com/github/awesome-copilot/tree/143a3d976b3c1603cc8932984d5e1f28501cb5fc/skills/github-actions-hardening) | Upstream | `development-tooling` |
| [performance-testing](../../plugins/development-tooling/skills/performance-testing/SKILL.md) | Local | `development-tooling` |
| [playwright-cli](https://github.com/microsoft/playwright-cli/tree/b85c7a736bb473bf55b584e54a09ffa698d6d871/skills/playwright-cli) | Upstream | `development-tooling` |
| [supply-chain-risk-auditor](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor) | Upstream | `development-tooling` |
| [tooling-conventions](../../plugins/development-tooling/skills/tooling-conventions/SKILL.md) | Local | `development-tooling` |
| [aks-cost-optimization](https://github.com/Azure/AKS-Skills/tree/20bf35201a79b324d2ca3e00e5c82020ff362024/skills/aks-cost-optimization) | Upstream | `operations-platforms` |
| [infra-jvm-optimization](../../plugins/operations-platforms/skills/infra-jvm-optimization/SKILL.md) | Local | `operations-platforms` |
| [kubernetes-resource-engineering](../../plugins/operations-platforms/skills/kubernetes-resource-engineering/SKILL.md) | Local | `operations-platforms` |
| [database-design](../../plugins/database-development/skills/database-design/SKILL.md) | Local | `database-development` |
| [database-performance](../../plugins/database-development/skills/database-performance/SKILL.md) | Local | `database-development` |
| [postgresql-development](../../plugins/database-postgresql-development/skills/postgresql-development/SKILL.md) | Local | `database-postgresql-development` |
| [postgresql-operations](../../plugins/database-postgresql-development/skills/postgresql-operations/SKILL.md) | Local | `database-postgresql-development` |
| [postgresql-performance](../../plugins/database-postgresql-development/skills/postgresql-performance/SKILL.md) | Local | `database-postgresql-development` |
| [security-auth-development](../../plugins/security/skills/security-auth-development/SKILL.md) | Local | `security` |
| [saas-dashboard-design](../../plugins/saas-development/skills/saas-dashboard-design/SKILL.md) | Local | `saas-development` |
| [saas-design](../../plugins/saas-development/skills/saas-design/SKILL.md) | Local | `saas-development` |
| [saas-readiness](../../plugins/saas-development/skills/saas-readiness/SKILL.md) | Local | `saas-development` |
| [compliance-design](../../plugins/governance/skills/compliance-design/SKILL.md) | Local | `governance` |
| [gdpr-readiness](../../plugins/governance/skills/gdpr-readiness/SKILL.md) | Local | `governance` |
| [soc2-readiness](../../plugins/governance/skills/soc2-readiness/SKILL.md) | Local | `governance` |
| [typescript-conventions](../../plugins/typescript-development/skills/typescript-conventions/SKILL.md) | Local | `typescript-development` |
| [go-conventions](../../plugins/go-development/skills/go-conventions/SKILL.md) | Local | `go-development` |

</details>

### Resource and invocation closure

Keep the 18 retained Matt skills together in development, including their research, interview, domain-modeling, implementation, review, retrospective and writing-for-agents dependencies. These supporting techniques help that workflow operate independently; they need no catch-all supporting package. Humanizer lives in documentation without making prose editing a hard dependency of development. Use Humanizer when available; ordinary writing still proceeds without it. Writing-for-agents remains available locally for the retrospective workflow.

Shared framing and owned Markdown references are checked within each package. Development carries TASKS.md/WORKFLOW.md; documentation uses its own composition framing, as do strategy and operations. Optional methods are selected by capability, and no shared file outside the package is required. Keep the complete Humanizer, diagram/presentation/explorer, supply-chain scripts, AKS references, ADK pair and LangChain group. Moving an acquired skill changes its destination and may require adaptation changes, but its reviewed source pin, license and native controls remain authoritative.

Figma remains optional tooling declared by frontend-development; the React technical package has no inherited Figma endpoint. Tool availability and authorized file access are separate from installing interface methods. Distribution uses complete built plugins. The legacy symlink helper is a migration aid for local skills and does not establish package independence.

### Verification coverage

The assignment covers 78 local skills and 39 distinct acquired skills exactly once, with no omissions or duplicate owners.

All packages build together with `--all` and independently with explicit selection. Package checks verify inventories, local-resource parity, notices, required framing, and transitive owned Markdown links staying inside their bundle. CI also checks the default development-only build. These checks do not establish agent behavior; behavioral evaluations remain deferred.

### Capability-based composition

The [architecture guide](../architecture.md) owns the explanation of capability selection, outcome responsibility and absent-specialist fallback. Shared workflow instructions describe expertise rather than hardcoded cross-package skill names; local entry points use the same direction. Strategy and operations retain concise in-bundle composition framing. Required internal resources and retained upstream dependency groups remain precise references.

Absent guidance falls back to project evidence, general expertise and appropriate primary sources while keeping acceptance and verification standards. A concrete decision or unavailable execution target can block dependent work; a missing skill alone cannot. Client discovery and metadata support are observed capabilities, not assumptions. Packaging and installation are documented separately from behavioral routing/absence evidence.
