---
name: browser-extension-testing
description: Plan and execute Chrome MV3 unit, component and real-extension tests. Use for worker restart, popup/panel lifecycle, site permissions, messaging and production-package verification with a compatible browser driver.
user-invocable: false
metadata:
  scope: stack-specific
  invocation: both
  role: support
  stack: Chrome, Manifest V3, Playwright, Puppeteer
  source: https://github.com/quangpl/browser-extension-skills/tree/249886cf8137086792b6c3a5a2f7adce117a9f8d
---

# Test the boundary the user depends on

Start with the changed behavior, supported Chrome versions, existing test runner and available execution target. Preserve Jest, Vitest, Playwright or Puppeteer where they already meet the need. A stack-specific example is not a reason to replace the application's suite. Build meaningful acceptance around observable effects, including denial and lifecycle behavior that the change can affect.

## Separate evidence levels

| Level | What it can establish | What remains outside it |
| --- | --- | --- |
| Unit/API mocks | Parsing, state transitions, permission/error handling and message construction | Browser grants, isolated worlds, actual worker termination or Chrome API behavior |
| Component/stories | Rendered states, keyboard interaction, shared tokens and overlays in that setup | Browser toolbar activation, popup dismissal and installed permissions |
| Loaded production extension | Integration of packaged manifest/resources and real extension contexts | Store acceptance, other browsers or a signed store-delivered update |
| Real surface/journey | Actual invocation, page effects, closure/reopening and relevant persisted outcomes | Untested OS/browser variants or external services replaced by fixtures |

Opening `chrome-extension://.../popup.html` in a normal tab is useful for component integration but does not reproduce the toolbar popup's destruction or an `activeTab` invocation grant. Check the actual surface when those behaviors matter. Do not convert a missing driver into a passing claim; complete independent checks and record the exact remaining boundary.

## Prepare a compatible isolated browser

Read [runtime drivers and lifecycle checks](references/runtime-drivers.md) before writing browser tests. Use a disposable profile, local controlled pages/providers and the production build directory. Record driver/browser versions and artifact identity. Do not load into a personal browser profile, reuse account sessions or disable sandboxing by default.

Modern supported Chromium configurations can run extensions headlessly. Choose a documented driver/browser combination, then use headed operation for actual browser-surface interaction or visual checks that the chosen driver cannot exercise headlessly. Branded Chrome and Chromium automation have different extension-loading support; record the actual executable/channel. A framework's development browser is not evidence for the production bundle.

Wait for the specific extension context rather than sleeping a fixed interval or selecting the first service worker on an arbitrary page. Some extensions have no worker; discover their identity through the supported runtime/driver mechanism instead. Close test-owned browser processes and servers and retain failures/artifacts without weakening assertions.

## Exercise consequential transitions

Select checks from the changed behavior:

- Complete the user operation, then observe its page/storage/backend effect independently of the success response. Close/reopen disposable UI and verify that only intended state survives.
- Terminate or allow suspension of the worker, then trigger a real extension event from another context. Verify restored state, event handling and absence of duplicated effects. A test keeping DevTools attached can alter normal worker lifetime; distinguish forced termination from observed idle suspension.
- Exercise missing, denied and revoked grants and restricted pages. Request optional access only through the required user interaction. An automation-granted permission proves a different path from user consent.
- Reject malformed messages, disallowed contexts and unapproved resources without a protected effect. Include tab/frame navigation or disconnect during an operation when that can change its target.
- Test existing-user data migration/update when schemas, permissions or lifecycle assumptions change. A clean-install pass does not establish update compatibility.

Use [extension security](../browser-extension-security/SKILL.md) for the authorization contract and [extension UI](../browser-extension-ui/SKILL.md) for rendered surface/portal checks. Use optional general journey, accessibility or visual expertise where available; otherwise retain their task outcomes with existing tools and primary documentation.

## Report what actually ran

Keep mocks, loaded-extension checks, real toolbar/panel interaction and external service outcomes separate. Include target/build identities, commands, assertions, failures and unexecuted scenarios. A successful browser launch, screenshot or collection of mock assertions does not establish the complete extension journey. Store submission/publication is outside testing unless explicitly authorized as a separate action.

The [source notes](../../references/sources.md) identify reviewed upstream material and current driver contracts.
