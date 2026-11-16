# Research methods: choose, judge and synthesize

Read when selecting an approach, judging whether a source is strong enough, or continuing without Mobbin or Refero.

## Choose the method by question

| Question | Method | Evidence it produces | What it cannot show |
| --- | --- | --- | --- |
| Which conventions do users already expect for this task? | Competitive screen review of two to four products | Observed structures, labels, states and differences | That users prefer or understand them |
| What should a multi-step flow include? | Flow review, including failure and recovery | Step order, decisions, system response and friction points | Task success in your product |
| How do comparable products compose a page or section? | Section or page review | Content hierarchy, density and composition choices | Which composition converts better |
| Which visual direction fits the brand? | Style and visual reference review, then a local render | Traits, color roles, type and surface ideas | Fit with your content and audience until rendered |
| Is a pattern current or deprecated? | Live product, changelog or design-system documentation | Dated, primary evidence | Whether the pattern works for your users |
| Does our candidate work for users? | [Usability research](../../usability-research/SKILL.md) | Observed task performance and comprehension | Market convention |
| Is a visual treatment accessible? | Rendered inspection and measurement | Actual contrast, focus, target and reflow behavior | Participant experience |

Desk research is the right method for convention, precedent and composition questions. It is the wrong method for claims about your users' behavior. Do not borrow a competitor's result as if it were your evidence.

## Judge source quality

Use the strongest available source for the claim, not the most convenient one:

1. **Project evidence** — accepted design system, analytics, support themes, prior research. Highest authority for fit with this product, but still limited to what it measured.
2. **Live product and primary documentation** — the actual interface, release notes, public design-system documentation. Current and inspectable; record the access date and state.
3. **Curated reference libraries** — Mobbin, Refero and similar. Efficient for discovery of shipped patterns. Captures can lag, selection is curated, and paid access limits coverage.
4. **Secondary commentary** — roundups, blogs, social posts. Use as a lead to a primary source, not as proof.
5. **Model memory or generated description** — a hypothesis. Verify it before repeating it.

A screenshot without a source, date and state is weak evidence. An MCP result without opening the referenced screen is a lead, not an observation.

## Sample deliberately

- Cover two to four products for a focused question; more is rarely worth the reading cost.
- Mix a direct competitor, an adjacent-category product and one product with a genuinely different approach.
- Prefer products whose audience, market and platform resemble the target; note where they diverge.
- Avoid selecting only famous products. Visibility is not representativeness, and survivors share conventions that may not generalize.
- For flows, inspect the whole sequence, not only the hero step. Count the steps and record where the user can leave or recover.
- For styles, compare multiple angles rather than selecting the first attractive result.

## Record weak and strong evidence

Weak: "Linear uses a dark pricing page."

Strong: "Linear's public pricing page, desktop Chrome, 2026-11-16, shows three plan cards above a feature-comparison table; the annual toggle changes displayed prices in place. Observation only; no user behavior was tested."

Weak: "Users expect a wizard here."

Strong: "Three of four comparable onboarding flows split identity verification into a separate step after account creation, and all three offer a recovery path. The fourth completes it inline. This is a convention, not a measured preference."

The second form lets a reviewer disagree with the inference without redoing the research.

## Synthesize

1. Cluster by user task and decision, not by product. A product-by-product tour hides the comparison.
2. Mark agreement and dissent. State the common convention and the credible alternative.
3. Separate common from good. Frequency is a signal about expectations, not about outcomes.
4. Translate observations into principles: "keep the total visible through the flow" rather than "copy this sticky bar".
5. Attach each principle to a candidate direction and the state it affects.
6. Name missing evidence: an untested state, an unrepresented audience, a metric nobody published, an inaccessible flow.
7. Cite the closest sources with product, URL and date. Do not overstate the sample.

## Evidence limits

- A shipped design proves only that a product shipped it. It does not prove conversion, retention, usability or accessibility.
- A recurring pattern is a convention. It can also be a shared mistake.
- A competitive review is not a usability test, even when the reviewer is expert.
- Captures can be stale, partial, logged out, region-specific or plan-specific.
- Public examples skew toward visible, successful and English-language products.
- Generated descriptions of screens can be wrong. Inspect the image or the live product before relying on detail.
- Screenshots do not show keyboard behavior, focus order, latency, persistence or screen-reader output.
- A paid library's absence is not evidence that a pattern is uncommon.

## Fallback without Mobbin or Refero

Continue with the same question and evidence standard:

1. **UI/UX Pro Max** for baseline candidates: product patterns, styles, palettes, typography, UX rules and stack guidance. Treat results as candidate material and check fit.
2. **Repository and design system** for accepted tokens, components, content and constraints. This outranks generic candidates.
3. **User-supplied references** for intent. Ask what the user values in each and whether the team has rights to use it.
4. **Public products** for current examples: marketing sites, documentation, changelogs, help centers, app-store listings and public screenshots. Open the source, not a repost.
5. **Public design systems** from comparable organizations for documented component and accessibility behavior.
6. **Local prototypes** when structure or visual direction needs comparison. Render the same content at the same fidelity; label it as a proposal.

If those sources cannot answer the question, say what is missing and which decision must proceed on judgment. Do not fabricate a reference, invent a product name or describe a screen you did not inspect. Do not claim that a library search was attempted when it was not.

## Access and privacy check

Before querying a third-party service:

- confirm the user's plan and authorization;
- confirm that the query contains no confidential design, customer data or unreleased name;
- use the client's OAuth or local credential store, never repository config;
- respect rate limits and provider terms;
- stop and ask when the only way to get an example is to bypass access control.

Record which service was used, the date and the query scope. The design record should show the preference and whether the task ran with or without it.
