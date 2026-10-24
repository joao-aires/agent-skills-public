---
name: security-auth-development
description: Design, implement or review authentication, authorization and identity
  lifecycle across application stacks. Use for sessions, federation, passkeys, machine
  identity, tenant/resource access and contextual identity-framework selection.
license: MIT
metadata:
  scope: generic
  invocation: both
  role: support
  references: references/sources.md
user-invocable: true
---

# Establish identity and authority through the lifecycle

Authentication establishes which identity the application is dealing with. Authorization decides whether that identity may perform a particular action on a particular resource now. Design both around the application: a successful sign-in does not establish membership of a tenant, permission to change a resource, or access to a paid capability.

Read the accepted application, its clients and deployment. Trace where identity is established, how it is carried to trusted code, and where resource permissions are enforced. Then follow the events that change authority, including membership changes, session expiry and account recovery. Preserve accepted providers and protocols unless the request or evidence justifies reconsideration.

## Choose the smallest sufficient identity architecture

Separate browser, native, service and delegated-agent clients; their credential handling and trust differ. Compare relevant mechanisms; sessions, protocol clients, brokers and managed services can compose rather than being mutually exclusive:

| Approach | Questions that affect selection |
| --- | --- |
| Framework-native sessions | Can the application meet its required identity lifecycle within its existing framework? |
| Protocol client | Which authentication, delegated-access or provisioning protocols must the application integrate? |
| Identity broker/platform | Which federation and provisioning requirements justify operating a separate identity system? |
| Managed identity service | Do data location, cost and operating capability fit the service boundary? |

Compare required recovery, MFA/passkeys, enterprise federation/provisioning, data location, cost and operating capability across the candidates. Read [pattern selection](references/patterns-and-selection.md) when comparing approaches and [research sources](references/sources.md) for first-party contracts and inspected project examples. Reuse mature protocol/cryptographic implementations. A provider feature or starter is not evidence that the complete application boundary is protected.

For federation and account linking:

- Distinguish authentication, delegated access and provisioning.
- Bind the actual issuer/subject to the local identity; verify tokens and redirects with compatible libraries and current protocol guidance.
- Treat linking as an ownership operation. Matching email strings or a claimed organization domain alone does not prove authority.
- Define how existing sessions, linked providers and recovery methods interact.

## Enforce resource and tenant permissions

Choose a policy model that can express the application's actual rules. Roles work well for stable groups of privileges; attributes help with contextual conditions; relationships express ownership, sharing and inherited access. These can compose. Compare whether the model makes legitimate grants, removals and audits understandable before adding a separate policy service.

Place enforcement where the action or data access is controlled by trusted code. Check the actual resource being requested, including its tenant and relevant lifecycle state; a client-selected organization or role is input to verify. At each trusted enforcement boundary:

- Verify subject, resource, action, tenant and relevant lifecycle/context. Default-deny unknown operations and prevent authority from client-supplied role/tenant fields.
- Cover HTTP/API calls, jobs, exports, support tools and AI/MCP actions.
- Apply the same semantics to listing/search, related resources and bulk operations as to individual reads/writes.

Keep membership, authentication and paid entitlements distinct. Check the product's authority-changing flows:

| Concern | Establish |
| --- | --- |
| Invitation | Scope, expiry, intended recipient and permitted role grants |
| Ownership or privileged support | Accepted rules for transfer, last-owner removal and support access |

When using an external policy engine, establish model version, consistency, cache, availability and synchronization choices. Loading the engine does not settle them automatically.

## Make lifecycle and recovery explicit

Follow the credential or session from enrollment to removal. Establish how it is issued and stored, how the application checks it, when it expires, and how it is refreshed, rotated or revoked. Decide what logout means for the current client and any other active sessions. These decisions determine how long previously granted access can remain usable.

Match cookie/browser protections, native secure storage and service credentials to the actual client. Check how authorization changes reach existing sessions and caches, not only how the next sign-in works. Token format alone does not determine security.

- Bound stale authorization according to accepted risk; invalidate or recheck when relevant authority changes. JWTs do not automatically provide immediate revocation or current membership.
- Treat enrollment, recovery, factor changes, linking and deprovisioning as security-sensitive flows. Use appropriate proof of control, reauthentication/step-up and abuse limits without creating trivial account-lockout attacks.
- Define service-identity ownership, least privilege, automated rotation/revocation and effects of credential compromise.
- Keep audit evidence useful without recording tokens or recovery secrets.

## Verify behavior and preserve scope

Exercise the applicable behaviors:

- Allowed and denied resource operations, including cross-user/tenant requests.
- Expiry/revocation, recovery/linking, privilege changes and replay.
- Applicable provider/key-rotation or outage behavior.

Check stale caches and existing sessions against the accepted revocation window.

Use available implementation/test expertise or version-matched primary documentation when specialists are absent. Return the architecture, framework tradeoffs, authority/lifecycle contract and actual evidence.

Ask about unresolved consequential choices such as enterprise identity requirements or recovery policy; choose ordinary implementation details within accepted scope. Installing identity guidance does not authorize a provider account, migration, credential rotation or live configuration change.
