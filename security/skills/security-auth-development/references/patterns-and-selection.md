# Identity and access pattern selection

Use this reference when choosing an approach or checking a changed trust boundary. Consult actual versions and editions; the examples are comparison starting points, not installed dependencies or endorsements for every project.

## Match the client and authority

| Situation | Compare | Questions that change the choice |
| --- | --- | --- |
| Server-backed browser application | Opaque server sessions; federation with an application session | Cookie scope, CSRF/origin protections, session fixation/rotation, server-side revocation and cache staleness |
| Browser SPA or native client | Current OAuth/OIDC client guidance; browser backend mediation where suitable | Public-client secrets, PKCE, redirect binding, token exposure/storage, refresh and logout; native external user-agent and deep-link ownership |
| Enterprise users | OIDC/SAML federation and provisioning where required | Identity-provider ownership, organization mapping, joiner/mover/leaver lifecycle, SSO enforcement, break-glass and purchased edition |
| Services and automation | Workload identities, short-lived tokens, client credentials or scoped API keys | Issuer/audience, credential owner, least privilege, rotation, environment separation and delegation |
| User-delegated tools/agents | Resource-scoped delegated authority | Consent/scope, confused-deputy prevention, per-action resource checks and durable audit context |
| Collaboration and sharing | RBAC, ABAC, relationship-based permissions | Domain relationships, role explosion, contextual rules, consistency and centralized policy cost |

OAuth supplies delegated authorization protocols; OpenID Connect adds an identity layer. Provisioning and application resource policy remain distinct. Use [OAuth Security BCP](https://www.rfc-editor.org/rfc/rfc9700.html), [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) and [OAuth for native applications](https://www.rfc-editor.org/rfc/rfc8252.html) when selecting/implementing those boundaries. Verify current browser-specific guidance and framework defaults rather than freezing a token-storage recipe here.

## Compare implementation families

- Existing framework-native accounts/sessions are often sufficient when their lifecycle and security support meet the need. For Django, inspect [django-allauth](https://docs.allauth.org/en/latest/); for compatible TypeScript applications, inspect [Better Auth](https://better-auth.com/docs). Check the selected adapter, plugins, edition and application authorization separately.
- A standards-based broker such as [Keycloak](https://www.keycloak.org/securing-apps/overview) can centralize federation and identity administration across stacks. Evaluate hosting, upgrades, recovery, protocol/client configuration and organizational mapping.
- Composable identity services such as [Ory Kratos](https://www.ory.com/docs/kratos/self-service) provide identity/account flows; that component alone is not an OAuth/OIDC authorization server. Establish which additional components and responsibilities the architecture actually needs.
- A relationship authorization service such as [OpenFGA](https://openfga.dev/docs/authorization-concepts) can express resource sharing and inherited relationships. It complements authentication; model tests, policy versioning, relationship updates, consistency and fail behavior remain application decisions.
- A managed service can reduce some operating work while adding pricing, data handling, service availability, export/migration and contractual constraints. Verify actual required capabilities and editions from primary sources before selection.

Choose by project requirements and supported versions, not a universal preferred vendor. Preserve an adequate accepted solution. Seek technical implementation expertise by capability; missing a matching specialist does not require installing one or weakening verification.
