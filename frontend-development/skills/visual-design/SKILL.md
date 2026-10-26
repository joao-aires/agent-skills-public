---
name: visual-design
description: Derive an interface's visual direction from its users, tasks, content and environment. Use for a new product, substantial redesign, semantic tokens or a design-to-implementation handoff across web, desktop and mobile; preserve accepted identity during ordinary changes.
user-invocable: true
metadata:
  scope: generic
  invocation: both
  role: support
---

# Give the interface a product-specific visual direction

Define how the product's purpose becomes hierarchy, composition, typography, color, density and motion. Use the accepted product outcome and [interaction design](../interaction-design/SKILL.md) for behavior and affected surfaces. Preserve an established identity unless changing it is the objective. Routine copy or minor token changes need proportionate checks.

## Establish the UI foundations first

Before wireframing or choosing components for a new interface or substantial redesign, establish the implementation and appearance decisions that the design must support. Read the existing application and accepted choices first; a small improvement should reuse them. Preserve the user's framework or component-system preference, and make an explicit recommendation with the relevant tradeoffs when the choice is open. Ask when a consequential choice remains unresolved; do not require the user to reapprove an established system for each screen.

| Foundation | Decision and consequence |
| --- | --- |
| Platform and component system | Identify web, extension, desktop DOM or native UI, the accepted runtime, and who owns component behavior and styling. For compatible web/DOM work, consider plain Tailwind, Tailwind with shadcn/ui, HeroUI, or a system specified by the user. Native applications need platform-appropriate components. |
| Appearance | Establish light, dark or both, system-following behavior and any manual override. For a new interactive application, recommend system appearance with light/dark overrides unless the brief calls for a different policy. Preserve an existing policy unless changing it is in scope. |
| Design-system ownership | Reuse an established system; otherwise define semantic roles and shared primitives. Identify how library defaults will be adapted to the product without competing token systems or divergent copies of the same control. |

Choose the component system for its fit to the product and platform:

- **Plain Tailwind** offers styling control but does not supply accessible behavior for complex widgets.
- **Tailwind with shadcn/ui** offers editable components and places their maintenance with the project.
- **HeroUI** is a component-library option for a compatible React application. Check the selected version's runtime, styling and interaction contracts.

Another requested library or an established CSS system remains a valid choice. Seek matching implementation expertise when available, or use the selected system's primary documentation; the design method does not depend on installing a technical plugin.

Record these decisions in the existing design note or handoff before deriving tokens and mockups. Carry the selected component anatomy, density, keyboard behavior and theme roles through the representative design and implementation. A library supplies primitives, not the product's visual identity. Read [foundation sources](references/ui-foundations.md) when comparing an unfamiliar library or resolving its theme behavior.

## Resolve the visual decision

Read the brief and work with the content the interface must actually carry. Identify what users need to notice first, how long they will spend reading or working, how much information they compare at once, and the environment in which they use the product. These questions give typography, density and composition a reason to take a particular form.

When direction is open, compare coherent alternatives that change the experience, rather than variations of the same starter. Explain how each handles the task and where it places attention. Choose a direction whose visual decisions can be traced to the brief: type should support the reading task, spacing should express relationships, color should establish roles, and motion should help explain change.

Distinguish requirements from inspiration and proposed choices. Use references for particular qualities you can name and adapt, not as whole layouts to imitate. Missing brand assets permit a reversible proposal that can be shown and critiqued; they do not require invented research or a blocked engagement.

Translate the direction into reusable roles. Give colors, type sizes, spacing and surfaces names that describe their use, then apply those roles consistently to shared components. These semantic tokens let the implementation preserve the design when a palette or component changes.

Map the roles across every supported appearance mode, including content, controls, status, focus and overlays. Dark mode needs an intentional palette rather than a background inversion. Keep deliberate differences where the task needs them.

Use available visual-execution craft for composition, typography and critique when choices are open; the accepted identity and actual brief remain authoritative. Derive character from the content and the way people work with it. A decorative domain motif or recolored starter does not explain why the design suits the product. Read [visual direction and review](references/visual-direction.md) for substantial new work, redesign or handoff, including how to connect the design to components and inspect the implemented result.

## Establish the shared page composition

Define how related views belong to the same application before composing them independently. Reusing buttons and tokens still leaves decisions about the surrounding layout: where identity and navigation live, how a page announces its purpose, and how its content aligns with neighboring views. Carry an adequate existing composition forward during ordinary changes.

| Shared concern | Establish across related views |
| --- | --- |
| Identity and navigation | Stable placement and hierarchy for product identity, global navigation and recurring actions. |
| Page hierarchy | Recognizable title, context and local-action regions, with consistent type roles and spacing. |
| Content frame | Related width, alignment, gutters, section rhythm and separator roles; allow a narrower reading measure within the frame where the content needs it. |
| Layout variants | Explain departures through task, platform or space constraints, and preserve recognizable roles when the arrangement changes. |

Map these choices to shared layout components or equivalent platform patterns as well as tokens. A focused editor, a dense collection and a settings form can need different content arrangements while keeping predictable orientation. Record consequential variants with the accepted design; a new route alone does not justify a new composition.

## Build and inspect the design

Reuse accepted designs and choose an artifact that can answer the remaining question. Figma can support shared design work when available and authorized; local HTML/CSS can reveal responsive or interactive behavior; SVG can explain a static layout or flow. An explicitly required format remains part of the deliverable.

1. Build a representative part of the experience using realistic content. Include a difficult state, content growth, supported appearance modes and the layouts the task needs, so the design is judged beyond its most flattering empty screen.
2. Inspect where attention goes, whether content remains readable and how the composition handles those conditions. Repair mismatches with the intended direction before applying the pattern elsewhere.
3. For work spanning views, compare representative related views together and move between them. Check the shared composition at supported widths and appearance modes, including short and long content. Resolve unexplained shifts or record a justified variant before calling the shared design complete. Without rendered access, return the comparison plan and identify the evidence still missing.

Keep the reason for the choices, proposed versus accepted status, important states and reusable component/token roles in the existing design record. Technical guidance maps them to the accepted platform and component system; a design recommendation does not authorize a framework migration or make a technical package mandatory.

Use [interface quality](../interface-quality/SKILL.md) for evidence-based critique and [UX writing](../ux-writing/SKILL.md) for task language. Reconcile the rendered implementation with the direction and report intentional deviations or unverified surfaces. A screenshot supports visual assessment; interaction, accessibility and persisted outcomes require their own evidence through the verification loop.

Return the direction, representative artifact, implementation mapping and actual review evidence within scope. Keep agent aesthetic assessment distinct from user acceptance and participant findings. A design-only request does not authorize implementation.
