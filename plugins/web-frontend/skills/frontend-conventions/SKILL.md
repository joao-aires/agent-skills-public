---
name: frontend-conventions
description: Build, extend or review React/Next.js interfaces using opinionated shadcn/Tailwind conventions and supplied visual references. Use for dashboards, customer applications, storefronts, content sites, navigation, styling, forms and frontend architecture; preserve accepted project choices during ordinary feature work.
---

# Frontend conventions

## Establish the direction

Read the request, `AGENTS.md`, existing components and accepted design decisions. For a new application, prefer Next.js App Router, TypeScript, Tailwind v4 and shadcn/ui. Preserve an established React/Vite or other frontend unless a migration is requested. Use the project's package manager, locked versions and component primitives; do not mix Tailwind v3/v4 or Radix/Base UI APIs casually. For new Next.js projects, use `@tailwindcss/postcss`, `@import "tailwindcss"` and CSS-first semantic tokens via `@theme`/`@theme inline`; follow the selected shadcn preset rather than creating a competing token system.

Accept screenshots, URLs, design files, an existing application, tokens or a short brief. Extract the intended audience, page types, navigation, density, typography, colors and interaction patterns. Separate authoritative requirements from inspiration; do not copy a reference product's assets, backend scale or dependency list. Describe inaccessible references as gaps rather than claiming to have inspected them. Resolve consequential conflicts once; make reasonable reversible choices for minor details.

Keep the accepted conventions and meaningful deviations in the existing design note or `AGENTS.md` link. No mandatory profile format or document per change. Different frontend types can have different profiles while sharing tokens and primitives. Establish a representative screen for a new visual direction, then reuse it. Ordinary feature work follows the accepted design without reopening the whole aesthetic.

## Choose the shell for the product

| Interface | Default structure |
| --- | --- |
| Operational dashboard | Persistent left sidebar: workspace/product identity at the top, labeled navigation groups, account/help near the bottom. Use page tabs for secondary destinations and at most one nested menu level; mobile navigation becomes a drawer. |
| Customer task application | Simple top navigation or a compact sidebar according to destination count. Prioritize the user's next action; use progressive disclosure and multi-step flows only when they reduce complexity. |
| Storefront or content site | Public header, relevant search/categories, readable product or reading layouts, and a useful footer. Optimize mobile browsing and checkout where applicable rather than inheriting an admin shell. |

Across types, place the page title and useful context on the left, its main action on the right, and filters above the content. Breadcrumbs express meaningful ancestry; tabs switch sibling views. Navigable destinations have URLs and working back/deep-link behavior. Public pages need meaningful titles/metadata and indexing appropriate to the product; private application data must not become indexable or leak into public metadata. Hide unavailable destinations only for usability; authorization remains a server responsibility.

## Make a coherent visual system

Absent branding or references, use a light neutral surface, dark readable text, subtle borders, modest shadows and one accessible blue accent. Start with the existing font or a system sans, consistent Lucide-compatible icons, a 4px spacing scale, roughly 24px desktop page padding, a 256px dashboard sidebar and 8px corners. These are starting values, not immutable geometry: adapt density, mobile spacing and content width to the task. Favor readable 14–16px text, at least 16px mobile form inputs, and restrained 150–200ms transitions.

Express choices as semantic tokens for surfaces, text, borders, emphasis and status; avoid scattered literal colors and magic sizes. Supply dark mode when required by the product or established system. Check contrast and respect reduced motion. Apply upstream component rules only to compatible installed APIs; do not introduce newer form primitives or refactor accepted patterns merely to satisfy an upstream example. Use reviewed shadcn components/blocks, shared variants and the project's class-merging convention. Keep one vocabulary for buttons, fields, headers and empty states. Avoid decorative gradients, gratuitous cards and different styling for each page.

Use tables for operational comparison and cards for distinct items. Metrics need a real decision, units and a time window; never invent data to make a dashboard look populated. Missing data is an explicit state. Preserve the selected design profile when choosing between equally valid layouts.

## Make interactions dependable

Use semantic controls, visible labels, keyboard access and clear focus. Use accessible primitives for menus/dialogs, return focus after closing, and never substitute tooltips or placeholders for labels. Include loading, empty, error, validation and permission states. Preserve input on recoverable failures, prevent duplicate submission and provide actionable errors. Destructive actions follow the existing confirmation or recovery convention.

Use pages for substantial editing, panels for quick inspection and dialogs for short decisions. For growing datasets, use bounded server pagination/filtering, consistent row actions and bulk actions with explicit selection scope. Put non-sensitive shareable view state in the URL. Localize dates, time zones, numbers and units deliberately.

Prefer React Hook Form with Zod for complex forms, TanStack Table for complex tables and a chart library such as Recharts when charts serve the task. Do not add these dependencies for a simple field or static list. Client validation helps users; the backend validates and enforces all business rules.

## Keep React and API boundaries clear

Organize by feature with shared primitives; avoid a bespoke application framework. In Next.js, default to Server Components for server data and small Client Components for interaction. Keep secrets on the server and authorize every server action/endpoint. Call hooks consistently, keep state close to its owner and avoid effects that merely derive state.

Use typed backend contracts, preferably generated from FastAPI OpenAPI where applicable. Choose a coherent fetching/cache strategy: use TanStack Query when interactive remote state warrants it, rather than duplicating Server Component requests. Scope private caches by identity/tenant, invalidate affected data after mutations and handle optimistic-update failures.

Avoid request waterfalls, oversized client bundles and avoidable layout shifts. Use appropriate image sizing, defer secondary work and measure actual problems before adding optimization complexity.

## Verify and use specialist guidance proportionately

Run relevant types, lint and build checks. Inspect rendered desktop/mobile layouts, navigation, keyboard focus and failure states. Test the critical journey against real persistence using the project's E2E workflow; a screenshot alone is insufficient. Keep changed contracts and accepted design decisions synchronized, and report checks actually performed.

These defaults cover routine work without reference browsing. Use bundled shadcn, Vercel React/composition and Tailwind design-system skills for unfamiliar components or deeper implementation questions. My default and the Tailwind upstream guide both target **v4**. Apply a requested v3-to-v4 upgrade as a focused migration: check browser compatibility, dependencies, configuration and rendered behavior; do not migrate an unrelated existing application silently. Consult [sources and exceptions](references/sources-and-exceptions.md) for version migrations or decisions these defaults do not resolve.
