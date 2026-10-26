---
name: browser-extension-ui
description: Design, implement or assess Chrome extension experiences by matching user tasks to suitable UI patterns and browser surfaces. Use for extension information architecture, surface lifecycle, injected UI, permission states and assets; preserve the product's design system.
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

## Derive the experience from the kind of work

Start with what someone is trying to accomplish, not with a popup template. A bookmark clipper, a searchable vault and a page assistant may all have a toolbar icon while needing different primary experiences. Conversely, a collection browser can work in a popup, a side panel or a full tab. Product type describes the work; surface describes where it happens.

For a new experience or substantial revision:

1. **Identify the main loop.** What brings someone in, what object do they recognize or change, and what tells them they are done? Establish whether the task concerns a page/selection, a site, a collection or a browser session. Include how often people repeat it and how long unfinished work may last.
2. **Match a reference structure.** Read the selector in [extension types and UI structures](references/extension-types.md), then the relevant patterns. Combine patterns when the accepted product genuinely contains several loops. A shared header or settings page does not make two extensions the same type.
3. **Allocate work to surfaces.** Use the platform table below to decide which parts need proximity to a page, persistence, comparison space or direct browser entry. Make each additional surface earn its place; a command-only utility may not need a popup at all.
4. **Adapt the structure.** Map the actual product objects, actions, roles and states into the selected arrangement. Account for the accepted component system, appearance policy and accessibility requirements. Resolve mismatches rather than adding features merely because a reference product has them.
5. **Trace the transitions.** Establish entry, location, affected scope, unfinished work, result freshness and return behavior. Read [experience patterns](references/experience-patterns.md) for cross-surface contracts and configuration as one of those transitions.

Capture the consequential choices in the existing design notes or wireflow: task → pattern → surfaces → transitions, with reasons for meaningful departures. This is a reasoning aid, not a required new document for every small UI edit. For a narrow fix, inspect the existing structure and change only the relevant boundary.

## Check the browser surface contract

| Surface | Consequence for the experience |
| --- | --- |
| Toolbar popup | Dismissal destroys the surface. Keep quick actions understandable and persist drafts/progress that must survive. Verify actual popup sizing and closure. |
| Side panel | Can support longer work alongside a page. Design for available width, tab/site context changes and panel closure/reopening. |
| Full extension tab/window | Gives collection review, bulk editing or longer work more room. Retain the intended source window/site and recoverable session if the extension tab moves or closes. |
| Options page | Suits substantial configuration. Establish navigation, validation and what takes effect immediately versus after saving. |
| Injected page UI | Must coexist with site content, styles, focus and navigation. State whether it assists, annotates or changes the host experience. |
| DevTools panel/sidebar | Belongs to an inspected target and the DevTools session. Handle target reload/disconnection and distinguish inspection from mutation. |
| New-tab, history or bookmarks override | Replaces a familiar browser destination. Preserve fast entry and the expected finding/navigation task; establish an explicit customization/reset path. |
| Toolbar action, keyboard command, context menu or omnibox | Can invoke a task without a persistent application shell. Bind it to the intended tab, selection or query and provide discoverable feedback/recovery. These are entry mechanisms, not interchangeable page layouts. |

A popup's documented maximum is a browser limit, not its recommended design size. Side-panel dimensions vary with the browser and user environment; support resizing and real content instead of assuming a fixed 320–400px contract. Check current [popup behavior](https://developer.chrome.com/docs/extensions/develop/ui/add-popup) and [side-panel capabilities](https://developer.chrome.com/docs/extensions/reference/api/sidePanel) for the target version.

Choose a surface that supports the task comfortably, rather than minimizing its size at the expense of comprehension. A quick popup and a larger workspace can share operations without sharing one compressed layout. A persistent page companion may reasonably make the side panel its primary UI, with no popup. Verify target-browser support before promising equivalent surfaces elsewhere; an injected sidebar, a native side panel and a DevTools sidebar have different hosts and authority.

## Implement the accepted system in context

Carry forward the accepted component system and appearance policy before choosing extension-specific layouts. Apply compatible project components and semantic tokens:

