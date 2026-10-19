# Sources and compatibility

[Maintainer guide](../maintainer-reference.md) · [Catalogue](#upstream-catalogue) · [Adaptations](#adaptations) · [Matt selection](#matt-pocock-selection) · [Application references](#application-references) · [Capability architecture](#product-and-capability-architecture) · [Documentation methods](#documentation-methods) · [Target ownership](#target-plugin-ownership)

## Upstream catalogue

For the collection-wide instruction review and retained objectives, see [guidance structure review](#guidance-structure-review).

The [lockfile](../../upstream.lock.json) owns exact commit/tree pins, licenses and adaptations. Built bundles include complete acquired skills and notices; source-only checkouts do not. I select sources for provenance, maintenance, licensing and fit with these workflows. Popularity is supporting evidence, not proof of correctness.

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

Acquisition verifies tree pins and copies resources without executing upstream scripts. Built `UPSTREAM.json`, `UPSTREAM-NOTICES.json` and license files record provenance. Trail of Bits material is CC-BY-SA-4.0; other acquired sources are MIT or Apache-2.0 as recorded at their pins. Bundles have mixed-license notices. Embedded live links/commands can still change despite source pinning. Private installed content is never redistributed.

## Matt Pocock selection

I reviewed the 27 previously bundled skills at [the pinned revision](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d) and retained 18, including their dependencies. Exclusions keep this bundle focused; they do not judge upstream quality.

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

The review on 2026-10-11 covered manifests, official template code and published guidance, not complete architecture audits. No application code, assets or unlicensed skill content was copied. Historical popularity counts are omitted; reviewed revisions remain below.

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

[Anthropic frontend-design](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design) adds visual execution craft to frontend-development without choosing a framework. The requested claude-code plugin copy references an absent LICENSE.txt; that repository's root terms do not establish a redistribution grant. The reviewed anthropics/skills copy has identical skill text and an included Apache-2.0 LICENSE.txt, so that is the acquired source. Visual-design owns direction and handoff, interaction-design owns behavior, frontend-design supplies subject-grounded composition/typography/craft, and interface-quality owns rendered critique. Use craft guidance for new visual decisions or requested redesigns; preserve accepted tokens/components and avoid adding a new style or approval ceremony to routine changes. Deterministic accessibility, interactions and persisted behavior need their own verification.

The [skills directory](https://www.skills.sh/getsentry/skills/agents-md) reports meaningful adoption for agents-md, and [frontend-design](https://www.skills.sh/anthropics/skills/frontend-design) is widely installed. Adoption supports discovery; source review and applicable evidence determine fit. Neither acquisition establishes behavioral improvement; those trials remain deferred.

## AI development, testing and operations segmentation

The generic ai-development skill owns application patterns, architecture tradeoffs, model/context/tool and protocol decisions, deterministic authority, conceptual evaluation levels and operating outcomes. Its prior quality, speech and interaction guidance remains in the entry point and linked references. Matching implementation expertise is optional; no evaluator, instrumentation SDK or vendor is a generic dependency.

Python ai-testing owns DeepEval test-case/dataset/metric integration and bounded script/pytest-style CI execution. Python ai-operations owns compatible OpenTelemetry providers/instrumentors/exporters, context propagation, privacy controls and received-signal verification. AI-conventions retains provider and FastMCP integration. These three local technical skills share ai-python-development with the acquired mcp-builder, for four skills in total. Generic operational signal/SLO decisions remain with operations methods, and Collector/backend deployment remains with matching platform/tool guidance. A Python evaluation runner need not imply a Python application.

The [DeepEval evaluation guide](https://deepeval.com/docs/evaluation-introduction), [metrics](https://deepeval.com/docs/metrics-introduction) and [CI instructions](https://deepeval.com/docs/evaluation-unit-testing-in-ci-cd) informed the original testing skill. The official [DeepEval skills](https://github.com/confident-ai/deepeval/tree/main/skills) were reviewed but not acquired: their mandatory intake/synthetic-data generation, hosted-service preference and fixed iteration defaults do not fit this collection's scope and composition principles. API documentation remains the implementation authority; no hosted account or generation loop is imposed.

The original operations skill uses [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/), [exporters](https://opentelemetry.io/docs/languages/python/exporters/) and the selected [GenAI conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/). These are technical integration choices, not a generic monitoring-vendor preference. Traces describe execution; evaluations assess quality, even when a platform offers both. No SDK/backend or live evaluation was installed or exercised for this guidance change.

## Supplied operations and explorer skills

The supplied portable operations archive contributes local guidance under this repository's license. Its separate source-notes companion, private inventories, incident identities, internal skills, factory runtime and fixed schedules are excluded. Public primary references remain with the skills.

| Bundle | Integration |
| --- | --- |
| development-workflow | system-mapping and bash-engineering; delivery guidance merged into delivery-pipelines |
| python-backend | python-automation-engineering |
| application-operations | Reliability, telemetry, incident/runbook/postmortem, Kubernetes/JVM, vulnerabilities, credentials and housekeeping guidance; backup/recovery merged into protect-and-restore-data |
| visual-communication | Separately supplied system-flow-explorer, including renderer, validator, examples and checks; local adaptations add agent-selected initial depth and independent entity expansion in sequence/C4 views |

Platform boundaries and invocation labels remain explicit. Interactive postmortems and architecture explorers start only on request; static system discovery stays separate from the explorer artifact model. Numerical examples are contextual. The [SDLC map](../sdlc.md) owns the current coverage catalogue.

## System and client design choices

I retain the pinned Matt codebase-design and domain-modeling techniques for interfaces and domain concepts. I reviewed [wshobson architecture-patterns](https://github.com/wshobson/agents/blob/main/plugins/backend-development/skills/architecture-patterns/SKILL.md), a widely installed backend-pattern skill, but keep it reference-only: its prescribed Clean/Hexagonal/DDD structures are narrower than product-led system decisions. My local system-design skill coordinates outcomes, alternatives, boundaries, operating constraints and delivery across new products and feature changes; it does not copy the upstream body or change existing source pins.

My desktop default is TypeScript + Tauri. My initial mobile recommendation is React Native + Expo for a TypeScript team, compared with Flutter, Kotlin Multiplatform and native UI when constraints warrant. The [platform selection reference](../../plugins/frontend-native-development/skills/native-client-development/references/platform-selection.md) contains first-party sources and actual native verification boundaries. AI interfaces can use complementary [AG-UI/A2UI contracts](../../plugins/ai-development/skills/ai-development/references/interaction-protocols.md); protocol/renderer versions and framework adapters must be checked together.

## Figma community review

I reviewed the supplied Community entries on 2026-10-16. These are candidates and external references, not newly acquired skills or evidence of tool compatibility. The [official catalogue](https://www.figma.com/community/ai-skills?resource_type=skills) includes workflows for Figma's own agent; a familiar skill name does not establish compatibility with a coding-agent MCP client.

| Candidate | Fit and material limits | Current decision |
| --- | --- | --- |
| [better-interface](https://www.figma.com/community/skill/61238/better-interface) | Broad craft review with concrete runtime evidence; the Community version also writes annotation cards and prescribes exact motion values. [The author's MIT repository](https://github.com/jakubkrehel/skills) has a different orchestration version with six required domain owners. | First craft-review candidate. Review the complete dependency group at a pin and compare findings with the existing reviewer before acquisition; do not substitute the GitHub version for the Community version silently. |
| [usability-test-guide](https://www.figma.com/community/skill/71690/usability-test-guide) | Neha Kodi's selected-frame moderated discussion guide, with goal-based tasks and neutral probes; writes a guide frame. It prepares research rather than conducting it. | First research-planning candidate; external use pending clear reusable licensing and tool capability. |
| [analyze-components](https://www.figma.com/community/skill/61009/analyze-components) | Component/style/variable inventory, canvas audit document and repairs, including orphan/instance changes. Long host-specific script/layout guidance. | Targeted design-system maintenance only; separate inspection from authorized repair and verify instance/binding preservation. Not a read-only audit by default. |
| [spacing-audit](https://www.figma.com/community/skill/70410/spacing-audit) | Audits and adjusts a prescribed 4/8pt scale. Preserves token bindings and asks before changing a deliberate alternative scale. | Optional focused review; accepted project tokens/density remain authoritative. Not a universal new spacing standard. |
| [balise-ux-writing](https://www.figma.com/community/skill/64048/balise-ux-writing) | Scoped review/rewrite/generate/harmonize modes, preserves product meaning and avoids invented claims. [The author's repository](https://github.com/mrstev3n/balise-skills) declares Apache-2.0; Community and repository versions need comparison at a reviewed pin. | First microcopy candidate; review resources and target-host adapters before acquisition. |
| [superfuture-design-review](https://www.figma.com/community/skill/65434/superfuture-design-review) | Prioritized broad critique; its frontmatter is named design-review and it overlaps better-interface. Numeric craft preferences need contextual interpretation. | Compare as an alternative reviewer, not a second mandatory critique of every screen. |
| [desktop-to-mobile](https://www.figma.com/community/skill/72495/desktop-to-mobile) | Creates a separate 390px mobile frame and menu states, with prescribed stacking/type/navigation transformations. Preserves original frame and existing variants where possible. | Optional responsive exploration; it does not produce or validate native iOS/Android behavior, tablet coverage or arbitrary widths. |

Several entries display the [Community Free Resource License](https://www.figma.com/community-free-resource-license/), which restricts use to the Figma platform and does not grant the redistribution/adaptation rights needed here. I keep those as links; no Community instructions or scripts are bundled. The usability guide's rendered page did not establish a redistribution license. Separately licensed author repositories require their own revision, dependency, resource and behavioral review before acquisition. No license exception, account connection or canvas mutation was accepted during this review.

Figma's [official MCP guide](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/) owns endpoint and client support. The web-frontend declaration adds no guarantee of agy OAuth/tool compatibility. Official Figma skills are available from [mcp-server-guide](https://github.com/figma/mcp-server-guide); the reviewed tree did not expose a root license, so this change does not redistribute that material.

## Local UI/UX capability owners

I added interface-quality, ux-writing and usability-research as original local guidance under this repository's license. They implement the accepted requirements and failure boundaries: evidence-based inspection, contextual design, scoped copy changes, component/token preservation, neutral research tasks and honest observation status. No Community skill text, scripts, private installed content or new upstream resources were acquired.

The Community candidates above remain references. The MIT better-interface repository delegates to a six-skill group and differs from the canvas-writing Community version; acquiring that group would add overlapping ownership and dependency/control adaptation. The Apache-2.0 Balise source remains a possible future comparison, not a silently substituted owner. I chose concise local owners with shared user/agent access and host-independent evidence boundaries, retaining Figma as an optional surface. This is a scope decision, not a claim that local guidance outperforms those sources. A controlled behavioral comparison has not run.

## Documentation methods

I use documentation-writing for authoring quality and architecture-documentation for useful structural, runtime, interface and deployment explanations. Documentation-conventions owns authoritative records and upkeep; system-design owns design choices. These are original local skills; no upstream resources or invocation controls are imported.

The earlier PR #8 source review compared [Anthropic doc-coauthoring](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/doc-coauthoring/SKILL.md) and [GitHub documentation-writer](https://github.com/github/awesome-copilot/blob/8bc0f5715b2ddc7901a62fddf144ded30d56de8b/skills/documentation-writer/SKILL.md). Context gathering, reader questions, accuracy and terminology fit; mandatory collaboration/outline approvals do not fit routine authorized upkeep. No new popularity or source review is claimed by this integration. Diátaxis and Google technical writing inform the authoring method; C4, arc42 and OpenAPI inform architecture coverage. References remain with the skills and do not establish complete standards conformance.

## Guidance structure review

I reviewed the 55 local skill entry points and screened the 37 pinned upstream entry points and their adaptations for scope, instruction hierarchy and project fit. This review is about agent guidance; it does not revalidate every upstream API example, reference, tool or operational procedure. The pinned sources and native invocation controls remain unchanged.

| Area | Decision |
| --- | --- |
| Workflow activities | Keep short activity entry points. Develop, Design and Setup now point to the owners of verification, specialist methods and foundations rather than repeat their checklists. Other activity entries remain focused on their distinct outcomes. |
| Shared engineering support | Consolidate the acceptance/test/inspect/repair loop in deliver-reliable-changes and worktree/commit/PR mechanics in git-contributions. Keep foundation artifacts explicit in project-conventions. Journey-testing owns platform, fixture and component evidence. Preserve detailed performance, resilience, security and documentation methods where they change decisions. |
| Architecture and stacks | System-design derives dependency suitability from intended use, constraints and supported contracts. Move production migration and multi-instance hosting detail behind relevant triggers; keep transaction, authorization and compatibility invariants visible. AI-specific speech and collaboration details stay in their domain references. |
| UI/UX | Center interface review on applicability, evidence and verified recommendations. Keep measurement detail/tooling in its reference. Copy follows authoritative behavior and complete consequences; research protects neutral observation and justified inference. Interaction-design owns affected-surface reconciliation. |
| Strategy | Retain the original strategy model, references, templates and compatibility fallback. Reuse suitable existing thesis/decision records instead of creating parallel files solely to match default filenames. Product-feedback guidance already connects evidence to a bounded decision. |
| Visual artifacts | Retain the complete original HTML implementation guides and resources behind short brief-driven entry points. Their visual profiles are starting choices for the requested artifact. Keep the explorer's schema/renderer contract: its specificity protects an executable interface. |
| Operations | Retain domain-specific methods and invariants for incident response, recovery, credential rotation, reliability, observability, capacity/cost, Kubernetes, JVM work and vulnerability management. Their detail protects consequential operations. Correct a broken postmortem reference. |
| Upstream specialists | Preserve reviewed sources, licenses and dependency resources. Version-specific API examples remain specialist material. Local framing preserves accepted project choices; explicit upstream workflows retain their controls and are not automatically invoked to reproduce their whole ceremony. |

The refactor preserves new-project onboarding/checks/tests/containers/CI/artifact/release foundations, TypeScript/Tauri and conditional mobile choices, contextual visual direction, Storybook plus real-platform testing, architecture/usage-term decisions, AI/protocol/authority boundaries and evidence-based completion. Concrete regressions remain in the evaluation definitions; preserving those outcomes does not require preserving every warning sentence. [Evaluation evidence](evaluations.md#guidance-refactor-validation) distinguishes package checks from behavior still needing a fresh run.

## Product and capability architecture

The method separation and [plugin ownership](#target-plugin-ownership) below are implemented in PR #19. Structural independence has repository/build checks; behavioral adherence remains unverified.

I separate the requested activity, reusable discipline and technical implementation. Activities own the engagement and stopping point; disciplines own decisions and evidence; technical conventions apply those decisions to an accepted stack. Role, applicability and invocation remain independent metadata dimensions. Plugins stay as useful delivery bundles rather than becoming one package per conceptual layer.

| Decision | Ownership and boundary |
| --- | --- |
| Business direction | Business-strategy retains its original strategic model and resources. |
| Product direction | Product-management owns problem evidence, priorities, useful scope, success signals and sequencing. Product-feedback owns evidence synthesis; refine owns engineering requirements. |
| System and service design | System-design owns architectural boundaries; backend-design owns service authority, state, failure and consumer contracts. Python conventions retain concrete runtime/persistence mechanics. |
| Interface design | Visual-design owns product-derived direction and token intent; interaction-design owns flows and coverage; interface-quality owns critique. React and native conventions implement these decisions with compatible primitives. |
| AI and protocols | Build-evaluated-ai owns provider-independent contracts, authority and evaluation. Ai-conventions owns Python/Gemini/FastMCP integration; upstream specialists retain ADK/LangChain implementation. Selected telemetry/backend setup belongs to tooling-conventions. |
| Navigation | Workflow-help recommends activities; develop coordinates an explicitly requested engagement. TASKS.md describes needed expertise and matches available descriptions, preserving fallback when specialists are absent. No global router or dependency engine is added. |

I reviewed Anthropic's product-brainstorming and roadmap-update skills at [33eeda1](https://github.com/anthropics/knowledge-work-plugins/tree/33eeda1e8fd856455b05479d13a0f85b5f803744/product-management/skills), under its [Apache-2.0 license](https://github.com/anthropics/knowledge-work-plugins/blob/33eeda1e8fd856455b05479d13a0f85b5f803744/LICENSE). They offer problem exploration, assumption testing, outcome-oriented roadmaps and dependency reasoning. Their larger workflow includes fixed ideation counts, connected-tool assumptions and suggested follow-ups that do not fit every bounded development request.

I also reviewed prioritize-features and identify-assumptions-new at [phuryn/pm-skills 07b34f6](https://github.com/phuryn/pm-skills/tree/07b34f64ee828df08953f505b7f747aef85ae7c6/pm-product-discovery/skills), under its [MIT license](https://github.com/phuryn/pm-skills/blob/07b34f64ee828df08953f505b7f747aef85ae7c6/LICENSE). They connect impact, effort, uncertainty and product risk, but prescribe a top-five result or a fixed eight-category treatment and introduce additional skill/framework dependencies. I keep these as reviewed references rather than import their orchestrations or scoring conventions. This is a scope and composition decision, not a demonstrated quality ranking.

The new product-management skill is original local guidance. It uses the accepted product outcomes and existing evidence/decision principles, with optional frameworks and no required research format, tracker, scoring formula or commercial study. No new upstream sources are acquired; reviewed pins, licenses, complete resources and native invocation controls are retained. Notices record the new destinations and scoped framing. The same principle guides the visual/backend/AI ownership split: preserve useful technical invariants and explicit preferences without repeating an entire product process in each stack.

Independently installable bundles retain concise essential defaults and discover optional methods through the observed inventory. Missing guidance does not select another stack, authorize installation or eliminate required outcomes. I preserve the seven-phase lifecycle, project foundations, implementation/verification loop and consequential-decision policy. The refactor stops before behavioral architecture evaluation; repository checks do not establish improved routing or application outcomes.

<a id="target-plugin-ownership"></a>

## Plugin ownership

The collection has 17 independent packages and 101 skills: 62 local and 39 acquired. Development is the default build; nine generic packages contain no stack-specific skills, and eight technical packages are explicitly selected. Source commit/tree pins, original resource groups and native invocation controls are preserved. Acquisition destinations follow the owners below; Humanizer uses documentation-local composition framing and the Python MCP wrapper uses Python-local conventions.

A plugin represents a useful installation choice. Workflow, application discipline and supporting capability describe its purpose; generic versus technical describes its applicability. These groups do not impose an execution order or dependencies. Installing a technical package makes expertise available without accepting its technology for a project. Keep accepted choices, select matching guidance from actual inventory and retain useful outcomes when optional specialists are absent.

### Package boundaries

The collection has nine generic capability packages and eight optional technical packages. These replace seven mixed bundles to provide independent choices. I group specialist tools and operating platforms into two explicit optional packages rather than create a plugin for every tool. Split those further only when independent installation is useful. No empty placeholder packages are planned.

| Plugin | Applicability | Skills | Responsibility |
| --- | --- | --- | --- |
| `strategy` | Generic | 4 | Business direction, product priorities and evidence-based feedback. |
| `development` | Generic | 41 | SDLC engagements, project foundations, contribution flow and verification; usable without stack packages. |
| `operations` | Generic | 12 | Service reliability, signals, incidents, recovery, capacity and security upkeep. |
| `frontend-development` | Generic | 6 | Experience and interface methods across web, desktop and mobile. |
| `backend-development` | Generic | 1 | Service authority, state, failure, durable work and consumer contracts. |
| `ai-development` | Generic | 1 | AI application/task design, evaluation, interaction/protocol contracts and authority across client/service boundaries. |
| `delivery` | Generic | 1 | CI/release/deployment methods, immutable artifacts, promotion, compatibility and recovery. |
| `documentation` | Generic support | 4 | Writing, architecture explanation, knowledge organization and prose editing. |
| `visualization` | Generic support | 3 | Diagrams, presentations and interactive system explanation; preserve executable resources. |
| `backend-python-development` | Technical | 3 | Python/FastAPI/persistence and Python automation; no backend service required for CLI work. |
| `frontend-reactjs-development` | Technical | 5 | React/Next.js/shadcn/Tailwind and their actual component APIs. |
| `frontend-native-development` | Technical | 1 | TypeScript/Tauri and React Native/Expo, platform lifecycle, packaging and native drivers. |
| `ai-adk-development` | Technical | 2 | Google ADK; preserve the paired architecture/builder skills. |
| `ai-langchain-development` | Technical | 4 | LangChain/LangGraph and dependencies/persistence as a complete group. |
| `ai-python-development` | Technical | 4 | Python provider/FastMCP adapters, DeepEval evaluation suites and OpenTelemetry AI instrumentation; no required agent framework or hosted backend. |
| `development-tooling` | Technical | 6 | Optional Bash, browser/load testing, delivery/configuration tooling and lockfile audit implementations. |
| `operations-platforms` | Technical | 3 | Optional JVM, Kubernetes and AKS expertise; match each skill independently to the actual platform. |

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

### Content that needs separating

Each skill has one owner. Generic methods and technical implementation now occupy separate packages:

| Current content | Generic owner | Technical owner |
| --- | --- | --- |
| project-conventions and its quality/local-environment references | development: foundation contracts, isolation/readiness and check-selection principles | Language defaults to matching stacks; Compose, hook/checker configuration and preferred diagnostics setup to development-tooling |
| delivery-pipelines and artifact/workflow references | delivery: verification, artifact identity, promotion, authorization and recovery | development-tooling: GitHub Actions/GHCR/container mechanics; ecosystem packaging mechanics to matching stacks |
| ai-conventions | ai-development: only provider-independent task/authority/evaluation and framework-selection reasoning | ai-python-development: Python/Gemini/FastMCP mechanics; ADK and LangChain implementations to their packages |
| ai-development and evaluation/interaction references | ai-development: AI task/model/context/tool decisions, skills and harness integration, protocol selection, deterministic authority, quality evidence and operating lifecycle | SDK/renderer integration to matching AI/frontend packages; backend/dashboard setup to development-tooling |
| native-client-development | frontend-development: experience needs; development/system-design: consequential platform choice | frontend-native-development: Tauri/Expo/native lifecycle and driver implementation |
| observability-operations and related local/AI references | operations: trustworthy outcome signals, collection/privacy/failure boundaries | development-tooling: selected Collector/backend deployment; language-specific instrumentation to matching stacks |
| performance-testing, journey-testing, resilience-testing and quality examples | development: meaningful workload/journey/fault evidence and execution scope | development-tooling: k6, Playwright and concrete checker commands; native drivers to frontend-native-development |

Existing personal preferences remain available in explicitly selected technical guidance or project instructions; they stop being universal generic defaults. AG-UI/A2UI and OpenTelemetry can remain conditional interoperability choices in methods, but implementation instructions must match accepted protocols and installed versions. The technical toolkit retains selected GitHub/GHCR, Compose, SigNoz/Langfuse and checker preferences as conditional implementation guidance. No new upstream tools are acquired.

### Complete existing-skill assignment

Each row has one current owner. Local links lead to the current source; upstream links lead to the exact acquired revision. Preserve every skill's complete resources, licenses, native controls and scope. The dispositions record the separation of method outcomes from technical implementation; each package is checked independently.

<details>
<summary>All 101 skills and their current owners</summary>

| Skill | Origin | Previous bundle | Current plugin | Disposition |
| --- | --- | --- | --- | --- |
| [business-opportunity-analysis](../../plugins/strategy/skills/business-opportunity-analysis/SKILL.md) | Local | business-strategy | `strategy` | Retain compatibility entry and resources; prefer business-strategy for new work. |
| [business-strategy](../../plugins/strategy/skills/business-strategy/SKILL.md) | Local | business-strategy | `strategy` | Retain method and resources. |
| [learn-from-product-feedback](../../plugins/strategy/skills/learn-from-product-feedback/SKILL.md) | Local | business-strategy | `strategy` | Retain method and resources. |
| [product-management](../../plugins/strategy/skills/product-management/SKILL.md) | Local | business-strategy | `strategy` | Retain method and resources. |
| [agents-md](https://github.com/getsentry/skills/tree/f57ada2d0b640406ea7e25b11d636c530e77c58b/skills/agents-md) | Upstream | New addition | `development` | Repository-instruction authoring with scoped, evidence-backed guidance. |
| [code-review](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/code-review) | Upstream | development-workflow | `development` | Retain method and resources. |
| [codebase-design](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/codebase-design) | Upstream | development-workflow | `development` | Retain method and resources. |
| [deliver-reliable-changes](../../plugins/development/skills/deliver-reliable-changes/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [dependencies](../../plugins/development/skills/dependencies/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [design](../../plugins/development/skills/design/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [develop](../../plugins/development/skills/develop/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [diagnosing-bugs](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/diagnosing-bugs) | Upstream | development-workflow | `development` | Retain method and resources. |
| [differential-review](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/differential-review/skills/differential-review) | Upstream | development-workflow | `development` | Retain method and resources. |
| [domain-modeling](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/domain-modeling) | Upstream | development-workflow | `development` | Retain method and resources. |
| [git-contributions](../../plugins/development/skills/git-contributions/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [grill-me](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/grill-me) | Upstream | development-workflow | `development` | Retain method and resources. |
| [grill-with-docs](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/grill-with-docs) | Upstream | development-workflow | `development` | Retain method and resources. |
| [grilling](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/grilling) | Upstream | development-workflow | `development` | Retain method and resources. |
| [handoff](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/handoff) | Upstream | development-workflow | `development` | Retain method and resources. |
| [harden](../../plugins/development/skills/harden/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [implement](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/implement) | Upstream | development-workflow | `development` | Retain method and resources. |
| [implement-spec](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/implement-spec) | Upstream | development-workflow | `development` | Retain method and resources. |
| [improve](../../plugins/development/skills/improve/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [improve-codebase-architecture](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/improve-codebase-architecture) | Upstream | development-workflow | `development` | Retain method and resources. |
| [journey-testing](../../plugins/development/skills/journey-testing/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [plan](../../plugins/development/skills/plan/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [project-conventions](../../plugins/development/skills/project-conventions/SKILL.md) | Local | development-workflow | `development` | Separate: retain foundation outcomes; move language, tooling and local-service defaults. |
| [property-based-testing](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/property-based-testing/skills/property-based-testing) | Upstream | development-workflow | `development` | Retain method and resources. |
| [prototype](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/prototype) | Upstream | development-workflow | `development` | Retain method and resources. |
| [refine](../../plugins/development/skills/refine/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [release](../../plugins/development/skills/release/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [research](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/research) | Upstream | development-workflow | `development` | Retain method and resources. |
| [resilience-testing](../../plugins/development/skills/resilience-testing/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [retro](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/retro) | Upstream | development-workflow | `development` | Retain method and resources. |
| [review](../../plugins/development/skills/review/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [security-and-privacy-design](../../plugins/development/skills/security-and-privacy-design/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [setup](../../plugins/development/skills/setup/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [system-design](../../plugins/development/skills/system-design/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [system-mapping](../../plugins/development/skills/system-mapping/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [tdd](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/tdd) | Upstream | development-workflow | `development` | Retain method and resources. |
| [test](../../plugins/development/skills/test/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [to-questionnaire](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/to-questionnaire) | Upstream | development-workflow | `development` | Retain method and resources. |
| [to-spec](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/to-spec) | Upstream | development-workflow | `development` | Retain method and resources. |
| [workflow-help](../../plugins/development/skills/workflow-help/SKILL.md) | Local | development-workflow | `development` | Retain method and resources. |
| [writing-for-agents](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/productivity/writing-for-agents) | Upstream | development-workflow | `development` | Retain method and resources. |
| [credential-lifecycle](../../plugins/operations/skills/credential-lifecycle/SKILL.md) | Local | application-operations | `operations` | Retain method and resources. |
| [incident-response](../../plugins/operations/skills/incident-response/SKILL.md) | Local | application-operations | `operations` | Retain method and resources. |
| [observability-operations](../../plugins/operations/skills/observability-operations/SKILL.md) | Local | application-operations | `operations` | Separate: retain signal contracts/operations; move backend installation and preferred-vendor configuration. |
| [operational-housekeeping](../../plugins/operations/skills/operational-housekeeping/SKILL.md) | Local | application-operations | `operations` | Retain method and resources. |
| [optimize-application-cost](../../plugins/operations/skills/optimize-application-cost/SKILL.md) | Local | application-operations | `operations` | Retain method and resources. |
| [plan-application-capacity](../../plugins/operations/skills/plan-application-capacity/SKILL.md) | Local | application-operations | `operations` | Retain method and resources. |
| [postmortem-facilitation](../../plugins/operations/skills/postmortem-facilitation/SKILL.md) | Local | application-operations | `operations` | Retain method and resources. |
| [postmortem-followup](../../plugins/operations/skills/postmortem-followup/SKILL.md) | Local | application-operations | `operations` | Retain method and resources. |
| [protect-and-restore-data](../../plugins/operations/skills/protect-and-restore-data/SKILL.md) | Local | application-operations | `operations` | Retain method and resources. |
| [reliability-design](../../plugins/operations/skills/reliability-design/SKILL.md) | Local | application-operations | `operations` | Retain method and resources. |
| [runbook-engineering](../../plugins/operations/skills/runbook-engineering/SKILL.md) | Local | application-operations | `operations` | Retain method and resources. |
| [vulnerability-management](../../plugins/operations/skills/vulnerability-management/SKILL.md) | Local | application-operations | `operations` | Retain method and resources. |
| [interaction-design](../../plugins/frontend-development/skills/interaction-design/SKILL.md) | Local | web-frontend | `frontend-development` | Retain method and resources. |
| [interface-quality](../../plugins/frontend-development/skills/interface-quality/SKILL.md) | Local | web-frontend | `frontend-development` | Retain method and resources. |
| [usability-research](../../plugins/frontend-development/skills/usability-research/SKILL.md) | Local | web-frontend | `frontend-development` | Retain method and resources. |
| [ux-writing](../../plugins/frontend-development/skills/ux-writing/SKILL.md) | Local | web-frontend | `frontend-development` | Retain method and resources. |
| [frontend-design](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design) | Upstream | New addition | `frontend-development` | Visual craft within accepted direction and scope. |
| [visual-design](../../plugins/frontend-development/skills/visual-design/SKILL.md) | Local | web-frontend | `frontend-development` | Retain method and resources. |
| [backend-design](../../plugins/backend-development/skills/backend-design/SKILL.md) | Local | development-workflow | `backend-development` | Retain method and resources. |
| [ai-development](../../plugins/ai-development/skills/ai-development/SKILL.md) | Local | ai-development | `ai-development` | Rename and broaden AI application development; retain authority/evaluation and interaction contracts, with vendor APIs in technical packages. |
| [delivery-pipelines](../../plugins/delivery/skills/delivery-pipelines/SKILL.md) | Local | development-workflow | `delivery` | Separate: retain delivery contracts; move provider/container/registry implementation. |
| [architecture-documentation](../../plugins/documentation/skills/architecture-documentation/SKILL.md) | Local | development-workflow | `documentation` | Retain method and resources. |
| [documentation-conventions](../../plugins/documentation/skills/documentation-conventions/SKILL.md) | Local | development-workflow | `documentation` | Retain method and resources. |
| [documentation-writing](../../plugins/documentation/skills/documentation-writing/SKILL.md) | Local | development-workflow | `documentation` | Retain method and resources. |
| [humanizer](https://github.com/blader/humanizer/tree/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8) | Upstream | development-workflow | `documentation` | Retain method and resources. |
| [architecture-diagramming](../../plugins/visualization/skills/architecture-diagramming/SKILL.md) | Local | visual-communication | `visualization` | Retain method and resources. |
| [presentation-building](../../plugins/visualization/skills/presentation-building/SKILL.md) | Local | visual-communication | `visualization` | Retain method and resources. |
| [system-flow-explorer](../../plugins/visualization/skills/system-flow-explorer/SKILL.md) | Local | visual-communication | `visualization` | Retain method and resources. |
| [backend-conventions](../../plugins/backend-python-development/skills/backend-conventions/SKILL.md) | Local | python-backend | `backend-python-development` | Retain Python mechanics; shared service decisions stay in backend-development. |
| [modern-python](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/modern-python/skills/modern-python) | Upstream | python-backend | `backend-python-development` | Retain matching technical implementation and resources. |
| [python-automation-engineering](../../plugins/backend-python-development/skills/python-automation-engineering/SKILL.md) | Local | python-backend | `backend-python-development` | Retain Python automation; use outside backend services remains supported. |
| [frontend-conventions](../../plugins/frontend-reactjs-development/skills/frontend-conventions/SKILL.md) | Local | web-frontend | `frontend-reactjs-development` | Retain React mechanics; shared visual/interaction decisions stay in frontend-development. |
| [shadcn](https://github.com/shadcn-ui/ui/tree/6b600cf1ff42f8a746747ea587e52af3ee224643/skills/shadcn) | Upstream | web-frontend | `frontend-reactjs-development` | Retain matching technical implementation and resources. |
| [tailwind-design-system](https://github.com/wshobson/agents/tree/46891e7e60da0e52baf1050b7b6391b64e84c6d9/plugins/frontend-mobile-development/skills/tailwind-design-system) | Upstream | web-frontend | `frontend-reactjs-development` | Retain matching technical implementation and resources. |
| [vercel-composition-patterns](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/composition-patterns) | Upstream | web-frontend | `frontend-reactjs-development` | Retain matching technical implementation and resources. |
| [vercel-react-best-practices](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices) | Upstream | web-frontend | `frontend-reactjs-development` | Retain matching technical implementation and resources. |
| [native-client-development](../../plugins/frontend-native-development/skills/native-client-development/SKILL.md) | Local | web-frontend | `frontend-native-development` | Separate: keep native implementation; framework-neutral experience decisions stay in frontend-development. |
| [adk-agent-builder](https://github.com/google/adk-python/tree/6be386d8939c4898aa2c0fc8a1f7cb34e7df7904/.agents/skills/adk-agent-builder) | Upstream | ai-development | `ai-adk-development` | Retain matching technical implementation and resources. |
| [adk-architecture](https://github.com/google/adk-python/tree/6be386d8939c4898aa2c0fc8a1f7cb34e7df7904/.agents/skills/adk-architecture) | Upstream | ai-development | `ai-adk-development` | Retain matching technical implementation and resources. |
| [langchain-dependencies](https://github.com/langchain-ai/langchain-skills/tree/16a992f09ab3ccfb642dd4f08d350d833d1990bf/config/skills/langchain-dependencies) | Upstream | ai-development | `ai-langchain-development` | Retain matching technical implementation and resources. |
| [langchain-fundamentals](https://github.com/langchain-ai/langchain-skills/tree/16a992f09ab3ccfb642dd4f08d350d833d1990bf/config/skills/langchain-fundamentals) | Upstream | ai-development | `ai-langchain-development` | Retain matching technical implementation and resources. |
| [langgraph-fundamentals](https://github.com/langchain-ai/langchain-skills/tree/16a992f09ab3ccfb642dd4f08d350d833d1990bf/config/skills/langgraph-fundamentals) | Upstream | ai-development | `ai-langchain-development` | Retain matching technical implementation and resources. |
| [langgraph-persistence](https://github.com/langchain-ai/langchain-skills/tree/16a992f09ab3ccfb642dd4f08d350d833d1990bf/config/skills/langgraph-persistence) | Upstream | ai-development | `ai-langchain-development` | Retain matching technical implementation and resources. |
| [ai-testing](../../plugins/ai-python-development/skills/ai-testing/SKILL.md) | Local | New addition | `ai-python-development` | Python DeepEval evaluation integration; generic acceptance stays outside the adapter. |
| [ai-operations](../../plugins/ai-python-development/skills/ai-operations/SKILL.md) | Local | New addition | `ai-python-development` | Python OpenTelemetry AI instrumentation and export verification. |
| [ai-conventions](../../plugins/ai-python-development/skills/ai-conventions/SKILL.md) | Local | ai-development | `ai-python-development` | Separate: keep Python/provider/MCP mechanics here; ADK and LangChain mechanics go to their own packages. |
| [mcp-builder](https://github.com/anthropics/skills/tree/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/mcp-builder) | Upstream | ai-development | `ai-python-development` | Retain complete acquired resources and native controls; protocol outcomes stay in ai-development. |
| [bash-engineering](../../plugins/development-tooling/skills/bash-engineering/SKILL.md) | Local | development-workflow | `development-tooling` | Retain matching technical implementation and resources. |
| [github-actions-hardening](https://github.com/github/awesome-copilot/tree/143a3d976b3c1603cc8932984d5e1f28501cb5fc/skills/github-actions-hardening) | Upstream | development-workflow | `development-tooling` | Retain GitHub Actions mechanics; delivery contracts stay in delivery. |
| [performance-testing](../../plugins/development-tooling/skills/performance-testing/SKILL.md) | Local | development-workflow | `development-tooling` | Retain k6 implementation; journey/verification decisions stay in development. |
| [playwright-cli](https://github.com/microsoft/playwright-cli/tree/b85c7a736bb473bf55b584e54a09ffa698d6d871/skills/playwright-cli) | Upstream | development-workflow | `development-tooling` | Retain matching technical implementation and resources. |
| [supply-chain-risk-auditor](https://github.com/trailofbits/skills/tree/82fe8226252622fa807643bdca1710901198553a/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor) | Upstream | development-workflow | `development-tooling` | Retain scripts and supported-lockfile limits; risk priority stays in dependencies/vulnerability-management. |
| [tooling-conventions](../../plugins/development-tooling/skills/tooling-conventions/SKILL.md) | Local | development-workflow | `development-tooling` | Added in task 2: owns selected CI/container/registry/checker/telemetry and web-driver implementation references. |
| [aks-cost-optimization](https://github.com/Azure/AKS-Skills/tree/20bf35201a79b324d2ca3e00e5c82020ff362024/skills/aks-cost-optimization) | Upstream | application-operations | `operations-platforms` | AKS only; retain all six references and platform limits. |
| [infra-jvm-optimization](../../plugins/operations-platforms/skills/infra-jvm-optimization/SKILL.md) | Local | application-operations | `operations-platforms` | JVM only; Kubernetes examples require matching infrastructure. |
| [kubernetes-resource-engineering](../../plugins/operations-platforms/skills/kubernetes-resource-engineering/SKILL.md) | Local | application-operations | `operations-platforms` | Kubernetes only; no platform adoption implied. |

</details>

### Resource and invocation closure

Keep the 18 retained Matt skills together in development, including their research, interview, domain-modeling, implementation, review, retrospective and writing-for-agents dependencies. These supporting techniques help that workflow operate independently; they need no catch-all supporting package. Humanizer lives in documentation without making prose editing a hard dependency of development. Use Humanizer when available; ordinary writing still proceeds without it. Writing-for-agents remains available locally for the retrospective workflow.

Shared framing and owned Markdown references are checked within each package. Development carries TASKS.md/WORKFLOW.md; documentation uses its own composition framing, as do strategy and operations. Optional methods are selected by capability, and no shared file outside the package is required. Keep the complete Humanizer, diagram/presentation/explorer, supply-chain scripts, AKS references, ADK pair and LangChain group. Moving an acquired skill changes its destination and may require adaptation changes, but its reviewed source pin, license and native controls remain authoritative.

Figma remains optional tooling declared by frontend-development; the React technical package has no inherited Figma endpoint. Tool availability and authorized file access are separate from installing interface methods. A new skills-only distribution was removed from the plan; the legacy symlink helper remains a migration aid and does not establish package independence.

### Inventory coverage and next boundary

The assignment covers 62 local skills and 39 distinct acquired skills exactly once, with no omissions or duplicate owners.

All packages build together with `--all` and independently with explicit selection. Package checks verify inventories, local-resource parity, notices, required framing, and transitive owned Markdown links staying inside their bundle. CI also checks the default development-only build. These checks do not establish agent behavior; behavioral evaluations remain deferred.

### Task-2 content separation

Project conventions now own foundation outcomes without choosing an application language, CI provider, container engine or telemetry vendor. Delivery pipelines retain promotion/trust/recovery contracts and discover optional implementation guidance. Tooling-conventions owns the moved quality, local-environment, workflow, artifact and telemetry-backend references, with container, browser and failure-tool details. Language lint defaults remain in their accepted stack owners.

AI methods retain provider-independent selection, deterministic authority, evaluation and protocol evidence. Concrete Python/provider APIs and versioned interaction examples live in ai-conventions; the paired ADK skills and complete LangChain group remain unchanged. Interface methods retain platform-independent behavior, while native-client-development owns compatible drivers and native implementation without requiring a Python backend. Observability retains signal outcomes with no preferred backend. Journey/resilience methods retain application/platform evidence and general workload/failure reasoning, with actual tool setup conditional.

The separation adds one technical supporting skill and moves resources, without changing existing names/native controls, source pins, acquisition adaptations or behavioral cases. The subsequent package move provides the development-only build and explicit technical selections. Behavioral evaluations remain deferred.

### Capability-based composition

The [architecture guide](../architecture.md) owns the explanation of capability selection, outcome responsibility and absent-specialist fallback. Shared workflow instructions describe expertise rather than hardcoded cross-package skill names; local entry points use the same direction. Strategy and operations retain concise in-bundle composition framing. Required internal resources and retained upstream dependency groups remain precise references.

Absent guidance falls back to project evidence, general expertise and appropriate primary sources while keeping acceptance and verification standards. A concrete decision or unavailable execution target can block dependent work; a missing skill alone cannot. Client discovery and metadata support are observed capabilities, not assumptions. The package moves and plugin-only onboarding are implemented; behavioral routing/absence comparisons are deferred.
