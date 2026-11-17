# Enterprise identity for SaaS tenants

Use when a customer cohort requires single sign-on, automated provisioning or domain-based
organization discovery. Establish the commercial commitment first: enterprise identity is a
supported product capability with setup, support and recovery obligations, not a checkbox.

## Decide the connection model

| Requirement | Questions |
| --- | --- |
| Single sign-on | Which protocol (SAML, OIDC) does the customer's IdP support, and who owns the connection configuration? |
| Provisioning | Does the customer need automated user/group lifecycle (SCIM), or is invitation-based onboarding sufficient? |
| Domain ownership | Must the customer prove control of an email domain before members can join or be auto-enrolled? |
| Role mapping | Are roles derived from IdP groups, assigned locally, or both? Which source wins on conflict? |
| Multiple IdPs | Does one organization need several connections, or is one connection per tenant sufficient? |
| Environment | Are test and production connections separate, with separate metadata and certificates? |

Do not add SSO or SCIM because a competitor lists it. Add it when the target cohort's
contract or operating model requires it, and resource the setup and support path.

## Single sign-on

- Bind the connection to the actual organization/tenant. An issuer and subject from one
  tenant must not authenticate into another.
- Verify signatures, audience, recipient, time conditions and replay protection with a
  compatible library; do not hand-roll assertion parsing.
- Decide whether just-in-time membership creation is allowed, what role it grants and
  whether domain verification is required first.
- Define session lifetime, logout behavior, IdP-initiated versus SP-initiated flows, and
  what happens to existing sessions when the connection changes.
- Keep a local break-glass administrator path for IdP outage, with alerting and review.
- Test certificate/metadata rotation and an expired or misconfigured connection.

Domain verification proves control of a domain at a point in time. It does not prove that
every user with that domain should join the organization. Decide whether verified-domain
auto-join is intended, and how existing accounts with conflicting membership are handled.

## SCIM provisioning

SCIM adds an external authority for membership lifecycle. Establish:

- the SCIM base URL, authentication method and tenant scoping;
- user and group resource mapping, including external ID stability;
- create, update, deactivate and delete behavior;
- group-to-role mapping and what happens to unmapped groups;
- pagination, filtering and delta behavior for large directories;
- duplicate email or external-ID handling;
- reconciliation when a provisioning event is missed or arrives out of order.

Deprovisioning is the consequential path. A deactivated user must lose organization access,
active sessions and personally owned credentials within the promised window. Decide whether
SCIM deactivation removes the local user entirely or only the membership; the customer
contract usually expects access removal, not account erasure.

SCIM is not a real-time guarantee. Reconcile the provider's directory against local
membership on a schedule, and provide an operator path for drift.

## Role mapping and least privilege

Map IdP groups to the smallest local roles that support the customer's work. Define:

- the default role for a user created by SSO or SCIM;
- what happens when a user belongs to no mapped group;
- whether local administrators may grant roles above the mapped role;
- how a mapping change affects existing members;
- who can change the mapping and how it is audited.

A group named "admins" is not proof of authority until the mapping is configured and
tested. Avoid mapping every provisioned user to an administrative role for convenience.

## Recovery and operating behavior

Enterprise identity creates new failure modes:

| Failure | Required behavior |
| --- | --- |
| IdP unavailable | Break-glass access works, is alerted and reviewed; ordinary users see an understandable error. |
| Misconfigured connection | Existing sessions are not silently granted broader access; setup can be corrected without deleting the organization. |
| Certificate expiry | Rotation is monitored before expiry; the failure is visible. |
| SCIM outage or missed event | Reconciliation detects drift and repairs membership. |
| Employee departure | Deprovisioning removes access and credentials within the accepted window. |
| Customer leaves | The connection, certificates, SCIM token and provisioned identities are revoked. |

## Evidence

- a successful SSO login mapped to the correct organization and role;
- a login from the wrong issuer/tenant rejected;
- JIT membership created with the expected default role;
- SCIM create, update, deactivate and delete observed locally;
- group-to-role mapping applied and an unmapped user handled as designed;
- IdP outage and break-glass access exercised;
- certificate or metadata rotation performed;
- deprovisioned user loses sessions and credentials within the promised window.

A configured connection in a dashboard is not evidence that login, mapping, provisioning or
deprovisioning works. Record which environments and identities were actually exercised.