- Preserve the installed Tailwind major and component primitives. Use their version-matched setup if genuinely missing.
- A React extension can use its existing shadcn/Tailwind setup without acquiring Next.js server rendering.
- Bundle approved fonts/icons locally where needed for CSP, offline use and performance. Choose them for the reading task rather than banning custom fonts universally.

Adapt the application's shared page composition to each browser surface. Keep identity, navigation and recurring actions recognizable across views with the same role; a popup, side panel and full tab may need different arrangements because of their space and lifecycle. Compare the actual affected surfaces and transitions, including browser-owned boundaries and scrolling behavior, before claiming consistency. Use project evidence and the general visual/interaction principles above when specialist guidance is unavailable.

### Appearance and density

Decide theme behavior from product requirements and the established system. If following browser/system appearance or offering an override, check the theme contract across surfaces:

- initial rendering without a theme flash;
- persisted manual overrides;
- live system changes according to the accepted policy;
- synchronization among open surfaces;
- overlays/portals, native form controls, focus, errors and contrast during and after a change.

Avoid duplicate competing token systems. Choose density that makes the real task readable with long labels, zoom and localization, rather than applying one compact recipe to every extension.

Use [injected UI and shared components](references/content-ui.md) when mounting into a site, moving components into a ShadowRoot or adapting overlays/portals. Style isolation, font/token inheritance and focus/event behavior need separate checks. Neither JavaScript isolated worlds nor Shadow DOM alone proves that an injected experience is safe or usable.

## Adapt information and controls to the task

In library and collection views, lead with the information that lets someone recognize an item, then its source/context and relevant state. Support search/filtering and explicit selection when collections grow. Explain whether a bulk action affects visible results, selected items or a broader scope; preserve exclusions and edits, and keep the consequence and recovery visible. Use a persistent action region when long scrolling would otherwise hide the decision. Density should serve comparison without making labels, focus or targets difficult to use.

Separate task controls from substantial configuration. Make defaults, immediate changes and explicit saves distinguishable, and explain when a change requires a fresh result. A setting changed in one view must not leave another view presenting a stale proposal as current. Surface status near the relevant action and distinguish saved configuration from verified service access. Optional integrations need clear recipients and distinct states for the capabilities they actually use, such as browser grants, account authorization or model support, rather than one ambiguous connected badge.

Derive navigation from the selected task structure: capture and confirmation, list and detail, conversation and sources, inspection and recording, or another supported loop. Make substantial configuration findable without interrupting frequent work. Apply the [transition method](references/experience-patterns.md#trace-transitions-between-surfaces-and-views) to settings, authentication, permission requests, editors and larger views alike; configuration is not the only departure that can lose context or drafts.

## Represent permission and lifecycle states

Explain the action and site scope before requesting access, request it at the relevant interaction and retain useful behavior when access is declined. Distinguish unsupported/restricted pages, absent grants, expired account access, empty results and a disconnected content script. Do not collapse these into an indefinite spinner or silently retry with broader permissions.

Keep accepted work and recoverable input outside a disposable popup. On reopen, reconstruct status from an appropriate source of truth rather than pretending the operation completed because the UI closed.

For context-sensitive actions:

- retain and show the relevant source window/page/site and account context;
- prevent focus changes or movement to another window from silently retargeting an accepted action;
- prevent stale results from being applied after navigation, changed selection or configuration;
- make synchronization or invalidation explicit when multiple views can edit the same operation.

## Inspect real surfaces and assets

1. Render representative content in the actual installed/unpacked extension surface, including a difficult state. Exercise keyboard opening/closing where relevant, focus order/restoration, zoom, scrolling and error recovery. Inspect before propagating a shared pattern.
2. Verify changes through affected popup, panel, options and injected callers. Component stories can expose states and portal problems; they do not establish browser-popup lifecycle or site permissions. Use [extension runtime testing](../browser-extension-testing/SKILL.md) for those claims.
3. Inspect toolbar/install icons at their real small sizes and listing images against current store requirements. Reuse brand assets, generate with appropriate available tools when authorized, and capture actual functioning UI for screenshots. Label temporary placeholders as unfinished and exclude them from a release-ready claim.

Return the implemented or assessed surfaces, preserved design decisions, observed behavior and remaining gaps. A critique request does not authorize source fixes or store asset uploads. [Source notes](../../references/sources.md) explain the platform sources and upstream selection.
