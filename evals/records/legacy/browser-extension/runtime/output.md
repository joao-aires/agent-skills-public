> Evidence copy: commands and executable fixture paths below refer to the original disposable evaluation workspace, not this evidence directory. Generated application/build/test sources remain outside the collection; this directory retains reports, machine observations, build identities and screenshots. Repeat the scenario from the recorded inputs to run a new trial.

# Disposable MV3 notes runtime trial

Completed using only the supplied browser-extension guidance, primary platform documentation, the installed Playwright driver, and the supplied isolated Chrome-for-Testing executable. Application, tests, browser profiles and reports were generated only inside this `runtime/` directory. No account, backend, personal profile, global install, publication or external service action was used.

## Result

**PASS: 13 production-extension acceptance checks.** The shipped popup saves a synthetic note, a new actual popup target restores it after destruction, the supported page reads its own note, content-script mutation attempts have no protected storage effect, and the extension recovers after a confirmed forced worker stop. A subsequent browser restart also preserves local storage.

Machine-readable results: [artifacts/results.json](artifacts/results.json). Console results: [artifacts/test.log](artifacts/test.log). Production manifest and per-file SHA-256 identities: [artifacts/build.json](artifacts/build.json).

The actual popup screenshot [artifacts/popup.png](artifacts/popup.png) and page screenshot [artifacts/research.png](artifacts/research.png) were opened and visually inspected. The saved text, labels, save state and injected local-note display are readable; the script-shaped synthetic note appears as literal text.

## Guidance read

All paths below are inside the specifically authorized source package `standalone-plugins/browser-extension-development/`:

- `skills/browser-extension-development/SKILL.md`
- `skills/browser-extension-testing/SKILL.md`
- `skills/browser-extension-security/SKILL.md`
- `skills/browser-extension-ui/SKILL.md`
- `skills/browser-extension-development/references/framework-and-migration.md`
- `skills/browser-extension-testing/references/runtime-drivers.md`
- `skills/browser-extension-security/references/permissions-and-messages.md`
- `skills/browser-extension-ui/references/content-ui.md`
- `references/sources.md`

No other evaluation folders, criteria or peer outputs were read. The source package was not modified. Its delivery skill was unnecessary because no store/release/publication action was requested.

Primary contracts consulted on 2026-10-21:

