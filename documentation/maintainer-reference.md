# Maintainer reference

Source selection, acquisition rules and validation evidence for this repository. For installation, start with the [README](../README.md#quick-start); for activities, use [Usage](usage.md); for coverage, use the [SDLC map](sdlc.md).

- [Upstream catalogue](#upstream-catalogue): bundled sources, licenses and adaptations.
- [Source selection](#source-selection): reference applications and compatibility decisions.
- [Matt Pocock selection](#matt-pocock-selection): each retained or excluded skill.
- [Maintaining the collection](#maintaining-the-collection): update and validation checks.
- [Generation trials](#generation-trials): harness-independent workflow evaluation and a local runner example.

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

The lockfile and built notices record adaptations and usage labels. Standard `metadata.scope`, `metadata.stack`, `metadata.invocation` and `metadata.role` describe applicability and preferred use without changing native controls. Packaging checks hashes and copies resources without running scripts. Pinning the source leaves embedded live documentation and commands free to change. Trail of Bits skills are CC-BY-SA-4.0; other included sources are MIT or Apache-2.0 as recorded at their pins. Built bundles carry mixed-license notices; private installed material is not redistributed.

### Additional references

- [Git worktrees](https://git-scm.com/docs/git-worktree), [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) and [GitHub CLI PR creation](https://cli.github.com/manual/gh_pr_create): contribution mechanics used by the local `git-contributions` skill; no additional MCP server is required.
- [Next.js agent guidance](https://github.com/vercel/next.js/tree/canary/skills): use documentation matching the application's chosen release.
- [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) and [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design): optional design guidance, constrained by existing tokens and direction. Reuse installed skills without copying private content.
- [Vercel web-design-guidelines](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines): reference only; the reviewed source did not declare a redistribution license and fetched floating guidance.
- [FastAPI](https://fastapi.tiangolo.com/), [Uvicorn](https://www.uvicorn.org/), [uv](https://docs.astral.sh/uv/), [SQLAlchemy](https://docs.sqlalchemy.org/en/20/), [Alembic](https://alembic.sqlalchemy.org/), [PostgreSQL](https://www.postgresql.org/docs/) and [FastMCP](https://gofastmcp.com/): first-party implementation documentation; no unified official skill for this entire backend stack is claimed.
- [Gemini audio](https://ai.google.dev/gemini-api/docs/audio), [pricing](https://ai.google.dev/gemini-api/docs/pricing) and [quotas](https://ai.google.dev/gemini-api/docs/rate-limits): verify the actual model and account before live tests.
- [C4](https://c4model.com/), [arc42](https://arc42.org/overview/), [MADR](https://adr.github.io/madr/) and [AGENTS.md](https://agents.md/): lightweight structures for project knowledge and scoped instructions.
- [shadcn MCP](https://ui.shadcn.com/docs/mcp) and [Playwright MCP](https://github.com/microsoft/playwright-mcp): optional live tools configured in the chosen client. Hooks use [client-specific extensions](https://agent-plugins.org/specification#8-client-extensions), not a portable hooks field.

SigNoz is a replaceable local observability preference, selected for OTel support and visible maintenance; its [support policy](https://signoz.io/support/) makes community support best-effort. Provider installation details, edition boundaries and resource requirements are linked from the owning skills and need version-specific checks.

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
| development-workflow | Added system-mapping and bash-engineering; merged cicd-release-management into delivery-pipelines |
| python-backend | Added python-automation-engineering for operational CLI/API tooling |
| application-operations | Added reliability-design, observability-operations, incident-response, runbook-engineering, postmortem-facilitation, postmortem-followup, kubernetes-resource-engineering, infra-jvm-optimization, vulnerability-management, credential-lifecycle and operational-housekeeping; merged backup-recovery into protect-and-restore-data |
| visual-communication | Added the separately supplied system-flow-explorer with its HTML renderer, strict JSON validator, examples and checks |

The integration retains substantive references while putting common decisions in entry points. It adds scope/invocation/role labels, canonical skill-name handoffs and explicit JVM boundaries. The factory framework and fixed schedules were not imported. Repeated reviews reuse existing records and stable finding identities; no tracker or schema framework is required. Interactive postmortem interviews and architecture explorers start only on request. Static system discovery stays separate from the explorer's artifact model.

Reference checks used the [Google SRE alerting chapter](https://sre.google/workbook/alerting-on-slos/), [Kubernetes HPA walkthrough](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/), [OpenTelemetry log model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) and [NIST patch-management guidance](https://csrc.nist.gov/pubs/sp/800/40/r4/final). Provider commands and behavior still require current installed-version checks. Examples and numerical thresholds remain conditional, not universal defaults.

## Naming and invocation

Use lowercase kebab-case. Local task entry points use short activities (`develop`, `test`, `review`); supporting guidance uses recognizable disciplines (`interaction-design`, `performance-testing`). Preserve established operations terminology and upstream names. `workflow-help` and `dependencies` are deliberate readable exceptions to verb-led task names. Rename folders/frontmatter and maintained references together, documenting old names in [migration](migration.md#local-skill-naming) rather than shipping duplicate aliases.

| Metadata | Meaning |
| --- | --- |
| `scope` | `generic` or `stack-specific` applicability |
| `stack` | Matching technologies for stack-specific guidance |
| `role` | `task` entry point or `support` guidance |
| `invocation` | Preferred `user`, `agent` or `both` usage |

Labels describe intended use; they do not enforce permissions. New task entries use native explicit-only controls. Most local supporting guidance sets `user-invocable: false` while remaining model-available. Client support varies. The recorded `support-visibility` adaptation sets upstream visibility only when absent; explicit upstream controls remain intact. `implementation-entrypoint` adds task/design/incremental-verification framing to retained upstream implement without replacing its original body or resources. The installed [TASKS.md](../plugins/development-workflow/TASKS.md) and [WORKFLOW.md](../plugins/development-workflow/WORKFLOW.md) hold the agent-facing execution/project-fit rules.

## Maintaining the collection

Keep each activity plugin under `plugins/<name>` with its manifest and complete resources. Keep user docs focused on installation, activities and expected outcomes. Put specialist implementation methods and diagrams beside their owning skills. Avoid duplicating rules across guides; the SDLC SVG is the main overview.

For an upstream update, review source/license changes, update full commit/tree pins in [upstream.lock.json](../upstream.lock.json), and inspect acquired resources and recorded adaptations. Add focused regression coverage when packaging behavior changes. Build into a fresh destination and replace installations through the client. Never package private installed material or execute upstream setup during acquisition. Update plugin versions when packaged content changes.

```bash
python scripts/validate_plugins.py
python scripts/check_collection.py
python -m unittest discover -s tests -v
```

CI also builds all seven bundles from their pins and runs `scripts/check_collection.py --built <destination>` to check complete skill inventories, source notices, local-resource byte parity and duplicate names. The source check covers maintained entry points and reader guides, relative links/headings and obsolete names from the migration table; it does not fetch external URLs or parse every example in preserved resources. Render meaningful diagram changes separately. Preserve upstream names, native controls, dependency groups and notices. The older creator validator omits some native optional fields; repository validation checks those types. A package check proves packaging, not application behavior.

### Evaluate engineering behavior

[Development workflow cases](../evals/development-workflows.json) contains 16 reusable prompts with evaluator-only criteria. They cover full-stack and existing-project journeys, populated migrations, durable effects, releases/recovery, k6, AI/MCP authority, controlled faults, contracts/configuration, maintenance, rough-idea decisions, global UI coverage, dependency policy and portable local telemetry.

For planning checks, give a fresh agent raw task/context, selected skills and explicit execution boundaries. For application trials, supply a representative disposable application or isolated checkout, accepted product/platform context and working commands. Keep evaluator criteria and previous diagnoses separate from the acting agent without hiding product requirements. Assess observable outcomes, actual diff/checks, evidence accuracy and unnecessary complexity; do not grade phrase matching or impose an arbitrary passing percentage.

Record task/application/skill revisions, client/model configuration, supplied context, actual commands/results and corrective interventions. Keep sensitive data out. Distinguish guidance failures from missing capabilities and planning success from execution success. Repair demonstrated failures and rerun the affected case independently. Cases do not scaffold an application or run automatically in CI.

### Generation trials

The `generation_trials` section in [the evaluation cases](../evals/development-workflows.json) defines tasks and evaluator criteria independently of the agent harness. Trial IDs, product briefs and expected evidence are portable. Run them interactively or through automation in a client that can load the selected guidance and operate the target repository; native plugin support, slash commands, a particular CLI and a trace format are not requirements.

| Trial | Acting phases | Evidence to collect |
| --- | --- | --- |
| New saved-search application | setup, agreed answers, develop | Actual startup/migrations, private persisted journeys, rendered UI, checks, feature worktree and local commit |
| Existing SQLModel library | improve, approve one scoped finding, implement | Reproduction/baseline, focused implementation, repository checks, preserved tools/contracts and local commit |
| Small documentation change | implement | Proportionate support selection and verification without full application ceremony |

Use disposable repositories with no production credentials or remotes accepting writes. Build the required bundles and load them through the harness's supported plugin or skill route, preserving complete resources, relative links and native invocation controls. Confirm the available skills, authentication, permissions and required capabilities before execution. A file copy or inventory listing does not establish that the agent used the guidance. Record unsupported controls or missing capabilities instead of silently changing the trial or claiming equivalent coverage.

Pass only the selected raw phase prompt to the acting agent, with its repository, installed guidance, product context and allowed actions. The `task` field identifies an activity; use the client's explicit selection mechanism or supported plain-language request, without assuming universal slash-command syntax. Keep evaluator criteria and previous diagnoses separate from the acting agent. After setup, answer consequential questions and save accepted answers as ordinary project context. After the OSS assessment, approve one evidence-backed change before implementation; no valid finding means select another bounded task, not invent a defect. Preserve phase context through conversation continuation or a factual handoff. Start independent reruns from a fresh checkout/context.

Record repository and guidance revisions, harness/model versions and configuration, loaded inventory, available tools, allowed actions and run limits. Establish baseline behavior and acceptance checks before implementation. Evaluate the actual diff, local commit, executed checks and runtime artifacts. Retain redacted tool events or session logs where available; if skill reads cannot be observed, mark routing evidence unknown rather than accepting a self-report as proof. Record interventions and reported resource/time usage without inventing missing metrics. Classify each result as completed, partial or blocked, separating guidance failures from capability limitations. Successful process exit or a positive final response alone is insufficient. Keep credentials out of prompts and evidence.

First run the complete bundles. Then repeat the same briefs against the same application baseline, harness, model, tools and permissions with pristine upstream skills and their native dependency groups, without local adapters or dangling local guidance links. If native prerequisites require unavailable external setup, record that limitation instead of changing invocation controls or inventing a tracker. Use equivalent plain-language activity requests where a local task name is absent upstream, recording that routing difference. Keep the requested outcome, ordinary product context and allowed actions identical; state that the baseline omits local conventions. Rerun demonstrated failures after a focused repair. Compare behavior, unnecessary work, missed guidance, repeated reading and available token/latency measurements. Comparisons across different harnesses/models must state those differences and cannot isolate the effect of the skills. A single trial is not a quality guarantee.

<details>
<summary>My local runner choice: agy</summary>

I selected `agy` for my local trials. This recipe is one way to execute the portable cases; it adds no dependency to the plugins or trial specification. For installation use the [README client instructions](../README.md#2-load-them-in-your-client).

With the required bundles built, use `agy plugin validate <bundle>` and `agy plugin list --json` to check packaging/discovery. For a headless phase, run `agy -p '<phase prompt>' --output-format stream-json --print-timeout 20m` from the target repository, capturing stdout/stderr outside it. Continue using the installed client's supported conversation option. The 20-minute timeout is a local run limit. Inspect tool events, soft denials, diffs and actual commands, since exit zero alone is insufficient. Grant the required scoped capabilities without disabling permissions globally. Use the client's sign-in flow; never put sign-in codes in the prompt or trace.

With `agy` 1.3.5, I validated and installed the three default built packages. Its inventory listed all 56 skills (47 workflow, three backend and six frontend), and installed files matched their complete built bundles; workflow version was 0.17.0. A minimal headless probe required a fresh Google sign-in and exited without generating a response. The pinned SQLModel checkout is prepared, but neither application-generation trial has run. Docker was also unavailable in this execution environment, independently blocking Compose verification. These are local run observations, not restrictions on other harnesses.

</details>

### Reduce repetition from observed use

Each rule has an owner: TASKS for request/automation scope, WORKFLOW for upstream project fit, project-conventions for repository foundations, git-contributions for contribution mechanics, deliver-reliable-changes for completion evidence, and specialist skills for their methods. Task entry points link those owners with relevance conditions. Optional bundles are resolved from actual inventory; there is no new dependency registry or automatic invocation of explicit-only tasks.

I removed the copied completion paragraph from develop/test and linked the existing owner. Keep a short safety boundary beside a live action when losing it would change authority. After the trials, inspect which guidance was actually loaded, which duplicate text affected behavior, and whether a pointer was missed. Consolidate one repeated rule at a time, then rerun the affected full and small-change trials before removing further text. Preserve upstream bodies/resources and record any adapter change. This avoids a speculative rewrite of the whole collection.

### Recorded evidence and limits

The collection contains seven plugins, 48 local skills and 37 pinned upstream skills. The generation follow-up passed 18 repository tests, metadata/containment checks, 224 maintained relative link/heading checks, all-seven-plugin builds and local-resource byte parity. CI now runs those collection checks alongside the explorer smoke checks. The checker covers a narrower explicit maintained-document set than the earlier manual resource-link review. Copilot CLI 1.0.95 previously discovered all 85 skills through isolated session-local mounts without old-name duplicates. The README three-plugin loading/discovery route was rechecked with 56 plugin skills, including every advertised task/convention entry point. The unchanged SDLC SVG had been rendered and inspected; original architecture references remained byte-identical after renaming. Earlier revision-specific records remain in Git history.

Fresh planning exercises covered project scope, migrations/authority, durable effects, releases/recovery, k6/fault boundaries, global UI interactions, unattended dependency policy, Electron evidence and two-worktree AI/telemetry setup. A separate disposable Git exercise executed a feature, tests, Conventional Commit and local-remote push while preserving unrelated edits; it did not publish a live GitHub PR. Explorer smoke checks exercised supplied/fresh models and HTML rendering. Browser verification was blocked by missing Chromium.

Direct Copilot installation was tried earlier, but CLI 1.0.95 warned that route was deprecated and a reinstall dropped an unrelated inventory entry; the README therefore uses session-local loading. VS Code configuration follows official documentation and has not been exercised. Discovery does not establish menu filtering, model compliance or universal client enforcement.

The local runner recipe above records the `agy` installation/discovery checks and current authentication/Compose blockers. No generation result is recorded for those prepared trials.

No full application trial, Compose stack, telemetry ingestion, native-device run, live AI quality evaluation, application load/fault test or live deployment/restore was established by these repository checks. Reference-lookup avoidance of 90 to 95% remains an unmeasured design goal. Source decisions and package tests do not establish compliance, savings or production quality. Specialist tool selection and current provider/platform documentation remain contextual; the relevant skill owns those details.
