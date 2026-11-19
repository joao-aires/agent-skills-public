# UI probe: compare rendered directions

A UI probe puts **several structurally different directions** on one real surface and lets the owner switch between them. Use it when the question is what a page, flow or component should be, not how its underlying logic works.

Read the [prototype method](../SKILL.md) first; the throwaway rules and the boundary with design apply here.

## When this is the right shape

- "What should this page look like?"
- "Show me a few options for this dashboard before we commit."
- "Try a different structure for the settings screen."
- Any question the owner would otherwise settle by imagining three vague mockups.

If the question is about rules, state or data shape, use the [logic probe](logic-probe.md) instead.

## Compose with installed capability

Seek the installed **interface-design** capability by its description for hierarchy, navigation, interaction behavior, accessibility and rendered fit. Seek **ux-writing** for labels, empty states, validation, errors and confirmations. Follow the project's **frontend implementation conventions** for routing, components, styling, tokens and data access.

Use each capability's actual description before relying on it. If one is absent, apply the project's existing design system, patterns and primary platform guidance; do not lower the evidence standard or invent a parallel design system. Compose by capability, not by importing or linking another package's files.

## Pick the host surface

A UI probe is easier to judge when it sits against the rest of the application: real header, sidebar, data, density and states. An isolated route is a vacuum where every variant looks acceptable.

**Prefer adjusting an existing page.** The route already exists. Keep its data loading, params, auth and shell, and swap only the rendered subtree. Gate the variants with a `?variant=` search parameter. If the new thing would naturally live inside an existing page, mount it there; that is still this shape.

**Use a new throwaway route only when there is no sensible host.** Follow the project's routing convention, include "prototype" in the route or filename, and keep the same `?variant=` pattern. Before choosing this, check once more whether an existing page could host it; an empty route hides the problems a populated one exposes.

## Generate the variants

Default to **three** variants; cap at five. More stop being different and start being noise.

Write the plan in one line at the top of the probe, for example: "Three variants of the settings page, switchable via `?variant=`, on the existing `/settings` route." That line is how someone returning later knows what was built and why.

Hold every variant to the same purpose, content and data. Make them **structurally different**: different layout, information hierarchy, primary affordance or reading order. Different colors, copy or card spacing is a tweak, not a variant. If two drafts converge, redo one with an explicit constraint such as "no card grid."

Give each a clear component name and keep them independent enough to disagree. A shared header or data hook is fine; a shared layout defeats the comparison. Cover the states the page actually has: empty, loading, error, denied, stale and a realistic dense case. Use realistic content, not lorem ipsum.

## Wire the switcher

Render the active variant from the URL search parameter, above the existing data fetch so only the subtree changes:

```tsx
// pseudo-code; adapt to the project's framework
const variant = searchParams.get('variant') ?? 'A';
return (
  <>
    {variant === 'A' && <VariantA {...data} />}
    {variant === 'B' && <VariantB {...data} />}
    {variant === 'C' && <VariantC {...data} />}
    <PrototypeSwitcher variants={['A', 'B', 'C']} current={variant} />
  </>
);
```

Put the switcher in one shared component where the project keeps shared UI. Give it:

- a previous and next control that wrap around;
- the current variant key and, when useful, its name;
- router-driven URL updates so the choice is shareable and survives reload;
- `←` and `→` keyboard support, except while an input, textarea or editable element has focus;
- a visual treatment distinct from the page, so it is clearly not part of the design under review;
- a development-only guard so a stray merge cannot ship it.

## Run and observe

Start it with one existing task-runner command. Send the owner the URL and the variant keys. The useful feedback is comparative: "the header from B with the sidebar from C," or "none of these; the primary action is in the wrong place." That is the design direction, not a request to polish one variant.

Record which variant won and why. If the owner mixes variants, record the combination and the reason, not just the winning label. If the answer is "none," record what the comparison ruled out.

## Capture and clean up

Fold the winning direction into the real code, rewritten to production standards. Remove the losing variants and the switcher from the main branch.

- **Existing page:** keep the accepted structure in the page; drop the prototype switcher and unused variants.
- **New route:** promote the winning direction to a real route and delete the throwaway route and switcher.

Record the answer in the design record or ECR validation section. If the full variant set is worth retaining as evidence, put it on the project's throwaway branch and link it; do not leave it in the main line to rot.

## Anti-patterns

- **Cosmetic variants.** Color, copy or spacing changes do not test a design direction.
- **A shared layout.** If every variant inherits the same structure, the probe cannot compare structures.
- **An empty route.** Prototyping outside the real shell hides density, navigation and data problems.
- **Production mutations.** Point writes at a stub; the question is what the surface should be, not whether the backend works.
- **Promoting prototype code directly.** Variant code has no tests, minimal error handling and a switcher attached. Rewrite it when folding it in.
- **Leaving the switcher or losing variants in main.** They confuse the next reader and can ship to users.
- **A rendered result with no recorded answer.** The screenshots are not the decision.
