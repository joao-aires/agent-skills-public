# Visual principles for product-specific interfaces

Use during initial visual direction, redesign, or targeted polish. These original, contextual heuristics are informed by the subjects of [Refactoring UI](https://refactoringui.com/) (Adam Wathan and Steve Schoger). Adapt them to real tasks, accessibility and existing design systems; do not treat a book's illustrative choice as a required palette, layout or color model.

## Begin with the feature and real content

Start with the user task and the information it needs, not a generic page chrome. Sketch enough structure to reveal the main flow; refine details incrementally. Low-fidelity or grayscale exploration can expose problems with hierarchy and grouping before visual decoration. Choose a coherent personality grounded in domain, audience and frequency of use. Constrain the number of arbitrary visual choices through reusable roles and scales, without turning the result into a copy of a familiar starter.

## Give attention an intentional hierarchy

- Identify the primary action, critical content, secondary context and optional metadata for each state. Support a clear first-glance reading order.
- Use size, weight, contrast, position and grouping in combination; do not merely make every heading larger.
- Reduce emphasis on secondary content without sacrificing legibility. Preserve actual heading semantics, essential field labels, accessible names and consequential units even when visible chrome is minimal.
- Distinguish important actions from dangerous or merely frequent actions. Do not make every button primary.
- Review intentional density separately from weak hierarchy: a useful operations table can be compact and still scannable.

**Check:** Can a new user identify the important information, scope and next action? Does that remain true with real data and role-specific states?

## Let spacing explain relationships

- Put related information closer together than unrelated sections; investigate gaps that imply ambiguous grouping.
- Establish a limited spacing/size vocabulary expressed through existing semantic tokens. Optical offsets are allowed when justified; avoid arbitrary one-off increments.
- Choose widths to suit the task. Long-form reading benefits from a bounded measure, while tables and canvases may need width. Avoid filling empty viewport area without purpose.
- Use grids only when they clarify meaningful relationships; choose fixed/fluid sizing from content growth and device needs rather than a single proportional formula.

**Check:** Compare normal and long content, zoom, localization and narrow widths. Can users still see what belongs together?

## Make type work for both reading and scanning

- Define readable type roles, weights, line lengths, line heights and alignment. A headline, annotation, row label and paragraph have different scanning needs.
- Favor correct baselines and optical alignment for text/icon combinations. Use tracking deliberately rather than on every micro-label.
- Distinguish links and controls by affordance and context, not color alone; preserve keyboard/focus visibility.
- Do not hide important labels merely because an unlabeled screenshot appears cleaner.

**Check:** Inspect real long labels, numerical values, locales, wrapping and the supported zoom range.

## Use color and depth to communicate roles

- Use semantic tokens for surface, foreground, muted content, interaction, status and focus, mapped intentionally into supported appearance modes.
- Construct sufficient shades for each role with the project's color system. HSL may help explain color relationships; it is not compulsory, and existing OKLCH/token systems remain valid.
- Foreground text on colored surfaces needs actual readable contrast. Status must not rely on hue alone. Measure applicable contrast rather than asserting it by eye.
- Use background shifts, elevation, borders and whitespace according to relationships. Consistent shadow direction can help perceived layers; too many borders or shadows often hide grouping rather than clarify it.
- Keep meaningful boundaries (selection, input, focus, alert) instead of applying a blanket no-border rule.

**Check:** Verify both supported themes, interactive states and meaningful accessibility requirements with actual rendered values.

## Images and finishing details

- Select imagery for meaningful content and composition, not because a hero is expected. Specify intended aspect ratio, crop, focal area, responsive resolution and fallbacks.
- Overlaid text must remain legible across unpredictable photos, including user uploads; scrims or separate text surfaces are sometimes safer than direct overlays.
- Treat empty and error states as opportunities to explain what happened and offer a real next action, not as occasions for generic illustration.
- Spend visual novelty where it serves the brief; remove ornamental cards, labels, dividers, gradients or animation that distract from work.

**Check:** Compare empty, loading, error, populated and unusually long/image-heavy states. Avoid a decorative solution that degrades usability.

## Resolve conflicting heuristics through the task

Spacious marketing pages and dense operator dashboards have different optimal density. Essential form labels and accessible names survive minimalism. Platform conventions, localization, user choices and accepted product character override stylistic recipes. Explain consequential exceptions; do not force universal aesthetics onto every interface.
