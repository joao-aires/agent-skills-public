---
name: browser-extension-ui
description: Implement or assess Chrome extension popup, side-panel, options and injected-page interfaces. Use for surface lifecycle, compact layouts, CSS isolation, component portals, permission states and extension asset integration; preserve the product's design system.
user-invocable: false
metadata:
  scope: stack-specific
  invocation: both
  role: support
  stack: Chrome, Manifest V3, browser DOM
  source: https://github.com/quangpl/browser-extension-skills/tree/249886cf8137086792b6c3a5a2f7adce117a9f8d
---

# Fit the experience to the browser surface

Read the accepted task, visual direction and interaction behavior before selecting layouts or components. Inspect existing tokens, typography, primitives and framework versions. Chrome's surface constraints affect implementation; they do not require a Google-like palette, a new font system or a component-library migration. Use available visual, interaction and accessibility expertise when relevant. Without it, establish task hierarchy and meaningful states from project evidence and inspect the rendered result.

## Choose the surface for the task

| Surface | Consequence for the experience |
| --- | --- |
| Toolbar popup | Dismissal destroys the surface. Keep quick actions understandable and persist drafts/progress that must survive. Verify actual popup sizing and closure. |
| Side panel | Can support longer work alongside a page. Design for available width, tab/site context changes and panel closure/reopening. |
| Full extension tab/window | Gives collection review, bulk editing or longer work more room. Retain the intended source window/site and recoverable session if the extension tab moves or closes. |
| Options page | Suits substantial configuration. Establish navigation, validation and what takes effect immediately versus after saving. |
| Injected page UI | Must coexist with site content, styles, focus and navigation. State whether it assists, annotates or changes the host experience. |
| DevTools or new-tab surface | Has distinct activation and lifetime. Add it only when it serves the accepted task. |

A popup's documented maximum is a browser limit, not its recommended design size. Side-panel dimensions vary with the browser and user environment; support resizing and real content instead of assuming a fixed 320–400px contract. Check current [popup behavior](https://developer.chrome.com/docs/extensions/develop/ui/add-popup) and [side-panel capabilities](https://developer.chrome.com/docs/extensions/reference/api/sidePanel) for the target version.

Choose the smallest surface that supports the task comfortably. A quick popup and a larger workspace can share operations without sharing one compressed layout; settings need their own space when configuration becomes substantial. Add a side panel when continuity alongside a page serves the task, not as a default requirement for every extension. Read [extension experience patterns](references/experience-patterns.md) when designing multiple surfaces, dense collection work or a substantial UI revision; it includes source-based lessons from maintained open-source extensions.

## Implement the accepted system in context

Carry forward the accepted component system and appearance policy before choosing extension-specific layouts. Apply compatible project components and semantic tokens. A React extension can use its existing shadcn/Tailwind setup without acquiring Next.js server rendering. Preserve the installed Tailwind major and component primitives; use their version-matched setup if genuinely missing. Bundle approved fonts/icons locally where needed for CSP, offline use and performance; choose them for the reading task rather than banning custom fonts universally.

Decide theme behavior from product requirements and the established system. If following browser/system appearance or offering an override, verify both initial rendering and persisted preference across surfaces. Treat first paint, persisted overrides, live system changes and synchronization among open surfaces as one theme contract. Include overlays/portals, native form controls, focus and errors; inspect contrast while the theme changes as well as after it settles. Avoid a theme flash or duplicate competing token systems. Use density that makes the real task readable with long labels, zoom and localization, not a fixed compact recipe for every extension.

Use [injected UI and shared components](references/content-ui.md) when mounting into a site, moving components into a ShadowRoot or adapting overlays/portals. Style isolation, font/token inheritance and focus/event behavior need separate checks. Neither JavaScript isolated worlds nor Shadow DOM alone proves that an injected experience is safe or usable.

## Make dense work and configuration understandable

Lead with the information that lets someone recognize an item, then its source/context and relevant state. Support search/filtering and explicit selection when collections grow. Explain whether a bulk action affects visible results, selected items or a broader scope; preserve exclusions and edits, and keep the consequence and recovery visible. Use a persistent action region when long scrolling would otherwise hide the decision. Density should serve comparison without making labels, focus or targets difficult to use.

Separate task controls from substantial configuration. Make defaults, immediate changes and explicit saves distinguishable, and explain when a change requires a fresh result. A setting changed in one view must not leave another view presenting a stale proposal as current. Surface status near the relevant action and distinguish saved configuration from verified service access. Optional integrations need clear recipients and distinct states for the capabilities they actually use, such as browser grants, account authorization or model support, rather than one ambiguous connected badge.

Give configuration a recognizable entry and return path across the chosen browser surfaces. An options page, a settings view in the extension workspace or a short adjacent panel can each fit a different task; do not require one layout for every extension. Preserve the original page/window context and unfinished work when configuration opens elsewhere. Read [configuration navigation](references/experience-patterns.md#navigate-to-configuration-and-back) when choosing that boundary or changing how several surfaces expose settings.

## Represent permission and lifecycle states

Explain the action and site scope before requesting access, request it at the relevant interaction and retain useful behavior when access is declined. Distinguish unsupported/restricted pages, absent grants, expired account access, empty results and a disconnected content script. Do not collapse these into an indefinite spinner or silently retry with broader permissions.

Keep accepted work and recoverable input outside a disposable popup. On reopen, reconstruct status from an appropriate source of truth rather than pretending the operation completed because the UI closed. For context-sensitive actions, retain and show the relevant source window/page/site and account context. A surface gaining focus or moving to another window must not silently retarget an accepted action. Prevent stale results from being applied after navigation, changed selection or configuration; make synchronization or invalidation explicit when multiple views can edit the same operation.

## Inspect real surfaces and assets

1. Render representative content in the actual installed/unpacked extension surface, including a difficult state. Exercise keyboard opening/closing where relevant, focus order/restoration, zoom, scrolling and error recovery. Inspect before propagating a shared pattern.
2. Verify changes through affected popup, panel, options and injected callers. Component stories can expose states and portal problems; they do not establish browser-popup lifecycle or site permissions. Use [extension runtime testing](../browser-extension-testing/SKILL.md) for those claims.
3. Inspect toolbar/install icons at their real small sizes and listing images against current store requirements. Reuse brand assets, generate with appropriate available tools when authorized, and capture actual functioning UI for screenshots. Label temporary placeholders as unfinished and exclude them from a release-ready claim.

Return the implemented or assessed surfaces, preserved design decisions, observed behavior and remaining gaps. A critique request does not authorize source fixes or store asset uploads. [Source notes](../../references/sources.md) explain the platform sources and upstream selection.
