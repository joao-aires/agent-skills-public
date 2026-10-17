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

Prefer Python/FastAPI/PostgreSQL and Next.js/shadcn for new web full-stack projects. For desktop prefer TypeScript + Tauri; for iOS/Android select a framework from product constraints, starting with React Native + Expo when TypeScript reuse fits. Use native-client-development when installed. Use system-design after product refinement and for consequential feature architecture before dependent planning/implementation. Add AI or MCP for a concrete capability. Preserve an existing stack and layout unless changing them solves an agreed problem.

## Adopt an existing project and assess the change

For initial adoption, discover authoritative startup/test/build/migration commands, architecture and consumers, identity/tenant rules, deployment targets, critical journeys and operating constraints. Reuse existing instructions and evidence; add only missing useful pointers. Installing the plugins grants no authority to restructure or modernize the application.

During a feature or fix, trace the affected paths and identify changed contracts, stored data, permissions, integrations, configuration and delivery consequences. Preserve useful legacy knowledge. Investigate contradictory code/docs and surface uncertainty that changes the outcome or risk; routine local choices can proceed. Keep this assessment inline for ordinary changes and record consequential decisions in the project's existing notes. Unrelated legacy debt remains separate unless it prevents the requested behavior.

Select verification through [deliver-reliable-changes](../deliver-reliable-changes/SKILL.md) and establish the objective workspace through [Git contributions](../git-contributions/SKILL.md) before foundation/feature writes. Those skills own the verification loop and worktree mechanics.

## Establish a small, navigable repository

- Put code, migrations, tests, dependencies, application configuration and scoped AGENTS.md under `applications/`. Separate `api/` and `web/` when they represent actual boundaries. Keep provider-required CI entrypoints in their required locations.
- Put product and engineering knowledge under `documentation/`; use `documentation-conventions` to create only useful documents.
- Keep root AGENTS.md focused on purpose, stack, startup/test commands, shared conventions and the requirement to synchronize affected docs with code and decisions. Put component-specific commands and exceptions beside that component. Link authoritative information instead of duplicating it.
- Record compatible dependencies and lockfiles, required configuration and a safe local setup. Make it possible to start and verify the first slice without guessing secrets or commands.
- Add boundaries, services and infrastructure when a concrete requirement justifies them. Prefer domain-oriented code over layers with no present responsibility.

Use the relevant backend/frontend/AI skills and installed upstream expertise; do not assume a reference is installed. Preserve compatible installed UI/UX guidance without redistributing private material. Capture repeated corrections as a short scoped instruction or an executable check, rather than accumulating generic rules.

## Complete new-project foundations

For a requested new application setup, create and validate the following applicable artifacts. A local-only execution boundary still permits preparing CI, release and deployment procedures; it does not authorize running remote publication or deployment.

| Foundation | Expected artifact and evidence |
| --- | --- |
| Human onboarding | Authored root README linking each application/component README, purpose, architecture, prerequisites, configuration, install/start/migrate/test/build and shutdown/reset commands. Replace starter text and empty files. AGENTS.md complements these user-facing docs. |
| Dependencies and configuration | Compatible manifests/lockfiles, safe .env examples, typed settings and actual lint/format/type/schema checks for code and configuration. Include YAML/actionlint, shell, Dockerfile and secret checks for files present; document scoped exceptions. |
| Behavior verification | Runnable focused backend and frontend/component tests plus the first useful journey scaffold/fixtures. Setup tests prove startup/configuration boundaries; develop adds actual feature acceptance/regression tests. A build or empty test suite is insufficient. |
| Containerized services | App-specific Dockerfiles and .dockerignore for each containerizable API/web/worker, a usable isolated Compose startup, migrations/readiness and owned data. Native clients use platform packaging; their Python services remain containerizable. |
| CI and release | GitHub Actions that install locked tools, run code/configuration/behavior checks, build relevant artifacts and retain redacted failure evidence. Release workflows define versions, immutable artifacts and intended registries. |
| Deployment and recovery | Document artifact promotion, required target/configuration/secrets, migrations, outcome verification and rollback/roll-forward. Implement target-specific automation when the target is agreed; an unknown target stays a blocker, not an invented cloud choice or pretend deploy job. |

Use delivery-pipelines for implementation and registry defaults. Demonstrate a clean-checkout command path and inspect the actual artifacts before declaring setup complete. Keep knowledge navigable rather than producing numerous ceremonial documents. Existing projects and tiny changes retain proportionate scope.

## Establish focused quality checks

