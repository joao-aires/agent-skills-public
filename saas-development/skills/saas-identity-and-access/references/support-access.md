# Support and administrative access

Use when operators, support staff or engineers can act on customer data or organization
state. The design question is not whether staff need access, but how much, for how long,
under whose authority and with what record.

## Separate access tiers

| Tier | Permits | Typical control |
| --- | --- | --- |
| Customer-visible diagnostics | Read scoped status, configuration and recent events. | Role-based staff permission; customer can see the access where promised. |
| Read-only customer data | Inspect records needed to diagnose an issue. | Reason, ticket link, time bound, data minimization. |
| Scoped impersonation | Act as a customer to reproduce a problem. | Explicit approval, short expiry, prominent indication, full audit. |
| Write or repair | Change customer configuration or data. | Higher approval, narrower scope, rollback or repair plan. |
| Break-glass emergency | Bypass normal approval during an incident. | Alerting, retrospective review, shortest possible duration. |

Prefer diagnostics and scoped tools over impersonation. A support engineer who can read a
tenant-scoped event log does not need the customer's password or a shared administrator
account.

## Make access a domain operation

For each access grant, record:

- the support actor and the customer/organization;
- the reason, ticket or incident;
- the scope (which resources, read or write);
- the approver where required;
- the start and expiry;
- the actions performed and the outcome;
- the customer notification or consent where the commitment requires it.

Support access should not be a permanent role that every engineer holds. Grant it for a
case, expire it automatically and revoke it when the case closes.

## Attribution and audit

Log the support actor separately from the customer. An action performed on behalf of a
customer should show both identities, not attribute the change to the customer or to a
shared "admin" account. Protect the audit trail from modification by the actor and retain it
according to the customer commitment.

Do not record passwords, tokens, full payment data or unnecessary personal data in the
support record. Record enough to reconstruct the action and its authority.

## Customer visibility and control

Decide whether customers can see, approve or revoke support access. Enterprise contracts
often require it; a small self-service product may not. Whatever the choice, do not claim
"no one can access your data" when staff can.

- Provide an access log or notification where promised.
- Let the customer deny or end access if the product offers that control.
- Distinguish support access from the customer's own administrator roles.
- Include subprocessors and provider support in the disclosure where relevant.

## Break-glass and recovery

Emergency access is necessary when the normal path is unavailable. Bound it:

- a separate, strongly authenticated path;
- alerting on use;
- a short session;
- a retrospective review with an owner;
- a documented reason and follow-up;
- rotation of any credential used.

Break-glass is not a permanent shared account. A successful emergency action does not
retroactively authorize unrelated access.

## Offboarding and review

- Remove support permissions when staff change role or leave.
- Review standing support roles and elevated permissions periodically.
- Revoke provider-side support sessions and shared credentials at case close.
- Check that a departed engineer's tokens and SSH keys are revoked, not only their product
  login.
- Keep the number of people who can grant emergency access small and known.

## Evidence

| Behavior | Evidence |
| --- | --- |
| Scoped grant | Actor can reach the intended tenant/resource and is denied another tenant. |
| Expiry | Access stops automatically at the agreed time. |
| Attribution | Audit shows support actor, customer and action separately. |
| Approval | Required approval is recorded before the action. |
| Customer visibility | Access appears in the customer log or notification where promised. |
| Break-glass | Alert, review and credential rotation follow the emergency use. |
| Offboarding | Departed staff lose support and provider access. |

A policy document and a role name do not establish that access is scoped or reviewed.
Inspect the actual grant, the audit record and the expiry behavior.
