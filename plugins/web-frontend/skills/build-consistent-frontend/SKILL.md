---
name: build-consistent-frontend
description: Build, modify or review Next.js/TypeScript and shadcn interfaces while preserving design consistency, responsive behavior, accessibility and performance. Use for screens, components, forms, navigation, UI fixes and rendered interface reviews.
---

# Build a consistent frontend

## Read the design before adding to it

Prefer Next.js App Router, TypeScript, shadcn/ui and the project's configured styling libraries for new applications; preserve established choices. Inspect shared components, tokens and at least one comparable screen before changing UI. Carry forward accepted design decisions and compatible installed UI/UX guidance; keep private material local.

For a new product, establish a small visual vocabulary early: typography, spacing, semantic colors, surfaces and a few reusable interaction patterns. Derive it from the intended users and task. Make a coherent first screen before multiplying screens. Use existing tokens in an established product; avoid a new palette, font, navigation system or dependency for a local feature.

## Choose patterns deliberately

| Situation | Preferred response |
| --- | --- |
| Similar interaction already exists | Reuse its component and behavior |
| A genuine new pattern is needed | Explain the product reason and make the pattern reusable |
| A mobile or accessibility defect exists | Fix the affected layout/interaction while preserving visual direction |
| The request is a redesign | Explore alternatives explicitly, then apply one coherent direction |

Use official shadcn expertise for component composition and Vercel React/composition skills for framework details. Use version-matched Next.js documentation rather than assuming every referenced API applies. Use shadcn MCP optionally against the configured registry; do not require it for ordinary component work.

## Implement the whole interaction

Represent loading, empty, error, success, validation and permission states where applicable. Make labels, keyboard operation, focus transitions and contrast part of the interaction, not a later polish pass. Use semantic controls and preserve accessible component behavior when composing shadcn primitives. Keep feedback actionable and avoid losing user input on recoverable failure.

For a saved-search list, reuse the established list/card and action patterns. Distinguish no saved searches from a failed load. Confirm deletion according to the project's destructive-action convention, handle a rejected deletion and update or revalidate the list after success. Do not merely remove a row optimistically without considering persistence and failure.

Keep domain decisions and authorization in the backend; synchronize UI/API types and error behavior. Prefer server rendering where appropriate and client components where interaction needs them. Keep secrets server-side and identity-dependent data isolated. Make cache/revalidation choices reflect freshness and user boundaries; avoid waterfalls and excessive client JavaScript without speculative rewrites.

## Verify the rendered result

Run applicable types/build checks and inspect affected screens in the browser at representative mobile and desktop sizes. Exercise the actual interaction, keyboard/focus behavior and relevant non-happy states. Use the installed E2E skill for critical journeys. If rendering is unavailable, state the gap instead of inferring visual correctness from source code.

Report reused patterns, any justified new design decision and checks actually performed. Measure performance before claiming an improvement; a refactor alone does not establish faster rendering. Fix drift against the accepted design rather than introducing another visual direction during verification.
