# Project Notes PRD

Purpose: prove a repeatable private browser/API/database journey, not a production SaaS.

Acceptance: a new user can register and create a note; it survives reload and logout/login; another account sees no notes and cannot retrieve the owner's note by ID. Anonymous access fails. Blank titles fail. Unsafe requests from another origin fail. UI reuses official shadcn components with mobile-safe layout and accessible labels.

Out of scope: email verification/recovery, rate-limited public signup, multi-tenant organizations, payment, deployment, AI product features. Optional AI/MCP tooling is separately selected.
