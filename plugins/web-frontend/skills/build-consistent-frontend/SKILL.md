---
name: build-consistent-frontend
description: Build or review Next.js and shadcn interfaces with consistent UI/UX, accessible interactions and sensible performance defaults.
---

# Build a consistent frontend

- Prefer Next.js App Router, TypeScript, shadcn/ui and the project's configured styling libraries for new applications. Use official shadcn and Vercel skills for implementation details when available.
- Read the existing components, tokens and design direction first. Reuse them across screens; avoid new palettes, fonts, spacing scales or navigation patterns without a product reason.
- Apply compatible UI/UX skills already installed in the working client. Keep private guidance local. Use design exploration deliberately rather than redesigning established screens while fixing them.
- Establish a coherent visual direction early in a new project. Favor clear hierarchy, familiar interactions and a small reusable component vocabulary.
- Handle loading, empty, error, success and permission states. Consider mobile/desktop layouts, labels, keyboard access, focus, contrast and validation feedback.
- Prefer server rendering where appropriate; use client components for interaction. Keep secrets server-side, avoid request waterfalls and excessive client JavaScript, and make caching decisions explicit.
- Inspect rendered screens and test important journeys. Measure performance when it matters instead of claiming improvement from code style alone.
- Use shadcn MCP optionally for registry/component work, configured against the actual application. Keep domain logic in the backend and keep UI/API contracts aligned.
