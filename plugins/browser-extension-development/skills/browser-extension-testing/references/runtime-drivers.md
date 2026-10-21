# Runtime drivers and lifecycle checks

## Select the supported combination

Use the project's installed versions and current primary guidance for [Playwright extensions](https://playwright.dev/docs/chrome-extensions) or [Puppeteer extensions](https://pptr.dev/guides/chrome-extensions). Confirm the browser executable/channel and supported extension-loading mechanism. Modern headless Chromium is different from older headless shells. Do not infer branded Chrome/Edge support from a Chromium test.

For Playwright, the documented approach uses bundled Chromium, a persistent context and extension-loading arguments. A minimal setup is:

```ts
import { chromium } from '@playwright/test';
import path from 'node:path';

const extensionRoot = path.resolve(process.env.EXTENSION_BUILD!);
const context = await chromium.launchPersistentContext('', {
  channel: 'chromium',
  headless: true,
  args: [
    `--disable-extensions-except=${extensionRoot}`,
    `--load-extension=${extensionRoot}`,
  ],
});
try {
  // Exercise the accepted operation and assert its independent effects here.
} finally {
  await context.close();
}
```

The caller supplies an existing production build path and installed test dependencies; this fragment is browser setup, not a finished test or permission grant. Use a unique test profile and controlled fixtures. Current Puppeteer offers its own extension-loading options/APIs; use that version's contract rather than transplanting Playwright setup or obsolete flags. Preserve the browser sandbox unless the actual isolated environment requires an evidenced exception.

## Discover and trigger the correct context

If the manifest declares a worker, wait for the target with an extension-origin URL and match the tested build's known identity/script. Filter out page service workers and unrelated extensions. Prefer event-driven waits with a bounded timeout; report the relevant browser diagnostic when the context never appears.

For a worker-recovery check:

1. Establish accepted state through the real extension caller and observe it in the appropriate storage/application boundary.
2. Terminate the worker through the driver's supported mechanism, or run a separately controlled idle-suspension experiment. Record which happened; do not silently use a forced kill as proof of a specific idle timer.
3. Trigger the next action through an extension page/content caller or browser event. A message sent by the worker to itself does not establish that an external caller can wake it.
4. Wait for the appropriate worker/context according to that driver version, then assert recovered state and the resulting effect. Driver handles can behave differently across restarts; do not assume every restart produces a fresh target event.

For extensions without a worker, use a documented installation/identity mechanism and test the actual declared entrypoints. Adding a worker merely to satisfy a test harness changes the product unnecessarily.

## Distinguish popup rendering from popup lifetime

Directly navigating to the popup URL can test its document/scripts and shared components. Use actual toolbar activation or a compatible documented action-opening mechanism for invocation and dismissal claims. Observe whether user-gesture and active-tab requirements are satisfied by that method. If the driver cannot operate the required surface, a scoped headed/manual check can supply that evidence; otherwise report it unverified.

Retain relevant context console errors, page/worker failures and a screenshot for visual findings. Inspect storage through a trusted test context and page effects through the affected page. For forbidden actions, verify no mutation/network effect, not only an error string. Isolate fixtures and close owned contexts/servers even when assertions fail; never attach these checks to a personal profile or production publisher account.
