# Read-only extension UI assessments

These are design and implementation assessments, not an implementation or a verified audit of a running extension. The available guidance was inventoried first. The requested `browser-extension-full-build/plugins` directory was absent, so guidance was read from the plugin directories directly under `browser-extension-full-build`. No application source, generated package, screenshot or running extension was supplied for these assessments. The user's scope takes precedence over suggestions in guidance to implement, render or verify a real application.

## Response 1 — A quick research note against the current page

**Recommend a toolbar popup for the first slice**, with durable local drafts and an explicit source-page label. The stated task is a short note, so a quick invocation and one primary action fit well. A side panel is a useful alternative if researchers need to keep reading, compare passages or revise a note while navigating. This recommendation is a product hypothesis based on the brief, not participant research.

Assume one researcher, local notes, no account and no off-device transfer for this slice. Do not introduce a backend, authentication or a UI framework to make this design concrete.

### Surface comparison

| Concern | Toolbar popup | Side panel |
| --- | --- | --- |
| Main advantage | Quick capture with a clear beginning and end. | Research page and editor remain available alongside each other. |
| Main cost | Clicking the page dismisses the popup; its document and React/component state, if any, disappear. | Uses horizontal space and needs a clear relationship between panel, tab and note. |
| Layout | A compact source header, labeled note field, save feedback and one primary button. Allow long titles and text to wrap. | Same information hierarchy with more editing space; adapt to browser/user resizing rather than prescribing one fixed width. |
| State | Reconstruct the page-bound draft and save result on every open. Closing must not imply either Save or Cancel. | Surviving longer does not make its state durable. Restore after closure/reload, and define behavior on tab changes and navigation. |
| Page access | A qualifying toolbar invocation can supply temporary `activeTab` access to the current page. | Opening the panel is not a standing grant over every tab it later displays beside. Access must follow the supported invocation/grant mechanism. |
| Added capability | Declare an action popup. | Use the side-panel manifest/API capability, including the `sidePanel` permission where required by the selected target. Establish global versus tab-specific panel behavior deliberately. |
| Verification | Actual toolbar opening, click-away destruction, reopen and persisted draft/save result. | Actual panel opening, resizing, tab/site changes, close/reopen and loss of access. |

A popup's maximum dimensions are a browser limit, not a recommended layout. A panel has no universal fixed-width contract. Both need checks with long source titles, meaningful note content, narrow available space and zoom.

### Concrete proposed interaction

A text wireframe is sufficient for this assessment:

```text
New research note                       Close
source.example · Source title wraps as needed
Page captured when this editor opened   Change page

Note
[ Why this source matters to my research…       ]
[                                               ]
Draft saved on this device

                                      Save note
```

The source title and origin orient the researcher; the note is the visual focus. “Change page” is conditional on the chosen surface and available grants. In the popup, reopening from another page creates or restores that page's draft. In the panel, keep the current draft pinned to its captured page; show “You’re viewing a different page” after a tab/navigation change and offer an explicit capture action. Do not silently attach an old note to a new page or clear a draft. Refreshing access may require invoking the extension on the new tab, rather than merely clicking inside an already-open panel.

| State/transition | Proposed behavior |
| --- | --- |
| Open on a supported page | Capture available title/URL and tab/document context; restore the matching draft. |
| Empty note | Visible label and brief prompt; Save unavailable with an understandable reason. Do not invent a character limit without a product requirement. |
| Typing | Persist recoverable draft updates outside the disposable UI. Show “Draft saved” only after the storage write succeeds. |
| Save | Commit a note tied to the captured source; disable duplicate submission until resolved. Distinguish a recoverable draft from a committed note. |
| Success | Show “Note saved on this device” after persistence completes, with Edit available while the surface remains open. |
| Storage failure | Retain the editable text, identify that it has not been saved and offer Retry. Never close the editor as a success response. |
| Restricted page or unavailable metadata | Explain the limitation. Offer manual source entry/local text capture if useful; do not request broader access as a silent fallback. |
| Close/reopen | Restore the most recently acknowledged persisted draft. Do not rely on unload-time writes. The behavior of the final in-flight keystrokes must be measured before claiming lossless capture. |
| Navigation during save | Finish against the original captured source or return a recoverable stale-context error. Never retarget to whichever tab is now active. |

