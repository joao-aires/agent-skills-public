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

Inspect what each configured check actually covers. Formatting, linting, typechecking and behavior tests establish different properties; a command or configuration filename alone does not prove coverage of the affected source. In mixed-language projects, verify file inclusion and compatible tool versions before treating a clean build as sufficient foundation evidence. Preserve an adequate existing toolchain rather than adding another tool for the same check.

## Match the requested change

Read the request, existing code and accepted decisions before choosing structure.

- For a new project, establish a useful first slice. For an existing application, identify which foundation the requested change actually affects and update only that part; do not repeat setup or start a repository-wide reorganization during ordinary feature work.
- State the smallest useful user journey and its observable acceptance criteria; carry forward answers already agreed.
- Resolve ambiguity that changes the product or data boundary, and make reversible implementation choices without another planning ceremony.
- Use the conversation as scope unless a separate spec is useful; require no tickets or tracker.

Use system-design after product refinement and for consequential feature architecture before dependent planning/implementation. Derive platform, runtime and service choices from accepted requirements and operating constraints; reuse an existing stack and layout unless changing them solves an agreed problem. Add AI or a protocol interface for a concrete capability. Select matching technical guidance only when available; its installation is not acceptance of that technology.

## Adopt an existing project and assess the change

Begin adoption by finding the repository's own route from checkout to running software. Read instructions and manifests, locate the startup/test/build/migration commands, and inspect the entry points those commands use. Trace a critical journey far enough to understand its service, data and identity dependencies. Check deployment definitions to understand the intended target, while keeping deployed state separate from repository intent.

Use that investigation to identify the conventions a contributor must preserve: component ownership, consumers, identity/tenant rules, configuration and operating constraints. Reuse existing instructions and add useful missing pointers. Installing the plugins grants no authority to restructure or modernize the application.

During a feature or fix, trace the affected paths and identify changed contracts, stored data, permissions, integrations, configuration and delivery consequences.

- Preserve useful legacy knowledge.
- Investigate contradictory code/docs and surface uncertainty that changes the outcome or risk; routine local choices can proceed.
- Keep this assessment inline for ordinary changes and record consequential decisions in the project's existing notes.
- Unrelated legacy debt remains separate unless it prevents the requested behavior.

Select verification through [deliver-reliable-changes](../deliver-reliable-changes/SKILL.md) and establish the objective workspace through [Git contributions](../git-contributions/SKILL.md) before foundation/feature writes. Those skills own the verification loop and worktree mechanics.

## Establish a small, navigable repository

- Keep code, migrations, tests, dependencies, configuration and scoped instructions discoverable within actual application/component boundaries. Preserve an established layout; choose a simple documented structure for a new repository. Keep provider-required entrypoints in their required locations.
- Put product and engineering knowledge under `documentation/`; use project knowledge organization and upkeep expertise to create only useful documents.
- Keep root AGENTS.md focused on purpose, stack, startup/test commands, shared conventions and the requirement to synchronize affected docs with code and decisions. Put component-specific commands and exceptions beside that component. Link authoritative information instead of duplicating it. For instruction-file authoring or pruning, seek available expertise in concise, scoped repository instructions and verify that required knowledge remains directly present or linked.
- Record compatible dependencies and lockfiles, required configuration and a safe local setup. Make it possible to start and verify the first slice without guessing secrets or commands.
- Add boundaries, services and infrastructure when a concrete requirement justifies them. Prefer domain-oriented code over layers with no present responsibility.

Use the relevant backend/frontend/AI skills and installed upstream expertise; do not assume a reference is installed. Preserve compatible installed UI/UX guidance without redistributing private material. Capture repeated corrections as a short scoped instruction or an executable check, rather than accumulating generic rules.

## Complete new-project foundations

For a requested new application setup, create and validate the following applicable artifacts. A local-only execution boundary still permits preparing CI, release and deployment procedures; it does not authorize running remote publication or deployment.

| Foundation | Prepare | Verify or distinguish |
| --- | --- | --- |
| Human onboarding | Authored root README linking each component README: purpose, architecture, prerequisites, configuration and install/start/migrate/test/build/shutdown/reset commands. | Replace starter text and empty files; AGENTS.md complements user-facing docs. |
| Dependencies and configuration | Compatible manifests/lockfiles, safe .env examples, typed settings, and lint/format/type/schema checks for code and configuration. | Validate the actual configuration and scripts with compatible checks, including secret detection; document scoped exceptions. |
| Behavior verification | Runnable focused backend and frontend/component tests plus the first useful journey scaffold/fixtures. | Setup tests establish startup/configuration; develop adds feature acceptance/regression. A build or empty suite is insufficient. |
| Build, packaging and local services | Reproducible definitions per deployable component; isolated real dependencies, initialization and readiness. | Containers use container build definitions when agreed; native clients use platform packaging. |
| CI and release | Selected-provider workflows using locked tools, code/configuration/behavior checks, artifact builds and redacted failure evidence. | Define release versions, immutable artifacts and intended distribution destinations. |
| Deployment and recovery | Promotion, target/configuration/secrets, migrations, outcome verification and rollback/roll-forward procedures. | Add target-specific automation when agreed; an unknown target stays a blocker, not an invented cloud choice or pretend deploy job. |

