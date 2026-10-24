# Permission and message boundaries

## Distinguish the grant mechanisms

Use [declared permissions](https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions), [activeTab](https://developer.chrome.com/docs/extensions/develop/concepts/activeTab) and each actual API method's documentation when deriving the manifest.

- `permissions` names API capabilities; `host_permissions` names site access. Some operations need both. `content_scripts.matches` selects static injection sites and can itself cause permission warnings.
- `optional_permissions` and `optional_host_permissions` make selected access available for runtime consent. Model request, denial and later revocation explicitly, with a useful fallback or a clear unavailable state.
- `activeTab` follows a qualifying user invocation and is revoked according to navigation/tab lifetime. It is not an always-on replacement for a feature that must run automatically.
- Access to sensitive tab properties differs from creating/updating tabs. There is no blanket `windows` manifest permission; check [the windows API's actual requirements](https://developer.chrome.com/docs/extensions/reference/api/windows).
- Restrict `web_accessible_resources` to resources and matching peers that actually need them. A content-script bundle is not a reason to expose every file in the extension.

Capture the functional reason for a grant so a reviewer can distinguish excess access from a necessary product capability. Verify the built package rather than relying only on a framework's source config.

## Validate at the privileged receiver

For each message operation, establish these checks before its effect:

1. Identify the permitted caller contexts using actual `MessageSender` fields. An extension-page-only operation should not become callable by any content script merely because `sender.id` matches. For page operations, establish the relevant tab/frame/document and allowed site.
2. Parse the message as untrusted data. Validate the operation, shape, sizes and identifiers; reject extra authority-bearing choices that the caller should not control.
3. Resolve sensitive destinations and authority on the trusted side. For example, a metadata lookup can accept a document identifier that resolves to a configured API route. Accepting a complete arbitrary URL transfers endpoint selection to the caller and needs a separate, defensible access policy, including redirects and credential handling.
4. Perform the operation with current grants and account/resource policy. Handle missing tabs, navigation and revoked access without switching targets or silently increasing permissions.
5. Return only the result the caller may receive. Give a bounded, non-sensitive error response on rejection or failure; do not leave callers waiting indefinitely.

When using callback-style asynchronous `sendResponse`, return literal `true` synchronously to keep the channel open and handle rejected work. Promise listener support depends on the supported browser/context version; check [the current messaging contract](https://developer.chrome.com/docs/extensions/develop/concepts/messaging) before choosing it. Separate internal and external messaging APIs and peer declarations.

Useful negative checks include an unknown operation, malformed payload, a content script calling an extension-page-only operation, an unexpected external peer, an ungranted site and a resource belonging to another account. Observe absence of the protected effect as well as the returned error.

## Inspect storage and code exposure

Use [storage area/access-level documentation](https://developer.chrome.com/docs/extensions/reference/api/storage) to decide which contexts can read each area. Local storage is persistent and inspectable; sync can replicate data across devices; session storage has a different lifetime and access default. Configure access deliberately where supported, clear appropriate state on sign-out and avoid assuming these APIs provide encryption or application authorization.

Review production executable resources and [MV3 CSP](https://developer.chrome.com/docs/extensions/reference/manifest/content-security-policy). Remote data is different from remotely hosted executable logic. Static bundled code, any WebAssembly and necessary sandbox pages must satisfy the current applicable browser/store rules. A blanket grep for `eval` or Base64 cannot establish a policy violation without examining context and data flow.

For broader implementation and assessment, consult [Chrome security guidance](https://developer.chrome.com/docs/extensions/develop/security-privacy/stay-secure) and the project's accepted security architecture. Confirm authentication and webhook processing through the selected backend's actual compatible libraries; never treat a CORS allowlist or client-side entitlement cache as the enforcement boundary.
