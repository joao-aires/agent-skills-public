---
name: runbook-engineering
description: Create, rewrite, exercise and audit operational runbooks for alerts,
  recovery or planned procedures with evidenced diagnostic branches, scoped actions,
  verification and reachable escalation.
metadata:
  scope: generic
  invocation: both
  version: '1.0'
  role: task
---

# Runbook engineering

Read [composition guidance](../../COMPOSITION.md) for optional expertise, fallback and scope.

Write the procedure a responder can use under pressure. A complete-looking template without established diagnostic knowledge creates false confidence.

## Modes and inputs

- **Interactive:** inspect the service/alert/procedure evidence, then ask for missing owner decisions and known handling.
- **Setup/feature:** create/update the affected procedures alongside monitors, contracts and release/recovery changes.
- **Recurring review:** audit changed or high-impact runbooks, broken links, stale signal identities and validation dates; patch evidenced gaps and track unresolved knowledge. Use a quality ratchet so unrelated legacy debt does not block every change.

Discover local publishing/navigation conventions, actual service/target identity, alert query/semantics, verified actions, dependencies and escalation. Preserve existing service-specific knowledge. For a live incident prioritize response; capture lessons for the runbook after stabilization.

Consult [references/runbook-guide.md](references/runbook-guide.md) for deeper implementation details when needed.

## Author and validate

1. State trigger/symptom, impact and applicability. Explain exactly what the signal measures and does not establish.
2. Provide numbered first checks with direct scoped queries/links/commands and expected observations. Resolve identity from contracts/configuration/live evidence, not shorthand naming.
3. Build diagnostic branches: observation -> hypothesis -> discriminating check -> next decision. Avoid “check logs” without specifying what to look for.
4. Give verified corrective actions with target, prerequisites, expected effect, blast radius, reversibility and stop conditions. Label untested procedures as such.
5. Define independent post-action verification and restoration of temporary controls. Pod readiness/alert recovery alone is not customer recovery.
6. State reachable owner/escalation routes and the evidence required for handoff; identify when escalation is the correct action.
7. Publish through the project's documentation workflow and connect alerts to the exact page. Renames need link migration, not assumptions based on monitor naming.
8. Check structure, placeholders, local links/navigation, provider query syntax and published reachability. Exercise representative steps in a suitable environment; record actual verification date/coverage.

## Completion evidence

Deliver changed runbooks, alert linkage, before/after gaps, deterministic checks, exercised paths and remaining unknowns. Assess diagnosis/action/recovery quality separately from formatting. A recurring audit should update stable findings rather than repeatedly score the same debt without a plan.
