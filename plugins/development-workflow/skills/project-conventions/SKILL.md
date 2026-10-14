---
name: project-conventions
description: Establish or maintain an application repository's structure, stack constraints,
  scoped AGENTS.md, local setup and delivery conventions. Use when explicitly asked
  to start, organize or review a project, or when the requested change affects those
  foundations; keep ordinary feature work within existing conventions.
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: false
---

Read [workflow framing](../../WORKFLOW.md) for skill selection and invocation boundaries.


# Establish and maintain project conventions

## Match the requested change

Read the request, existing code and accepted decisions before choosing structure. For a new project, establish a useful first slice. For an existing application, identify which foundation the requested change actually affects and update only that part; do not repeat setup or start a repository-wide reorganization during ordinary feature work. State the smallest useful user journey and its observable acceptance criteria; carry forward answers already agreed. Resolve ambiguity that changes the product or data boundary, and make reversible implementation choices without another planning ceremony. Use the conversation as scope unless a separate spec is useful; require no tickets or tracker.

Prefer Python/FastAPI/PostgreSQL and Next.js/shadcn for new full-stack projects. Add AI or MCP for a concrete capability. Preserve an existing stack and layout unless changing them solves an agreed problem.

## Adopt an existing project and assess the change

For initial adoption, discover authoritative startup/test/build/migration commands, architecture and consumers, identity/tenant rules, deployment targets, critical journeys and operating constraints. Reuse existing instructions and evidence; add only missing useful pointers. Installing the plugins grants no authority to restructure or modernize the application.

During a feature or fix, trace the affected paths and identify changed contracts, stored data, permissions, integrations, configuration and delivery consequences. Preserve useful legacy knowledge. Investigate contradictory code/docs and surface uncertainty that changes the outcome or risk; routine local choices can proceed. Keep this assessment inline for ordinary changes and record consequential decisions in the project's existing notes. Unrelated legacy debt remains separate unless it prevents the requested behavior.

For shared saved searches, inspect existing ownership and all affected reads/writes before adding access grants. Preserve private defaults and define recipient permissions from the agreed scope; hiding UI controls does not enforce them. Select focused verification using `deliver-reliable-changes`, rather than invoking every installed skill.

## Establish a small, navigable repository

- Put code, migrations, tests, dependencies, application configuration and scoped AGENTS.md under `applications/`. Separate `api/` and `web/` when they represent actual boundaries. Keep provider-required CI entrypoints in their required locations.
- Put product and engineering knowledge under `documentation/`; use `documentation-conventions` to create only useful documents.
- Keep root AGENTS.md focused on purpose, stack, startup/test commands, shared conventions and the requirement to synchronize affected docs with code and decisions. Put component-specific commands and exceptions beside that component. Link authoritative information instead of duplicating it.
- Record compatible dependencies and lockfiles, required configuration and a safe local setup. Make it possible to start and verify the first slice without guessing secrets or commands.
- Add boundaries, services and infrastructure when a concrete requirement justifies them. Prefer domain-oriented code over layers with no present responsibility.

Use the relevant backend/frontend/AI skills and installed upstream expertise; do not assume a reference is installed. Preserve compatible installed UI/UX guidance without redistributing private material. Capture repeated corrections as a short scoped instruction or an executable check, rather than accumulating generic rules.

## Establish focused quality checks

For new projects configure the checks relevant to the actual files: Python Ruff lint/format and a compatible type checker; JS/TS ESLint and the project's formatter/type checker; YAML yamllint, GitHub Actions actionlint, shell ShellCheck, and Gitleaks secret detection where applicable. Preserve accepted tools in existing projects rather than installing a second equivalent stack. Keep tool versions/configuration reproducible and avoid an all-in-one Super-Linter dependency.

Use prek for a new local Git-hook runner when suitable; retain working pre-commit, Lefthook or other accepted setups. Pre-commit hooks run on the staged change; pre-push can run broader checks. These are local feedback mechanisms, distinct from server-side pre-receive hooks. CI repeats required checks over an explicit change range or full tree and is authoritative because local hooks can be absent or bypassed. A clean staged scan is not a clean history scan.

Document exact install/run commands, file ownership, exclusions and when to run each check in scoped AGENTS.md. Run affected lint/format/type checks during implementation, fast staged checks before commits and required broader checks before PR readiness. Keep slow integration/platform/load checks outside every commit. Handle partially staged files carefully: inspect formatter edits and restage only the intended hunks. Do not hide findings, dump detected secrets into artifacts, rewrite history, replace global hooks or bypass checks to obtain a green result. Inspect hooksPath and worktree behavior; install/verify repository-local shims without overwriting unrelated configuration. See [quality-check references](references/quality-checks.md).

