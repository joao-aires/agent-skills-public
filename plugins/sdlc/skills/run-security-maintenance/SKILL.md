---
name: run-security-maintenance
description: Run credential lifecycle and vulnerability remediation operations — inventory, issue, rotate, revoke and retire credentials, and triage, remediate and verify findings across dependencies, images, infrastructure and deployed targets.
metadata:
  kind: activity
  scope: generic
  invocation: both
  phase: maintenance
  domain: security
---

# Run security maintenance

Maintain the two security surfaces that change without a feature release: credentials and vulnerabilities. Stop at verified remediation or retained residual risk.

Read [activity system](../activity-system/SKILL.md) for scope and stopping point. This is an operations activity, not a security design or compliance assessment. Design decisions belong to [design-security](../design-security/SKILL.md), scoped code fixes to [harden](../harden/SKILL.md), and applicability and evidence to [run-compliance-assessment](../run-compliance-assessment/SKILL.md).

Both surfaces follow the same operating loop: establish the authoritative inventory, connect each item to the actual consumer or deployed artifact, remediate within authority, verify the real target, and retain the residual risk.

## Choose the work

- **Credentials:** inventory, issue, rotate, revoke and retire secrets, keys and certificates. Read [credentials](references/credentials.md) for the lifecycle, [secrets architecture](references/secrets-architecture.md) for delivery design and [credential record](references/credential-record.md) for the metadata record.
- **Vulnerabilities:** triage scanner findings against the resolved component, image or deployed artifact, then remediate and rescan. Read [vulnerabilities](references/vulnerabilities.md), [patch management](references/patch-management.md) and [remediation record](references/remediation-record.md).
- **Recurring review:** reconcile both inventories with previous findings, retain original deadlines and ages, and prepare bounded changes. Do not reset a finding's age or accept risk merely to clear a dashboard.

## Operating rules

- Use the authoritative system of record for credential metadata and scanner findings. Link it. Do not create a competing Markdown copy.
- Keep secret values out of reports, tickets, logs and generated artifacts. Record metadata and status, not values.
- Connect each finding or credential to the affected service, artifact and environment before deciding severity or remediation.
- Execute rotation, revocation, rollout, status and risk acceptance only within the job's explicit authority.
- Verify the replacement credential or fixed artifact is actually used by every affected consumer or target. A successful update, build or scan is not proof of closure.
- Hand an exposed credential or active exploitation path to [run-incident-response](../run-incident-response/SKILL.md) when impact is live.

## Completion evidence

Report the inventory scope, findings by target, actions, verification, overdue or blocked work, residual risk and owner. Distinguish discovered, issued, migrated, verified, revoked, fixed, deployed and closed states. Use the ECR or [Run operations review](../run-operations-review/SKILL.md) for the durable summary. Keep the detector and secret manager as the operational authorities.
