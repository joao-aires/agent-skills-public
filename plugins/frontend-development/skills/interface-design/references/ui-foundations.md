# Choosing UI foundations

Use this reference when the component system is unresolved or the selected library's theme behavior is unfamiliar. The decision belongs before dependent component specifications and mockups; it does not reopen an accepted stack during a small change.

## Compare ownership and fit

| Choice for compatible DOM applications | What the project takes responsibility for | Useful primary reference |
| --- | --- | --- |
| Plain Tailwind | Styling and product-specific composition; use native controls or proven accessible behavior primitives for complex interactions. Utility classes alone do not establish dialog focus or keyboard semantics. | [Tailwind documentation](https://tailwindcss.com/docs) |
| Tailwind with shadcn/ui | Editable component source, a coherent primitive/preset choice, semantic tokens and keeping local changes compatible with updates. | [shadcn introduction](https://ui.shadcn.com/docs), [theming](https://ui.shadcn.com/docs/theming) |
| HeroUI | A compatible React component library, its supported anatomy/interaction contracts and theme integration. Check the selected major: a migration guide is not permission to upgrade an existing application. | [HeroUI version/migration contracts](https://heroui.com/en/docs/react/migration) |
| Another requested or established system | Its supported platform, component behavior, theming and update responsibilities. Preserve the user's choice and the application's existing design-system investment. | The selected system's official documentation and actual installed version |

The choice should account for runtime/platform compatibility, the required interactions, customization needs, accessibility behavior, bundle/CSP constraints and the team's maintenance ownership. Do not combine component libraries merely to reproduce a screenshot; mixing them needs a concrete benefit and a plan for tokens, focus, overlays and dependencies.

## Design appearance as behavior

Decide supported modes, default selection, system following and the meaning of a manual override. Recommend light/dark/system for a new interactive application unless context warrants a narrower policy; static artifacts or accepted single-mode systems need not acquire a theme switch.

Define semantic roles for backgrounds, content, controls, focus, status and overlays in each supported mode. Keep the product's hierarchy and identity while choosing readable mode-specific values. A component preset provides implementation defaults; it does not settle the product's density, typography or composition.

Verify the first frame as well as the settled screen. A saved preference, delayed hydration, system change or newly opened secondary surface can reveal inconsistent appearance that a static screenshot misses. Check native controls, placeholders, disabled states, overlays and transitions with representative content and keyboard focus. [Tailwind's dark-mode guide](https://tailwindcss.com/docs/dark-mode) explains system and selector-driven mechanisms for that stack; other systems should use their own supported mechanism.

Carry the accepted decisions into the design record and technical implementation. These sources establish component and styling contracts, not evidence that a particular application's accessibility or usability has been verified.
