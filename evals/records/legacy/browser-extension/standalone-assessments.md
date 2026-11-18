# Browser-extension standalone assessments

Prepared 2026-10-21. Scope: planning/readiness only, using the permitted browser-extension package and primary public Chrome documentation. The two scenarios below are independent. Scenario 1 is local-only; scenario 2 retains its existing backend.

## 1. Plain JavaScript MV3 page annotator

**Assessment:** A small plain JavaScript extension is sufficient. Keep the accepted JavaScript implementation and use ordinary packaged extension files. There is no requirement for React, TypeScript, WXT, CRXJS, a component library, a backend or an account system. The available extension guidance can support this plan without acquiring optional frontend, general security or delivery specialists.

### Proposed first slice

Assume the first slice annotates the current page's main document only after the user clicks the toolbar action, with a visible result and an undo/remove action. The exact annotation rule and supported sites remain product decisions; do not silently expand this into automatic browsing-history collection, all-frame processing or persistent cross-site annotations. For this scoped baseline, page annotations last for the document's lifetime. Durable annotations would need a separately defined data/retention and restoration design.

| Context/file | Scoped responsibility |
| --- | --- |
| `manifest.json` | MV3 metadata, toolbar action, a service-worker entrypoint and only justified permissions. |
| Service worker | Register the action handler synchronously at module initialization. Capture the invoked tab, invoke packaged annotation code for that target and report success/failure. Keep this operation short. |
| Injected content code | Read only the content needed for the annotation, manipulate the shared page DOM and own cleanup/undo. Keep DOM work out of the worker, which has no page DOM. |
| Packaged styles/icons | Use scoped annotation classes and locally packaged assets. Avoid global resets or styles that change unrelated site content. |

