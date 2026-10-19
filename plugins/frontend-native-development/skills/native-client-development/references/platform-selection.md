# Select desktop and mobile platforms

Check current first-party documentation, required native modules, supported OS/tool versions and the team's capabilities before choosing. Preserve accepted choices. These are candidates with different tradeoffs, not a ranking independent of the product.

| Candidate | Useful starting condition | Decision-changing constraints |
| --- | --- | --- |
| TypeScript + Tauri | My desktop default; reuse a web UI with a native shell | Rust/toolchain and platform packaging; restricted IPC/capabilities; native integrations and WebView behavior |
| React Native + Expo | TypeScript/React team, shared iOS/Android client and native navigation | Native module compatibility, development builds, platform-specific behavior and upgrade/build requirements |
| Flutter | Shared UI with Dart and custom rendering is acceptable | New language/ecosystem, plugins and platform accessibility/integration requirements |
| Kotlin Multiplatform | Kotlin team or shared domain code with native or Compose UI | Swift/Kotlin interoperability, library support and separate native UI/tooling responsibilities |
| SwiftUI + Jetpack Compose | Deep platform integration or distinct platform experiences | Two implementations and platform-specific testing/release work |

Tauri mobile is another option when web reuse and supported plugins fit; do not assume desktop plugin behavior or UX carries across mobile. React Native recommends a framework such as Expo. Use Expo development builds for actual native-module/runtime verification; cloud EAS builds are optional and do not grant paid-service or store-publication authority.

Record the chosen client stack, tested modules, backend API contract, offline requirements, device connectivity and lifecycle strategy. Evaluate one useful journey on both platforms before claiming parity. Keep simulator/device, release-signing and store-delivery results distinct.

Sources checked 15 October 2026; verify version-specific support when used:

- [Tauri prerequisites](https://v2.tauri.app/start/prerequisites/) and [frontend configurations](https://v2.tauri.app/start/frontend/).
- [React Native framework guidance](https://reactnative.dev/blog/2024/06/25/use-a-framework-to-build-react-native-apps), [Expo development builds](https://docs.expo.dev/develop/development-builds/introduction/) and [local builds](https://docs.expo.dev/guides/local-app-overview/).
- [Flutter platform integration](https://docs.flutter.dev/platform-integration).
- [Kotlin Multiplatform templates](https://kmp.jetbrains.com/templates/) for shared or native UI.
