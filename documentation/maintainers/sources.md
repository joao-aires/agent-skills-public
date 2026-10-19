# Sources and compatibility

[Maintainer guide](../maintainer-reference.md) · [Catalogue](#upstream-catalogue) · [Adaptations](#adaptations) · [Matt selection](#matt-pocock-selection) · [Application references](#application-references) · [Capability architecture](#product-and-capability-architecture) · [Documentation methods](#documentation-methods)

## Upstream catalogue

For the collection-wide instruction review and retained objectives, see [guidance structure review](#guidance-structure-review).

The [lockfile](../../upstream.lock.json) owns exact commit/tree pins, licenses and adaptations. Built bundles include complete acquired skills and notices; source-only checkouts do not. I select sources for provenance, maintenance, licensing and fit with these workflows. Popularity is supporting evidence, not proof of correctness.

| Bundle | Source | Selected skills |
| --- | --- | --- |
| web-frontend | [Vercel](https://github.com/vercel-labs/agent-skills) | React best practices, composition patterns |
| web-frontend | [shadcn](https://github.com/shadcn-ui/ui/tree/main/skills/shadcn) | Official shadcn |
| web-frontend | [Wshobson](https://github.com/wshobson/agents/tree/46891e7e60da0e52baf1050b7b6391b64e84c6d9/plugins/frontend-mobile-development/skills/tailwind-design-system) | Tailwind design system (v4; preserve existing project versions) |
| development-workflow | [Matt Pocock](https://github.com/mattpocock/skills) | 18 curated engineering/productivity skills; [selection review](#matt-pocock-selection) |
| development-workflow | [Humanizer](https://github.com/blader/humanizer) | humanizer: edit prose across the lifecycle |
| development-workflow | [Microsoft Playwright](https://github.com/microsoft/playwright-cli) | playwright-cli |
| development-workflow | [GitHub awesome-copilot](https://github.com/github/awesome-copilot/tree/main/skills/github-actions-hardening) | GitHub Actions hardening |
| development-workflow | [Trail of Bits](https://github.com/trailofbits/skills) | property-based-testing, differential-review, supply-chain-risk-auditor |
| application-operations | [Microsoft Azure AKS-Skills](https://github.com/Azure/AKS-Skills/tree/20bf35201a79b324d2ca3e00e5c82020ff362024/skills/aks-cost-optimization) | aks-cost-optimization with its six references; applies only to AKS |
| python-backend | [Trail of Bits](https://github.com/trailofbits/skills/tree/main/plugins/modern-python) | modern-python |
| ai-development | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) | mcp-builder |
| ai-development | [Google ADK](https://github.com/google/adk-python/tree/main/.agents/skills) | adk-agent-builder, adk-architecture |
| ai-development | [LangChain](https://github.com/langchain-ai/langchain-skills) | langchain-fundamentals, langchain-dependencies, langgraph-fundamentals, langgraph-persistence |

## Adaptations

| Area | Packaged behavior or limitation |
| --- | --- |
| Frontend and Python | Pointers to local conventions; accepted project choices take precedence. Tailwind v4 is the new-project default; existing versions need no automatic migration. shadcn guidance applies to compatible installed primitives. |
| MCP and AI | Local framing prefers Python/standalone FastMCP for new servers and distinguishes it from MCP SDK examples. Existing choices remain authoritative; MCP-only work needs no LLM evaluation. |
| Matt workflows | Preserve dependency groups, resources and native controls. Add [workflow framing](../../plugins/development-workflow/WORKFLOW.md); tickets remain optional and setup is explicit. Map `docs/agents/` to `documentation/engineering/` and `docs/adr/` to `documentation/decisions/adr/`, respecting existing paths. |
| Targeted Matt changes | Remove stale setup prerequisites from three skills; give implement-spec a tracker-neutral description. Implement receives pointers to task, contribution and verification guidance without replacing its body. |
| Review and supply chain | differential-review uses its included method without an unavailable registered agent. The pinned supply-chain parser does not cover pnpm/yarn; missing coverage is not a clean audit. |
| AKS cost | Azure AKS only, with its six references. Other platforms use contextual first-party guidance. |
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

Implementation details and exceptions live beside [frontend conventions](../../plugins/web-frontend/skills/frontend-conventions/references/sources-and-exceptions.md) and [backend conventions](../../plugins/python-backend/skills/backend-conventions/references/sources-and-exceptions.md). First-party stack documentation supplies backend details; no unified official FastAPI/SQLAlchemy/Alembic skill is claimed. The target of avoiding reference lookup in 90 to 95% of routine uses remains unmeasured.

## Reference-only and excluded sources

| Source | Decision |
| --- | --- |
| [Vercel web-design-guidelines](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) | Reference only: no declared redistribution license at review and a floating guideline fetch. |
| [Amplitude analyze-feedback](https://github.com/amplitude/builder-skills/tree/51838c2d85560466d1bbc174ea0e645bb9c44ea9/analytics-skills/skills/analyze-feedback) | Reference only: Amplitude MCP dependency and no explicit redistribution license at the reviewed pin. No MCP is configured; the local feedback skill works with existing evidence. |
| Jezweb tailwind-v4-shadcn | Not acquired: directory absent at reviewed repository HEAD `1260fa7439b36b18dbf16648ccc7fb44783f6c23`; published setup was Vite-specific. |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Optional installed expertise, constrained by accepted UI direction. No private material is copied. |

Optional [shadcn MCP](https://ui.shadcn.com/docs/mcp) and [Playwright MCP](https://github.com/microsoft/playwright-mcp) require client setup. Hooks use [client extensions](https://agent-plugins.org/specification#8-client-extensions), not a portable hooks field. SigNoz is a replaceable local OTel preference; its [community support is best-effort](https://signoz.io/support/). Provider versions, resources and edition limits require contextual checks; operating/security guidance does not establish compliance.

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

My desktop default is TypeScript + Tauri. My initial mobile recommendation is React Native + Expo for a TypeScript team, compared with Flutter, Kotlin Multiplatform and native UI when constraints warrant. The [platform selection reference](../../plugins/web-frontend/skills/native-client-development/references/platform-selection.md) contains first-party sources and actual native verification boundaries. AI interfaces can use complementary [AG-UI/A2UI contracts](../../plugins/ai-development/skills/build-evaluated-ai/references/interaction-protocols.md); protocol/renderer versions and framework adapters must be checked together.

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

I separate the requested activity, reusable discipline and technical implementation. Activities own the engagement and stopping point; disciplines own decisions and evidence; technical conventions apply those decisions to an accepted stack. Role, applicability and invocation remain independent metadata dimensions. Plugins stay as useful delivery bundles rather than becoming one package per conceptual layer.

| Decision | Ownership and boundary |
| --- | --- |
| Business direction | Business-strategy retains its original strategic model and resources. |
| Product direction | Product-management owns problem evidence, priorities, useful scope, success signals and sequencing. Product-feedback owns evidence synthesis; refine owns engineering requirements. |
| System and service design | System-design owns architectural boundaries; backend-design owns service authority, state, failure and consumer contracts. Python conventions retain concrete runtime/persistence mechanics. |
| Interface design | Visual-design owns product-derived direction and token intent; interaction-design owns flows and coverage; interface-quality owns critique. React and native conventions implement these decisions with compatible primitives. |
| AI and protocols | Build-evaluated-ai owns provider-independent contracts, authority and evaluation. Ai-conventions owns Gemini/ADK/LangChain/FastMCP and concrete observability integration defaults. |
| Navigation | Workflow-help recommends activities; develop coordinates an explicitly requested engagement. TASKS.md links conditional methods and adapters from actual inventory. No global router or dependency engine is added. |

I reviewed Anthropic's product-brainstorming and roadmap-update skills at [33eeda1](https://github.com/anthropics/knowledge-work-plugins/tree/33eeda1e8fd856455b05479d13a0f85b5f803744/product-management/skills), under its [Apache-2.0 license](https://github.com/anthropics/knowledge-work-plugins/blob/33eeda1e8fd856455b05479d13a0f85b5f803744/LICENSE). They offer problem exploration, assumption testing, outcome-oriented roadmaps and dependency reasoning. Their larger workflow includes fixed ideation counts, connected-tool assumptions and suggested follow-ups that do not fit every bounded development request.

I also reviewed prioritize-features and identify-assumptions-new at [phuryn/pm-skills 07b34f6](https://github.com/phuryn/pm-skills/tree/07b34f64ee828df08953f505b7f747aef85ae7c6/pm-product-discovery/skills), under its [MIT license](https://github.com/phuryn/pm-skills/blob/07b34f64ee828df08953f505b7f747aef85ae7c6/LICENSE). They connect impact, effort, uncertainty and product risk, but prescribe a top-five result or a fixed eight-category treatment and introduce additional skill/framework dependencies. I keep these as reviewed references rather than import their orchestrations or scoring conventions. This is a scope and composition decision, not a demonstrated quality ranking.

The new product-management skill is original local guidance. It uses the accepted product outcomes and existing evidence/decision principles, with optional frameworks and no required research format, tracker, scoring formula or commercial study. No new upstream text/resources are acquired, and existing upstream pins, notices and native invocation controls remain unchanged. The same principle guides the visual/backend/AI ownership split: preserve useful technical invariants and explicit preferences without repeating an entire product process in each stack.

Independently installable bundles retain concise essential defaults and discover optional methods through the observed inventory. Missing guidance does not select another stack, authorize installation or eliminate required outcomes. I preserve the seven-phase lifecycle, project foundations, implementation/verification loop and consequential-decision policy. The refactor stops before behavioral architecture evaluation; repository checks do not establish improved routing or application outcomes.
