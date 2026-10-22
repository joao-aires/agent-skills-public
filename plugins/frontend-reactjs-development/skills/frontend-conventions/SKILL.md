---
name: frontend-conventions
description: Build, extend or review React/Next.js interfaces using the selected component system, compatible styling
  conventions and supplied visual references. Use for dashboards, customer applications,
  storefronts, content sites, navigation, styling, forms and frontend architecture;
  preserve accepted project choices during ordinary feature work.
metadata:
  scope: stack-specific
  invocation: both
  stack: React, Next.js, Tailwind, shadcn
  role: support
user-invocable: false
---

# Frontend conventions

## Establish the direction

Read the request, `AGENTS.md`, existing components and accepted design decisions. Establish the component system and light/dark/system appearance policy with visual and interaction design expertise before dependent implementation. Preserve the user's choice of plain Tailwind, Tailwind with shadcn/ui, HeroUI or another compatible system; installed guidance is not a reason to switch libraries. The shadcn-specific conventions below apply when that system is selected. For another library, retain the design/verification outcomes and use its version-matched primary contracts and available implementation expertise.

| Context | Applicable starting guidance |
| --- | --- |
| New web application | When the stack is open, prefer Next.js App Router and TypeScript; recommend a compatible component/styling system through the UI foundation decision. Tailwind v4 with shadcn/ui is a candidate, not an override of an accepted choice. |
| Tauri React/Vite DOM interface | Apply the visual/interaction process and compatible Tailwind/shadcn conventions; web SSR defaults are inapplicable. |
| Browser extension DOM interface | Preserve its bundler and extension entrypoints; apply compatible components/tokens. Server rendering/actions require a real server and do not run in extension pages/workers. |
| React Native | Use native components, not DOM primitives. |
| Desktop or iOS/Android | Also use native-platform implementation and driver expertise. |

Preserve an established React/Vite or other frontend unless migration is requested. Use the project's package manager, locked versions and primitives; keep Tailwind v3/v4 and Radix/Base UI APIs compatible.

When Tailwind v4 is selected for a new Next.js project, use `@tailwindcss/postcss`, `@import "tailwindcss"` and CSS-first semantic tokens via `@theme`/`@theme inline`. When using shadcn/ui, follow its selected preset rather than creating a competing token system. For another system, use its own supported theme mechanism and avoid mixing incompatible Tailwind/component major versions.

Use visual design expertise for product-derived direction, accepted references and semantic token intent, and interaction design expertise for behavior. These generic methods apply beyond React; this skill owns the compatible React/Next.js implementation. Record meaningful stack deviations in the existing project note.

## Design behavior and account for every affected surface

Use interaction design expertise before meaningful new or changed UX. Define goals, flows, information/actions and state transitions in concise text; add wireframes/mockups only where they settle spatial/visual uncertainty. Resolve consequential choices and state reversible assumptions before coding; reuse agreed direction without another approval ceremony. Do not invent UX independently as each page is implemented.

For cross-cutting work, inventory affected surfaces, establish a representative interaction pattern and reconcile the final result, using relevant expertise when available. Propagate shared implementations and verify actual callers/variants; preserve intentional differences and report incomplete coverage.

## Implement the accepted visual system

Translate the accepted direction into semantic roles before assigning utilities across pages. Establish which tokens represent the page, raised surfaces, primary and secondary text, emphasis, interactive controls and status. Map those roles through the selected system’s supported token/theme mechanism. With Tailwind, use compatible CSS variables and theme pairs; another system does not need Tailwind scaffolding. Retain the selected component system as the implementation foundation.

Build shared component variants for repeated differences that have a meaning in the product. Keep one-off layout choices close to their caller, and move a repeated pattern into a shared composition when its behavior and appearance need a common owner. Reuse the selected system’s reviewed primitives/blocks and the project's class-merging convention so local overrides do not quietly create a competing visual system. Preserve deliberate density and platform variants.

Compose the product's layouts from those primitives. Implement the accepted light/dark/system policy across first paint, saved preferences, live changes and all affected surfaces, including portals. Use version-matched guidance for unfamiliar compatible APIs; establish typography, composition and product character through visual design reasoning. A component library supplies implementation primitives, not the product direction.

## Make interactions dependable

Use semantic controls, visible labels, keyboard access and clear focus.

