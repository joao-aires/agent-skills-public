# Sources and project interpretation

This original guidance draws decision patterns from standards and selected public implementation/documentation paths. No source code, upstream instructions or product defaults are copied into the package. A reference example is not a complete security audit or a reason to select its stack.

| Project and reviewed revision | Inspected boundary | Guidance informed |
| --- | --- | --- |
| [Keycloak](https://github.com/keycloak/keycloak/blob/7c62788efa63ebe99531f29de41ba9c7bf753c5c/docs/documentation/server_admin/topics/identity-broker/first-login-flow.adoc) | First-broker-login and account-linking flow; Apache-2.0 repository | Account linking needs ownership proof and an explicit identity mapping; email coincidence alone is insufficient. |
| [Better Auth](https://github.com/better-auth/better-auth/blob/fb48619083d292639797eaa3c7168a010f1e3308/packages/better-auth/src/plugins/organization/routes/crud-invites.ts) | Organization invitations and verification conditions; MIT repository | Separate invitation capability, recipient identity, membership and role-grant authority. Defaults vary with configuration. |
| [Ory Kratos](https://github.com/ory/kratos/blob/b86338da04a040247a07f46100a86dcfb3875909/examples/go/session/tosession/main.go) | Session-validation example and first-party self-service documentation; Apache-2.0 repository | Validate sessions through the actual supported boundary and distinguish identity flows from OAuth authorization-server responsibilities. |
| [OpenFGA](https://github.com/openfga/openfga/blob/fb8e7df866742a0c947e3066919ee59ac9e70eea/docs/check/README.md) | Relationship-check semantics; Apache-2.0 repository | Model resource authorization independently of login and reason about inherited relationships and policy evaluation. |

## Primary references to consult conditionally

- For login/recovery/factors: [OWASP authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html), [session management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) and [WebAuthn](https://www.w3.org/TR/webauthn-3/); check recommendation status and actual platform support.
- For resource authority: [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).
- For federation: [OAuth Security BCP](https://www.rfc-editor.org/rfc/rfc9700.html), [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html) and the selected provider's documentation.
- For implementation choice: the links in [pattern selection](patterns-and-selection.md). Review maintenance, advisories, licensing, editions, interoperability and actual deployment capabilities before acceptance.

Source references in metadata support attribution/discovery; they do not implement routing, install software or grant external authority.
