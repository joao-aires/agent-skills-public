# Option review: make the direction choice visible

Read when a consequential interface choice is open and the user must judge directions before implementation. This reference covers construction, presentation and decision capture; [research methods](research-methods.md) covers the evidence behind them.

## When an option set is required

Use at least three directions when the choice affects structure, navigation, core interaction, visual identity, trust or accessibility, or is expensive to reverse. Typical triggers:

- a new product, substantial redesign or greenfield surface;
- information architecture, navigation or a core flow;
- onboarding, checkout, pricing, permissions, identity or destructive actions;
- a brand or visual direction that will propagate across surfaces;
- a change that spans several screens, roles or platforms;
- the user is explicitly comparing directions.

A routine local change is exempt. See [the routine exception](#routine-change).

## Construct materially different directions

Choose two or three lenses that genuinely separate the options. A direction is a coherent stance, not a color swap.

| Lens | Optimizes | Typical sacrifice |
| --- | --- | --- |
| Task efficiency | Fewest steps, fast repeat use, keyboard fluency | Discoverability for new users; warmth |
| Trust and accessibility | Predictability, explicit state, low cognitive load | Density and expressive character |
| Expressive or brand-led | Distinct identity, memorability, emotional fit | Familiarity; implementation and performance cost |
| Data density | Comparison, scanning and expert throughput | Breathing room; first-run comprehension |
| Progressive disclosure | Calm first view, staged complexity | Extra step; hidden capability |
| Platform-idiomatic | Native expectations and system behavior | Cross-platform uniformity; brand differentiation |

For each direction, state:

- **Name and lens** — what stance it takes.
- **Structure and flow** — what the user sees first, the step order and the main action.
- **Optimizes** — which outcome or constraint it serves.
- **Sacrifices** — what it gives up or puts at risk.
- **States** — empty, loading, busy, error, denied, stale and recovery behavior.
- **Visual rules** — hierarchy, density, type, color, surfaces and motion intent.
- **Accessibility implications** — focus order, labels, targets, contrast and reduced motion.
- **Evidence** — which observed sources or project constraints support it.
- **Unknowns** — what still needs a prototype, test or decision.

Three cosmetic variants of one layout are not an option set. Neither are options that differ only in component library, spacing scale or illustration style. If all directions share the same flow and hierarchy, the choice is not yet consequential enough to present that way.

## Match fidelity

Compare like with like:

- Use the same representative task, realistic content, viewport and state coverage for every direction.
- Use wireframes or wireflows for structure; rendered mockups or a runnable slice for appearance and behavior.
- Give every direction a linked artifact. Do not compare one polished mockup against a paragraph.
- Label the fidelity and what it does not show. A static mockup does not demonstrate keyboard behavior or loading latency.
- Keep the evidence visible: a direction derived from a reference should say which observation it adapts.

If one direction cannot be built at comparable fidelity within the time available, say so and limit the recommendation rather than inflating a sketch into a decision.

## Present and collect feedback

Show the directions together, in one view or a short sequence, using identical content. State the recommendation and the reasoning before asking for a decision. Ask a decision-shaped question:

- "Which direction should carry the first implementation slice?"
- "Is the density right for daily expert use, or should we favor the calmer first-run view?"
- "Does the expressive direction fit the brand, or should we stay closer to the incumbent system?"

Do not ask users to choose hex values, spacing tokens or component names. Translate vague feedback ("more modern") into a visible change and show it. When work is unattended or the user delegates, choose the reversible direction, record the assumption and proceed; do not wait indefinitely.

Capture:

- which directions were shown and at what fidelity;
- the feedback in the user's terms;
- what changed in response and what did not;
- the chosen direction, owner and status;
- unresolved objections and the condition that would reopen the choice.

No response is not approval. If the user did not answer, report the implemented assumption and its evidence rather than describing the direction as accepted.

## Record the decision

Keep one record beside the existing brief, design proposal or task:

```markdown
Decision:
Question and scope:
Directions shown (fidelity, artifact):
Optimizes / sacrifices:
Feedback and what changed:
Chosen direction:
Chosen because:
Rejected because:
Accepted/delegated by:
Status: proposed | accepted | rejected | superseded
Revisit if:
Evidence still missing:
```

Link the artifacts a reviewer needs. Do not create a separate document per direction, and do not let the record replace the rendered evidence.

## Anti-patterns

- three cosmetic variants or three copies of one layout;
- the same lens applied to every direction;
- reference collages with no stance, tradeoff or recommendation;
- comparing a finished mockup with a rough description;
- directions that omit empty, error, denied and recovery states;
- hiding the recommendation to avoid influencing the user;
- treating a competitor's pattern as proof of quality;
- presenting a library result as the proposed design;
- implementing before feedback and the decision record exist;
- reopening a settled direction without new evidence or changed scope.

## Routine change

For a reversible, low-impact change, skip the option set:

- state the one recommended direction;
- give a short rationale tied to the task and existing system;
- name any alternative that was considered and why it was rejected;
- use the smallest check that would catch a wrong choice.

A token adjustment, copy correction, obvious defect repair or established component reuse does not need three directions or a feedback round.
