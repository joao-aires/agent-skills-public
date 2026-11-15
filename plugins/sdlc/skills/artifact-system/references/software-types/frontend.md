# Frontend

## What this is

Software with a graphical user interface: web applications, desktop clients, mobile and native clients, and browser extensions. The user acts through screens and the system's behavior is judged through the rendered experience.

## Design record must show

- the main user task and the flow that completes it;
- affected screens and navigation;
- states: empty, loading, busy, success, error, denied and stale;
- accessibility: keyboard path, focus, labels, contrast and assistive technology behavior;
- responsive and platform behavior where the accepted target requires it;
- the existing design system, tokens and components to reuse;
- an artifact that lets a reviewer judge the direction.

A frontend design record does not need a C4 diagram or an API contract unless the change also crosses those boundaries.

## Typical artifacts

Use a linked artifact at comparable fidelity for each option. Read [design specification](../../../design-spec-guide/SKILL.md) for flows, wireframes, mockups, prototypes, states, content, accessibility and handoff.

A design specification can be carried by wireframes, mockups, Figma frames, rendered slices, interactive prototypes or component-state views. A text description alone is not sufficient when layout, hierarchy, interaction or visual direction is the question.

## Seam decisions

When the frontend meets a backend or AI component, decide once:

- mapping of API errors and denials to UI states;
- loading, empty, no-results and stale distinctions;
- pagination, ordering and refresh behavior;
- authentication, tenant and permission failures;
- retry, duplicate submit and optimistic update behavior;
- offline, reconnect and conflict behavior.

## Variants and constraints

| Variant | Constraint owner |
| --- | --- |
| Browser extension | `browser-extension-development` — MV3 lifecycle, permissions, runtime messaging, store delivery |
| React/Next.js | `frontend-reactjs-development` — components, tokens, framework behavior |
| Native/Tauri/Expo | `frontend-native-development` — platform lifecycle, packaging, native verification |
| SaaS dashboard | `saas-development` — tasks, entitlements, billing administration |
| Design system or theme | `frontend-development` and the project's accepted system |

These are constraints on the frontend baseline, not separate software types.

## Verification that counts

- rendered flow at a named revision and environment;
- interaction states actually exercised;
- keyboard and assistive-technology path where claimed;
- the accepted design system preserved, not replaced by preference;
- prototype or usability observation when the question is about comprehension or task success.

## Optional specialists

`interface-design` for structure, interaction and visual craft; `ux-writing` for consequential copy; `usability-research` for participant evidence; the matching frontend pack for implementation constraints. If a specialist is absent, use the generic method, project evidence and primary sources; do not lower the evidence standard.

## Not required

C4 context/container views for a UI-only change, an API contract when no boundary changes, migration design, or a runbook.

## Example

A saved-searches panel using an existing API:

```markdown
- Affected type: frontend
- Backend: not affected — existing contract is sufficient
- States: empty, loading, saving, saved, error, denied
- Artifact: wireframe for each state plus a rendered narrow/wide slice
```