Use a real textarea, visible label, visible focus, logical keyboard order and an announced save/error status. If a shortcut is proposed, document it beside the button and verify composition/IME behavior; it must supplement the visible action. Do not make a dismissible popup responsible for a nested confirmation that cannot prevent browser dismissal.

### Permissions, persistence and authority

For metadata capture plus local note storage, the initial permission proposal is `activeTab` and `storage`; add side-panel capability only for that surface. Reading tab title/URL after an invocation does not itself require DOM injection, a general `tabs` permission or all-site host access. `scripting` becomes relevant if the accepted feature later injects an editor or reads a selected passage through a content script. Automatic site integration would need a separately justified host/content-script access design; it is outside this first slice.

Use `storage.local` for committed notes and recoverable drafts, assuming on-device persistence is the accepted behavior. `storage.session` cannot satisfy persistence across browser restarts; `storage.sync` introduces replication, quota and privacy implications and is not implied by “save a note.” Storage is not encrypted secret storage. Store only the source metadata and note needed for this task, explain local retention and provide a deletion path in any eventual notes management surface. Source URLs can contain private query/fragment data: settle retention/redaction rules explicitly rather than silently changing the association.

Give a note a stable note identifier and store its source URL/title snapshot, text, modification time and revision. Bind in-flight page operations to the captured tab/document as applicable; a tab ID alone is not a durable note identity. Define whether an exact URL or an accepted normalized URL identifies a page before merging drafts; do not infer canonical equivalence. Repeated Save/retry should update the same intended note rather than create accidental duplicates.

The popup or panel may write local state directly if that fits the architecture. A service worker is not mandatory for this local feature. If used for coordination, it is event-driven and restartable; its globals cannot own drafts or be the only evidence of a completed save. Distinguish durable acknowledgment from “message received.” Any privileged receiver must validate the operation, caller and payload, not just TypeScript types or a matching extension ID.

### Proposed visual direction, without selecting a framework

Two coherent candidates fit different research habits:

- **Quiet capture tool — recommended:** low-chrome neutral surface, a readable UI sans, a dominant note field, subdued source metadata and one restrained action accent. It minimizes interruption when moving through many research sites.
- **Reading notebook:** warmer page surface, a serif for source/title hierarchy and more generous editorial spacing. It supports reflection and longer reading, but consumes more of a compact popup and needs care to keep metadata and controls easy to scan.

Both are proposals, not accepted identity. For the first slice, use semantic roles such as surface, text-primary, text-secondary, action, focus, error and saved-status; choose actual colors/type and measure contrast in a later authorized rendered prototype. Avoid adopting Chrome's visual identity by default. No decision here selects React, WXT, CRXJS, Tailwind or shadcn.

### Verification approach and present limits

A future authorized prototype should show populated, empty, long-content, unavailable-page and storage-error states in both candidate surfaces if the surface decision remains open. Then test the selected surface as a loaded production extension: real invocation/grant, denied or revoked applicable access, navigation during save, immediate click-away/reopen, offline local capture and browser restart. Independently inspect stored note/source associations. If a worker exists, force a restart and separately distinguish actual idle suspension from forced termination.

A web preview or a popup URL opened in a normal tab cannot establish actual popup destruction or `activeTab` invocation. No visual mockup was rendered and no browser test ran for this design assessment. This is a concrete behavioral proposal and comparison, not proof of usability, accessibility or platform compatibility.

## Response 2 — Assessing the existing note-editing dialog

