# Frontend and backend convention sources

Reviewed on 2026-10-11. Repository stars and skills.sh installs indicate adoption. I also consider official maintenance, production patterns, source availability and licenses; popularity alone cannot establish correctness. The guides cover everyday decisions inline and link to details for exceptions. I aim to avoid reference lookup in 90 to 95% of routine uses. That rate has not been measured.

## Included expertise

| Skill | Why included | Acquisition |
| --- | --- | --- |
| Official `shadcn` | First-party component, registry and project guidance; about 100.7k skills.sh installs | Existing MIT pin retained in `upstream.lock.json`; full resources/license packaged. |
| Wshobson `tailwind-design-system` | Semantic tokens, reusable components and responsive/accessibility patterns; about 68k skills.sh installs, repository about 40.4k stars | MIT; pinned to `46891e7e60da0e52baf1050b7b6391b64e84c6d9`; Tailwind v4 specialization. |
| Vercel React/composition | First-party React performance and composition expertise | Existing per-skill MIT pins retained. |
| Trail of Bits modern-python; Anthropic MCP builder | Python tooling and optional MCP implementation | Python tooling stays in python-backend; MCP builder is in ai-development. |
| Google ADK; LangChain/LangGraph | First-party AI framework guidance when AI is required | Existing `ai-development` bundle; install alongside backend only when applicable. |

All acquired frontend skills receive a recorded pointer to `frontend-conventions`. Accepted design, framework and Tailwind versions take precedence; specialist guidance does not authorize redesign/migration. Packaging does not execute upstream scripts. No new MCP servers, hooks or application templates are introduced.

## Open-source application references

The review covered dependency manifests, official template code and published guidance. It did not audit whole architectures or copy application code, assets or unlicensed skill content.

| Source | Reviewed revision | Evidence and limits |
| --- | --- | --- |
| [Dub](https://github.com/dubinc/dub) (~24.9k stars) | `bc7eeb882ead4652ed375545db81bb79b72137e8` | Next.js/React, Tailwind v3, Radix, table/form primitives. Evidence that mature applications need not migrate to v4 to follow coherent conventions. |
| [Cal.diy](https://github.com/calcom/cal.diy) (~48.9k stars; redirect from cal.com) | `54343aa685ae8f33159d2f485ec4a57bad5c574a` | Next.js, Tailwind v4 and reusable UI packages. Reference only; do not transplant scheduling-specific architecture. |
| [Supabase Studio](https://github.com/supabase/supabase/tree/master/apps/studio) (~111.4k repository stars) | `8617532ae1a41571d5d557cd24c6f5f2565d9230` | Tailwind/Radix, tables/forms and multiple framework paths. Repository adoption does not measure Studio usage; not a prescription for its backend scale. |
| [FastAPI full-stack template](https://github.com/fastapi/full-stack-fastapi-template) (~45.9k stars) | `7257e606cb94eada1dca40173e2b7f99dd549bc6` | First-party auth, sessions and full-stack integration. Uses SQLModel and Vite; my SQLAlchemy/Next.js defaults remain explicit. |
| [FastAPI best practices](https://github.com/zhanymkanov/fastapi-best-practices) (~18.2k stars) | `5e00aa6095521f0d00e4eec2ef0afa44cd566af4` | Domain organization, blocking/async distinctions and production cautions. Community reference, not a package; no redistribution license assumed. |

Authoritative details are linked within each skill's `references/sources-and-exceptions.md`: Next.js, Tailwind, shadcn, SQLAlchemy, Alembic, PostgreSQL, FastAPI, OWASP, AI providers and FastMCP. Generic guidance remains local so agents do not need to reconstruct the conventions from these sites.

## Excluded or retained as references

- Jezweb's `tailwind-v4-shadcn` listing exists on skills.sh, but the directory is absent at the reviewed repository HEAD (`1260fa7439b36b18dbf16648ccc7fb44783f6c23`) and its published setup is Vite-specific. It was not acquired or used as a Next.js setup recipe.
- Vercel `web-design-guidelines` fetches a floating external guideline and has no declared skill redistribution license at the reviewed revision. Keep the public guidelines as a reference instead of silently vendoring it.
- Backend conventions, official docs and the existing specialist bundles cover FastAPI and auth. I have not added an unverified third-party omnibus skill.

## Resolved upstream tensions

Tailwind v4 is the new-project default, matching the acquired Tailwind skill. Handle existing-project upgrades as focused migrations; loading a skill does not request an upgrade. shadcn rules apply to compatible installed primitives. Python tooling and MCP acquisition add conventions pointers without altering SDK examples: modern-python preserves accepted tooling, and the AI plugin's MCP builder follows the standalone Python FastMCP preference. Standalone package/import and installation/migration guidance were checked against [official FastMCP docs](https://gofastmcp.com/getting-started/installation); the Next.js v4 setup follows [official Tailwind docs](https://tailwindcss.com/docs/installation/framework-guides/nextjs).
