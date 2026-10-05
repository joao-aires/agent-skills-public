# Portable development plugin design

Status: initial implementation, 2026-10-04

## Goal and enforcement

Establish stack, layout, documentation and design conventions once per project, then apply and verify them on every change. Plugins supply portable expertise; project-level AGENTS.md preserves decisions; templates/scripts reduce repeated generation; tests/CI detect drift. Instructions alone cannot guarantee outcomes.

## Plugin boundaries

| Plugin | Responsibility |
| --- | --- |
| development-workflow | Bootstrap, acceptance criteria, documentation synchronization, delivery verification |
| python-backend | Python/FastAPI/Uvicorn, SQLAlchemy/Alembic/PostgreSQL, optional FastMCP |
| web-frontend | Next.js/shadcn, Vercel practices, stable tokens/components and UX review |
| ai-development | ADK or LangChain/LangGraph, Gemini generation/transcription, evaluations |
| business-strategy | Preserved strategy v2.2 and compatibility entrypoint |
| visual-communication | Preserved HTML diagrams and presentations |

The first three comprise the full-stack profile. AI is optional. The core standard packages skills and MCP; it does not define portable dependencies/collections/hooks/agents/rules fields. profiles/full-stack.json is our installation convention, not a new standard manifest. Client extensions are optional adapters, never the sole correctness mechanism.

## Project layout

| Path | Contents |
| --- | --- |
| Root AGENTS.md / project-profile.json | Global contract, chosen stack, actual versions/commands, unresolved choices |
| applications/api/ | Source, migrations, tests, package/lock, containers, ci/ scripts, scoped AGENTS.md |
| applications/web/ | Next.js source/tests, components.json, package/lock, containers, ci/ scripts, scoped AGENTS.md |
| applications/tooling/ | Shared structural checker and development scripts |
| documentation/ | Product, architecture, contracts, plans, decisions, UX, operations, verification |
| .github/workflows/ | GitHub-required entrypoints calling application-specific scripts/commands |

AI/MCP modules default to the backend. A separate worker or MCP application is introduced only when its deployment/lifecycle requires it. Avoid shared packages before actual reuse exists. uv and pnpm are greenfield defaults; preserve existing project package managers during adoption. Pin stable compatible versions, not floating model/library assumptions. Vercel is a frontend hosting option; backend/database hosting needs a decision.

## Workflow

1. Scaffold conventions into a new empty directory; adopt existing repositories through reviewed merging.
2. Define the short PRD, non-goals, stable requirement IDs and acceptance criteria.
3. Resolve versions, auth, deployment and optional AI/MCP requirements; record consequential decisions in ADRs.
4. Define tokens and one reference screen; implement a complete browser → API → PostgreSQL flow.
5. For each change read scoped instructions, load relevant available skills, implement the scope, update affected docs, and run real checks.
6. Inspect rendered UI when it changes and review code/documentation consistency. Report evidence and unresolved limitations.

## Documentation structure

Architecture uses arc42 narrative, C4 context/containers, and MADR-style ADR records. PRDs, roadmaps and implementation plans use explicit local templates; no universal PRD standard is claimed.

The scaffold includes product/prd.md, product/roadmap.md, plans/feature-template.md, architecture/overview.md, architecture/c4/context.md and containers.md, architecture/data-model.md, architecture/schemas/README.md, decisions/adr/template.md, decisions/decision-log.md, ux/design-system.md, operations/runbook.md, verification/strategy.md and traceability.md. AI profiles add ai-evaluations.md.

These are honest templates/placeholders until populated from a real product, not completed architecture diagrams or deployed behavior. Start lean and expand only where needed.

Every meaningful change identifies documentation impact: behavior → PRD/acceptance; boundaries → architecture/C4; persistence/contracts → data model/generated schemas; interaction/visual choices → UX contract; deployment/recovery → runbook; material choices → ADR/log. Update affected documentation in the same change. Supersede historical ADRs rather than rewriting them. Generated contracts derive from application code/database state with actual regeneration commands. A touched file does not prove semantic consistency.

## Upstream integration