- [Playwright extension testing](https://playwright.dev/docs/chrome-extensions): persistent contexts, packaged extension loading and worker-handle behavior.
- [Chrome action API](https://developer.chrome.com/docs/extensions/reference/api/action#method-openPopup): the compatible `action.openPopup()` method opens the actual browser action surface on Chrome 127+.
- [Chrome storage API](https://developer.chrome.com/docs/extensions/reference/api/storage): local persistence and `TRUSTED_CONTEXTS` access controls.
- [Chrome messaging](https://developer.chrome.com/docs/extensions/develop/concepts/messaging): asynchronous callback replies remain compatible with literal `return true`.
- [Worker lifecycle](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers/lifecycle): restore durable state after termination and register event listeners independently of asynchronous state loading.
- [CDP ServiceWorker](https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker/) and [CDP Target](https://chromedevtools.github.io/devtools-protocol/tot/Target/): controlled stop/status observation and attachment to the real popup target.
- [Chrome team's flag-removal notice](https://groups.google.com/a/chromium.org/g/chromium-extensions/c/1-g8EFx2BBY/m/S0ET5wPjCAAJ): Chrome for Testing retains extension-loading flags even though official regular Chrome does not. The supplied CfT binary was used and loading was observed, rather than substituting a regular/personal Chrome executable.

## Implementation and authority map

This is a new plain, dependency-free extension. A deterministic build copies the authored local entrypoints to `dist/`, verifies manifest resources exist and hashes the resulting files. No framework or development server is needed; there is no HMR or remote executable resource in production.

| Context | Operation | Authority and lifetime |
| --- | --- | --- |
| Actual action popup | `note.read`, `note.save` for Alpha or Beta | Worker accepts only its exact extension popup URL and same extension ID. Saves validate a 2,000-character limit, exact keys, revision and request ID. Durable storage completes before success acknowledgment. |
| Static top-frame content script | `pageNote.read` | Worker requires same extension ID, a top-frame tab sender, active document lifecycle, loopback host and exact supported research path. Resource comes from browser-supplied sender URL, never a caller-supplied URL or note ID. This operation accepts only the `type` key. |
| Service worker | Validation, serialized writes, durable reads | Message listener is installed synchronously. Each handler awaits storage access initialization; all note values are loaded from local storage. Only a boot ID and the write queue are temporary globals. |
| `storage.local` | Persistent note records | Access is explicitly restricted to trusted extension contexts. Content scripts must use the bounded read operation and cannot directly read, write or clear the store. |

Production grants are only `storage` and the static match `http://127.0.0.1/research/*`. Match patterns cover local ports; the runtime server picks a fresh available port and binds only `127.0.0.1`. The product supports exact `/research/alpha` and `/research/beta` resources. There is no `tabs`, `scripting`, `activeTab`, `management`, arbitrary host permission, externally-connectable declaration or web-accessible resource. The local site receives no account/token/credential data. The note is shown using `textContent`, never inserted as executable HTML. Shadow DOM provides presentation isolation; worker validation provides authority.

The installed extension grants were independently read with `chrome.permissions.getAll()` and recorded in the results. Broad access and optional permission consent were unnecessary for this fixed controlled-site feature.

## Commands and execution

From this directory:

```sh
node build.mjs
node test.mjs
```

The trial also ran `node --version` (v26.7.0) and read the installed driver version (1.64.1). The test imports the already-installed Playwright module at `evaluation-work/pr10-browser-tools/node_modules/playwright/index.mjs`; no package download or install is required. The executable defaults to the exact supplied Chrome-for-Testing app path and can be overridden with `TEST_CHROME` for an explicitly chosen compatible isolated binary.

Browser: **Chrome for Testing 156.0.8078.4**, revision `@f842f52ef39fd97b449eb27cff414bf05a98ddce`, macOS arm64 executable. Browser-reported OS user-agent compatibility text is also recorded in JSON; it does not replace the supplied executable identity. A fresh `runtime/profile-*` directory is created per trial and removed afterward. Both browser launches are headed, with Chromium sandboxing explicitly enabled. No `--no-sandbox` flag or personal profile is used.

Production artifact: **Local Research Notes 1.0.0**, extension ID `mdcaeonmhphljlahnbapeoajmoocepni` at this absolute unpacked path. The ID is discovered from the precise extension worker URL rather than hardcoded into the tests; an unpacked extension ID can change when its directory changes. Build SHA-256: **`517b245d09c0d7cbc38500ce192d3c16cb498488b893a37fc07d2c82b8b01d91`**.

The test's HTTP server, navigation waits, context discovery, protocol requests and browser lifecycle calls are scoped to the trial. The finalizer closes owned browser contexts, closes the server and removes the disposable profile, including on the recorded failed attempts. A process-list check after the successful run found no Chrome process using the runtime profile or extension paths; only the inspection command itself matched.

## Checks that actually ran

1. Validate the production manifest and all declared entrypoint files; inspect its narrow permissions.
2. Open the **actual action popup** through Chrome's documented `action.openPopup()` API. Playwright does not include this native surface in `context.pages()`, so attach to its actual `Target` through CDP. Type the synthetic note with `Input.insertText`, click Save with CDP mouse input and independently inspect `chrome.storage.local` for text and revision 1.
3. Close the popup with its own `window.close()`, wait for target destruction, reopen with `action.openPopup()` and require a different target ID with restored text. This is not a tab masquerading as a popup.
4. Click the shipped content script's Refresh button and observe its page display. Verify the script-shaped note remains inert. Verify no content UI is injected in the matching child frame because production is top-frame only.
5. Send nine denied/malformed requests from the **real production content-script isolated world**, reached through CDP, with browser-generated sender metadata. Cases: content attempts popup save; content attempts cross-note popup read; read includes attacker text; read includes another note ID; read includes arbitrary URL; unknown delete; null; array; non-string type. Require the exact bounded error and an independent full-storage equality check after each denial.
6. From the same real content-script world, attempt direct `storage.local.get`, `set` and `clear`. Require API denial and unchanged full storage after every attempt.
7. From the trusted popup, reject oversized text, unsupported note ID and malformed revision. Replay the accepted request ID and verify no extra revision or timestamp change. Change the text for that request ID and require conflict without mutation.
8. Race two valid popup saves of Beta with the same starting revision. Require exactly one accepted write, one revision conflict and a single persisted revision.
9. Inject malformed persisted Alpha data from the trusted test context, require the real worker read to return `DATA_INVALID`, and verify no silent rewrite. Restore the controlled valid fixture snapshot. This is explicit test fault injection, not an exposed production hook.
10. Navigate controlled local pages: unsupported path and separate hostname `localhost` receive no content injection; an injected but unknown research resource receives a bounded denial. Storage stays unchanged.
11. Observe the exact extension worker version through CDP, call `ServiceWorker.stopWorker`, and wait for `runningStatus: stopped`. Click the **shipped content-script Refresh button** to wake the worker. Require displayed saved text, a different production boot ID, restored storage, and a replay that does not duplicate the write. The worker handle is not assumed to become a new Playwright worker event or target ID.
12. Inspect installed grants independently.
13. Close Chrome and relaunch the **same disposable profile**. As an additional disk-durability check only, navigate a tab to the popup document, require restored text and exact storage equality. The actual popup-lifetime claim comes from steps 2–3.

## Iterations retained

- `probe.mjs` / `artifacts/probe.json`: establishes that this browser's actual popup is a separate unattached page target and is not a normal Playwright page.
- `artifacts/attempt-1.json`: harness failure locating popup due to Node's custom-scheme URL `origin` behavior; changed the harness to construct the extension scheme/host explicitly. No application check was weakened.
- `artifacts/attempt-2.json`: first nine groups passed, then the stale popup CDP session failed after opening a separate tab. Chrome had dismissed the actual popup on focus change. The harness now rediscovers/reopens the popup before independent storage inspection.
- `artifacts/attempt-3-passed.json`: all 13 groups passed.
- `artifacts/results.json` / `artifacts/test.log`: final run after bounding additional browser lifecycle calls; authoritative latest results.

## Limits

This establishes one local unpacked production extension on the supplied Chrome-for-Testing/macOS/Playwright combination. No cross-browser, regular signed Chrome, store acceptance, packed update, data migration, toolbar pinning, install-warning dialog or external/account/backend behavior is claimed. The fixture deliberately has no store icons or publication assets and is not presented as store-ready.

`action.openPopup()` is a documented action-opening mechanism and creates the actual surface, but no physical toolbar-icon click or `activeTab` grant path was tested. No feature needs `activeTab`. Popup destruction/reconstruction was observed; keyboard dismissal, zoom, localization and broad accessibility review were outside this minimal runtime task.

The lifecycle check proves **forced termination and external-caller wakeup**, not natural 30-second idle suspension or a specific idle timing guarantee. DevTools/CDP attachment can affect natural worker lifetime. The boot ID is harmless production diagnostic metadata and is not persistent state.

No crash-at-the-exact-storage-commit-instruction experiment was performed. The accepted durable save is acknowledged after storage resolves, and the tested replay of the latest request survives worker restart. Idempotence records only the latest accepted request per note; it is not an unbounded historical request ledger. The corrupted-state experiment checks persisted-data handling, not a real disk-full/quota condition. Browser/network-level errors were not exhaustively instrumented; observable assertions and the retained collected page errors establish the stated checks only.
