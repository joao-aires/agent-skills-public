# Injected UI and shared components

## Establish the integration boundary

Content scripts normally have an isolated JavaScript environment, but share the host page's DOM. Their CSS can affect the site and site rules can affect injected nodes. Choose isolation according to the feature:

| Technique | Useful when | Consequences to verify |
| --- | --- | --- |
| Narrowly scoped classes/selectors | Small intentional page annotations | No global reset, style leakage or collision with host rules |
| Shadow DOM | A substantial embedded component needs a style boundary | Tokens/fonts, portals, event retargeting, focus, accessibility and theme inheritance |
| Extension-origin iframe | A separate extension page is the appropriate boundary | Web-accessible resource exposure, communication and framing; no direct access to host DOM |

Shadow DOM is a CSS/DOM encapsulation tool, not an authorization boundary. A closed root is not a secret store. Use a page-world bridge only for a feature that genuinely needs it, validate its inputs and expose the narrowest operation. Read [Chrome content-script boundaries](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts) and the chosen framework's content-UI integration before mounting.

## Adapt the real component system

Shared components may assume their styles, tokens and portal root live on `document.body`. Moving the trigger into a shadow root without moving the menu/dialog can produce an unstyled or hidden overlay and broken focus behavior.

- Mount compatible generated CSS and semantic variables at the intended root; do not inject a global Tailwind reset into an arbitrary host page. Keep light/dark selectors and custom font resources effective inside the chosen boundary.
- Use the installed primitive's supported portal/container API. Render overlays where their styles and stacking/focus behavior remain coherent. Do not replace a working accessible primitive with a visual imitation merely to avoid configuring its container.
- Test labels and accessible names in the actual boundary, focus entry/Tab/Escape/restoration, outside interaction and event retargeting. Check whether dismissal belongs to the embedded panel or the entire browser surface.
- Handle SPA navigation and reinjection without duplicate roots, listeners or stale page references. Clean up owned nodes/listeners when the feature unmounts and preserve unrelated page state.

Layering requires inspection of the actual stacking context and browser top layer. An arbitrarily large `z-index` does not establish that an overlay appears correctly or remains usable. The page can also change after injection; verify the meaningful interaction against representative host behavior.

## Keep assets and communication compatible

Reference bundled resources through supported extension URLs and declare only the web exposure actually needed. Test icons/fonts/styles in the production build, where development-server URLs are unavailable. Follow the accepted theme and identity rather than treating the host site's CSS as the product's design tokens.

Communicate with privileged contexts using the package's [message-boundary guidance](../../browser-extension-security/references/permissions-and-messages.md). A host-page event should never become a generic command channel for credentials, arbitrary fetches or script execution.
