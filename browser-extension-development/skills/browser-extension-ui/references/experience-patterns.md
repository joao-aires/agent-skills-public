# Extension experience patterns

Use this to establish behavior across surfaces and views after choosing a task structure from [extension types](extension-types.md), or when changing an existing transition. Start with the accepted work and visual/component foundations. Source review can suggest useful patterns; it does not establish participant usability or make an upstream product's layout appropriate for every extension.

## Give each surface a clear job

A popup works well for a short recognition-and-action loop. A side panel can retain a task alongside a page. An options page gives substantial configuration room. A full extension tab can support comparison, filtering and bulk editing. Combine surfaces only when those jobs justify them, and make the transition understandable: what work continues, what context is retained and whether anything has already changed.

Keep shared business operations and state contracts consistent while adapting composition to available space. The larger view should provide useful comparison and navigation rather than merely stretching a popup. The popup should not become an entire settings application in miniature. Verify actual browser lifetimes and grants; a normal tab displaying popup HTML is useful for rendering checks but cannot prove toolbar-popup behavior.

## Retain scope and work

| Decision | What the interface needs to make true |
| --- | --- |
| Source identity | An operation belongs to an explicit window, page, account or collection. Focus changes, moving an extension tab and opening another surface do not silently replace that identity. |
| Ongoing work | Closing a transient view does not erase accepted progress or make a pending operation appear complete. Reopening reconstructs actual status and recoverable edits. |
| Concurrent views | Define whether edits synchronize, conflict or invalidate results. A late response cannot replace a newer decision; the operation boundary checks freshness as well as the UI. |
| Bulk selection | Explain whether an action affects selected items, filtered results or the whole collection. Preserve deliberate exclusions and make incomplete results visible. |
| Consequence and recovery | Keep the primary action understandable during scrolling. For reversible or partially recoverable changes, expose the actual recovery scope and remaining limitations. |

Use a recognizable title, source/domain and meaningful state hierarchy for dense lists. Search and filtering should reduce finding effort; they should not hide selection scope. Judge long titles, missing metadata, large collections, zoom and keyboard interaction rather than only a short polished fixture.

## Make configuration and access states legible

Separate settings that take effect immediately from draft values that need saving. Explain whether a change affects ongoing work, requires a new result or applies on the next session. Put errors and confirmation near their task instead of leaving them beyond a long page's visible region.

A browser grant, stored connection configuration, authenticated account and supported model/feature are different states. Represent the ones that matter to the operation. Explain the recipient and purpose before requesting access, retain useful behavior on refusal, and expose revocation/disconnection where users can find it. A successful settings save does not prove a service request succeeded.

Apply the accepted appearance policy across popup, options, larger views and overlays. Test first paint, persisted overrides, live system changes and consistency between already-open surfaces. Include native controls and intermediate transitions in contrast assessment; matching page backgrounds alone does not establish a coherent dark mode.

## Trace transitions between surfaces and views

Treat navigation as a change in work context, not simply a change of URL or component. Trace the important departures and returns for the selected extension type. A clipper can hand a draft to an editor, a vault can open authentication before filling, and a page companion can continue a conversation in a full tab. All need an explicit account of what continues and what may change.

| Question | Establish before implementation |
| --- | --- |
| What initiates the transition? | Toolbar, selection, shortcut, browser controls or an in-app action. Direct entry may have no earlier workspace or return destination. |
| What identifies the work? | Original page/window, selected objects, account, conversation, draft or job. Focus alone is usually an unreliable identity. |
| What survives departure? | Recoverable inputs, deliberate edits, selection, progress and relevant reading position. A transient surface cannot be the sole owner of required state. |
| What can change elsewhere? | Permissions, authentication, defaults, source content or another view's edits. Decide what synchronizes, applies later, conflicts or invalidates a result. |
| How does the person return? | Recognizable return/close action, browser navigation or a reused destination. Restore a useful location and focus without repeating the operation. |

Keep frequent choices for the active operation near its work; give substantial durable configuration a findable home. A shortcut and a canonical destination should reach the same persistence/validation contract. The same reasoning applies to account setup, access requests and advanced editors: proximity helps a small related decision, while a longer task can need a dedicated view. Do not solve every departure with a dialog or every persistent preference with another browser tab.

Browser entry is a special case of this method. Chrome exposes declared options through its own controls; the [options guide](https://developer.chrome.com/docs/extensions/develop/ui/options-page) documents embedded and full-page forms. Those entries must work without an earlier workspace. A browser-hosted options page and a settings route within the application can share one configuration model while having different return behavior. Similarly, a native side panel may be opened independently and can have tab-specific or shared scope; establish the actual policy instead of assuming that visual continuity implies context continuity.

Exercise the chosen transition from both an existing task and independent entry where supported. Change, cancel or fail the secondary task, then return. Confirm original scope, recoverable inputs, location and result freshness. Opening another view must not itself repeat a consequential operation. Test simultaneous views when they can affect the same work, rather than validating each screen in isolation.

## Source-based lessons

These are observations of public source, not imported code, brand assets or claims that these extensions are objectively the best designed.

| Reference | Observed structure | Transferable lesson |
| --- | --- | --- |
| Raindrop [extension routes](https://github.com/raindropio/app/blob/a3e44eb34b0d8a3d4fab85059ed0f7f564806baf/src/routes/extension/index.extension.js) and [tab screen](https://github.com/raindropio/app/blob/a3e44eb34b0d8a3d4fab85059ed0f7f564806baf/src/routes/extension/tabs/index.js) | Clipper and tab-management views have distinct routes; the tab view composes selection, destination, metadata and submission. | Give a surface a task and make selection, destination and consequence visible. |
| Raindrop [theme roles](https://github.com/raindropio/app/blob/a3e44eb34b0d8a3d4fab85059ed0f7f564806baf/src/co/screen/basic/themes.module.css) | Theme values cover text, backgrounds, emphasis and status. | Maintain semantic roles across modes instead of patching isolated colors. |
| Bitwarden [browser surface lifecycle](https://github.com/bitwarden/clients/blob/9a03963fa07cf881f38028c7c282511b76d5481e/apps/browser/src/platform/browser/browser-api.ts) | Popup, sidebar and popout contexts have different focus and teardown behavior. | Treat lifecycle and source context as part of the interaction contract. |

Use the current [Chrome UI options](https://developer.chrome.com/docs/extensions/develop/ui) and relevant API references to verify platform contracts. A source pattern suggests a design choice; actual installed-extension journeys establish whether the resulting implementation behaves correctly.
