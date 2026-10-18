---
name: frontend-conventions
description: Build, extend or review React/Next.js interfaces using opinionated shadcn/Tailwind
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

Read the request, `AGENTS.md`, existing components and accepted design decisions. For a new web application, prefer Next.js App Router, TypeScript, Tailwind v4 and shadcn/ui. For desktop or iOS/Android also use [native-client-development](../native-client-development/SKILL.md). A Tauri React/Vite DOM interface still follows this visual/interaction process and the compatible Tailwind/shadcn conventions; only web SSR defaults are inapplicable. React Native uses native components, not DOM primitives. Preserve an established React/Vite or other frontend unless a migration is requested. Use the project's package manager, locked versions and component primitives; do not mix Tailwind v3/v4 or Radix/Base UI APIs casually. For new Next.js projects, use `@tailwindcss/postcss`, `@import "tailwindcss"` and CSS-first semantic tokens via `@theme`/`@theme inline`; follow the selected shadcn preset rather than creating a competing token system.

Use [visual design](../visual-design/SKILL.md) for product-derived direction, accepted references and semantic token intent, and [interaction design](../interaction-design/SKILL.md) for behavior. These generic methods apply beyond React; this skill owns the compatible React/Next.js implementation. Record meaningful stack deviations in the existing project note.

## Design behavior and account for every affected surface

Use [interaction-design](../interaction-design/SKILL.md) before meaningful new or changed UX. Define goals, flows, information/actions and state transitions in concise text; add wireframes/mockups only where they settle spatial/visual uncertainty. Resolve consequential choices and state reversible assumptions before coding; reuse agreed direction without another approval ceremony. Do not invent UX independently as each page is implemented.

For cross-cutting work, interaction-design owns the affected-surface inventory, representative pattern and final reconciliation. Propagate shared implementations and verify actual callers/variants; preserve intentional differences and report incomplete coverage.

## Implement the accepted visual system

Map the accepted visual direction to semantic CSS variables and compatible Tailwind theme pairs. Reuse reviewed shadcn primitives/blocks, shared variants and the project's class-merging convention. Preserve the selected preset rather than layering a competing token system over it. Use consistent component semantics for surfaces, text, emphasis and status; preserve deliberate density and platform variants.

Compose the product's layouts from those primitives. Add dark mode when required by the product or established system. Use upstream shadcn/Tailwind guidance for unfamiliar compatible APIs; visual-design owns typography, composition and product character. A component library supplies implementation primitives, not the product direction.

## Make interactions dependable

Use semantic controls, visible labels, keyboard access and clear focus. Use actual compatible shadcn/Radix/Base UI primitives for menus/dialogs, not handwritten visual lookalikes lacking semantics or focus behavior. Verify focus containment, dialog roles/labels and restoration to the invoking control after closing, and never substitute tooltips or placeholders for labels. Include loading, empty, error, validation and permission states. Preserve input on recoverable failures, prevent duplicate submission and provide actionable errors. Destructive actions follow the existing confirmation or recovery convention.

Use pages for substantial editing, panels for quick inspection and dialogs for short decisions. For growing datasets, use bounded server pagination/filtering, consistent row actions and bulk actions with explicit selection scope. Put non-sensitive shareable view state in the URL. Localize dates, time zones, numbers and units deliberately.

Prefer React Hook Form with Zod for complex forms, TanStack Table for complex tables and a chart library such as Recharts when charts serve the task. Do not add these dependencies for a simple field or static list. Client validation helps users; the backend validates and enforces all business rules.

## Keep React and API boundaries clear

Organize by feature with shared primitives; avoid a bespoke application framework. In Next.js, default to Server Components for server data and small Client Components for interaction. Keep secrets on the server and authorize every server action/endpoint. Call hooks consistently, keep state close to its owner and avoid effects that merely derive state.

Use typed backend contracts, preferably generated from FastAPI OpenAPI where applicable. Choose a coherent fetching/cache strategy: use TanStack Query when interactive remote state warrants it, rather than duplicating Server Component requests. Scope private caches by identity/tenant, invalidate affected data after mutations and handle optimistic-update failures.

Avoid request waterfalls, oversized client bundles and avoidable layout shifts. Use appropriate image sizing, defer secondary work and measure actual problems before adding optimization complexity.

## Deploy the frontend as an application

Test the production build/start path, configuration and representative authenticated journey; development-server success is narrower evidence. Identify build-time and runtime settings. `NEXT_PUBLIC_*` values are public and compiled into the client build; changing deployment environment variables does not rewrite that bundle. Prefer an explicit runtime configuration boundary when one artifact must serve different environments, exposing only safe values. If a build must differ, give it a new identity and validate it.

When deploying multiple instances or changing hosting, read [production hosting and configuration](references/sources-and-exceptions.md#production-hosting-and-configuration) for cache scope/invalidation, identity isolation, version skew and proxy behavior. Verify the actual served path and affected outcome; local startup cannot establish fleet-wide behavior. Delivery-pipelines owns promotion and recovery mechanics.

## Verify and use specialist guidance proportionately

Run relevant types, lint and build checks. Evaluate rendered visual quality against the product-derived direction separately from functional, accessibility and journey checks. Inspect actual target layouts with realistic content, navigation, keyboard focus and failure states; repair visible discrepancies and recheck before completion. A screenshot baseline cannot establish taste, and an automated accessibility check cannot establish usability. Test the critical journey against real persistence using the project's E2E workflow; a screenshot alone is insufficient. Keep changed contracts and accepted design decisions synchronized, and report checks actually performed.

These defaults cover routine work without reference browsing. Use bundled shadcn, Vercel React/composition and Tailwind design-system skills for unfamiliar components or deeper implementation questions. My default and the Tailwind upstream guide both target **v4**. Apply a requested v3-to-v4 upgrade as a focused migration: check browser compatibility, dependencies, configuration and rendered behavior; do not migrate an unrelated existing application silently. Consult [sources and exceptions](references/sources-and-exceptions.md) for version migrations or decisions these defaults do not resolve.

For API changes, verify actual client behavior against supported provider contracts, including errors, optional fields and pagination. Generated types do not prove semantic compatibility. Keep old open browser sessions in the supported-consumer set during rollout and route planned breaks through backend/delivery guidance.

For meaningful visual critique or refinement, use [interface quality](../interface-quality/SKILL.md); it owns critique evidence and prioritization; visual-design owns product-derived direction and these conventions implement it in the selected stack. Use [UX writing](../ux-writing/SKILL.md) for material task language. Use [usability research](../usability-research/SKILL.md) for a requested study or real unresolved user question, rather than requiring research for routine frontend work.
