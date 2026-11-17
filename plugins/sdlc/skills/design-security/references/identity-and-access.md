# Identity and access design

Use this reference when a change introduces or moves authentication, sessions, federation, passkeys, machine identity, recovery or resource and tenant permissions.

Authentication establishes which identity the application is dealing with. Authorization decides whether that identity may perform a particular action on a particular resource now. Neither one establishes membership of a tenant, permission to change a resource, or access to a paid capability. Keep those questions separate even when one product feature or provider appears to answer all of them.

## Separate the questions

| Question | What it establishes | What it does not establish |
| --- | --- | --- |
| Authentication | Which identity is present, and how that was proven | Membership, role, entitlement or resource access |
| Session | How the authenticated state is carried to trusted code | Current authority after a role or membership change |
| Federation | Trust in an external issuer and its subject | Local organization mapping or permission |
| Provisioning | Which accounts and groups exist in the application | That the next request is authorized |
| Authorization | Whether this subject may act on this resource now | Identity quality or business entitlement |
| Entitlement | Whether the tenant or plan includes a capability | Permission for a specific user or resource |
| Delegation | Whose authority a client or provider exercises | That the delegation is still intended or narrow |
| Audit | What was attempted, allowed and changed | That the control was correctly designed |

## Choose the smallest sufficient identity architecture

Separate browser, native, service and delegated-agent clients; their credential handling and trust differ. Sessions, protocol clients, brokers and managed services can compose rather than being mutually exclusive.

| Approach | Questions that affect selection |
| --- | --- |
| Framework-native sessions | Can the application meet its identity lifecycle within the existing framework and deployment? |
| Protocol client | Which authentication, delegated-access or provisioning protocols must the application integrate? |
| Identity broker/platform | Which federation and provisioning requirements justify operating a separate identity system? |
| Managed identity service | Do data location, cost, operating capability and exit terms fit the service boundary? |
| External policy service | Do authorization rules, scale, consistency and audit needs exceed what application code can own clearly? |

Compare required recovery, MFA/passkeys, enterprise federation and provisioning, data location, cost and operating capability across the candidates. Reuse mature protocol and cryptographic implementations. A provider feature or starter is not evidence that the complete application boundary is protected.

Read [identity and access pattern selection](patterns-and-selection.md) for client/authority matching and candidate implementation families.

## Federation and account linking

- Distinguish authentication, delegated access and provisioning. OAuth supplies delegated authorization; OpenID Connect adds an identity layer; provisioning and application resource policy remain separate.
- Bind the actual issuer and subject to the local identity. Verify tokens, redirects, audiences and nonces with compatible libraries and current protocol guidance.
- Treat linking as an ownership operation. Matching email strings or a claimed organization domain alone does not prove authority.
- Define how existing sessions, linked providers, factors and recovery methods interact when a link is added or removed.
- Map organizations and groups deliberately. A directory group is input to a local policy decision, not automatically a tenant role.
- Keep joiner, mover and leaver behavior explicit, including what happens when the identity provider is unavailable.
- Provide a sanctioned break-glass path for enterprise SSO without creating a permanent bypass.

Consult the [OAuth Security BCP](https://www.rfc-editor.org/rfc/rfc9700.html), [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html) and [OAuth for native applications](https://www.rfc-editor.org/rfc/rfc8252.html) for the boundaries they cover. Verify current browser and framework guidance instead of freezing a token-storage recipe here.

## Resource and tenant authority

Choose a policy model that can express the application's actual rules. Roles work well for stable groups of privileges; attributes help with contextual conditions; relationships express ownership, sharing and inherited access. These can compose. Compare whether the model makes legitimate grants, removals and audits understandable before adding a separate policy service.

Place enforcement where trusted code controls the action or data. At each enforcement boundary:

- Verify subject, exact resource, action, tenant and relevant lifecycle or context. Default-deny unknown operations.
- Prevent authority from client-supplied role, tenant or entitlement fields.
- Cover HTTP/API calls, jobs, exports, support tools and AI/MCP actions.
- Apply the same semantics to listing, search, related resources and bulk operations as to individual reads and writes.
- Check the resource after every state transition that can change ownership or visibility.

Keep membership, authentication and paid entitlements distinct. Check the authority-changing flows the product actually has:

| Concern | Establish |
| --- | --- |
| Invitation | Scope, expiry, intended recipient, permitted role grants and what happens if the recipient already has an account |
| Ownership transfer | Who may initiate it, who must accept it, and what happens to prior access |
| Last-owner removal | Whether the tenant can become unadministrable, and the recovery path |
| Privileged support access | Consent, scope, duration, audit and revocation |
| Sharing and inheritance | Whether a grant can leak through a parent, group or link |
| Deprovisioning | Which sessions, tokens, links and entitlements end, and when |

When using an external policy engine, establish model version, consistency, cache, availability, synchronization and fail behavior. Loading the engine does not settle them automatically.

## Sessions and credential lifecycle

Follow the credential or session from enrollment to removal. Establish how it is issued and stored, how the application checks it, when it expires, and how it is refreshed, rotated or revoked.

- Decide what logout means for the current client and for other active sessions.
- Match cookie and browser protections, native secure storage and service credentials to the actual client.
- Bound stale authorization according to accepted risk; invalidate or recheck when relevant authority changes.
- Do not assume a token format provides immediate revocation or current membership. JWTs can remain valid after a role or tenant change.
- Treat enrollment, recovery, factor changes, linking and deprovisioning as security-sensitive flows. Use appropriate proof of control, reauthentication or step-up, and abuse limits that do not create a trivial account-lockout path.
- Give service identities an owner, least privilege, automated rotation or revocation, and a defined effect of compromise.
- Keep audit evidence useful without recording tokens, recovery secrets or factor values.

Token format alone does not determine security. The issuance, validation, storage, lifetime and revocation path do.

## Revocation and change propagation

Authority changes in more places than the next sign-in: membership removal, role change, plan downgrade, provider unlink, password reset, device loss and offboarding.

- Define the acceptable window during which stale authority may remain usable.
- Check how the change reaches existing sessions, cached decisions, tokens and delegated grants.
- Invalidate or recheck when the resource, tenant or entitlement changes, not only when authentication expires.
- Test revocation at the consumer and target that actually enforce it; a status change in an admin console is not proof.
- Check provider key-rotation and outage behavior when the application depends on external validation.

## Machine identity and delegation

- Prefer scoped workload identities and short-lived tokens over shared long-lived secrets. Validate issuer, audience, subject and target restrictions.
- Separate environments and least-privilege roles; a build credential should not also administer production.
- Prevent confused-deputy behavior: a service acting for a user must check the user's authority for the exact resource, not only its own.
- Keep delegated scopes narrow and re-check the resource per action, including durable tool or agent context.
- Record the credential owner and the operation that consumes it so rotation and revocation have a target.

## Verify the design

- Allowed and denied operations for the intended user, another user and another tenant.
- Listing, search, export and bulk operations against the same rules as a single read.
- Expiry, logout, revocation, recovery, linking, factor change and deprovisioning.
- Role, membership and entitlement changes against existing sessions and caches.
- Service credential rotation, provider key rotation and provider outage behavior.
- Replay of a used token, code or invitation, and a repeated request after an uncertain result.

Record the authority and lifecycle contract, the accepted revocation window and the evidence actually observed. Leave unresolved identity choices — enterprise requirements, recovery policy, provider selection — with the owner who can decide them.