For this user-invoked operation, start with `activeTab` plus `scripting`, without persistent host permissions or `<all_urls>`. A qualifying action invocation grants temporary access; active-tab queries and directly opening an extension URL are not equivalent grants. Cross-origin navigation and tab closure revoke access, while same-origin navigation can retain it. Restricted pages remain unsupported. Target the main frame by default; broader frame access requires its own need and evidence. See [Chrome activeTab](https://developer.chrome.com/docs/extensions/develop/concepts/activeTab) and [scripting](https://developer.chrome.com/docs/extensions/reference/api/scripting).

A toolbar click handled by the worker can supply the first slice without a popup. If a popup later becomes necessary for annotation input, keep accepted input/progress outside its disposable DOM and verify actual dismissal/reopening. Do not rely on the popup staying open to finish work.

The content operation should be idempotent: a second invocation updates or removes its owned annotation rather than duplicating nodes, listeners and styles. Treat page text as untrusted. Insert text with safe DOM APIs; do not interpret page-derived strings as HTML or executable code. Preserve links, editable controls, page event handling and unrelated DOM state. Use narrow CSS for simple annotations; introduce Shadow DOM only if a substantial embedded control needs it, then verify focus, tokens and event behavior. Shadow DOM is not an authorization boundary.

No runtime message bridge is needed merely to add one. If one is required, define a small fixed operation and bounded payload, permitted sender contexts and target tab/frame/document. Validate at the privileged receiver; a matching extension ID alone does not authorize a content script to perform every worker operation. Never accept arbitrary fetch destinations or script strings from the page. Navigation/disconnection must fail safely against the original target, with no replay on another tab.

Keep transient annotation state in the content context for this baseline. Add `storage` only if accepted preferences or durable user work require it; browser storage is inspectable, not a secret store. Worker globals are temporary caches. Any future durable job must persist its accepted state before acknowledgment and recover without duplicated effects after a restart. No secret-bearing operation currently justifies a backend.

### Verification plan, not results

Use the project's existing tools if later implementation is authorized. Do not replace its runner or install a new driver just because the guidance gives an example.

1. Inspect the eventual project instructions, scripts/lockfile, minimum Chrome version, authored manifest and production output. Build only with its accepted production process. Check the emitted manifest and every referenced resource, grants, CSP, bundled code and absence of development-server URLs. Source configuration alone is insufficient.
2. Use focused unit checks for annotation matching, idempotency/cleanup and any message validation. These establish logic, not browser permissions or extension lifetime.
3. Load the production artifact into a disposable supported Chrome/Chromium profile using an already available compatible driver or a scoped manual setup. Record the actual browser executable/version, driver/version, source revision and artifact identity. Do not use a personal profile. If no driver is available, retain independent static checks and record real-browser integration as unverified.
4. Invoke the actual toolbar action on a controlled page. Independently inspect the page for the intended annotation and undo result; a success response alone is insufficient. Confirm no page effects before invocation, no duplicate annotation on repeated clicks and correct behavior on empty/no-match pages.
5. Exercise cross-origin navigation, reload, tab closure and permission loss during work, plus restricted pages. Confirm useful errors and no effects on another tab or stale document. Test SPA changes/reinjection if supported. Do not infer activeTab coverage from a popup rendered in an ordinary tab.
6. Verify keyboard access, visible focus, readable labels/contrast, zoom, long content and hostile host CSS. Preserve page interactions. If annotation controls are injected, verify focus entry, Escape and restoration in their actual DOM boundary.
7. Terminate the declared worker through a supported test mechanism, then invoke the action again externally and confirm handling still works without duplicated state. Distinguish forced termination from idle suspension; attached DevTools can affect worker lifetime. No artificial keep-alive is part of the design.

Without optional frontend/accessibility, security/privacy or delivery specialists, retain these outcomes using the extension guidance, existing tools, rendered inspection and primary documentation. Their absence does not justify installing guidance, changing stacks or declaring a reduced standard. It limits specialist coverage; it does not make permission, DOM-safety, packaging or real-surface checks optional. This request authorizes planning only, so none of the implementation or runtime steps above was executed.

## 2. Chrome/MV3 release readiness and local packaging plan

**Assessment:** Not release-ready on the supplied facts. Local preparation can proceed without a publisher connection. Preserve GitLab CI and the Django/PostgreSQL backend, along with their accepted authentication, deployment and release controls. There is no basis for a migration to GitHub Actions, another backend/database, a new identity provider or a global uploader.

| Supplied fact | Readiness consequence | Scoped next step |
| --- | --- | --- |
| ZIP encloses the extension in `dist/` | Packaging blocker if its manifest is at `dist/manifest.json`. Chrome requires the manifest at ZIP root. | Package the contents of the actual production extension root, retaining their relative paths. Inspect the archive afterward. |
| One listing screenshot is a placeholder | Listing evidence is incomplete. It cannot count as a truthful screenshot of the candidate. | Replace it with a real candidate capture, or remove it if the remaining listing still meets requirements. Validate every retained asset. |
| No publisher connection configured | Upload/submission/publication are unavailable in this assessment; publisher identity and item status are unknown. | Record the external boundary. No account creation, credential setup or uploader installation. |
| Existing GitLab CI | Accepted delivery infrastructure. | Describe local verification/build/package stages within the existing pipeline; no pipeline edits in this task. |
| Django/PostgreSQL backend | Accepted backend; its existence does not establish security or compatibility. | Verify extension-to-service contracts and relevant update/auth behavior later, preserving the stack. |

The ZIP and screenshot issues are user-reported facts, not independently observed archive/image findings. Their exact paths, contents and severity within the real candidate cannot be verified because no application/artifact inspection was authorized or performed. A missing publisher connection is not itself a code or store-policy violation.

### Local candidate plan

1. Identify the accepted source revision, release version, lockfile, production build command and actual extension output root from the project when authorized. In a multi-target build, do not assume every directory named `dist` is the loadable root. Use the existing GitLab runtime/cache/artifact policy and locked dependencies; no tools or packages are installed by this assessment.
2. Build with the accepted production configuration. Inspect the generated MV3 manifest, entrypoints, referenced assets, permissions, web-accessible resources, CSP and intended service endpoints. Check for accidentally included secrets, private data, test credentials, development-server references and remote executable logic. Contextual review is required; a string scan alone cannot establish a vulnerability or policy violation.
3. Check the manifest's actual `version`, independently of package labels. Chrome uses one to four dot-separated integers with defined bounds; an npm prerelease suffix is not automatically valid. For an update, establish a version higher than the existing release once that release identity is known. [Chrome version rules](https://developer.chrome.com/docs/extensions/reference/manifest/version).
4. Create a new ZIP outside the production root, adding that root's **contents**, rather than the parent directory. The expected listing starts with `manifest.json` and its sibling resources, not `dist/manifest.json`. Preserve internal resource paths; do not rewrite valid manifest paths merely to compensate for an erroneous enclosing folder. Check archive entries, JSON parsing, missing references, accidental source/backend files, private content, junk directories and nested archives. Source-map inclusion is a deliberate exposure decision, not inherently a violation. [Chrome package preparation](https://developer.chrome.com/docs/webstore/prepare).
5. Extract the ZIP into a fresh temporary directory and load that exact unpacked candidate in an isolated supported browser. Exercise the main journey and negative/lifecycle cases appropriate to the extension. Record production-browser identity and outcomes. Test relevant previous-version data migration, permission changes and backend/API compatibility; a clean-install pass does not prove update safety. Do not contact a production backend as an implicit test action.
6. Capture the candidate's functioning UI on controlled non-private content. Current screenshot guidance specifies at least one screenshot, depicting the actual experience, with square corners/full bleed at 1280×800 or 640×400. Verify required icons and promotional assets against the same current guidance. A placeholder is unfinished even if it has valid dimensions. [Chrome listing images](https://developer.chrome.com/docs/webstore/images).
7. Prepare an evidence-based listing and data-flow record: single purpose, justified grants, local/off-device data, backend recipients, retention/deletion, consent and any account/commercial behavior. Reconcile disclosures with extension and Django behavior. Browser grants and CORS do not replace backend account/resource authorization, and client bundles cannot conceal confidential service keys. Current store policy requires narrow necessary access and truthful listing/data disclosures; actual data handling determines the privacy-policy requirement. No compliance verdict is possible without implementation evidence. [Chrome Web Store policies](https://developer.chrome.com/docs/webstore/program-policies/policies).
8. Retain the tested ZIP, SHA-256 digest, source revision, lockfile/configuration identity, manifest/version, build/browser versions, test outputs, listing assets and explicit gaps as one release-candidate record. Promote those same bytes later; a rebuilt candidate needs its own relevant evidence.

In GitLab, the eventual verify/build/package job should produce those local artifacts without publisher credentials. Keep any privileged promotion jobs separate from untrusted contribution verification and under existing release policy. Planning a release does not authorize uploads on every push/tag. No GitLab configuration has been changed here.

### External stages and stopping point

Upload, review submission and publication are distinct actions. This request stops at assessment and a local packaging plan. No uploader is selected or installed; no publisher service, dashboard or authenticated API is contacted; no credentials/accounts are configured. Public documentation retrieval does not establish a publisher connection.

Before any separately authorized future promotion, the existing publisher/item identity, exact ZIP digest/version, intended distribution and approved credential mechanism would need to be established. Preserve any existing trusted release authorization rather than inventing another ceremony. After an ambiguous external response, inspect item/version state before retrying. Store publication and installed-user adoption are separate evidence, and neither review duration, acceptance, immediate fleet rollout nor immediate downgrade is guaranteed. The current publishing documentation separates upload from submission and supports control of publishing after review. [Chrome publishing process](https://developer.chrome.com/docs/webstore/publish).

## Guidance files read

All local guidance reads were limited to this allowed package root:

`standalone-plugins/browser-extension-development`

- `skills/browser-extension-development/SKILL.md`
- `skills/browser-extension-testing/SKILL.md`
- `skills/browser-extension-testing/references/runtime-drivers.md`
- `skills/browser-extension-security/SKILL.md`
- `skills/browser-extension-security/references/permissions-and-messages.md`
- `skills/browser-extension-ui/SKILL.md`
- `skills/browser-extension-ui/references/content-ui.md`
- `skills/browser-extension-delivery/SKILL.md`
- `skills/browser-extension-delivery/references/release-evidence.md`
- `references/sources.md`

The security, UI, testing and delivery files above are supporting **browser-extension** guidance within the permitted package. They are not evidence that optional general frontend, security or delivery specialists are installed or available. The framework/migration reference, package metadata and upstream notices were listed by file inventory but not opened; no scaffolding or migration was needed.

## Actual checks and limits

**Performed:** Listed files under the permitted package; read the ten guidance files above; consulted the seven primary public Chrome documentation pages linked in this report, including targeted permission, ZIP-root, screenshot, version and policy sections; created and read back this output report. Public references were retrieved on 2026-10-21. Documentation establishes contracts, not exercised application behavior.

**Not performed:** Application/source-repository inspection or modification; dependency installation; skill installation; scaffolding; builds; ZIP creation/extraction or digest calculation; image inspection/capture; browser launches; automated or manual extension tests; GitLab execution/configuration; backend/network integration tests; publisher/account setup; uploader installation; upload, submission or publication. No other plugin package or evaluation file was inspected. Only the requested report and its output directory were created.

**Still unverified:** Both applications' actual manifests/code/resources, Chrome support floor, CI commands, test tooling availability, archive contents, screenshot contents, privacy disclosures, backend contracts, prior published version, update compatibility and all publisher state. The plans intentionally make no passing test, store compliance or release-success claims for those boundaries.
