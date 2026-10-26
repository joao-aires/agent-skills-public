---
name: browser-extension-development
description: Design, implement, debug or migrate Chrome Manifest V3 extensions. Use for extension entrypoints, background lifecycle, messaging, persistence and WXT/CRXJS integration; preserve the accepted UI framework and backend.
user-invocable: false
metadata:
  scope: stack-specific
  invocation: both
  role: support
  stack: Chrome, Manifest V3, WXT, CRXJS
  source: https://github.com/quangpl/browser-extension-skills/tree/249886cf8137086792b6c3a5a2f7adce117a9f8d
---

# Build around the extension's execution boundaries

Use this expertise within the requested activity. A design request ends at design; implementation uses accepted requirements and the project's contribution process. For new work, establish the user action, sites/data involved and useful first slice before selecting entrypoints. Reuse established decisions without another questionnaire. This package targets Chrome/MV3; other browser APIs, stores and background models need their own compatibility evidence.

## Establish the actual application

Inspect project instructions, package scripts and lockfile, source configuration, generated manifest and supported browser versions. Trace the feature through the contexts that actually execute it:

| Context | Responsibility and lifetime |
| --- | --- |
| Popup | Short interaction; destroyed when dismissed. Save meaningful work outside its component/DOM state. |
| Side panel or options page | Longer interaction, still subject to closure and reload. Reconstruct state and pending work deliberately. |
| Content script | Operates on a particular page/frame; shares the DOM with the site while normally running in an isolated JavaScript world. Navigation and extension updates can invalidate it. |
| Extension service worker | Event-driven coordination without a DOM. Can terminate and restart; process globals are temporary caches. |
| Backend, when needed | Trusted credentials, account/resource authority or durable remote work. It is a separate service with its own accepted stack. |

Place each operation where its authority and lifetime fit. A short popup cannot own a long export merely because it started it. Define where completion is stored, how another UI discovers progress, and what happens if the user closes the surface or the worker restarts. A local-only extension does not automatically need a backend or account system.

## Preserve the chosen implementation

For existing work, use its framework, package manager, formatter and test runner. For an unresolved new project, compare the smallest sufficient approach: plain bundled extension entrypoints, WXT's entrypoint conventions or CRXJS's Vite integration. Choose from required browsers, framework compatibility, build control, maintenance and team familiarity. React alone does not settle the extension framework.

Read [framework configuration and migration](references/framework-and-migration.md) when scaffolding, changing entrypoints or moving from MV2. Distinguish authored manifest configuration from generated output. Inspect the production manifest after the build: source configuration alone cannot establish packaged permissions, paths or CSP. A React extension surface runs bundled client code; server rendering and server actions belong to an actual server application, not its popup or worker.

Use available interaction/visual expertise for the experience and matching language/framework expertise for implementation. Without those specialists, derive behavior and visual choices from the accepted product and project, consult primary sources and retain the same verification standards. No optional skill installation is required.

## Make messaging and state explicit

Define small messages around application operations: the caller's context, supported payload, permitted resource, response/error and whether retry can duplicate an effect. TypeScript types help callers but do not validate incoming messages. Use [permissions and security](../browser-extension-security/SKILL.md) for authority, runtime validation and privileged actions.

### Make worker restart behavior part of the operation

Register worker event listeners synchronously at module initialization. Restore needed state within the handler instead of awaiting startup before registering listeners.

For work whose outcome must survive a restart or lost response:

- Persist accepted jobs/checkpoints before acknowledging durable work.
- Use appropriate storage and idempotent or reconcilable effects.
- Recover progress rather than keeping the worker artificially alive as a substitute for a recovery design.

Use alarms for suitable scheduled work rather than assuming an in-memory timer will survive suspension. Establish timing precision from the selected browser API.

Handle unavailable content scripts, closed tabs, revoked access and invalidated extension contexts as ordinary lifecycle states. Surface an actionable result and preserve recoverable drafts. Never replay a privileged action against a different tab merely because the original disappeared.

## Verify the integrated feature

Build the production output, load that output into an isolated supported browser and exercise the user action through its real contexts. Use [extension testing](../browser-extension-testing/SKILL.md) for driver and lifecycle evidence, and [extension UI](../browser-extension-ui/SKILL.md) for actual surfaces. Report the framework/browser/build tested, observed effects and unavailable checks. Unit mocks, a web preview and successful hot reload establish narrower claims than a working packaged extension.

The [source notes](../../references/sources.md) distinguish reviewed upstream ideas from maintained platform guidance.
