# Browser extension development plugin: Chrome Manifest V3 end to end

The `browser-extension-development` plugin carries methods for Chrome Manifest V3: architecture, permissions and trust boundaries, extension surfaces, real-extension testing and store delivery. It is stack-specific and assumes the extension decision is already made.

## Purpose

Use this package when the work depends on how Chrome extensions actually behave: service-worker lifecycle and restarts, messaging and persistence, permission grants and content-script boundaries, popup and panel surfaces, testing against a real loaded extension, and a production package that a store will accept.

## Responsibilities

| Skill | Type | Responsibility |
| --- | --- | --- |
| [browser-extension-development](skills/browser-extension-development/SKILL.md) | method | MV3 entry points, background lifecycle, messaging, persistence, migration and debugging |
| [browser-extension-security](skills/browser-extension-security/SKILL.md) | method | Permissions, trust boundaries, content-script messaging, privacy and least privilege |
| [browser-extension-ui](skills/browser-extension-ui/SKILL.md) | method | Task-to-surface matching across popup, side panel, options, content UI and commands |
| [browser-extension-testing](skills/browser-extension-testing/SKILL.md) | method | Unit, component and real-extension tests, worker restart, lifecycle and site permissions |
| [browser-extension-delivery](skills/browser-extension-delivery/SKILL.md) | method | Production ZIP contents, listing and privacy evidence, store readiness |

## Boundaries

- Web application design and general interface work stay with their generic activities.
- Store account operations, publisher identity and payment details are not automated here.
- A failed store review is evidence to act on; this package does not bypass review or permissions.

## Maintenance

Bump `plugin.json` when packaged content changes. Keep the skill descriptions as the selection surface: a new capability needs a description that says when to use it and when not to, not a route from another skill. Acquired skills stay pinned in `agent-depot.json`; update them through [upstream maintenance](https://github.com/joao-aires/agent-skills-public/blob/main/docs/maintainers/upstreams.md) and never edit the upstream body.
