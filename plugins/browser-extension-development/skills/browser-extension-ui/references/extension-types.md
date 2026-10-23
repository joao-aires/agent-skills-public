# Extension types and UI structures

Read the selector first, then only the patterns relevant to the product. These are starting structures derived from recurring extension tasks and public product/source references, not a browser taxonomy, copied screen designs or a requirement to implement every destination. Hybrids are normal: a bookmark product can combine capture, a searchable library and page annotation. Choose a primary loop and attach secondary loops where they actually support it.

## Select by task, not by toolbar appearance

| Main user need | Start with | Likely primary surface | What changes the choice |
| --- | --- | --- | --- |
| Save, copy, translate or transform one item quickly | [Quick action and capture](#quick-action-and-capture) | Direct action or short popup | Review/editing, destination choice or a longer job needs more room. |
| Find a saved item and use it in the current context | [Contextual library and vault](#contextual-library-and-vault) | Searchable popup or side panel | Large-scale organization belongs in a workspace; sensitive items need appropriate lock/reveal states. |
| Think, ask, compare or research alongside a page | [Persistent page companion](#persistent-page-companion) | Native side panel or deliberately injected sidebar | Page context may be pinned, follow the active tab or be selected explicitly; establish which. |
| Fill, correct or edit something at its point of use | [Inline assistance](#inline-assistance) | Anchored injected UI | Long composition or multiple sources may warrant an adjacent panel/editor. |
| Read or alter the page's presentation | [Page adaptation and reading](#page-adaptation-and-reading) | Page plus compact controls | A focused reading mode can become a separate view; global and per-site behavior must remain distinguishable. |
| Understand or change protection/rules for this site | [Site control and status](#site-control-and-status) | Scoped popup/status controls | Diagnostics and rule management can need separate views. |
| Compare, organize or apply changes to many items | [Collection and session workspace](#collection-and-session-workspace) | Full extension tab, sometimes side panel | Small frequent retrieval can have a quick-entry popup without duplicating the whole workspace. |
| Capture media/documents or run a job, then inspect its result | [Capture, job and editor](#capture-job-and-editor) | Short launch UI plus durable progress/result view | Immediate one-step captures can use the quick-action pattern alone. |
| Define repeatable browser work, triggers or site integrations | [Workflow and automation management](#workflow-and-automation-management) | Management workspace plus contextual run controls | Simple accepted automation can remain a setting; authoring recipes is a different task from running them. |
| Start browsing from a personalized destination | [Browser destination and dashboard](#browser-destination-and-dashboard) | New-tab or another deliberate browser-page override | A dashboard unrelated to browser entry may just need a normal extension tab. |
| Inspect a running page or diagnose its behavior | [Developer inspection](#developer-inspection) | DevTools panel/sidebar | A lightweight status indicator can be auxiliary; the inspected target owns the session. |
| Act through shortcuts, selection menus or address-bar queries | [Command-first utility](#command-first-utility) | Commands, context menu, omnibox or small overlay | A persistent shell is justified only by further task needs. |

AI, synchronization, account access and billing are capabilities that can occur within several types; they do not by themselves determine a navigation structure. A page assistant is not automatically conversational, and a conversational UI is not automatically permission to read every open tab.

## Quick action and capture

Use when the outcome is a small completed action against a page, selection, link or file. The interface should make the target and consequence recognizable without asking someone to navigate a miniature dashboard.

**Reference structure:** invocation → target preview → necessary destination/choices → action → receipt or recoverable error. If there are no meaningful choices, invocation can perform the accepted action directly and report its result. A successful click is not proof that saving or uploading finished.

- Show only information needed to recognize the item and make the decision. A title/source preview and collection/tag chooser can be useful; a complete library is a different loop.
- Distinguish an existing saved item from a new capture, and an in-progress save from success. Preserve a meaningful draft if the popup closes before completion.
- Escalate to an editor when composition or review outgrows the brief interaction, retaining the original target and destination. Do not require a larger workspace just to repeat the quick action.

Raindrop's [capture and sidebar documentation](https://help.raindrop.io/install-extension) demonstrates that quick saving and ongoing library use can coexist. SingleFile's [usage reference](https://github.com/gildas-lormeau/SingleFile/blob/215d83a5ba23635f01a6b867b4b4124262aae33c/README.MD#getting-started) distinguishes starting/cancelling a save, selection scope and optional annotation. Those are useful task boundaries, not a prescription for their exact menus.

**Probe:** invoke from a selection, close the transient UI during a controlled save, then recover its actual state without saving the wrong item or duplicating the operation.

## Contextual library and vault

Use when someone recognizes an existing object, inspects it and uses it on the current page or in another destination. Bookmark libraries and credential vaults share a search/list/detail grammar, while their consequences differ substantially.

**Reference structure:** current-context suggestions + search/filter → item list → detail/edit → use/open/copy action. Offer a recognizable route to broader organization and configuration when those capabilities exist. In narrow surfaces, list and detail can be sibling views with a Back action; wider surfaces can retain both.

- Decide whether selecting a row opens its details or executes its main action. Keep that meaning stable and distinguish secondary actions such as copying, editing or deleting.
- Show whether results match the current site, the chosen collection or the entire account. A selected filter must not silently redefine the target of an action.
- Sensitive vaults need locked, unlocked, reveal, account and target-mismatch behavior. A bookmarking product should not acquire those states merely because it uses the same list structure. Conversely, a password manager cannot inherit a bookmark clipper's low-consequence interaction unexamined.

Bitwarden's [autofill guide](https://bitwarden.com/help/auto-fill-browser/) documents contextual suggestions, filtering, viewing and several invocation paths. Its [extension guide](https://bitwarden.com/help/getting-started-browserext/) also describes popout/sidebar variants. Use these to investigate action meanings and lifecycle differences rather than copying a bottom navigation bar into every library.

**Probe:** change the active site while inspecting an item, return from an edit, and use a result from search. The visible context, chosen object and action target should agree.

## Persistent page companion

Use when reading and the extension task need to remain visible together: conversation, translation, research notes, source comparison or guided work. A side-panel-first product is a complete primary structure; it need not be a fallback opened from a popup.

**Reference structure:** context/source control + session navigation → working area (conversation, notes or results) → persistent input/actions. Put references and task details beside or behind the relevant result. Provide history/new-session navigation only if sessions are supported. A full-tab view can help extended work while keeping the same session identity.

The key decision is **what follows navigation**. A conversation might remain pinned to its original document, follow the active tab only for the next request, or accept explicitly selected sources. Make the chosen policy visible, including when a source is unavailable or no longer current. Avoid silently replacing a draft's target when the browser tab changes.

Distinguish a browser-native panel from a sidebar injected into the page. They can look similar while having different sizing, availability, styling, focus and permission boundaries. A companion that performs actions also needs review/stop/recovery controls appropriate to those actions; a chat transcript alone is not an adequate operation status view.

Page Assist's pinned [panel entry](https://github.com/n4ze3m/page-assist/blob/68985760b6ddcdbb12aa24491e1d5a0608b23cce/src/entries/sidepanel/App.tsx) and [routes](https://github.com/n4ze3m/page-assist/blob/68985760b6ddcdbb12aa24491e1d5a0608b23cce/src/routes/chrome.tsx) separate panel chat/settings from the larger view. Hypothesis' [annotation client](https://github.com/hypothesis/client/blob/a7b7400d0d706d4357ec37c2a3610b25dcca89d5/README.md) offers a page-annotation counterpart. These establish different implementations of page-adjacent work, not the superiority of one surface.

**Probe:** switch sites, resize/close/reopen the panel, and return to an unfinished session. Check source identity, draft/progress, keyboard access and stale result behavior. Test the actual panel host, not only a tab rendering its HTML.

## Inline assistance

Use when the relevant choice belongs to a field, text selection, sentence or page object. This includes credential suggestions, writing corrections, small translations and contextual annotations.

**Reference structure:** discoverable field/selection affordance → anchored suggestion or short editor → accept/dismiss → changed content with appropriate recovery. A panel may hold longer detail while the anchor continues to identify what will change.

- Preserve text selection/caret and identify the target across scrolling, reflow, frames and host-app updates. An accepted suggestion must not land in the field that happened to gain focus later.
- Give dismiss/escape and keyboard paths clear behavior. Avoid intercepting normal typing or obscuring the host's own validation, submit controls and accessibility semantics.
- Restrict sensitive-field access and requested grants to the accepted feature. Style isolation prevents some collisions; it does not establish safe message authority or trustworthy page content.

Bitwarden's [inline autofill](https://bitwarden.com/help/auto-fill-browser/#inline-menu) provides a concrete reference for selection at the field. Read [injected UI integration](content-ui.md) when implementing the anchor, overlays or portals; generic component defaults may mount outside the isolated root.

**Probe:** dismiss with the keyboard, edit the field before a delayed suggestion returns, and navigate/re-render the host. The extension should neither swallow the user's edit nor act on a stale target.

## Page adaptation and reading

Use when the main outcome is the page itself becoming easier to read, more accessible or differently presented. The extension UI controls the adaptation; it should not compete with the reading surface.

**Reference structure:** current site + effective mode → small relevant controls → per-site override/reset; durable defaults and exception lists in an appropriate management view. A dedicated reader can add article navigation and reading controls when that is the accepted task.

Explain the difference between the global default, an explicit site override and the currently effective result. A page that cannot be modified is different from an extension deliberately switched off. Keep returning to the original presentation straightforward; live preview should not make the save/reset meaning ambiguous.

Dark Reader's [help](https://darkreader.org/help/en/) distinguishes global activation, current-site control and site-specific adjustments. Its pinned [options composition](https://github.com/darkreader/darkreader/blob/4d3450b584ee7c0c8a3c04e830716128acbe89db/src/ui/options/body/body.tsx) separates longer-term management areas. Borrow the scope distinction, not its framework or all its controls.

**Probe:** apply a site override, navigate within and beyond that site, then reset it. Verify both page effect and the UI's effective-state explanation, including a restricted page.

## Site control and status

Use for protection, blocking, site permissions, network/privacy controls or other policies whose effective state matters more than a list of content. The main question is often “what is happening here, and what changes if I act?”

**Reference structure:** site identity + effective status → scoped primary control → relevant evidence/counts → optional exceptions/diagnostics → policy management. Distinguish extension-wide, site-wide and current-page effects before arranging toggles.

Summarize the effective state rather than exposing every rule on the first screen. Advanced rules, logs and diagnostics can support investigation without crowding the common control. A badge can indicate state, but should have a meaningful accessible equivalent and must not imply protection that is unavailable on the current page.

The uBlock Origin [popup guide](https://github.com/gorhill/uBlock/wiki/Quick-guide:-popup-user-interface) demonstrates scoped control and expandable detail. This is an interaction reference; it does not establish that its original platform/API implementation is suitable for the target Chrome/MV3 version.

**Probe:** change a site exception, distinguish pending/reload-required behavior from effective protection, and restore the prior policy. Verify the action scope instead of judging only the switch's appearance.

## Collection and session workspace

Use when organizing many tabs, bookmarks, downloads or saved sessions requires comparison, selection, editing or bulk changes. These tasks usually benefit from more space than a transient popup provides.

**Reference structure:** collection/window/account scope → search/filter + explicit selection → list/board/detail → review of proposed changes → apply and recovery where supported. Keep collection navigation separate from item actions. A compact entry point can offer recent work or one useful shortcut rather than a compressed copy of the whole workspace.

Selection and scope are the critical contract: “all” may mean all visible items, all selected items or the entire collection. Make that distinction understandable and retain deliberate exclusions when filters change. An item's identity should survive reordering; a moved extension tab should not silently retarget another browser window.

For proposed bulk changes, separate the editable proposal from effects already applied. Configuration or external edits can make it stale. Preserve work when possible, and explain the particular change that requires a fresh result. Read [experience contracts](experience-patterns.md#retain-scope-and-work) for source identity and concurrent views.

**Probe:** review a realistically large collection, filter it, exclude items, change a name and visit another view. Return with the same scope and deliberate edits; check actual apply/recovery separately from the rendered review.

## Capture, job and editor

Use when a capture, recording, export or other job continues beyond the launch gesture and produces something to inspect, edit or deliver. Treat launch, execution and result as different states with a connected identity.

**Reference structure:** capture scope/destination → start → durable running/paused/error state → result preview/editor → export/save/share. Expose stop/cancel during execution where the operation supports it. A recording can need persistent visible controls on or beside the page; a background export may instead need a recoverable jobs view.

Preserve what is being captured and distinguish finishing the job from successfully writing or uploading the output. If editing is supported, cancellation, unsaved changes and return to the result need clear behavior. Content already captured, provider access and a pending upload are different recovery concerns. Do not invent recording, sharing or cloud delivery for a simple local page saver.

SingleFile's pinned [save, batch and annotation usage](https://github.com/gildas-lormeau/SingleFile/blob/215d83a5ba23635f01a6b867b4b4124262aae33c/README.MD#additional-notes) illustrates portions of this loop. Recording controls are a related design variant, not a claim about SingleFile's features.

**Probe:** close the launch view, navigate the source and simulate a failed output write. Show actual job state and a truthful recovery path rather than a success toast from the initial click.

## Workflow and automation management

Use when people define or install repeatable work, inspect its scope and decide when it runs. This differs from a capture tool's single job: the durable object is a recipe, rule or script, and an execution is one instance of it.

**Reference structure:** workflow list + enabled/trigger state → recipe/detail editor → scope and execution configuration → explicit run/enable → run history with stop/error/recovery. A contextual popup can show which workflows apply to this site and offer a short run action; it need not reproduce the authoring workspace.

Keep editing, saving, enabling and executing distinguishable. A workflow saved successfully may never have run; one successful run does not prove that its schedule or all target sites work. Expose meaningful site/account/data scope before activation. Represent partial effects and retry boundaries so that retrying a failed later step does not blindly repeat earlier consequential actions. If externally supplied scripts or recipes are supported, their provenance and requested access need appropriate review; UI pattern selection does not establish permission to execute arbitrary remote code.

Automa's pinned [product description](https://github.com/AutomaApp/automa/blob/a4cbe34a60c92873c48c2470ca8ab1d96c22c7a0/README.md) describes block-based browser workflows and scheduling. It is a reference for the distinction between authoring and execution, not an approved execution architecture or a dependency recommendation.

**Probe:** edit an enabled recipe, run it against a controlled target, interrupt it after a partial effect and inspect the result. The UI should explain which definition ran, what happened and what a retry would do.

## Browser destination and dashboard

Use when opening a new tab, history or bookmarks is itself the intended entry into the product. This is a replacement of a familiar browser destination, not merely a large extension page.

**Reference structure:** immediate useful content/search → lightweight navigation to supported areas → deliberate customization mode → return/reset. A customized dashboard can organize widgets or shortcuts; a history replacement still needs understandable finding and date/source context.

Prioritize fast useful rendering and predictable keyboard behavior. Keep customization controls subordinate during ordinary use, and maintain readability over variable backgrounds and themes. Chrome new tabs initially focus the address bar; do not rely on automatically focusing an in-page search field. An extension can override only one of the documented Chrome destinations, so verify [override constraints](https://developer.chrome.com/docs/extensions/develop/ui/override-chrome-pages) before promising several replacements.

Tabliss' pinned [dashboard](https://github.com/joelshepherd/tabliss/blob/765a3f0b10968ee6e3a9ddf5c5360960fb4bf0ee/src/views/dashboard/Dashboard.tsx) composes background, widgets and an overlay. Use this as a structure to investigate when building a personalized start page, not as a reason to add widgets to unrelated extensions.

**Probe:** open a fresh browser tab with slow/offline data, use the keyboard, change customization and reset it. Distinguish the installed override from a normal tab showing the same HTML.

## Developer inspection

Use when the user is inspecting a particular running target, exploring its structure or recording behavior. The inspected target, not whichever tab was most recently active, owns the work.

**Reference structure:** target/connection status → inspection or recording mode → searchable tree/timeline/table → selected-object details → relevant edits/export. Navigation follows the inspected data and diagnostic task; tools may need resizable splits rather than a consumer-app settings shell.

Distinguish passive observations from changes that execute code or mutate the target. Specify what survives reload, reconnect and closing DevTools; stale selections and lost recordings need explicit states. React's [Developer Tools guide](https://react.dev/learn/react-developer-tools) illustrates component and profiler areas. Chrome's [DevTools extension guide](https://developer.chrome.com/docs/extensions/how-to/devtools/extend-devtools) defines the actual host/API lifetime.

**Probe:** inspect two different targets, reload one, and reconnect while a selection/recording exists. Keep evidence and edits bound to the intended target.

## Command-first utility

Use when a keyboard shortcut, selection context menu or address-bar query is the fastest complete interaction. Some useful extensions need little persistent UI.

**Reference structure:** contextual invocation → optional concise chooser/overlay → action/result → discoverable help, customization or recovery. A command palette needs searchable choices and reliable focus; a direct command may need only concise feedback and an accessible way to inspect its state.

Respect text-entry contexts, shortcut conflicts and Escape behavior. Make alternatives discoverable for users who cannot use the default shortcut. Menus should contain operations relevant to the actual selection/link/page. A command that opens a larger task should preserve that target rather than retarget after focus changes.

Vimium's pinned [bindings and customization guide](https://github.com/philc/vimium/blob/5aa29614bf1dce05e0d316f8c38722e17f9b38c3/README.md) demonstrates keyboard-first navigation, transient modes and help/options access. Chrome's [UI catalogue](https://developer.chrome.com/docs/extensions/develop/ui) documents commands, context menus, actions and omnibox as different invocation mechanisms.

**Probe:** invoke while typing, cancel an incomplete command, use an alternative entry, then return focus to the original task. A missing popup is not a defect if the supported loop is complete and discoverable.

## Adapt and verify the chosen structure

Use the selected pattern to derive hypotheses, not to bypass design. Before implementation, resolve the questions that change the structure:

| Decision | Evidence or consequence to consider |
| --- | --- |
| Primary loop and supporting loops | Accepted journeys, actual objects and frequent actions; remove destinations for absent capabilities. |
| Navigation grammar | Capture/receipt, list/detail, conversation/sources, preview/editor or inspection/details; provide location and return cues appropriate to that grammar. |
| Surface composition | Need for page proximity, duration, width/comparison, browser entry and available APIs; avoid one mandatory popup/panel/options combination. |
| Scope and authority | Source tab/window/site/account, selection, permission and data recipient; UI context must agree with the trusted operation boundary. |
| State and interruption | Drafts, pending jobs, manual edits, concurrent views and stale results; define the effect of closure, navigation and configuration changes. |
| Visual treatment | Existing tokens/components, readable hierarchy/density, supported appearance modes, accessible targets and appropriate progressive disclosure. |

Use representative content and difficult states from the chosen loop when reviewing. Check real surface behavior as well as screenshots. A source inspection supports a design inference; it does not prove user comprehension, cross-browser parity or runtime correctness. Consult current official contracts when implementing a platform boundary, and distinguish documented behavior from what was actually exercised.
