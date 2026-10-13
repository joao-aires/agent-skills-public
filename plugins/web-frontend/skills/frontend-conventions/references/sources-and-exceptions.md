# Sources and exceptions

The main skill supplies everyday decisions. Open these only for a specific unanswered question; examples are evidence for patterns, not templates to copy.

| Need | Primary source and limits |
| --- | --- |
| Components, sidebar and accessibility primitives | [Official shadcn documentation](https://ui.shadcn.com/docs), [sidebar](https://ui.shadcn.com/docs/components/sidebar) and the bundled `shadcn` skill. Verify the project's registry, primitive family and installed version. |
| Next.js server/client and auth boundaries | [Next.js authentication guide](https://nextjs.org/docs/app/guides/authentication); bundled Vercel React and composition skills. Never infer server authorization from client visibility. |
| Tailwind configuration | [Official Next.js integration](https://tailwindcss.com/docs/installation/framework-guides/nextjs) and bundled `tailwind-design-system`. My new-project default and upstream guidance are v4/CSS-first; existing v3 projects keep their configuration unless migration is requested. Next.js uses the relevant PostCSS setup, not a Vite plugin. |
| Interface review | [Vercel interface guidelines](https://vercel.com/design/guidelines) and [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/). These remain references; no undeclared upstream redistribution license is assumed. |
| Operational product examples | [Dub](https://github.com/dubinc/dub), [Supabase Studio](https://github.com/supabase/supabase/tree/master/apps/studio) and [Cal.diy](https://github.com/calcom/cal.diy). Observe navigation, reusable primitives and state handling; their routing, versions and business domains differ. |

A supplied reference can define another frontend profile: identify its audience, shell, navigation, density, tokens, component behavior and responsive/accessibility expectations, then record only the accepted decisions. Do not replace an existing profile without a request. A public marketing page does not establish a private dashboard's behavior.

## Production hosting and configuration

Use [Next.js self-hosting](https://nextjs.org/docs/app/guides/self-hosting) for version-matched cache coordination, rollout skew, Server Actions and proxy behavior; managed hosting may supply some of these mechanisms. Use [environment-variable guidance](https://nextjs.org/docs/app/guides/environment-variables) to distinguish values embedded during build from server runtime configuration. A build ID alone does not implement all deployment routing/cache requirements. Review private data and generated output at every caching boundary.
