# Frontend native development plugin: Tauri and React Native clients

The `frontend-native-development` plugin carries one method for desktop and mobile clients built with TypeScript: Tauri for desktop and React Native/Expo for iOS and Android. It is stack-specific and applies after the client platform and backend contract are accepted.

## Purpose

Use this package when the work depends on native client mechanics: platform lifecycle, permissions, packaging, device and simulator verification, or the boundary between the client and an application backend.

## Responsibilities

| Skill | Type | Responsibility |
| --- | --- | --- |
| [native-client-development](skills/native-client-development/SKILL.md) | method | Tauri and React Native/Expo client structure, platform lifecycle, packaging and native verification |

## Boundaries

- General interface design and interaction method stay with the design activity.
- Web React and Next.js implementation belongs to the React package.
- Backend contracts, release authorization and store operations remain with their owners.

## Maintenance

Bump `plugin.json` when packaged content changes. Keep the skill descriptions as the selection surface: a new capability needs a description that says when to use it and when not to, not a route from another skill. Acquired skills stay pinned in `agent-depot.json`; update them through [upstream maintenance](https://github.com/joao-aires/agent-skills-public/blob/main/docs/maintainers/upstreams.md) and never edit the upstream body.
