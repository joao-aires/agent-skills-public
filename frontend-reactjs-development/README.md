# Frontend React development plugin: React, Next.js, shadcn and Tailwind

The `frontend-reactjs-development` plugin carries implementation guidance for React and Next.js interfaces, with shadcn components, Tailwind design systems and performance patterns. It is stack-specific and composes with generic interface design.

## Purpose

Use this package when an accepted interface design needs React implementation: component structure and composition, the selected styling and component system, accessible primitives, data fetching and rendering boundaries, and performance work that survives review.

## Responsibilities

| Skill | Type | Responsibility |
| --- | --- | --- |
| [frontend-conventions](skills/frontend-conventions/SKILL.md) | method | React/Next.js structure with the selected component system, styling conventions and implementation checks |
| [shadcn](skills/shadcn/SKILL.md) | method (acquired) | Component installation, composition, styling and debugging in shadcn projects |
| [tailwind-design-system](skills/tailwind-design-system/SKILL.md) | method (acquired) | Design tokens, component libraries and responsive patterns with Tailwind v4 |
| [vercel-composition-patterns](skills/vercel-composition-patterns/SKILL.md) | method (acquired) | Component composition patterns that replace boolean-prop proliferation |
| [vercel-react-best-practices](skills/vercel-react-best-practices/SKILL.md) | method (acquired) | React and Next.js performance guidance for writing and reviewing code |

## Boundaries

- Information architecture, interaction and visual direction belong to interface design; this package implements them.
- Backend contracts, data authority and deployment stay with their owning activities.
- A component library preference does not select the stack; the project does.

### Acquired sources

| Skill | Source | Pin |
| --- | --- | --- |
| shadcn | shadcn-ui-ui | `6b600cf` |
| tailwind-design-system | wshobson-agents | `46891e7` |
| vercel-composition-patterns, vercel-react-best-practices | vercel-labs-agent-skills | `063bee9` |

## Maintenance

Bump `plugin.json` when packaged content changes. Keep the skill descriptions as the selection surface: a new capability needs a description that says when to use it and when not to, not a route from another skill. Acquired skills stay pinned in `agent-depot.json`; update them through [upstream maintenance](https://github.com/joao-aires/agent-skills-public/blob/main/docs/maintainers/upstreams.md) and never edit the upstream body.
