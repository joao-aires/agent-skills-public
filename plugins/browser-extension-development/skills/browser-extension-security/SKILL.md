---
name: browser-extension-security
description: Design, implement or review Chrome MV3 permissions and extension trust boundaries. Use for manifest grants, content-script messaging, privileged fetch/injection, extension storage and browser-to-backend identity.
user-invocable: false
metadata:
  scope: stack-specific
  invocation: both
  role: support
  stack: Chrome, Manifest V3
  source: https://github.com/quangpl/browser-extension-skills/tree/249886cf8137086792b6c3a5a2f7adce117a9f8d
---

# Connect browser privileges to permitted operations

Trace what the feature reads, changes or sends, on which sites, for which actor and after which user action. Review source and built manifest together. A manifest grant permits the extension to use browser capabilities; it does not authorize every message, remote resource or backend account operation. Apply this method within the requested design, implementation or review scope.

## Derive grants from behavior

Build a small operation-to-access map. Check the actual API methods, accessed fields and supported Chrome versions in primary documentation instead of assigning a permission from a namespace name.

| Intended behavior | Decision to establish |
| --- | --- |
| Act on the current page after the user invokes the extension | Can temporary `activeTab` access and the needed API permission satisfy it? What happens on navigation or a restricted page? |
| Run automatically on known sites | Which content-script matches and host/API grants does the feature really require? |
| Enable an optional site integration | Can runtime optional host access preserve useful behavior when the user declines or revokes it? |
| Fetch from a backend in an extension context | Which fixed origins/endpoints need host access, and what separate application authorization applies? |

`activeTab` is temporary access following a qualifying invocation; merely querying the active tab or opening a popup URL in a test is not the same event. Broad host access can be necessary for a user-selected all-sites feature, but must be justified by that behavior and its disclosure. Never add it as scaffold convenience or remove it without preserving an explicitly required capability.

Read [permission and message boundaries](references/permissions-and-messages.md) for implementation and audit details. Verify denied/revoked access and the installed permission warning, not only the happy path. Recheck the production manifest after framework generation.

## Treat each context according to its trust

Page DOM, page events, content-script inputs and external messages can be attacker-controlled. The isolated JavaScript world and Shadow DOM do not make the shared page content trustworthy. A same-extension sender ID alone does not establish which operation a content script may request.

At the privileged handler:

- Define allowed sender contexts and validate message shape, resource identifiers and requested effects.
- Resolve privileged endpoints and operations from trusted application configuration.
- Bind a page-sensitive operation to the relevant tab/frame/document and current grant, accounting for navigation between request and completion.

Do not turn the worker into a generic arbitrary-URL fetcher, script executor or backend credential proxy.

For external messaging, explicitly constrain the intended peers and inspect sender information with the current API contract. Unknown operations and invalid payloads should fail without performing an effect or returning sensitive details. Bound request size, work and retries to the actual operation. Type declarations and grep scans are aids, not evidence that these boundaries hold.

## Keep secrets and backend authority in the right place

Anything distributed in the extension can be inspected. A build-time environment variable does not conceal a provider secret in emitted JavaScript. Public identifiers are different from confidential keys; use a trusted service when the feature genuinely requires a secret, without prescribing its language, database or identity provider.

Use the accepted authentication architecture and current browser/provider guidance for OAuth clients, redirects, scopes, token type and backend validation. Enforce account/resource/paid-feature authority at the trusted service where it matters. CORS and an extension ID are not authentication; configure allowed origins according to the actual deployment without relying on them for authorization. Hosted checkout can avoid embedding payment credentials, while webhook processing and entitlements remain server responsibilities.

Choose storage by lifetime and exposure. `storage.local` and `storage.sync` are not encrypted secret stores; review content-script access and use supported access controls where needed. Keep ephemeral sensitive state short-lived, scope stored data to the account/site that owns it, and define sign-out/revocation and migration behavior. Consent, disclosure and retention follow the real data flow, including analytics and off-device processing.

## Substantiate findings and fixes

Exercise permitted and denied messages, unsupported sites, absent grants, navigation races and applicable account/resource boundaries. Inspect production resources for remote executable code, excessive exposure and accidentally bundled credentials. Show the path from untrusted input to an actual effect before assigning exploitability or severity; absence of TypeScript or a matching grep result alone is not a vulnerability.

Use available general security/privacy expertise for broader threat and identity decisions; otherwise investigate with project evidence and [primary sources](../../references/sources.md). Return concrete findings, fixes when authorized, actual checks and remaining uncertainty. Store policy assessment belongs with [delivery readiness](../browser-extension-delivery/SKILL.md), and cannot guarantee approval.