Prefer first-party Vercel/shadcn implementation/review skills and ADK/LangChain skills selected by framework. The backend plugin supplies this precise stack policy and official references; no verified first-party unified skill for the entire backend stack is asserted. Installed UI/UX skills must be inspected; prior recommendations are not installation evidence.

Keep project governance separate from upstream expertise. Upstream skills guide implementation; local accepted requirements/decisions determine scope and style. UI/UX Pro Max is constrained by the local design system; Anthropic frontend-design is opt-in exploration.

This release references upstream skills rather than vendoring them. Acquisition is a client operation. Before redistribution record exact source commit/release, skill paths, checksums, licenses and network/script behavior. Preserve attribution and inspect transitive resources/containment. Updating upstream content should create a reviewable diff. Do not publish private user skill content.

## MCP and Gemini

Skills-only plugins conform; no dummy server is necessary. FastMCP is application code when tools are required. shadcn MCP is an optional development integration configured against the actual web application's components.json. Portable stdio defaults to plugin-root cwd, so a project path cannot be assumed. No automatic MCP config is bundled.

Keep keys out of manifests. Standard placeholder expansion supports PLUGIN_ROOT and PLUGIN_DATA only; arbitrary secret/project placeholders must not be assumed portable.

Gemini is preferred for live LLM/transcription tests. Model capability, free tier, quota, account and region require verification at model selection. Never silently switch to paid usage. Ordinary CI uses deterministic fixtures/mocks; optional live evaluations measure behavior/schema/tools/latency/cost and transcription quality. Uploaded-audio understanding and live streaming voice are separate requirements.

## Implemented verification and limits

Implemented: bundled official schemas, plugin metadata/containment checks, profile-reference validation, conventions scaffold, project metadata/doc/link checks, negative scaffold tests and this repository's validation CI.

Still project-specific: runnable stack initialization, real lint/types/build/tests, PostgreSQL integration/migration checks, browser/accessibility verification, generated schema drift and live AI evaluations. These are requirements to configure, not commands falsely claimed installed/passing. Structural checks cannot prove prose is truthful or certify all client behavior.

Behavioral evaluations should include ordinary CRUD, ADK assistant, durable LangGraph workflow, MCP tools, UI component reuse, DB schema change, existing-repo adoption and attempted stack/design drift. This initial independent forward test exercises project-bootstrap only; it is not full cross-client certification.

## Migration

All four prior skills were moved with their complete supporting resources. Names and business-strategy v2.2 content remain unchanged. Strategy compatibility sibling routing remains within its plugin. Legacy sync detects new paths and repairs owned old links without deleting unrelated links. Manually configured root skills/ paths require updating; package symlinks escaping the plugin root are not used.

The repository name remains unchanged. No personal skill installation/client configuration is modified. Install selections through actual client-supported flows; do not promise a universal plugin installer.

## Follow-up

Acquire/review/pin relevant upstream skills in the user's actual clients. Exercise the conventions against a real app and refine on observed drift. Runnable stack starter code is a separate tested increment. Add client adapters only for concrete needs that portable instructions/project checks do not cover.

## References

https://agent-plugins.org/specification
https://arc42.org/overview/
https://c4model.com/diagrams
https://adr.github.io/madr/

## Holistic workflow extension

See [full-stack-standard.md](full-stack-standard.md). development-workflow now includes maintain-agent-harness, test-end-to-end and deliver-reliable-changes. New scaffolds include engineering context/lessons, E2E, delivery, observability and security documents. Profile metadata declares readiness and an explicit real-stack Playwright testing contract. The structural checker detects missing critical commands/journeys for implemented/deployed claims; it does not execute those commands or prove those claims true. Upstream catalogue adds focused browser/testing/debugging/CI/security/documentation sources. Application starter code, upstream installation and live app E2E remain separate tasks.

## Reproducible upstream packages

The profile builder acquires selected upstream skill directories at locked commits and packages their references and notices inside plugin boundaries. See [installation](installation.md), [workflow map](workflow-map.md), and `upstream.lock.json`. Earlier reference-only catalogue descriptions apply only to sources absent from that lock. No MCP runtime is automatically installed.
