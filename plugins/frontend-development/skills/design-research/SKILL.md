---
name: design-research
description: Research shipped products, flows and visual directions before settling an interface decision. Use for competitive and reference research, design benchmarks and pattern evidence; choose sources, separate observation from inference, respect access and privacy limits, and feed material into a comparable option set. Works without paid reference services.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: technical
  domain: frontend
  phase: design
  scope: generic
  invocation: both
  role: support
---

# Research interface precedent before choosing

Design research reduces uncertainty about what users already know, how comparable products sequence a task, which content and states a surface must carry, and which visual direction fits the brand. It supplies evidence for a decision; it does not make the decision, replace user research or authorize copying.

This method supports [interface design](../interface-design/SKILL.md). Interface design owns the brief, direction and implementation; [usability research](../usability-research/SKILL.md) owns participant studies. [UI/UX Pro Max](../ui-ux-pro-max/SKILL.md) is always used as baseline design intelligence, not as a fallback after other sources fail.

## Frame the question

State the decision the research should inform and what answer would change it. A useful question names the user task, platform or product category, and unit of comparison:

- "How do expense tools let a user split and reimburse a line item on mobile?"
- "Which composition do developer-tool pricing pages use for usage-based tiers?"
- "What recovery path follows a failed identity check in banking onboarding?"

"Ideas for a dashboard" is not a research question. Inspect the existing brief, design system, product evidence and accepted references first. Ask only for the facts that change the comparison.

## Ask once about reference libraries

Ask the user once, early in the engagement, whether they want or can use Mobbin or Refero. If yes and the server is connected, use it. If no, unavailable or unanswered, continue with the baseline below and record the preference in the research or design record. Do not ask again unless access changes.

Both are optional paid services; the task must complete without them. Absence changes convenience and the breadth of examples, not the evidence standard. Never imply that a weaker method was used because a paid service was unavailable.

| Source | Use for | Authority |
| --- | --- | --- |
| UI/UX Pro Max (always) | Candidate styles, palettes, typography, UX rules and stack guidance | Baseline design intelligence; candidate material, not research evidence |
| Repository and design system | Accepted tokens, components, copy, states and product constraints | Highest authority for fit with this product |
| User-supplied references | Screens, links or files the user already trusts | Strong for intent; verify rights and currency |
| Public product and competitor research | Live or documented shipped interfaces, app listings, changelogs | Direct observation when current; check what is public |
| Local prototypes | Comparing structure or visual direction on the same content | Evidence about the candidate, not about the market |
| Mobbin or Refero (optional) | Searchable screens, flows, sections and styles from shipped products | Efficient discovery; still secondary to the live product |

Read [research methods](references/research-methods.md) when choosing an approach, judging source quality or working without Mobbin or Refero.

## Scope the comparison

Fix the platform, product category, user goal, audience and constraints before collecting examples. Choose the unit that matches the question:

- **Screens** for a state, component or layout pattern: pricing table, empty state, permission prompt, settings form.
- **Flows** for sequence, decisions, recovery and system response: onboarding, checkout, cancellation, account deletion.
- **Sections or pages** for composition and content hierarchy: hero, pricing section, documentation index, footer.
- **Styles** for visual direction: typography, color roles, spacing, surfaces, imagery and component feel.

Compare two to four products. A useful set includes a direct competitor, an adjacent-category product and one outlier with a different approach. Do not generalize from a single famous product or from whichever examples a search returns first.

## Gather and record evidence

Preserve enough context that another person can inspect the source and judge the claim:

| Field | Keep |
| --- | --- |
| Product and platform | Name, web/iOS/Android/desktop, market or region |
| Source | Canonical URL and, for a library, its canonical item URL |
| Currency | Capture date, app version or release note; mark stale captures |
| Surface and state | Screen, flow step, section or style; signed-in/out, paid/free, error/empty |
| Observation | What is visibly present or documented |
| Inference | What you think it means for the user or decision |
| Relevance | Which direction or constraint it informs |
| Rights | Public, user-supplied, licensed library or confidential |