## Provide a reproducible local environment

For new containerizable services, default to Docker Compose for the frontend/API/workers and their actual dependencies: database, Redis/Valkey, queues, object storage or local email capture only where needed. Preserve a working existing setup unless changing it is in scope. Keep app-specific Compose/configuration beside application/development infrastructure and root entry commands as useful; do not move provider-required files or impose a template. Host-native hot reload can use the same dependencies when documented.

Provide one documented startup path, migrations, representative non-sensitive seed data, actual service/application readiness, shutdown and safe reset commands. Readiness must include required initialization; container start order alone is insufficient. Isolate Compose project names, ports, credentials and data per feature worktree/test run. Use explicit test stores/owned fixtures, persistent volumes for development data, pinned compatible images and bounded resources. Never reset an unspecified or shared database; destructive volume removal must be an explicit scoped action.

Offer observability through a documented profile or companion Compose stack, with OpenTelemetry collection and a replaceable backend. Prefer SigNoz for a new unified local view after checking supported self-hosted components and available resources; keep an accepted backend. Add Langfuse only for a concrete AI dataset/experiment/evaluation workflow. Avoid running duplicate full telemetry stacks by default. Select a current supported vendor installation, not a copied stale Compose manifest. Document how the app and backend stacks connect, which services/profiles are required for each check and how agents query diagnostics. Observability should be easy to start without making every fast test depend on it.

Desktop/mobile clients and simulators normally run on their supported host and connect to Compose services through documented addresses; container-only backend checks do not establish native-client behavior. Keep external side effects controlled with local sinks/fixtures. Make opt-in real-provider boundaries explicit; do not silently use production credentials or real email/payment effects. Use delivery-pipelines for CI reuse and observability-operations when available for detailed portable instrumentation; these defaults are sufficient when that plugin is absent. Consult [local environment references](references/local-environment.md) for setup details.

## Include operating constraints in design

Use `security-and-privacy-design` for changed data flows and authority boundaries. Identify critical latency/concurrency constraints, durable state and meaningful recovery needs early; choose simple hosting that meets them. Bring capacity, cost and data-recovery guidance into design when relevant rather than treating them as production afterthoughts. Use `delivery-pipelines` when creating CI/CD. Do not introduce platforms or complete operations frameworks merely because their skills are available.

## Keep foundations aligned as the project evolves

Treat repository structure, dependency/runtime choices, configuration contracts, scoped instructions and delivery commands as maintained project decisions. Update affected commands, lockfiles and authoritative documentation alongside a relevant change. Resolve conflicting instructions at their proper scope; avoid copying the same rules into every component. Use `documentation-conventions` for knowledge upkeep and `delivery-pipelines` plus installed GitHub Actions hardening for delivery mechanics; this skill coordinates the project conventions rather than duplicating specialist guidance.

Start a full setup or structural review only when requested. Apply existing conventions during feature work, and suggest a broader change when a concrete problem warrants it rather than silently migrating the application.

## Prove the affected capability

For a saved-search application, start with saving a named filter and reopening it through the UI, API and database. Include ownership enforcement if users have private data. Defer sharing, recommendation agents and a generic workflow engine until requested. Prefer a real useful flow over disconnected mock screens and endpoints.

Finish by showing how to start the application, what journey works, which checks ran and what remains incomplete. Verify the applicable startup, migration and browser/API path; distinguish mocked providers from real integrations. Keep first-slice knowledge and decisions current. Do not describe a scaffold or a successful build alone as a working application.

## Maintain configuration and supported dependencies

Treat application settings and flags as behavioral interfaces. Use typed/validated inputs, explicit precedence and a small set of useful defaults; reject invalid required settings/combinations without silently weakening authority. Distinguish build, startup and dynamic settings. Track the effective non-secret configuration revision and source of truth; inspect authorized effective values without dumping secrets or personal data. Configuration-only changes need proportionate tests and recovery just as code changes do.

Maintain the supported runtime/dependency set and update process alongside lockfiles. Routine upgrades need release-note/deprecation review, coherent coupled versions, meaningful tests and a recovery route even without a vulnerability. Keep changes focused; major upgrades are deliberate migrations, not silent modernization. Use vulnerability-management for security-driven priority when available. Flag unsupported/EOL choices with evidence rather than replacing them unasked.