- Use actual compatible primitives from the selected system for menus/dialogs, not handwritten visual lookalikes lacking semantics or focus behavior.
- Verify focus containment, dialog roles/labels and restoration to the invoking control after closing, and never substitute tooltips or placeholders for labels.
- Include loading, empty, error, validation and permission states.
- Preserve input on recoverable failures, prevent duplicate submission and provide actionable errors.
- Destructive actions follow the existing confirmation or recovery convention.

### Layout and data interaction

Use pages for substantial editing, panels for quick inspection and dialogs for short decisions.

- For growing datasets, use bounded server pagination/filtering, consistent row actions and bulk actions with explicit selection scope.
- Put non-sensitive shareable view state in the URL.
- Localize dates, time zones, numbers and units deliberately.

| Required interaction | Candidate for compatible projects |
| --- | --- |
| Complex forms | React Hook Form with Zod |
| Complex tables | TanStack Table |
| Charts that serve the task | A chart library such as Recharts |

Simple fields and static lists need not acquire these dependencies. Client validation helps users; the backend validates and enforces all business rules.

## Keep React and API boundaries clear

- Organize by feature with shared primitives; avoid a bespoke application framework.
- In Next.js, default to Server Components for server data and small Client Components for interaction.
- Keep secrets on the server and authorize every server action/endpoint.
- Call hooks consistently, keep state close to its owner and avoid effects that merely derive state.

Use typed backend contracts, preferably generated from FastAPI OpenAPI where applicable. Choose a coherent fetching/cache strategy: use TanStack Query when interactive remote state warrants it, rather than duplicating Server Component requests. Scope private caches by identity/tenant, invalidate affected data after mutations and handle optimistic-update failures.

Avoid request waterfalls, oversized client bundles and avoidable layout shifts. Use appropriate image sizing, defer secondary work and measure actual problems before adding optimization complexity.

## Deploy the frontend as an application

Test the production build/start path, configuration and representative authenticated journey; development-server success is narrower evidence.

- Identify build-time and runtime settings.
- `NEXT_PUBLIC_*` values are public and compiled into the client build; changing deployment environment variables does not rewrite that bundle.
- Prefer an explicit runtime configuration boundary when one artifact must serve different environments, exposing only safe values.
- If a build must differ, give it a new identity and validate it.

When deploying multiple instances or changing hosting, read [production hosting and configuration](references/sources-and-exceptions.md#production-hosting-and-configuration) for cache scope/invalidation, identity isolation, version skew and proxy behavior. Verify the actual served path and affected outcome; local startup cannot establish fleet-wide behavior. Seek available delivery expertise for promotion and recovery mechanics.

## Verify and use specialist guidance proportionately

For new compatible React projects, use TypeScript and ESLint with the project formatter; preserve existing accepted tools and configure their actual commands.

- Run relevant types, lint and build checks.
- Evaluate rendered visual quality against the product-derived direction separately from functional, accessibility and journey checks.
- Inspect actual target layouts with realistic content, navigation, keyboard focus and failure states; repair visible discrepancies and recheck before completion.
- A screenshot baseline cannot establish taste, and an automated accessibility check cannot establish usability.
- Test the critical journey against real persistence using the project's E2E workflow; a screenshot alone is insufficient.
- Keep changed contracts and accepted design decisions synchronized, and report checks actually performed.

These defaults cover routine work without reference browsing. Use bundled shadcn, Vercel React/composition and Tailwind design-system skills for unfamiliar components or deeper implementation questions. The bundled Tailwind guide targets **v4** and applies when that styling system is selected. Apply a requested v3-to-v4 upgrade as a focused migration: check browser compatibility, dependencies, configuration and rendered behavior; do not migrate an unrelated existing application silently. Consult [sources and exceptions](references/sources-and-exceptions.md) for version migrations or decisions these defaults do not resolve.

For API changes, verify actual client behavior against supported provider contracts, including errors, optional fields and pagination. Generated types do not prove semantic compatibility. Keep old open browser sessions in the supported-consumer set during rollout and route planned breaks through backend/delivery guidance.

For meaningful visual critique or refinement, seek available interface assessment expertise. Prioritize findings against the product-derived visual direction and implement accepted changes with this stack's compatible primitives. Use interface-language expertise for material task language. Use usability research expertise for a requested study or real unresolved user question, rather than requiring research for routine frontend work.
