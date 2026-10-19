# Selected browser and component drivers

Preserve a compatible existing suite. For a new selected web automation setup, Playwright provides browser journeys and reviewed visual comparisons; use installed playwright-cli for exploratory operation where useful. This technical preference does not make it a generic workflow requirement.

- [Playwright best practices](https://playwright.dev/docs/best-practices): semantic locators, isolated data and observable-state assertions.
- [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots): controlled rendering and reviewed baselines.
- [Playwright Electron](https://playwright.dev/docs/api/class-electron): experimental support and native-dialog limits.
- [Storybook testing](https://storybook.js.org/docs/writing-tests): actual component/provider states, interaction assertions, accessibility and reviewed visual comparisons with a compatible runner. A build or published catalogue alone does not prove the interaction; no paid service is required.

Use platform-native expertise for native runtime/packaging coverage. Playwright Electron support is experimental and must be checked for the selected version; renderer automation does not establish native dialogs, updates or filesystem integration. Native client and backend services use separate runtime boundaries, even when Compose supplies services for a test.
