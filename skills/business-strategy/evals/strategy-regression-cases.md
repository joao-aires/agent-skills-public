# Business Strategy v2 — Regression Cases

These cases are intended to catch strategy-quality regressions when the skill changes. They are not factual benchmarks; current market facts should be researched at run time.

## Scoring Rubric

Score each dimension 0–2:

- **Thesis mutation** — does the skill revise the initial idea when evidence warrants it?
- **Competitive completeness** — product, capability, whole-vision, trajectory, substitutes
- **Alternative generation** — genuinely different strategic options before convergence
- **Non-obvious insight** — synthesis goes beyond source summaries
- **Evidence discipline** — facts, assumptions, inferences, counter-evidence, contradictions
- **Wedge quality** — entry path plus expansion logic
- **Customer behavior / culture** — included when it changes adoption or GTM
- **Future robustness** — separates invariants from fragile assumptions
- **Economic coherence** — market, GTM, pricing, expansion and financial model agree
- **Falsifiability** — critical assumptions have tripwires / tests
- **Decision usefulness** — clear recommendation and what would change it

A strong deep run should score at least 18/22 with no zero in thesis mutation, evidence discipline, or decision usefulness.

---

## Case 1 — Managed-Agent Platform Thesis

### Prompt

> I want to build an open-source equivalent of a hyperscaler's managed-agent platform. What should the product be, what is the wedge, how could it make money, and could it become a very large company?

### Expected behavior

The skill should:

- avoid assuming an OSS clone is the best strategy;
- map runtime, identity, memory, policy, observability, credentials, orchestration, governance, and user-facing surfaces by layer;
- identify hyperscalers and adjacent platforms as whole-vision competitors;
- analyze what those incumbents can plausibly bundle in 12–36 months;
- generate alternative control points / abstractions;
- distinguish today's "agent" implementation from invariant needs such as authorization, accountability, delegation, assurance, or workflow control where supported by evidence;
- explicitly mutate the thesis if generic runtime is becoming commoditized;
- separate OSS adoption from enterprise monetization;
- model economics only after choosing a plausible strategic position.

### Failure modes

- produces only a feature matrix;
- concludes "competitive market" without proposing a stronger thesis;
- assumes the employee-like agent metaphor persists indefinitely;
- jumps to TAM and €100M ARR before resolving the product layer.

---

## Case 2 — Straightforward SaaS Revenue Potential

### Prompt

> A transcription/productivity SaaS has three simple subscription tiers. Estimate how large the business could become and what would drive the revenue outcome.

### Expected behavior

The skill should stay lightweight and emphasize:

- user / buyer
- reachable market
- pricing and conversion
- retention / expansion
- customer-count × ARPU scenarios
- distribution constraints
- gross margin

It should **not** run an unnecessary full future-market strategy process unless the facts reveal a strategic issue.

---

## Case 3 — Consumer Product: Portugal versus United States

### Prompt

> We have a consumer product that works in the US. Should we launch the same proposition in Portugal or adapt the wedge and positioning?

### Expected behavior

The skill should explicitly investigate concrete differences in:

- customer behavior
- purchasing power / substitution economics
- trust and privacy
- language and category framing
- local channels
- incumbents
- regulation where relevant

It should not use generic national-culture scores as a substitute for market evidence.

---

## Case 4 — Crowded Market

### Prompt

> I want to enter a mature project-management market. It looks crowded. Is there still a viable strategy?

### Expected behavior

The skill should generate alternatives across:

- underserved segment
- workflow-specific wedge
- distribution channel
- business model
- integration / platform layer
- geography
- category reframing

It should not stop at "the market is saturated" or recommend competing head-on without a mechanism.

---

## Case 5 — Technically Novel Infrastructure Startup

### Prompt

> We have a technically differentiated infrastructure layer in a fast-moving AI market. Is the technical advantage enough to build a durable company?

### Expected behavior

The skill should:

- map which capabilities are likely to commoditize;
- identify platform dependencies;
- distinguish current technical edge from accumulating assets and control points;
- run future-state scenarios;
- test open-source/internal-build substitutes;
- analyze distribution and enterprise adoption, not only technical merit;
- state what must be true for the advantage to become durable power.

---

## Review Procedure

When changing the skill materially:

1. Run at least Cases 1, 2, and 5.
2. Compare conclusions and intermediate reasoning against the expected behavior.
3. Inspect whether new instructions caused over-processing of simple cases.
4. Record any failure mode that escaped the existing suite as a new regression case.

The objective is not identical prose across runs. The objective is preserving the strategy behaviors that matter.