Choose reproducible code, configuration and secret checks for the files and risks present; preserve accepted tools in existing projects. Use [quality-check references](references/quality-checks.md) for tool defaults, staged/full-tree scope and hook setup. Configure individual focused tools rather than a blanket Super-Linter dependency.

Local hooks provide fast feedback on intended staged changes; CI independently enforces required checks over its declared scope. Keep expensive platform/integration checks outside every commit. Document exact commands, ownership and exceptions, and verify the setup in the actual worktree. Git contributions owns safe staging and commit-time verification.

## Provide a reproducible local environment

For new containerizable services, default to Docker Compose for the frontend/API/workers and their actual dependencies: database, Redis/Valkey, queues, object storage or local email capture only where needed. Preserve a working existing setup unless changing it is in scope. Keep app-specific Compose/configuration beside application/development infrastructure and root entry commands as useful; do not move provider-required files or impose a template. Host-native hot reload can use the same dependencies when documented.

Provide one documented startup path, migrations, representative non-sensitive seed data, actual service/application readiness, shutdown and safe reset commands. Readiness must include required initialization; container start order alone is insufficient. Isolate Compose project names, ports, credentials and data per feature worktree/test run. Use explicit test stores/owned fixtures, persistent volumes for development data, pinned compatible images and bounded resources. Never reset an unspecified or shared database; destructive volume removal must be an explicit scoped action.

Make diagnostics available through an optional Compose profile or companion stack, with OpenTelemetry and a replaceable backend. Prefer SigNoz for a new unified local view when its supported footprint fits; use Langfuse for a concrete AI evaluation workflow. Preserve an accepted backend and avoid competing full stacks. Read [local environment references](references/local-environment.md) when implementing profiles, connectivity or backend setup; use observability-operations for deeper signal contracts when installed.

Native clients/simulators run on their supported host with documented service addresses. Control external effects through fixtures or explicitly opted-in sandboxes. Backend containers establish service behavior; actual native clients require their own checks through journey-testing.

## Include operating constraints in design

Use `security-and-privacy-design` for changed data flows and authority boundaries. Identify critical latency/concurrency constraints, durable state and meaningful recovery needs early; choose simple hosting that meets them. Bring capacity, cost and data-recovery guidance into design when relevant rather than treating them as production afterthoughts. Use `delivery-pipelines` when creating CI/CD. Do not introduce platforms or complete operations frameworks merely because their skills are available.

Agree the authoritative PRD/requirements, implemented architecture and target-design sources when establishing foundations. Use the project's existing work tracker or a lightweight ledger; add detail only when it answers a real decision. Keep operations observability and service-level definitions alongside runbooks, with candidate/approved/measured states explicit. Do not force a document tree or full planning ceremony on a routine fix.

## Keep foundations aligned as the project evolves

Treat repository structure, dependency/runtime choices, configuration contracts, scoped instructions and delivery commands as maintained project decisions. Update affected commands, lockfiles and authoritative documentation alongside a relevant change. Resolve conflicting instructions at their proper scope; avoid copying the same rules into every component. Use `documentation-conventions` for knowledge upkeep and `delivery-pipelines` plus installed GitHub Actions hardening for delivery mechanics; this skill coordinates the project conventions rather than duplicating specialist guidance.

Start a full setup or structural review only when requested. Apply existing conventions during feature work, and suggest a broader change when a concrete problem warrants it rather than silently migrating the application.

## Prove the affected capability

Verify the first slice through its real entrypoint, user-visible outcome and persistent/authority boundaries. Use the agreed scope to defer unrelated capabilities. Demonstrate startup/migration and affected platform/API paths, with fixture/live boundaries explicit. A scaffold or successful build establishes a narrower result than a working application. Keep commands and first-slice knowledge current and report missing checks through deliver-reliable-changes.

## Maintain configuration and supported dependencies

Treat application settings and flags as behavioral interfaces. Use typed/validated inputs, explicit precedence and a small set of useful defaults; reject invalid required settings/combinations without silently weakening authority. Distinguish build, startup and dynamic settings. Track the effective non-secret configuration revision and source of truth; inspect authorized effective values without dumping secrets or personal data. Configuration-only changes need proportionate tests and recovery just as code changes do.

Maintain the supported runtime/dependency set and update process alongside lockfiles. Routine upgrades need release-note/deprecation review, coherent coupled versions, meaningful tests and a recovery route even without a vulnerability. Keep changes focused; major upgrades are deliberate migrations, not silent modernization. Use vulnerability-management for security-driven priority when available. Flag unsupported/EOL choices with evidence rather than replacing them unasked.
