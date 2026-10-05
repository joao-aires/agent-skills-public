# Opinionated full-stack development standard

Status: conventions implemented; selected upstream integrations are acquired by the pinned profile builder; runnable starter implementation remains a separate increment. Reviewed 2026-10-05.

## Design rationale

Optimize time to a verified user outcome and repeated correctness, rather than code volume or the number of installed skills. The profile combines short persistent project rules, selectively loaded specialist skills, reusable starter assets, exact commands, meaningful tests and feedback from observed failures. More instruction text is not automatically a better harness.

These conventions incorporate recurring engineering themes: consistent component systems, contract-defined integration, performance/reliability/maintainability, bounded agent execution, current source-grounded context and repeatable verification. Detailed mechanisms below are recommendations encoded in this repository, not claims that every previous application used them.

## Core defaults

| Concern | Default | Enforcement/evidence |
| --- | --- | --- |
| Scope | Small PRD with primary journey, non-goals and acceptance criteria | Requirement-to-test mapping |
| Architecture | Modular FastAPI backend plus Next.js frontend; optional AI/MCP adapters | Local boundaries, ADR for material departures |
| Integration | Code-derived OpenAPI, typed frontend client, explicit error contract | Schema generation/diff and integration tests |
| Setup | Committed versions/locks, predictable setup/dev/migrate/seed commands | Same scripts locally and in CI |
| UI | shadcn components, one token/variant system, representative screen | Rendered review, focused visual/accessibility tests |
| Data | PostgreSQL and Alembic; explicit ownership/constraints/transactions | Real database integration and migration verification |
| E2E | Playwright against real frontend/API/database/auth | Critical journey evidence, persistence/negative cases |
| Agents | Short root/scoped AGENTS.md with reference/command routing | Structural checks and harness behavioral evaluations |
| Documentation | Same-change updates for affected behavior/architecture/decisions | Generated contract checks plus semantic diff review |
| CI/CD | Fast deterministic checks, integrated smoke, reviewed release/recovery | CI evidence and post-deploy smoke |
| Operations | Useful logs/health, diagnostic signals, ownership and recovery | Verified commands; budgets appropriate to use |
| AI | Direct SDK when enough; one justified agent framework | Offline tests and distinct live model evaluations |
| Learning | Corrections become checks or narrow context changes | Regression cases and measured correction/token cost |

## Important blind spots

### A working application needs reproducible environment setup

A folder structure cannot remove repeated setup work. A future runnable starter should include compatible pinned dependencies, application entrypoints, PostgreSQL orchestration, reviewed migrations, deterministic synthetic seed data and one primary integration test. Setup must work from a clean environment. This release gives the contract/templates, not fictitious runnable commands.

### Acceptance and domain correctness

Define the primary user's actual task and behavior before implementation. Use tests at the layer that can prove each condition. For financial/calculation apps use units, precision/rounding and invariants; for automation apps use explicit states/idempotency/retries; for research/data apps track sources/freshness/uncertainty. These are capability-specific extensions, not mandatory features for all projects.

### Authentication and resource authorization

Session/auth handling and resource ownership need an explicit design. Test unauthorized access in the backend, not just hidden frontend controls. Multi-tenant applications require explicit tenant scope and distinct-principal tests; ordinary single-user prototypes should not inherit an unnecessary tenant platform.

### Data evolution and recovery

A migration generated successfully can still lock a large table or break compatibility. Review constraints/indexes/backfills and rollout sequencing; check real PostgreSQL. Application rollback and database recovery are separate procedures. Operational production claims require tested backup/restore or an appropriate documented provider strategy.

### UI consistency includes behavior

One visual system must cover forms, validation, navigation and loading/empty/error/permission states. Do not freeze a project-specific desktop-only or brand decision into every project. Upstream design intelligence operates within local tokens and accepted direction. Accessibility needs keyboard/focus review as well as automated checks.

### Async work and third-party boundaries

Introduce queues/workers only when a use case needs durable async execution. Define timeout/retry/idempotency behavior, observable failure and cancellation where relevant. The real application stack remains under E2E tests even if external providers are stubbed. Live tests run separately and must respect existing authority, account quotas and side effects.

### Deployment and operations

Verify the actual deployed revision with a smoke journey. Do not ship a preview using production data/credentials. Ensure config validation, health, useful logs, scoped secrets and recovery. Instrument critical flows and measure latency/error/cost before investing in a complex monitoring platform. Kubernetes, Terraform or a factory control plane are conditional tools, not universal prototype dependencies.

### Source and skills lifecycle