**The proposed dialog can be assessed within the accepted React/Vite/CRXJS, Tailwind v3 and Radix architecture.** Retain the warm editorial palette, licensed bundled serif and light-only styling. These are accepted requirements, not defects. No migration to Next.js, WXT, Tailwind v4, another primitive library, system-only typography or dark mode is justified by this request.

No dialog code, design image or running build was provided, so there is no substantiated finding that its contrast, focus behavior or layout is currently broken. The items below are assessment criteria and implementation risks to examine, not invented defects or completed fixes.

### Interaction and shared component contract

A dialog is a reasonable candidate for editing a short note in context. Keep the note's source visible and unambiguous, put the labeled editor above secondary metadata, and distinguish Save from Cancel. If the real proposal contains substantial navigation or long research workflows, evaluate whether the chosen dialog still supports the accepted task; do not redesign it preemptively.

Before implementation, trace each actual caller: extension popup, side panel/options page if present, and injected editor. Record intentional differences rather than assuming every possible surface exists. A single shared dialog definition is insufficient evidence that all portals and caller overrides work.

Proposed contract: open with the current stored revision and captured source; edit a separate recoverable draft; Save updates the same note and reports success only after persistence; Cancel follows the existing discard/recovery convention. During saving, prevent duplicates and preserve text on failure. If another surface edits the note, use revision/conflict handling so a stale save cannot silently overwrite newer work. Navigation or extension invalidation must leave a recoverable draft and must not redirect its source association.

Use the installed Radix Dialog primitive and its compatible APIs for Title, description where useful, labeled textarea, focus entry, containment, Escape and focus restoration. Initial focus usually belongs in the short-note field; test whether it obscures context or behaves differently for assistive technology. Avoid nested forms/dialogs unless the existing interaction requires them. If the invoking page control disappears after navigation, define a valid fallback focus target. Saving/error feedback needs an accessible live status; color alone is insufficient.

Distinguish the dialog's close behavior from its containing browser surface. Radix can govern Escape/outside interaction within its document, but cannot veto toolbar-popup destruction when the user clicks away. A dirty-state confirmation inside a popup cannot be the sole data-loss strategy.

### Implement within the accepted system

Inspect existing component variants, semantic CSS variables, Tailwind v3 configuration/content paths, installed Radix versions and the bundled font rules before proposing a change. Reuse these sources of truth. Preserve v3-compatible utilities/configuration; do not paste v4 CSS-first setup or install dependencies for a simple note form. React/Vite extension pages are bundled client code; server components/actions do not run in the popup or service worker.

Retain the editorial serif in its accepted roles and verify real glyph coverage, wrapping, loading and fallback behavior. Confirm its existing license covers the intended bundled distribution if this is not already recorded; no new licensing/account workflow is authorized. Use the same light tokens in extension pages and injected UI even when the host site or OS is dark. The accepted light-only choice still needs readable controls, focus and status indicators, but does not create a dark-mode requirement.

Inspect the production CRXJS output when implementation is authorized: authored configuration alone cannot establish final script paths, CSP, fonts, permissions or exposed resources. Development-server font/style success is weaker evidence than an offline production package.

### Injected research-site editor: the critical boundary

Content-script isolated JavaScript worlds do not isolate CSS or DOM. A host page's resets, fonts, stacking contexts and SPA lifecycle can break a visually correct extension-page dialog.

