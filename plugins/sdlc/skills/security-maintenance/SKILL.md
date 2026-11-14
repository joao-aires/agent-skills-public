---
name: security-maintenance
description: Maintain operational security surfaces by inventorying, rotating and retiring credentials and by triaging, remediating and verifying vulnerabilities across dependencies, images, infrastructure and deployed targets.
metadata:
  kind: activity
  origin: local
  scope: generic
  invocation: both
  role: task
  phase: maintenance
  pack: sdlc
  domain: security
---

# Security maintenance

Maintain the security surfaces that change without a feature release: credentials and vulnerabilities. Both follow the same operating loop: establish the authoritative inventory, connect each item to the actual consumer or deployed artifact, remediate within authority, verify the real target, and retain the residual risk.

Read [activity system](../activity-system/SKILL.md) for scope and stopping point.

## Choose the work

- **Credentials:** inventory, issue, rotate, revoke and retire secrets, keys and certificates. Read [credentials](references/credentials.md) for the lifecycle, [secrets architecture](references/secrets-architecture.md) for delivery design and [credential record](references/credential-record.md) for the metadata record.
- **Vulnerabilities:** triage scanner findings against the resolved component, image or deployed artifact, then remediate and rescan. Read [vulnerabilities](references/vulnerabilities.md), [patch management](references/patch-management.md) and [remediation record](references/remediation-record.md).
- **Recurring review:** reconcile both inventories with previous findings, retain original deadlines and ages, and prepare bounded changes. Do not reset a finding's age or accept risk merely to clear a dashboard.

## Operating rules

- Use the authoritative system of record for credential metadata and scanner findings. Link it; do not create a competing Markdown copy.
- Keep secret values out of reports, tickets, logs and generated artifacts. Record metadata and status, not values.
- Connect each finding or credential to the affected service, artifact and environment before deciding severity or remediation.
- Execute rotation, revocation, rollout, status and risk acceptance only within the job's explicit authority.
- Verify the replacement credential or fixed artifact is actually used by every affected consumer or target. A successful update, build or scan is not proof of closure.
- Hand an exposed credential or active exploitation path to [incident response](../incident-response/SKILL.md) when impact is live.

## Completion evidence

Report the inventory scope, findings by target, actions, verification, overdue or blocked work, residual risk and owner. Distinguish discovered, issued, migrated, verified, revoked, fixed, deployed and closed states. Use the ECR or the operations review for the durable summary; keep the detector and secret manager as the operational authorities.
