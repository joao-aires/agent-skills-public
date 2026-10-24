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

The [extension experience patterns](../skills/browser-extension-ui/references/experience-patterns.md) reference pins inspected Raindrop and Bitwarden source for surface composition, theme roles and lifecycle distinctions. These are source-based design lessons, with no imported application code/assets or claim of measured user outcomes. Generic visual guidance owns the early component-system/appearance decision; platform guidance applies it to actual browser surfaces and lifetimes.
