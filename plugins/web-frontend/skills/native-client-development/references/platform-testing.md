# Native platform testing

Use a maintained driver compatible with the actual application/runtime and named OS. Preserve existing suitable tooling. A driver establishes only the boundaries it exercises; a browser preview or a mobile authoring app cannot establish native runtime behavior.

| Surface | Starting point | Boundary to verify |
| --- | --- | --- |
| Web | Playwright plus installed browser CLI/MCP for exploration | Actual browsers, responsive sizes, keyboard/focus and relevant role variants |
| Tauri | Supported native/WebView automation for the actual target; component/browser checks supplement it | Packaged shell, IPC capabilities, lifecycle and OS integration; web preview is narrower evidence |
| Electron | Playwright Electron support where compatible (experimental) | Renderer coverage does not prove native dialogs, packaging, updates or filesystem integration |
| Native desktop | Platform-native automation or an appropriate maintained Appium driver | Named supported OS and packaged application; inspect driver maintenance/limitations |
| Android/iOS | Maestro for suitable flows or Appium/platform-native tooling | Actual emulator/device, lifecycle, permissions, keyboard, offline and supported OS behavior |

A mobile viewport is not a native-mobile test. Maestro's desktop authoring app does not automate arbitrary native desktop applications. Compose can supply backend services; desktop clients and simulators normally run on the appropriate host. Record device/OS/browser/build identities. Test the selected application's real platform; supporting these methods does not add those frameworks to this repository.

First-party driver references:

- [Maestro supported platforms](https://docs.maestro.dev/get-started/supported-platform): check mobile/web scope and device setup; its desktop authoring app does not automate arbitrary desktop apps.
- [Appium drivers](https://appium.io/docs/en/latest/ecosystem/drivers/): check the selected platform's maintenance and server/driver compatibility independently.
- [Playwright Electron](https://playwright.dev/docs/api/class-electron): experimental renderer automation has native integration limits.

Exercise the packaged application's real IPC/capabilities, secure storage, permissions, lifecycle, backend connectivity, update and persistence behavior where relevant. Native release-signing evidence and a development runtime remain separate claims. Verify iOS and Android independently, identifying simulator/device, OS and build revision.