1. **Choose or retain a deliberate mounting boundary.** For a substantial injected editor, a ShadowRoot is a plausible styling boundary if compatible with the current architecture. Do not require a migration if existing scoped styles or an extension-origin iframe already satisfy the requirements. Shadow DOM is not an authorization or secrecy boundary.
2. **Keep the dialog and its styles together.** If mounted in a ShadowRoot, place compiled compatible CSS, semantic variables and font declarations where they apply. Scope Tailwind's reset to the editor boundary rather than injecting global Preflight into arbitrary research sites. Inspect inherited properties, dimensions and box sizing explicitly.
3. **Configure Radix's portal container.** A trigger inside the ShadowRoot with a default portal under host `document.body` can produce an unstyled overlay and incoherent focus/stacking behavior. Use the installed primitive's supported container mechanism to keep overlay/content within the intended styled boundary. Do not replace Radix with a homemade visual imitation to avoid this work. Actual Shadow DOM focus/event behavior must be tested rather than assumed from a container setting.
4. **Inspect stacking and modality.** Test host sticky headers, overlays, transforms and browser top-layer content. A very large `z-index` does not outrank every stacking context or the top layer. Verify outside interaction, background scrolling, focus trapping, labels, Escape and focus return in the actual injected boundary. The host page must remain usable after closure.
5. **Handle page lifetime.** Own one editor root per intended document/frame, avoid duplicate listeners/roots during reinjection or React development remounts, and clean up only extension-owned nodes/listeners. Handle SPA navigation, tab navigation, unavailable content scripts and invalidated extension contexts. Reject late responses for stale documents.
6. **Bundle and expose narrowly.** Resolve assets using supported extension URLs. Declare only fonts/styles/iframe resources that actually require web accessibility, scoped to matching sites. Inspect production loading under relevant host CSP rather than assuming every resource works because it is bundled. Never expose the entire extension package for convenience.

An iframe would provide a different origin/style boundary but adds framing, resource exposure, focus and messaging considerations; it is an alternative to assess only if the existing approach needs it, not an authorized replacement. A page-world bridge is unnecessary for ordinary note editing; if existing integration requires one, expose narrowly validated operations.

### Permissions and note authority

Preserve the existing permission model unless an evidenced change is needed. User-invoked injection can potentially use temporary `activeTab` plus `scripting`; automatic research-site injection requires the appropriate matches and grants. These are different product behaviors. Do not broaden to all sites to hide failures. Represent restricted pages, absent/revoked access and disconnected scripts separately, with recoverable input and an actionable next step.

Trace edit/save messages through the current architecture. Validate payload shape/size, allowed operation, note identifier, revision and actual sender context at the privileged receiver. For injected callers, bind operations to the expected tab/frame/document and relevant site/grant. The host page must not choose arbitrary note resources or turn the worker into an arbitrary fetch/script endpoint. A sender sharing the extension ID is insufficient authorization. Render note text as text; do not convert untrusted notes or page metadata into unsanitized HTML.

Keep durable notes and recoverable drafts outside component state and restartable worker globals. Deliberately restrict storage access to the contexts that need it where supported; content scripts need not receive the entire note library. If the accepted extension already has an account/backend, retain its architecture and enforce resource ownership there. Neither a new backend nor account setup is implied by this assessment.

### Verification approach

| Evidence level | Checks to perform during a separately authorized implementation | Claims it cannot establish alone |
| --- | --- | --- |
| Source/package inspection | Existing instructions, locked versions, actual callers, Tailwind v3 tokens, font integration, portal root, persistence/messages and final CRXJS manifest/resources. | Rendered visual quality or real permission behavior. |
| Existing unit/component suite | Save/failure/retry, duplicate prevention, conflict/stale-source handling, labeled controls and keyboard behavior in the component setup; malformed/unauthorized messages cause no protected effect. | Browser-popup destruction, actual worker termination or real host-page interference. |
| Rendered assessment | Compare with accepted warm editorial design; realistic long titles/notes, font loading, narrow widths, zoom, focus/status visibility and light-only appearance on dark host sites. Measure actual color pairs before making contrast claims. | User acceptance, persisted save outcomes or complete accessibility. |
| Production extension in isolated supported browser | Real toolbar/panel invocation where present; edit/save/reopen; persisted text and correct source; permission decline/revocation; restricted pages; navigation and invalidated context; worker restart if present. | Store approval or other browser/OS variants. |
| Injected journeys | Controlled representative research pages with aggressive resets, sticky overlays and SPA changes; Radix portal/focus/Tab/Shift+Tab/Escape/outside behavior, scrolling and cleanup; offline production font/icon/style loading. Include targeted assistive-technology checks. | Every research site or future host-page change. |