References can drift and upstream scripts may fetch additional unpinned guidance. Acquire narrow reviewed skill selections with exact source version and license; record dependencies and installation routes. Preserve local policies when upstream defaults differ. Do not treat a popular catalogue as certified for this project's needs.

## Agent context design

Root AGENTS.md carries enduring invariants, exact entrypoints and completion evidence; scoped application files contain relevant local detail. project-profile.json stores structured choices and argument arrays, while docs store current product/architecture state. Skills hold reusable procedures. Mechanical constraints belong in tools/CI wherever feasible. Keep one canonical owner per rule and avoid duplicating entire upstream guides.

Version-matched references matter. Vercel reported that a compressed AGENTS.md documentation index performed better than optional skill activation on its particular Next.js evaluation. That supports testing explicit reference routing; it does not establish that AGENTS.md universally beats skills for all tasks.

Use bounded build-test-diagnose-fix loops. Continue authorized reversible work without ceremony; surface real ambiguity/authority limits. Parallel work is useful only when boundaries/contracts and authorization permit it. Do not make a multi-agent system mandatory to build a simple app.

## E2E policy

A full-stack E2E claim requires browser → real Next.js → real FastAPI → migrated PostgreSQL and actual application auth. Browser route interception of the app's API is an isolated UI test. External email/payment/LLM boundaries may be stubbed in ordinary CI with disclosure.

Require a primary complete user journey with persistence after refresh, critical resource authorization/invalid-input checks and meaningful error behavior. Keep exhaustive domain edge cases in unit/integration tests. Use stable role/label selectors and state-based waiting. Start with critical Chromium tests on PRs; expand browser/device matrices according to supported targets and risks. Add axe plus keyboard/focus review for affected screens.

Use isolated fixtures/data per parallel worker and clean up runtimes. Retain failure traces, screenshots and browser/API logs with privacy-safe retention. Do not let retries hide flakiness or a healer remove assertions/skip critical tests/approve baselines. Changes in expected behavior require accepted requirements and reviewable evidence.

## CI/CD policy

Use the same lock-derived runtime versions and project commands locally and in CI. Check lint/types/unit tests, database integration/migrations, build/schema alignment and critical E2E. Do not over-filter integrated tests based only on frontend path changes. Review untrusted PRs, token scopes, secrets, action pinning, artifact retention, job timeouts/concurrency and supported OIDC configuration.

Promote the tested revision/artifact where the platform allows. Deploy only within actual authorized scope, use isolated previews/staging, verify post-deploy smoke and document rollback/forward recovery. Match safety mechanisms to risk rather than requiring canary infrastructure for every personal project.

## Upstream selection

See upstream-sources.md for source links and status. A focused starting set is:

- Official shadcn skill, relevant Vercel React/composition/web-design skills and version-matched Next.js docs/skills.
- Official Playwright skill/CLI and Test Agents for browser exploration and durable test authoring.
- Trail of Bits modern-python for uv/Ruff/pytest conventions.
- Selective Superpowers systematic-debugging and verification-before-completion, subject to local workflow and no redundant re-execution without a reason.
- GitHub community github-actions-hardening and CI/CD instructions when pipeline files are involved.

Load ADK or LangChain skills only for the selected AI framework. Use security/property-based/Sentry review/document coauthoring/MCP authoring guidance when the task warrants it. Default adoption should not load all of these into every context.

## Fit and trade-offs

Superpowers provides substantial process discipline, but its complete global workflow can impose approval/planning/TDD/delegation habits beyond this profile. Start with its narrow debugging/verification skills; full-framework adoption should be a deliberate choice. Anthropic webapp-testing is a useful local browser helper but not the entire full-stack test strategy. doc-coauthoring is useful for substantive specs and reader testing, not an obligatory multi-stage interview for every docs update. Trail of Bits is excellent specialist guidance but includes deep auditing tools not needed on every change; redistribution also requires preserving its applicable license. GitHub-hosted community instructions and agent definitions may require adaptation rather than being treated as portable skills.

## Remaining highest-value increment

A tested runnable starter proving one browser/API/PostgreSQL flow will save more repeated setup and correction than adding another large instruction catalogue. Build that once, then benchmark representative agent tasks against it. Measure time to first verified journey, success/correction rates, regressions, flakiness, UI/doc drift and token/tool cost. Promote harness changes only when the evidence supports improvement.

## Research references

https://agents.md/
https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
https://playwright.dev/docs/test-agents
https://playwright.dev/docs/best-practices
https://playwright.dev/docs/accessibility-testing
https://github.com/obra/superpowers
https://github.com/trailofbits/skills
https://github.com/github/awesome-copilot
