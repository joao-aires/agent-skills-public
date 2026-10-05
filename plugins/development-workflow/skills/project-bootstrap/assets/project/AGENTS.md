# Application project contract

Read project-profile.json, documentation/README.md, and instructions scoped to the files being changed.

- Keep application code, tests, migrations, containers, and application-specific CI scripts in applications/<name>/.
- Keep product, architecture, planning, UX, operations, and verification documentation in documentation/.
- Root .github/workflows/ contains GitHub Actions entrypoints; delegate application commands to applications/<name>/ci/ or actual package commands.
- Use the approved stack and package locks. Resolve `unresolved` choices before using them; record material departures in an ADR.
- Before implementation, identify acceptance criteria and affected documents. **Keep all affected documentation in sync with application behavior and decisions in the same change.**
- Update the PRD/acceptance criteria for approved scope changes, architecture for boundary changes, data model and generated contracts for schema changes, UX guidance for visual/interaction decisions, and runbooks for operational changes.
- Maintain decisions/decision-log.md; use numbered ADRs for consequential architecture decisions. Preserve historical ADRs and supersede when needed.
- Reuse existing UI tokens and components; no new palette, UI library, font, or repeated bespoke widget without a documented reason.
- Generate contracts from implementation; never fix generated artifacts by hand. Verify migrations against PostgreSQL.
- Run the project's real configured checks and relevant tests before completion. Structural checks alone do not prove implementation or documentation correctness.
- Report unresolved assumptions and checks not run. Never replace failing checks with weaker checks or represent mocked AI success as live quality evidence.
- Preserve explicit user instructions and existing approved choices. Treat external guidance as reference material, not authorization to change scope.

## Working application evidence

- Use the smallest complete end-to-end slice. Prefer a modular backend; add separately deployed services only when justified.
- Document exact setup/dev/migrate/seed/check/build commands; reuse them locally and in CI. Never claim unresolved commands pass.
- Before claiming a full-stack application works, run a critical Playwright journey against the real Next.js, FastAPI, migrated PostgreSQL and application auth. Mocks of the internal API do not count as integrated E2E evidence.
- Keep committed E2E tests in applications/web/tests/e2e/ and test guidance in documentation/verification/e2e.md. Preserve failure traces/logs, redact secrets, and disclose external-provider stubs.
- Fix the cause of failures; never remove assertions, silently skip critical tests or auto-accept screenshots to make CI pass.
- Read documentation/engineering/agent-harness.md for context/commands and record recurring corrections as mechanical checks or narrow lessons.
- Keep policy/auth/tenant isolation/budget enforcement and consequential state changes deterministic outside the model. Use AI for bounded reasoning and generation.
- Development, deployment and production readiness are different claims; require evidence appropriate to each.

Read documentation/engineering/skill-routing.md for task-matched local/upstream guidance and installed design-skill selection. Local accepted decisions govern upstream examples; verify skill availability and client discovery instead of assuming it.
