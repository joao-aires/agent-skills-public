---
name: build-consistent-frontend
description: "Build or review Next.js and shadcn/ui applications with TypeScript, existing design tokens, Vercel performance practices, accessibility, responsive behavior, and stable UI/UX conventions."
---

# Consistent frontend

Read `references/frontend-contract.md`, local AGENTS.md, `components.json`, the design-system document, existing components, and the package lock before coding.

Use Next.js App Router, TypeScript, shadcn/ui, and the configured Tailwind/base/icon libraries. Prefer server components; make client components only where interaction or browser state requires them. Keep provider secrets on the server. Use the FastAPI backend for business logic; Next.js routes may handle frontend session/BFF concerns without duplicating the domain layer.

Load the official shadcn skill for composition and registry operations; use its MCP server when available and correctly scoped to the application's components.json. Load version-matched Next.js agent documentation and relevant Vercel React/composition guidance. Consult upstream sources listed in this plugin's references; do not claim a reference is installed.

If Vercel web-design-guidelines is explicitly available, apply it for UX review; otherwise use the local UX contract and version-matched first-party documentation. The public builder does not acquire that unlicensed source. If UI/UX Pro Max is installed, constrain it to the existing tokens, components, and approved visual direction. Verify availability rather than assuming installation. Treat Anthropic frontend-design as an explicit exploration option, not the default during consistency cleanup. Preserve user-installed design guidance that is compatible with project decisions.

Reuse existing components and semantic tokens. Do not introduce new fonts, palettes, spacing scales, navigation patterns, animation styles, or UI kits without a documented reason. Establish one design-system contract for a new project before repeating screens.

Cover loading, empty, error, success, and permission states. Verify mobile and desktop layouts, keyboard navigation, focus, labels, contrast, reduced motion, and validation messages. Use accessible primitives rather than recreating controls.

Prevent waterfalls and unnecessary client JavaScript; use framework images/fonts and deliberate caching and invalidation. Measure relevant performance rather than claiming optimization from style changes.

Review rendered screens and affected user journeys. Update UX documentation and API client contracts when behavior changes.
