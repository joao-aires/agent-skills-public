# Maintainer reference

Source selection, acquisition rules and validation evidence for this repository. For installation and skill use, start with [usage](usage.md); for coverage, use the [SDLC map](sdlc.md).

- [Upstream catalogue](#upstream-catalogue): bundled sources, licenses and adaptations.
- [Source selection](#source-selection): reference applications and compatibility decisions.
- [Matt Pocock selection](#matt-pocock-selection): each retained or excluded skill.
- [Maintaining the collection](#maintaining-the-collection): update and validation checks.

## Upstream catalogue

Built plugins include the sources below at the commit/tree pins in [upstream.lock.json](../upstream.lock.json), with complete resources and license notices. Local-only checkouts do not contain acquired upstream skills. Sources are selected for provenance and fit; see [source selection](#source-selection) for adoption evidence and exclusions.

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

### How they fit my conventions

- Follow local guidance and accepted project choices. Frontend sources receive a `frontend-conventions` pointer; Python tooling receives a `backend-conventions` pointer. MCP builder receives AI/MCP framing, including Python/standalone FastMCP preference and the SDK distinction.
- The curated Matt set retains the dependencies of its interview, implementation, design and retrospective skills. Router, tracker and unrelated workspace workflows are excluded; see the selection review. They retain their invocation metadata and receive a pointer to [workflow framing](../plugins/development-workflow/WORKFLOW.md). Tickets are optional; setup runs only on request.
- Matt's built documentation paths map `docs/agents/` to `documentation/engineering/` and `docs/adr/` to `documentation/decisions/adr/`. Existing project paths remain authoritative. Three retained skills have stale setup prerequisites removed; tracker operations remain explicitly requested.
- `differential-review` uses its included adversarial methodology rather than dispatching an unavailable registered agent. `supply-chain-risk-auditor` retains its scripts/lockfile; its pinned parser does not cover pnpm/yarn, so missing coverage is not a clean audit.
- AKS cost guidance applies only to Azure AKS. General operations skills select the actual cloud/service and its current first-party documentation; they do not import an operator runtime or assume one platform.

The lockfile and built notices record adaptations and usage labels. Standard `metadata.scope`, `metadata.stack` and `metadata.invocation` describe applicability and preferred use without changing native controls. Packaging checks hashes and copies resources without running scripts. Pinning the source leaves embedded live documentation and commands free to change. Trail of Bits skills are CC-BY-SA-4.0; other included sources are MIT or Apache-2.0 as recorded at their pins. Built bundles carry mixed-license notices; private installed material is not redistributed.

### Additional references

- [Git worktrees](https://git-scm.com/docs/git-worktree), [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) and [GitHub CLI PR creation](https://cli.github.com/manual/gh_pr_create): contribution mechanics used by the local `contribute-code` skill; no additional MCP server is required.
- [Next.js agent guidance](https://github.com/vercel/next.js/tree/canary/skills): use documentation matching the application's chosen release.
- [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) and [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design): optional design guidance, constrained by existing tokens and direction. Reuse installed skills without copying private content.
- [Vercel web-design-guidelines](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines): reference only; the reviewed source did not declare a redistribution license and fetched floating guidance.
- [FastAPI](https://fastapi.tiangolo.com/), [Uvicorn](https://www.uvicorn.org/), [uv](https://docs.astral.sh/uv/), [SQLAlchemy](https://docs.sqlalchemy.org/en/20/), [Alembic](https://alembic.sqlalchemy.org/), [PostgreSQL](https://www.postgresql.org/docs/) and [FastMCP](https://gofastmcp.com/): first-party implementation documentation; no unified official skill for this entire backend stack is claimed.
- [Gemini audio](https://ai.google.dev/gemini-api/docs/audio), [pricing](https://ai.google.dev/gemini-api/docs/pricing) and [quotas](https://ai.google.dev/gemini-api/docs/rate-limits): verify the actual model and account before live tests.
- [C4](https://c4model.com/), [arc42](https://arc42.org/overview/), [MADR](https://adr.github.io/madr/) and [AGENTS.md](https://agents.md/): lightweight structures for project knowledge and scoped instructions.
- [shadcn MCP](https://ui.shadcn.com/docs/mcp) and [Playwright MCP](https://github.com/microsoft/playwright-mcp): optional live tools configured in the chosen client. Hooks use [client-specific extensions](https://agent-plugins.org/specification#8-client-extensions), not a portable hooks field.

### Reference-only selections

[Amplitude analyze-feedback](https://github.com/amplitude/builder-skills/tree/51838c2d85560466d1bbc174ea0e645bb9c44ea9/analytics-skills/skills/analyze-feedback) depends on Amplitude MCP and had no explicit redistribution license at the reviewed pin. It is not acquired or configured; my feedback guide works with existing evidence. Vercel web-design-guidelines is also reference-only for its undeclared redistribution license and floating guideline fetch.

The operations skills link to PostgreSQL, Kubernetes, CloudNativePG, Velero and cloud-provider docs for contextual implementation. Security guidance uses OWASP and applicable authoritative privacy rules; it does not establish compliance. The [SDLC mapping](sdlc.md) follows a seven-phase split; different models may group planning and analysis together.

## Source selection

Reviewed on 2026-10-11. Repository stars and skills.sh installs indicate adoption. I also consider official maintenance, production patterns, source availability and licenses; popularity alone cannot establish correctness. The guides cover everyday decisions inline and link to details for exceptions. I aim to avoid reference lookup in 90 to 95% of routine uses. That rate has not been measured.

Official shadcn had about 100.7k skills.sh installs at review, and Wshobson's Tailwind design-system skill about 68k (its repository had about 40.4k stars). Both are MIT-licensed. Vercel provides first-party React/composition guidance; the backend uses official implementation docs and the existing Python/MCP specialists rather than an unverified omnibus skill. Upstream pins and licenses are in the lockfile.

### Application references

The review covered dependency manifests, official template code and published guidance. It did not audit whole architectures or copy application code, assets or unlicensed skill content.

| Source | Reviewed revision | Evidence and limits |
| --- | --- | --- |
| [Dub](https://github.com/dubinc/dub) (~24.9k stars) | `bc7eeb882ead4652ed375545db81bb79b72137e8` | Next.js/React, Tailwind v3, Radix, table/form primitives. Evidence that mature applications need not migrate to v4 to follow coherent conventions. |
| [Cal.diy](https://github.com/calcom/cal.diy) (~48.9k stars; redirect from cal.com) | `54343aa685ae8f33159d2f485ec4a57bad5c574a` | Next.js, Tailwind v4 and reusable UI packages. Reference only; do not transplant scheduling-specific architecture. |
| [Supabase Studio](https://github.com/supabase/supabase/tree/master/apps/studio) (~111.4k repository stars) | `8617532ae1a41571d5d557cd24c6f5f2565d9230` | Tailwind/Radix, tables/forms and multiple framework paths. Repository adoption does not measure Studio usage; not a prescription for its backend scale. |
| [FastAPI full-stack template](https://github.com/fastapi/full-stack-fastapi-template) (~45.9k stars) | `7257e606cb94eada1dca40173e2b7f99dd549bc6` | First-party auth, sessions and full-stack integration. Uses SQLModel and Vite; my SQLAlchemy/Next.js defaults remain explicit. |
| [FastAPI best practices](https://github.com/zhanymkanov/fastapi-best-practices) (~18.2k stars) | `5e00aa6095521f0d00e4eec2ef0afa44cd566af4` | Domain organization, blocking/async distinctions and production cautions. Community reference, not a package; no redistribution license assumed. |

Authoritative details are linked within each skill's `references/sources-and-exceptions.md`: Next.js, Tailwind, shadcn, SQLAlchemy, Alembic, PostgreSQL, FastAPI, OWASP, AI providers and FastMCP. Generic guidance remains local so agents do not need to reconstruct the conventions from these sites.

### Exclusions

- Jezweb's `tailwind-v4-shadcn` listing exists on skills.sh, but the directory is absent at the reviewed repository HEAD (`1260fa7439b36b18dbf16648ccc7fb44783f6c23`) and its published setup is Vite-specific. It was not acquired or used as a Next.js setup recipe.
- Vercel `web-design-guidelines` fetches a floating external guideline and has no declared skill redistribution license at the reviewed revision. Keep the public guidelines as a reference instead of silently vendoring it.
- Backend conventions, official docs and the existing specialist bundles cover FastAPI and auth. I have not added an unverified third-party omnibus skill.

### Compatibility decisions

Tailwind v4 is the new-project default, matching the acquired Tailwind skill. Handle existing-project upgrades as focused migrations; loading a skill does not request an upgrade. shadcn rules apply to compatible installed primitives. Python tooling and MCP acquisition add conventions pointers without altering SDK examples: modern-python preserves accepted tooling, and the AI plugin's MCP builder follows the standalone Python FastMCP preference. Standalone package/import and installation/migration guidance were checked against [official FastMCP docs](https://gofastmcp.com/getting-started/installation); the Next.js v4 setup follows [official Tailwind docs](https://tailwindcss.com/docs/installation/framework-guides/nextjs).

## Matt Pocock selection

I reviewed all 27 previously bundled skills at [the pinned revision](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d), including their invocation rules, prerequisites and calls to other skills. The bundle now retains 18. I selected techniques that help application work without requiring Matt's entire workflow or duplicating a local entry point.

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

Retained dependencies are included with their resources. Three acquired skills have targeted, recorded adaptations that remove calls to the excluded setup skill; `implement-spec` also gets a tracker-neutral description. Other tracker references are interpreted through [workflow framing](../plugins/development-workflow/WORKFLOW.md#project-fit). Native invocation controls and attribution remain intact.

Removing a skill from this bundle does not judge its upstream quality. The excluded skills can fit different activities; I am keeping this collection focused on the application workflows described here.

## Supplied operations and explorer skills

I integrated the portable `operations-skills` archive into the existing activity bundles. The independently authored portable guidance cites public primary sources; the separate source-notes companion was excluded. No private inventories, incident identities or original internal skills are packaged. These are local guidance under this repository's license, not another upstream source in the lockfile.

| Destination | Added or enriched guidance |
| --- | --- |
| development-workflow | Added system-mapping and bash-engineering; merged cicd-release-management into build-delivery-pipelines |
| python-backend | Added python-automation-engineering for operational CLI/API tooling |
| application-operations | Added reliability-design, observability-operations, incident-response, runbook-engineering, postmortem-facilitation, postmortem-followup, kubernetes-resource-engineering, infra-jvm-optimization, vulnerability-management, credential-lifecycle and operational-housekeeping; merged backup-recovery into protect-and-restore-data |
| visual-communication | Added the separately supplied system-flow-explorer with its HTML renderer, strict JSON validator, examples and checks |

The integration retains substantive references while putting common decisions in entry points. It adds scope/invocation labels, canonical skill-name handoffs and explicit JVM boundaries. The factory framework and fixed schedules were not imported. Repeated reviews reuse existing records and stable finding identities; no tracker or schema framework is required. Interactive postmortem interviews and architecture explorers start only on request. Static system discovery stays separate from the explorer's artifact model.

Reference checks used the [Google SRE alerting chapter](https://sre.google/workbook/alerting-on-slos/), [Kubernetes HPA walkthrough](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/), [OpenTelemetry log model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) and [NIST patch-management guidance](https://csrc.nist.gov/pubs/sp/800/40/r4/final). Provider commands and behavior still require current installed-version checks. Examples and numerical thresholds remain conditional, not universal defaults.

## Maintaining the collection

Keep each plugin under `plugins/<name>` with its manifest and complete skill resources. Keep usage, scope/invocation labels, the SDLC map and source notices consistent when skills change. Standard labels describe intended use; preserve native upstream invocation controls.

For an upstream update, review the new source and license, update its full commit/tree pins in `upstream.lock.json`, and inspect the rebuilt skill/resources and any adaptations. Add a focused regression check when packaging behavior changes. Build into a fresh destination; replace installations through the client's supported route. Never package private installed material or execute upstream setup during acquisition.

Run repository checks:

```bash
python scripts/validate_plugins.py
python -m unittest discover -s tests -v
```

Also check changed Markdown links/anchors, inspect meaningful generated diagrams, and exercise changed guidance on a realistic task. Match validation to the claim: an application journey needs application tests; a metadata check proves metadata only.

### Evaluate engineering behavior

[Development workflow cases](../evals/development-workflows.json) contains eleven reusable task prompts with evaluator-only acceptance criteria. They cover a new full-stack journey, an existing-project feature, a populated-schema change, a durable export, a compatible release, current incident/recovery, k6 execution across three targets AI/MCP authority, controlled faults, configuration/contracts and routine upgrades/retirement. The cases exercise outcomes and judgment; they do not require one exact architecture or produce an application scaffold.

For a planning check, provide the case's raw task/context, selected skill paths and explicit local-only scope to a fresh agent. For an execution trial, supply a representative disposable application or isolated checkout, accepted product/platform context and working local commands. Establish target/action boundaries before execution. Provide every material product requirement and authority constraint in the task context. Keep evaluator checks and previous diagnoses separate from the acting agent; assess outcomes afterward without hiding product requirements or leaking an intended implementation. Cases are maintained here and are not installed as an application workflow or run by default in CI.

Inspect the diff and actual checks. Automate observable assertions such as persistence across restart, unauthorized access denial, resumed backfills and duplicate-effect handling when the supplied application supports them. Review scope, maintainability, visual consistency, evidence accuracy and unnecessary complexity separately. Do not grade by phrases repeated from a skill or impose a fixed passing percentage without a justified rubric.

Record the case/prompt revision, application/skill revisions, client/model configuration, supplied context, actual commands/results, artifacts and user corrections. Keep sensitive data out and distinguish guidance failures from missing tools or environment access. Count corrective interventions and characterize them instead of inventing token/time savings. Planning success is not execution success. Record blockers and any unexecuted cases; repair guidance from demonstrated failures, then rerun the affected case independently.

### Recorded evidence and limits

Checks recorded through 2026-10-12 include 13 helper tests, metadata/containment and Markdown link checks, and builds of all seven plugins with 37 upstream skills (55 total). Tests cover pinned acquisition, root-level skills, resource/license preservation, adaptations, labels, stale setup removal, overwrite protection and managed-link repair.

Copilot CLI 1.0.95 discovered all 55 plugin-sourced skills through isolated session-local mounts. Excluded entries were absent, MCP builder was in the AI bundle, and retained Matt invocation controls matched their sources. Earlier direct installs preserved package files, but a reinstall dropped an unrelated inventory entry; usage therefore recommends session-local loading for rebuilt bundles. VS Code configuration follows official docs and was not exercised here.

Fresh, mostly plan-only exercises covered project setup, unsafe ownership/transactions/migrations, UI failure states, AI evaluation, delivery/recovery, capacity/cost/feedback and contextual stack choices. The latest exercises kept MCP-only work free of model dependencies and outlined serial implementation without tracker setup or parallel agents. A separate disposable Git exercise executed a small feature, tests, a Conventional Commit and a local-remote push while preserving an unrelated user edit; it did not publish a live GitHub PR.

Humanizer was installed in the working environment and applied to repository prose. The lifecycle image was rendered and inspected. Earlier detailed traces and revision-specific results remain in Git history.

The 2026-10-13 operations/explorer integration passed 14 repository tests, plugin metadata/containment checks, source/local-package relative-link checks and an all-seven-plugin build: 33 local plus 37 upstream skills, 70 total. Copilot CLI discovered all 70 plugin skills. Built local resources matched source bytes and excluded Python runtime caches. Explorer smoke tests passed three cases and rendered both the supplied example and a fresh repository-case model. Browser checks could not launch because Chromium was absent; no browser check passed. The lifecycle SVG was rendered and inspected.

Fresh exercises covered async exports with stuck work and missing telemetry, recovery with a surviving datastore and active writers, and an evidence-backed repository explorer. They retained unknown outcomes, separated historical alerts from current impact, preserved existing data, and distinguished local evidence from a baseline Git revision. These were plans and synthetic artifacts, without live service access. The older creator validator accepted the 14 new Markdown guidance skills; its allowed-field list omits the explorer's standard `compatibility` field, which the repository validator checked instead.

These checks establish packaging, discovery and interpretation of supplied cases. They do not establish application quality, live model quality, deployment/restore success, savings, legal compliance or universal client enforcement. Reference-lookup avoidance of 90 to 95% remains an unmeasured design goal. Controlled failure guidance now defines experiment and recovery boundaries; the supplied operations guidance now covers observability, incident response and SLIs/SLOs.

## k6 performance guidance

`test-application-performance` adds local k6, application-on-runner and deployed non-production execution modes to development-workflow. It uses official k6 references and inline decisions for workload models, correctness thresholds, offered/achieved load, safe targets, failure propagation, fixtures and cleanup. Application scripts and workflows are authored in the target repository; no scaffold, cloud service or operator is bundled. Fault-injection behavior is covered by test-application-resilience; specific platform tools remain optional.

Validation for this addition: 14 repository tests, skill-creator and plugin validation, changed documentation/skill links, and a rebuilt workflow bundle with complete local resources passed. A fresh planning exercise covered an async export, missed offered load, isolated runner services and staging email effects. The collection now has 34 local plus 37 pinned upstream skills. No application k6 run or deployed-environment test was executed in this skills repository.

The production-guidance refinement passed 14 repository tests, plugin/creator validation, changed relative-link checks and rebuild/resource-parity checks for workflow, backend and frontend bundles. Two fresh planning exercises covered populated ownership migration with partial export effects and an existing-project sharing/release scenario. Eight reusable evaluation cases are defined; full application trials have not run.

## Engineering maintenance and controlled failures

`test-application-resilience` adds outcome-led local/isolated/non-production failure guidance with explicit observation, fault confirmation, stop and cleanup/recovery boundaries. References cover chaos principles, pytest and optional Toxiproxy; no tool or live action is configured. Common decisions are inline, and existing skills cover compatibility, effective configuration/flags, suite health, proactive upgrades and deprecation/removal. Pact is reference-only and optional; no contract broker is required.

The evaluation catalogue now includes controlled-failure, contract/configuration and upgrade/retirement cases. Domain-specific practices remain contextual, rather than adding mandatory SaaS, payments or search architecture. The collection has 35 local plus 37 pinned upstream skills across the same seven plugins.

Validation for this refinement passed 14 repository tests, plugin/creator checks, source relative links and builds of all seven plugins with local-resource parity and no bytecode. Copilot CLI discovered all 72 plugin skills. The updated SDLC SVG was rendered and inspected. Fresh planning cases covered bounded failures with provider ambiguity and contract/configuration, flaky-gate, upgrade and retirement decisions. No injected fault, application load test or live mutation was executed; the 11 full application cases remain defined for later trials.
