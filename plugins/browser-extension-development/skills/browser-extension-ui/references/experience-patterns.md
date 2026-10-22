# Extension experience patterns

Use this when a new extension needs several surfaces, when collection work outgrows a popup or when revising an existing experience. Start with the user's task and accepted visual/component foundations. Source review can suggest useful patterns; it does not establish participant usability or make an upstream product's layout appropriate for every extension.

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

## Source-based lessons

These are observations of public source, not imported code, brand assets or claims that these extensions are objectively the best designed.

| Reference | Observed structure | Transferable lesson |
| --- | --- | --- |
| Raindrop [extension routes](https://github.com/raindropio/app/blob/a3e44eb34b0d8a3d4fab85059ed0f7f564806baf/src/routes/extension/index.extension.js) and [tab screen](https://github.com/raindropio/app/blob/a3e44eb34b0d8a3d4fab85059ed0f7f564806baf/src/routes/extension/tabs/index.js) | Clipper and tab-management views have distinct routes; the tab view composes selection, destination, metadata and submission. | Give a surface a task and make selection, destination and consequence visible. |
| Raindrop [theme roles](https://github.com/raindropio/app/blob/a3e44eb34b0d8a3d4fab85059ed0f7f564806baf/src/co/screen/basic/themes.module.css) | Theme values cover text, backgrounds, emphasis and status. | Maintain semantic roles across modes instead of patching isolated colors. |
| Bitwarden [browser surface lifecycle](https://github.com/bitwarden/clients/blob/9a03963fa07cf881f38028c7c282511b76d5481e/apps/browser/src/platform/browser/browser-api.ts) | Popup, sidebar and popout contexts have different focus and teardown behavior. | Treat lifecycle and source context as part of the interaction contract. |

Use the current [Chrome UI options](https://developer.chrome.com/docs/extensions/develop/ui) and relevant API references to verify platform contracts. A source pattern suggests a design choice; actual installed-extension journeys establish whether the resulting implementation behaves correctly.
