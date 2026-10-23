# Browser-extension sources and boundaries

This package contains five original supporting skills for Chrome Manifest V3. They apply inside the collection's existing development activities and remain useful as a standalone technical package. No UI framework, backend language, identity provider, browser driver or publishing service is installed by this guidance. Other browsers/stores require their own compatibility investigation and evidence.

## Reviewed upstream skill collection

Reviewed [quangpl/browser-extension-skills at `249886cf8137086792b6c3a5a2f7adce117a9f8d`](https://github.com/quangpl/browser-extension-skills/tree/249886cf8137086792b6c3a5a2f7adce117a9f8d), including its twelve entrypoints and relevant framework, messaging, UI, testing, security and publishing references. The repository is [MIT licensed](https://github.com/quangpl/browser-extension-skills/blob/249886cf8137086792b6c3a5a2f7adce117a9f8d/LICENSE). Its scope helped identify extension-specific decisions that generic web guidance misses.

| Upstream area | Useful contribution | Treatment here |
| --- | --- | --- |
| extension-create/dev/migration | Contexts, entrypoints, framework detection and MV2-to-MV3 concerns | Original platform implementation guidance; actual framework configuration and behavior preservation govern migration |
| extension-manifest/analyze/review | Grants, CSP, messaging, data handling and store risks | Separate browser authority checks from store readiness; evidence-based findings without approval predictions |
| extension-ui/assets | Small surfaces, popup lifetime, injected styles and icons/listing images | Preserve accepted product identity and compatible components; platform constraints do not prescribe a universal theme or layout |
| extension-test | Unit, component and loaded-extension boundaries | Current driver contracts, worker recovery and real-surface evidence, preserving the project's runner |
| extension-backend/payment/publish | Extension-to-service boundaries and release preparation | Retain the browser integration decisions; no prescribed NestJS/MongoDB, payment provider, credential flow or automatic publication |

The upstream set is not acquired wholesale. Its instructions mix a separate development workflow with platform expertise, named optional helpers and framework/design defaults; several technical examples require substantive correction. These original skills use the reviewed material as source references, checked against primary documentation, rather than applying an extensive string-rewrite layer. There are no acquired files from this source and no Agent Depot artifact for a source-reference-only dependency. If upstream resources are acquired later, preserve their unmodified snapshots, MIT notice and reviewed pins through the repository's acquisition flow.

## Primary implementation contracts

Use these sources when changing the corresponding boundary, and verify the installed versions and target browser. They are consulted conditionally, not required reading for every extension task.

| Concern | Primary source |
| --- | --- |
| Event-driven background lifetime | [Worker lifecycle](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers/lifecycle), [MV3 migration](https://developer.chrome.com/docs/extensions/develop/migrate) |
| Grants and current-page invocation | [Declare permissions](https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions), [activeTab](https://developer.chrome.com/docs/extensions/develop/concepts/activeTab), actual API method references |
| Context and privilege boundaries | [Content scripts](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts), [messaging](https://developer.chrome.com/docs/extensions/develop/concepts/messaging), [security](https://developer.chrome.com/docs/extensions/develop/security-privacy/stay-secure), [storage](https://developer.chrome.com/docs/extensions/reference/api/storage) |
| Bundled execution | [Manifest/CSP](https://developer.chrome.com/docs/extensions/reference/manifest/content-security-policy), [manifest version](https://developer.chrome.com/docs/extensions/reference/manifest/version) |
| Framework configuration | [WXT entrypoints](https://wxt.dev/guide/essentials/entrypoints.html), [CRXJS manifest](https://crxjs.dev/concepts/manifest/), [CRXJS Vite setup](https://crxjs.dev/guide/installation/from-scratch/) |
| Real browser testing | [Playwright extension guide](https://playwright.dev/docs/chrome-extensions), [Puppeteer extension guide](https://pptr.dev/guides/chrome-extensions) |
| Store readiness and promotion | [Policies](https://developer.chrome.com/docs/webstore/program-policies/policies), [review](https://developer.chrome.com/docs/webstore/review-process), [API](https://developer.chrome.com/docs/webstore/api) |

These references establish documented contracts, not exercised application behavior, store approval or cross-browser parity. The repository's evaluation records state which bounded checks were actually performed.

## Experience-design references

The UI skill separates extension task types from browser surfaces. [Extension types and structures](../skills/browser-extension-ui/references/extension-types.md) provides starting arrangements for quick capture, contextual libraries/vaults, page companions, inline assistance, page adaptation, site controls, collection workspaces, capture/jobs/editors, workflow automation, browser destinations, developer inspection and command-first utilities. Each pattern explains when it fits, how to adapt it and what journey would challenge it. Products can combine patterns; the list is a design aid, not a required screen inventory or an exhaustive classification of products.

The patterns cite public product documentation and inspected, pinned source where relevant: Raindrop and Bitwarden for capture/library/context; Page Assist and Hypothesis for page-adjacent work; Dark Reader for effective site settings; uBlock Origin for scoped control; SingleFile for capture and result stages; Automa for workflow authoring/execution; Tabliss for a browser-entry dashboard; React Developer Tools for inspection; and Vimium for command-driven interaction. Chrome's UI/API references establish platform contracts. These are original design inferences with no imported application code/assets, license acquisition or claim of measured user outcomes. A product's existence is not evidence that its implementation fits the current MV3 target.

[Extension experience patterns](../skills/browser-extension-ui/references/experience-patterns.md) owns shared scope, state, access and transition contracts, including configuration as one kind of departure and return. Generic visual guidance owns the early component-system/appearance decision; platform guidance applies it to actual browser surfaces and lifetimes.