Use delivery expertise when available for delivery contracts, and matching technical guidance for selected provider, packaging and registry mechanics. Missing optional guidance does not remove the foundation outcomes above. Demonstrate a clean-checkout command path and inspect the actual artifacts before declaring setup complete. Keep knowledge navigable rather than producing numerous ceremonial documents. Existing projects and tiny changes retain proportionate scope.

## Establish focused quality checks

Choose checks according to the mistakes they can catch in this repository. A parser or schema validator catches malformed configuration; a type check catches incompatible interfaces within its model; a behavior test observes an operation; a secret scan inspects the material included in its declared scope. Use complementary checks where their failure modes differ, and keep their commands reproducible.

Preserve accepted tools in existing projects. Know whether each command examines staged files, the current tree, generated output or history before claiming coverage. Use matching stack and development-tool guidance for implementation details. Select checks with useful failures and clear ownership rather than adopting a blanket tool suite.

Local hooks provide fast feedback on intended staged changes; CI independently enforces required checks over its declared scope. Keep expensive platform/integration checks outside every commit. Document exact commands, ownership and exceptions, and verify the setup in the actual worktree. Git contributions owns safe staging and commit-time verification.

## Provide a reproducible local environment

Use the selected runtime and development-service mechanism for only the dependencies the useful slice needs. Keep application-specific configuration beside its owner and provide documented root entry commands where useful. Preserve a working environment; no container engine or hosted service is required merely to satisfy this method.

Provide startup, initialization/migrations, representative non-sensitive seed data, actual readiness, shutdown and safe reset commands.

- Isolate project identities, ports, credentials and data per feature worktree/test run.
- Use explicit owned test stores and appropriate development persistence.
- Never reset an unspecified or shared database; destructive cleanup needs the established target/action scope.

Make useful diagnostics queryable without introducing a monitoring vendor.

- Preserve an accepted backend; use available observability expertise for signal contracts and guidance for the selected development tools for selected service/backend configuration.
- Keep readiness and received telemetry as separate evidence.
- Control external effects through fixtures or explicitly opted-in sandboxes.
- Native clients and simulators require their supported host and actual platform checks; backend execution cannot establish client behavior.

## Include operating constraints in design

Assess changed data flows and authority boundaries, seeking matching security/privacy expertise when available. Identify critical latency/concurrency constraints, durable state and meaningful recovery needs early; choose simple hosting that meets them. Bring capacity, cost and data-recovery guidance into design when relevant rather than treating them as production afterthoughts. Use delivery expertise when creating CI/CD. Do not introduce platforms or complete operations frameworks merely because their skills are available.

Agree the authoritative PRD/requirements, implemented architecture and target-design sources when establishing foundations. Use the project's existing work tracker or a lightweight ledger; add detail only when it answers a real decision. Keep operations observability and service-level definitions alongside runbooks, with candidate/approved/measured states explicit. Do not force a document tree or full planning ceremony on a routine fix.

## Keep foundations aligned as the project evolves

Treat repository structure, dependency/runtime choices, configuration contracts, scoped instructions and delivery commands as maintained project decisions. Update affected commands, lockfiles and authoritative documentation alongside a relevant change. Resolve conflicting instructions at their proper scope; avoid copying the same rules into every component. Use project knowledge organization and upkeep expertise for knowledge upkeep and available delivery expertise for delivery contracts and matching technical guidance for implementation; this skill coordinates the project conventions rather than duplicating specialist guidance.

Start a full setup or structural review only when requested. Apply existing conventions during feature work, and suggest a broader change when a concrete problem warrants it rather than silently migrating the application.

## Prove the affected capability

Verify the first slice through its real entrypoint, user-visible outcome and persistent/authority boundaries. Use the agreed scope to defer unrelated capabilities. Demonstrate startup/migration and affected platform/API paths, with fixture/live boundaries explicit. A scaffold or successful build establishes a narrower result than a working application. Keep commands and first-slice knowledge current and report missing checks through deliver-reliable-changes.

## Maintain configuration and supported dependencies

Treat application settings and flags as behavioral interfaces.

- Use typed/validated inputs, explicit precedence and a small set of useful defaults; reject invalid required settings/combinations without silently weakening authority.
- Distinguish build, startup and dynamic settings.
- Track the effective non-secret configuration revision and source of truth; inspect authorized effective values without dumping secrets or personal data.
- Configuration-only changes need proportionate tests and recovery just as code changes do.

Maintain the supported runtime/dependency set and update process alongside lockfiles.

- Routine upgrades need release-note/deprecation review, coherent coupled versions, meaningful tests and a recovery route even without a vulnerability.
- Keep changes focused; major upgrades are deliberate migrations, not silent modernization.
- Use vulnerability prioritization and remediation expertise for security-driven priority when available.
- Flag unsupported/EOL choices with evidence rather than replacing them unasked.
