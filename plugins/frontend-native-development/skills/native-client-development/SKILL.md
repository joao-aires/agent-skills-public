---
name: native-client-development
description: Build and verify TypeScript Tauri desktop clients and iOS/Android clients
  connected to application backends. Use for native shell integration, accepted mobile frameworks, platform lifecycle, secure client storage, packaging and native testing;
  preserve established client frameworks.
user-invocable: false
metadata:
  scope: stack-specific
  invocation: both
  stack: TypeScript, Tauri, React Native, Expo, iOS, Android
  role: support
---

# Build native clients

## Apply the accepted platform choices

Preserve existing native stacks. For my new applications:

| Target | Starting candidate and conditions |
| --- | --- |
| Desktop | TypeScript with Tauri and a compatible SPA such as React/Vite. Keep Tauri's Rust shell and dependencies explicit. |
| TypeScript mobile | React Native + Expo when shared code fits the accepted product. Research unsupported native modules before promising parity. |

Consequential framework selection belongs to system design; this skill supplies compatibility evidence and implementation for the selected stack. Read [platform selection](references/platform-selection.md) when selecting or revisiting a framework.

A hosted backend remains a separate service with its accepted stack. Bundle a local sidecar only when an accepted offline/local requirement justifies its packaging, lifecycle and update costs.

## Implement the platform experience

Use installed visual design expertise for product-derived visual direction/rendered review and interaction design expertise for behavior; otherwise retain explicit design intent, affected states and actual client verification. Native-client guidance complements these rather than replacing product/UX work.

- For React/Tauri DOM clients, use installed guidance for the accepted frontend stack for compatible shadcn/Tailwind implementation defaults; React Native uses native primitives.
- Reuse domain/API contracts and design tokens where suitable, while implementing platform-appropriate components and navigation. Web shadcn components are not React Native widgets.
- Account for keyboard, touch, safe areas, screen readers, Back/deep links, permission denial and platform lifecycle.
- Keep human drafts across errors and foreground/background transitions.

## Define the client/backend boundary

Authenticate on the server and enforce ownership there.

- Store credentials/session material through platform-appropriate secure storage; avoid embedding backend/provider secrets or a production identity bypass.
- Fixture identities require explicit local/test opt-in, production rejection and tests for that boundary.
- Constrain Tauri commands/capabilities, IPC inputs, allowed origins and remote content.
- Use deterministic application authorization for all model-proposed client actions.

Follow a client operation across both network and application lifecycle changes. Decide whether an interrupted request can be retried, how the client discovers an operation that may already have completed, and what happens to unsaved input when the application moves to the background or is restarted. Keep local display state separate from server-confirmed state so reconnection does not turn stale content into an authoritative update.

Document backend addresses for host, simulator/emulator and physical devices, development network policy and production TLS. Device localhost is not the host backend. Define the accepted offline/cache behavior and how synchronization conflicts and cancellation are presented. Supporting drafts or cached reads does not automatically require a fully offline product.

## Establish and prove platform delivery

Keep the repository and each client reproducible: root/client READMEs, scoped instructions, locked dependencies, frontend/Rust/native configuration checks, tests and platform build commands. Preserve an accepted backend build/runtime mechanism; native clients are packaged for their platforms, not as Docker runtime images.

Use delivery expertise when available for artifact/release/recovery contracts and matching tooling for provider configuration. Document signing/notarization, provisioning, update compatibility and store submission prerequisites. Configuring a pipeline does not authorize signing-service changes or publication.

Verify frontend components/contracts and backend integration, using [platform testing](references/platform-testing.md) for driver compatibility, then launch the actual Tauri binary or each target's development build on a supported simulator/device.

- Exercise login, persisted mutations/restart, cross-user denial, failure/draft behavior, navigation and lifecycle.
- Separate iOS and Android results.
- A browser preview, TypeScript check, Expo Go session or backend container cannot establish native release/runtime coverage.
- Missing Xcode, Rust, Android SDK, signing or devices remains a named blocked capability.
