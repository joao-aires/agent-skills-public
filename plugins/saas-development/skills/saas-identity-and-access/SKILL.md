---
name: saas-identity-and-access
description: >-
  Expertise and methods for SaaS identity and access. Design or assess SaaS organization
  authority beyond basic authentication, including membership, roles, invitations, ownership
  transfer, SSO/SCIM, machine identity, support access, tenant isolation and revocation. Use
  when hosted-product access crosses organizations, enterprise customers or operational staff.
  It informs the activity that composes it; that activity owns the decision and stopping
  point.
license: MIT
metadata:
  kind: method
  domain: saas
  phase: design
  scope: generic
  invocation: both
  references: ../../references/sources.md
user-invocable: true
---

# Govern organizations, membership and delegated access

Authentication establishes an identity. A hosted product still has to decide which
organization that identity belongs to, what it may do there, how it got that authority and
how quickly the authority can be removed. Those are product and tenancy contracts, not
properties of a sign-in library.

This method owns the SaaS organization and access model. General authentication,
session and authorization mechanics belong to security design; privacy and
data-flow decisions belong to security design; tenant and lifecycle decisions
belong to `saas-design`. Use those capabilities where the question is theirs, and keep the
organization contract explicit here.

Start from the accepted organization model, current roles and the customer cohorts the
product serves. Do not add enterprise identity, machine credentials or support
impersonation merely because a reference product has them. Each capability adds authority
that must be granted, reviewed, audited and revoked.

## Reading path

| Need | Read |
| --- | --- |
| Organization, membership, roles, invitations, ownership and removal | [Organization model](references/organization-model.md) |
| SSO, SCIM, domain verification, role mapping and break-glass | [Enterprise identity](references/enterprise-identity.md) |
| API keys, service accounts, scopes, rotation and ownership | [Machine identity](references/machine-identity.md) |
| Support and administrative access, approval, attribution and audit | [Support access](references/support-access.md) |
| Authentication, sessions, policy enforcement and revocation mechanics | Security design guidance |
| Data minimization, retention and provider flows | Security design guidance |
| Tenant isolation, lifecycle and customer closure | `saas-design` |

## Model the organization

Define the entities the product actually needs: user, organization, workspace, membership,
role, invitation, service account and ownership. Decide whether a workspace is a billing
unit, a resource boundary or merely a view; those choices affect every permission check.

- A person may belong to several organizations; membership is per organization and can
  differ in role.
- A customer may pay for one organization while operating several workspaces.
- A resource has one owning tenant even when several users can access it.
- Guests and external collaborators are members with narrower scope, not a separate
  security model.
- Organization deletion and ownership transfer are domain operations with preconditions,
  not cascading deletes.

Read [organization model](references/organization-model.md) for the relationships,
invariants and evidence.

## Define roles and invitations narrowly

Separate organization administration, resource permission and paid entitlement. A role
describes what a member may do; a plan describes what the organization bought; a resource
policy describes access to a particular record. Do not collapse them into one flag.

- Grant the smallest role that supports the member's work; make privileged roles explicit.
- Decide who may invite, what role an invitation may carry and whether invitations expire.
- Bind an invitation to the intended recipient and organization; possession of a link is
  not proof of authority.
- Prevent removal of the last owner and define an ownership-transfer path with an auditable
  acceptance.
- Propagate role and membership changes to active sessions, caches, jobs and exports.

Read [organization model](references/organization-model.md) for invitation, ownership and
last-owner rules.

## Add enterprise identity only when promised

SSO and SCIM are customer commitments with operating consequences: per-tenant IdP
configuration, certificate rotation, provisioning reconciliation, role mapping and a
recovery path when the IdP or provisioning is unavailable. Add them when a target customer
or contract requires them, not as a generic maturity marker.

- Treat authentication, delegated access and provisioning as separate protocols.
- Verify the issuer and subject against the local tenant; do not trust an email domain
  alone as proof of organization membership.
- Define just-in-time membership and SCIM as different onboarding models with different
  failure and removal behavior.
- Provide a bounded break-glass path for IdP outage and record its use.

Read [enterprise identity](references/enterprise-identity.md) for the connection, mapping
and recovery decisions.

## Issue and revoke machine identity

API keys, service accounts and OAuth clients act without a human present. They need an
owner, a purpose, a scope, an expiry or rotation plan and a revocation path that takes
effect within the promised window.

- Scope credentials to a tenant, environment and set of actions; avoid account-wide keys.
- Show a secret once and store a hash or provider reference, not the secret itself.
- Support overlapping rotation and immediate revocation; record last use.
- Detect orphaned credentials whose owner has left or whose integration is retired.
- Keep agent and automation credentials narrower than the human who authorized them.

Read [machine identity](references/machine-identity.md) for the credential model and
evidence.

## Bound support and administrative access

Operational staff may need to diagnose or repair customer state. That access is a
privileged domain operation, not an invisible superuser. Make it scoped, time-bound,
attributable and visible to the customer where the commitment requires it.

- Prefer read-only diagnostics and scoped tools over shared accounts or broad impersonation.
- Require a reason, an approver where risk warrants it, and an expiry.
- Log the support actor and the customer action separately; do not attribute support work
  to the customer.
- Keep break-glass emergency access alerting and retrospectively reviewed.
- Remove support access when the case closes and when staff leave.

Read [support access](references/support-access.md) for the tiers, approval and audit
decisions.

## Carry tenant isolation through authority

Every trusted boundary must resolve the tenant from verified context, not from a
client-supplied organization ID or role. Check the subject, resource, action, tenant and
relevant lifecycle state together. Apply the same rules to API calls, jobs, exports,
support tools, search and AI/tool actions.

Stale authority is still authority. Define how long a removed membership, changed role or
revoked credential remains usable in sessions, caches and tokens, and test the actual
window. A short-lived token does not by itself provide immediate revocation.

## Verify and report

Exercise the behaviors that carry authority:

- allowed and denied cross-organization access;
- invitation expiry, replay, wrong recipient and role escalation;
- last-owner removal and ownership transfer;
- SSO login, SCIM create/update/deactivate and IdP outage where promised;
- API key rotation, revocation and cross-tenant denial;
- support access grant, expiry, attribution and customer visibility;
- membership change propagation to an existing session or cached decision.

Return the organization model, role and invitation rules, identity connections, credential
lifecycle, support-access contract, evidence and remaining gaps. Installing an identity
provider, changing a live IdP connection or accessing customer data requires separate
authorization.