Keep observation separate from interpretation. "Checkout shows the order total in a sticky footer through all three steps" is an observation. "This probably reduces hesitation about shipping cost" is an inference that needs validation. "Use a sticky total" is a recommendation.

Record states, not only the happy path: empty, loading, busy, error, denied, stale, conflict and recovery where they exist. Note visible accessibility cues such as focus treatment, label placement and target size, but do not certify accessibility from a screenshot.

Check recency before relying on a pattern. Interfaces change; a capture may predate a redesign, a regional variant or a plan-specific flow. Prefer the live product or a dated primary source, and say when you could not verify current behavior.

A pattern is a convention, not proof of conversion, usability or quality. Several products may share a weak default. Report how many products you inspected, how they were selected, and what the sample cannot support. Do not call something a best practice on the strength of a reference collage.

## Respect privacy, access and rights

- Do not send confidential designs, unreleased product names, customer data or internal screenshots to a third-party MCP without explicit permission. Query text may be logged by the provider.
- Verify the user's plan and authorization before querying a paid library. Do not bypass a paywall, scrape behind authentication or use another person's session.
- Respect published rate limits and back off on throttling. Mobbin documents 60 requests per 60 seconds per user and `Retry-After` on HTTP 429; Refero documents up to 8,000 tool calls per monthly period per licensed user.
- Keep credentials, bearer tokens and authorization headers out of repository configuration. Connect through the client's OAuth flow or local user configuration.
- Keep queries generic. Do not include secrets, customer names or unreleased specifications in a search string.
- Do not copy protected layouts, branding, illustration, text or assets. Extract the principle, then design against the user's brand, content, design system and accessibility requirements. Respect site terms and licenses.

If a source is paywalled or inaccessible, say so and use the fallback sources rather than guessing at its contents.

## Synthesize into the option set

Return what the decision needs, not a tour of products:

- the question and comparison scope;
- a small evidence table with observation, inference and source;
- candidate directions, each with what it optimizes and sacrifices;
- the conventions that appear across products and the dissent that matters;
- accessibility, content and state implications;
- the recommendation and what would change it;
- evidence still missing.

For consequential UI, hand at least three materially different directions to [interface design](../interface-design/SKILL.md) at comparable fidelity. Read [option review](references/option-review.md) for direction construction, presentation, feedback capture and the decision record. A routine local change needs a short precedent note and one recommendation, not an option exercise.

Never present a reference as the proposed design. A direction adapts an observed principle to this product; it is not a reskin of one source.

## Work without Mobbin or Refero

Use UI/UX Pro Max for baseline candidates, the repository and accepted design system for fit, user-supplied references for intent, and public product sites, documentation, changelogs and app-store listings for current examples. Compare candidate structures in a local prototype on the same content when the question is structural or visual. State which sources you actually inspected. If no credible comparison exists, say so and reason from the task, constraints and known conventions rather than inventing precedent.

## Sources and fit

- [Mobbin MCP](https://mobbin.com/mcp) and [Mobbin docs](https://docs.mobbin.com/mcp/) document the endpoint, plans, OAuth access, tools, rate limit and evidence limits used above. Checked 2026-11-16.
- [Refero MCP](https://refero.design/mcp), [Refero MCP getting started](https://doc.refero.design/mcp/getting-started) and [Refero tools](https://doc.refero.design/mcp/tools) document the endpoint, paid plans, OAuth or bearer access, call allowance and search layers. Checked 2026-11-16.
- [Competitive Usability Evaluations](https://www.nngroup.com/articles/competitive-usability-evaluations/) (Nielsen Norman Group) separates expert competitive review from testing with users and recommends a small competitor set. It informs the method boundary here; it does not endorse a particular library.
- [UX Research Cheat Sheet](https://www.nngroup.com/articles/ux-research-cheat-sheet/) (Nielsen Norman Group) places competitive analysis in the explore phase alongside design review and prototype testing. Use it to keep desk research distinct from participant evidence.

These sources describe access and method; they do not grant rights to reuse screens, text or assets. Product names and URLs are cited for identification only.