Preserve the existing test runner. Before adding runtime tests, check the installed driver's current extension-loading contract and supported Chrome/Chromium channel. Use an isolated disposable profile and controlled pages, and record browser/driver/build identities. Headless checks can establish only the interactions that driver supports; use actual headed/manual browser-surface checks when toolbar or panel operation requires them. Opening `chrome-extension://…/popup.html` as a normal tab does not reproduce the toolbar lifecycle or grant. Forced worker termination and observed idle suspension are different evidence; keeping DevTools attached can change normal suspension behavior.

During eventual implementation, run existing relevant type/lint/build checks and meaningful behavior tests, then inspect the production extension. Record every affected caller as checked, intentionally unchanged or unverified. Fixes would need separate authorization; this assessment makes no source changes. Current result: the architectural approach is feasible in principle, with injection/portal, focus, durable state and source-binding behavior as the main boundaries needing evidence.

## Guidance files read

All paths below are relative to `built-plugins/`:

- `browser-extension-development/skills/browser-extension-ui/SKILL.md`
- `browser-extension-development/skills/browser-extension-ui/references/content-ui.md`
- `browser-extension-development/skills/browser-extension-development/SKILL.md`
- `browser-extension-development/skills/browser-extension-testing/SKILL.md`
- `browser-extension-development/skills/browser-extension-testing/references/runtime-drivers.md`
- `browser-extension-development/skills/browser-extension-security/SKILL.md`
- `browser-extension-development/skills/browser-extension-security/references/permissions-and-messages.md`
- `frontend-development/skills/interaction-design/SKILL.md`
- `frontend-development/skills/visual-design/SKILL.md`
- `frontend-development/skills/visual-design/references/visual-direction.md`
- `frontend-development/skills/interface-quality/SKILL.md`
- `frontend-reactjs-development/skills/frontend-conventions/SKILL.md`

The browser-extension guidance governed surface lifecycle, permissions and isolation; interaction/visual guidance supplied behavior and an open-direction comparison for request 1; interface quality and frontend conventions supplied read-only review criteria and version-compatible preservation for request 2. Guidance defaults for new web applications were not treated as requirements for an extension or permission to migrate the accepted stack.

## Actual checks and limits

- Confirmed the working directory and inventoried `SKILL.md`/`AGENTS.md` names within the supplied guidance tree. Checked the requested `plugins` location conditionally and used the fallback direct plugin layout.
- Read only the guidance files listed above; did not read peer outputs or other evaluation files. Their instructions were treated as guidance within the user's assessment-only scope.
- Checked this output document for both responses, the guidance record, the checks/limits section, Tailwind v3 preservation and the injected Radix/ShadowRoot discussion; these document-completeness checks passed.
- Cross-checked the two proposed responses against the supplied surface, lifecycle, security, injected-UI, version-preservation and evidence-level guidance.
- Created this requested assessment output only. No source repository changes, dependency installation, project scaffolding, app/account setup, browser loading, tests, build, contact with services or publication occurred.
- No repository audit, screenshots, contrast measurements, browser/driver version checks, license-document inspection, runtime accessibility checks or extension journeys were performed. No claim of a passing build, safe package, WCAG conformance, validated visual quality or user approval is made.
- External primary-documentation links contained in the guidance were not fetched because this assignment prohibits contacting services. Exact current API availability, supported target Chrome versions, side-panel behavior, Radix version behavior and automation-driver contracts remain items for current primary-documentation verification during authorized implementation. Platform descriptions here are design constraints drawn from the supplied guidance, not fresh compatibility certification.
