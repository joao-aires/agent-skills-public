---
name: browser-extension-delivery
description: Prepare or review Chrome MV3 release packages and Chrome Web Store readiness. Use for production ZIP contents, listing/privacy evidence, update compatibility and authorized upload/submission/publication; preserve existing CI and release policy.
user-invocable: false
metadata:
  scope: stack-specific
  invocation: both
  role: support
  stack: Chrome, Manifest V3, Chrome Web Store
  source: https://github.com/quangpl/browser-extension-skills/tree/249886cf8137086792b6c3a5a2f7adce117a9f8d
---

# Deliver the reviewed extension artifact

Establish the requested stopping point: readiness assessment, local packaging, upload, review submission or publication. Preparation does not imply authorization for the later actions. Reuse the project's CI, versioning and release authority. Use available general delivery, privacy/security and product expertise for shared decisions; without it, retain artifact traceability, compatible updates, truthful disclosure and controlled promotion using project evidence and current primary sources.

## Establish the release candidate

Build the accepted source with locked dependencies and production configuration. Determine the extension's actual browser version field, independently of an npm/package release label. Inspect the generated manifest and full packaged tree, including code/resources from dependencies. An extension store ZIP contains the built extension with `manifest.json` at its root, not the source repository or its parent build directory.

Use [release evidence and automation](references/release-evidence.md) for packaging and CI details. Keep the tested artifact's identity through promotion; rebuilding after verification can produce a different candidate. Check client data migrations and behavior changes for existing installations, especially permission changes and account/entitlement compatibility. Store delivery and browser update timing are asynchronous; do not promise immediate fleet-wide rollout or downgrade.

## Assess the listing and data flow

| Evidence | What to reconcile |
| --- | --- |
| Functional purpose | Actual extension behavior, advertised capabilities, installation/onboarding and accessible reviewer steps |
| Access requests | Generated grants, necessary site/API scope and user-facing permission justification |
| Data handling | Actual collection, local/off-device processing, recipients, retention and relevant disclosure/consent |
| Assets | Bundled icons and current store dimensions/formats; real screenshots of the candidate rather than placeholders |
| Executable content | Bundled code, CSP, dependencies and the current remotely hosted code rules |
| Commercial behavior | Accurate pricing/entitlement claims and permitted account/payment flows, if the product has them |

Verify current [Chrome Web Store policies](https://developer.chrome.com/docs/webstore/program-policies/policies), [review process](https://developer.chrome.com/docs/webstore/review-process) and dashboard requirements for the intended distribution. Policies and API versions change. A source scan can identify evidenced risks and missing information; it cannot guarantee approval, a rejection code or a review duration. Distinguish observed violations, plausible risks and questions requiring publisher evidence.

For review-only work, return findings with concrete artifact/source locations, impact and next checks. Repair only within the requested scope. Keep secrets, private user data and account credentials out of reports and screenshots. Ask only for unresolved publisher/product decisions that affect the release; ordinary technical facts should be investigated first.

## Separate preparation from external promotion

1. Assemble the candidate ZIP, local checks and listing/permission/privacy drafts. Return actual verification and remaining release blockers.
2. Before an authorized external action, establish the publisher/item identity, intended channel/visibility, exact artifact and credential mechanism. Use an existing configured account and the current API/tool contract. Do not request secrets in conversation or create publisher/cloud accounts as an implicit setup step.
3. Perform only the authorized stage. Uploading bytes, submitting for review and publishing to users are distinct effects. After an ambiguous response, inspect current item/version/review state before retrying; avoid duplicate submissions or promoting the wrong draft.
4. Verify the resulting item status and candidate identity using supported observations. An API success or completed CI job is not evidence that users received the version. Retain pending review/rollout and unavailable installed-version checks as explicit limits.

Existing trusted automation can authorize specific stages through its established policy; this skill does not add a new approval ceremony to already-authorized actions. It also does not create that authority from a Git tag or a passing test. Recovery planning must account for store/browser update constraints and compatible data; a newer corrective version may be required instead of an immediate rollback.

The [source notes](../../references/sources.md) record the upstream review and the primary publishing contracts.
