# Readiness evidence

Use this reference to choose evidence for a stated readiness claim. The rows are prompts, not a scorecard or a required sequence.

## Evidence table

| Area | Claim to establish | Credible minimum evidence | Frequent false pass |
| --- | --- | --- | --- |
| Reliability | The accepted journeys meet their objectives for the stated population and window. | SLI query and population, target/window, error-budget policy, observed data including started-but-unfinished work and missing-data behavior. | Endpoint availability multiplied into a journey claim; a target with no observed series or owner. |
| Observability and alerts | An operator can detect, localize and confirm recovery of the likely failures. | Symptom alerts with routing, no-data policy, dashboards or queries, linked runbook, sampled signal receipt in the selected backend. | A green dashboard, a running collector or a declared exporter with no query evidence. |
| Security and authority | The target enforces the intended identity, permission and data boundaries. | Target configuration, allowed and denied path checks, secret scope, administrative and break-glass path review. | A policy document, rendered security setting or single-tenant test treated as operating proof. |
| Capacity and failure behavior | Demand fits headroom and degradation is bounded under peaks, rollout surge and dependency failure. | Representative load or measured peak with units/window, quota and dependency limits, saturation behavior, controlled failure or degradation check. | Requests compared with node capacity only; no dependency limit, peak or failure case. |
| Recovery and rollback | Service can be restored within RTO and accepted data loss, and code rollback does not assume away irreversible data change. | Exercised rollback in a safe target, restore with recovery point and elapsed time, schema/compatibility check, duplicate-effect controls. | Backup job success; a previous image with an incompatible migration; replication treated as backup. |
| Runbooks, on-call and support | A responder can act and a customer can reach help for this cohort. | Exercised diagnostic path, routing and escalation test, current ownership, support entry point, status communication owner. | A runbook page or on-call schedule with no exercise or reachable owner. |
| Limits and open risks | Remaining limitations are explicit and owned. | Named owner, consequence, expiry or review condition, excluded populations and decision authority. | A "known issue" without owner, impact or end condition. |

## Failure signals

| Signal | What it may indicate | Next evidence |
| --- | --- | --- |
| No-data alerts are absent while dashboards appear healthy. | The system may be silent, not healthy. | Query the source series and the alert path directly. |
| An SLO has a target but no error-budget policy or owner. | Compliance cannot drive a decision. | The accepted decision rule, owner and response to budget exhaustion. |
| Alerts route to a channel with no acknowledged owner or runbook. | Detection does not become response. | Routing test, responder confirmation and a usable procedure. |
| Load evidence excludes dependencies, quotas, rollout surge or node loss. | Headroom is overstated. | Representative demand plus the limiting dependency and failure case. |
| Recovery evidence predates a schema, storage, key or topology change. | The proven path may no longer be the current path. | Re-run the path or mark recovery unverified. |
| Rollback reverts only the image while the migration is irreversible. | Application rollback cannot restore the service. | Compatibility analysis, forward fix or data-recovery path. |
| Readiness rests on one tenant, replica, region or provider account. | The claim is narrower than the cohort. | Evidence at the promised isolation and failure boundary. |
| A security control is evidenced only by policy or configuration. | Design is not operating effectiveness. | Target enforcement plus allowed and denied observations. |
| A launch depends on a manual step absent from the runbook. | The operating path is person-dependent. | Document, exercise and assign the step, or remove the dependency. |
| The same incident cause recurs without corrective evidence. | Readiness has not improved. | Corrective change, verification and updated runbook or alert. |
| Capacity headroom is measured at average, not peak or failure. | Normal operation hides saturation. | Peak demand, surge and degraded-mode behavior. |
| An open risk has no owner or expiry. | It cannot be accepted or tracked. | Decision owner, consequence and review condition. |

## Limits

- A checklist, green dashboard, certification or prior launch does not establish readiness for a different scope.
- Readiness is relative to a cohort, environment and next bounded action; there is no universal "production ready".
- Inspected configuration is not operating behavior, and one observation window does not cover every season, tenant or peak.
- Staging and load tests cannot establish production provider behavior, network paths or scale by themselves.
- Managed services move operational mechanics to the provider; they do not transfer accountability for the application's promises.
- Absence of evidence is unknown. Absence of an observed failure is not evidence of readiness.
- Readiness decays after material change, incidents, scale changes, provider/dependency changes or expired accepted limits.
- This assessment does not establish customer acceptance, legal compliance, commercial viability or permission to release.
- One assessment cannot silently cover environments, tenants, regions or populations that were not examined.

## Recording

When a durable record is needed, map the result into the [assurance assessment contract](../../artifact-system/references/contracts/assurance-assessment.md):

| Contract section | Readiness content |
| --- | --- |
| Applicability and scope | Service, consumers/cohort, environment, launch mode, period and exclusions. |
| Controls | Readiness criteria by area, with owner and expected evidence. |
| Evidence | Command or scenario, revision/target, population/window and result. |
| Gaps and exceptions | Defect, unresolved decision, missing execution/access or accepted limit, with impact and owner. |
| Disposition | Ready, ready with limitations or not yet ready; what is not claimed and who decides next. |
| References | SLOs, runbooks, test/load/failure results, recovery records, open risks and prior assessments. |

Reuse an existing launch or operations-readiness record instead of creating a second register.

Public background: [Google SRE launch checklist](https://sre.google/sre-book/launch-checklist/), [OpenSLO specification](https://openslo.com/specification/), [Prometheus alerting practices](https://prometheus.io/docs/practices/alerting/).
