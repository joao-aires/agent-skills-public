---
name: native-client-development
description: Build and verify TypeScript Tauri desktop clients and iOS/Android clients
  connected to application backends. Use for native shell integration, mobile framework
  selection, platform lifecycle, secure client storage, packaging and native testing;
  preserve established client frameworks.
user-invocable: false
metadata:
  scope: stack-specific
  invocation: both
  stack: TypeScript, Tauri, React Native, Expo, iOS, Android
  role: support
---

# Build native clients

For my new desktop applications, prefer TypeScript with Tauri. Use a compatible SPA frontend such as React/Vite; keep Tauri's Rust shell and its dependencies explicit. A hosted Python/FastAPI backend remains a separate service. Bundle a Python sidecar only when an accepted offline/local requirement justifies its packaging, lifecycle and update costs. Preserve existing native stacks.

For iOS/Android, compare current React Native + Expo, Flutter, Kotlin Multiplatform and native SwiftUI/Jetpack Compose against the product. Prefer React Native + Expo as the starting candidate when TypeScript reuse and a shared client fit; this is a recommendation to assess, not a universal platform choice. Read [platform selection](references/platform-selection.md) when selecting or revisiting a framework. Preserve an accepted framework and research unsupported native modules before promising cross-platform parity.

Use [visual-design](../visual-design/SKILL.md) for product-derived visual direction and rendered review, and [interaction-design](../interaction-design/SKILL.md) for behavior. Native-client guidance complements these rather than replacing product/UX work. For React/Tauri DOM clients, use [frontend conventions](../frontend-conventions/SKILL.md) for compatible shadcn/Tailwind implementation defaults; React Native uses native primitives. Reuse domain/API contracts and design tokens where suitable, while implementing platform-appropriate components and navigation. Web shadcn components are not React Native widgets. Account for keyboard, touch, safe areas, screen readers, Back/deep links, permission denial and platform lifecycle. Keep human drafts across errors and foreground/background transitions.

## Define the client/backend boundary

Authenticate on the server and enforce ownership there. Store credentials/session material through platform-appropriate secure storage; avoid embedding backend/provider secrets or a production identity bypass. Fixture identities require explicit local/test opt-in, production rejection and tests for that boundary. Constrain Tauri commands/capabilities, IPC inputs, allowed origins and remote content. Use deterministic application authorization for all model-proposed client actions.

Document backend addresses for host, simulator/emulator and physical devices, development network policy and production TLS. Device localhost is not the host backend. Define supported offline/cache behavior, reconnection, synchronization conflicts and cancellation rather than silently fabricating a fully offline product.

## Establish and prove platform delivery

Keep root and client READMEs, scoped instructions, locked dependencies, frontend/Rust/native configuration checks, tests and platform build commands. Use delivery-pipelines when available for GitHub Actions, backend Dockerfiles/Compose, native artifact builds and release procedures. Native clients are packaged for their platforms, not as Docker runtime images. Document signing/notarization, provisioning, update compatibility and store submission prerequisites; configuring a pipeline does not authorize signing-service changes or publication.

Verify frontend components/contracts and backend integration, then launch the actual Tauri binary or each target's development build on a supported simulator/device. Exercise login, persisted mutations/restart, cross-user denial, failure/draft behavior, navigation and lifecycle. Separate iOS and Android results. A browser preview, TypeScript check, Expo Go session or backend container cannot establish native release/runtime coverage. Missing Xcode, Rust, Android SDK, signing or devices remains a named blocked capability.
