# Business Strategy — Regression Cases

These cases catch strategy-quality regressions when the skill changes. They are behavioral benchmarks, not factual benchmarks; current market facts should be researched at run time.

## Scoring Rubric

Score each dimension 0–2 when it is relevant to the case:

- **Thesis quality and mutation** — provisional thesis is explicit and changes when evidence warrants it
- **Evidence discipline** — decision-changing claims, counter-evidence, facts vs assumptions/inference
- **Market/customer reality** — actual workflow, buyer, behavior/culture and market system when material
- **Competition and alternatives** — substitutes, three competition levels, trajectories, genuinely different options
- **Wedge / beachhead quality** — coherence, depth-of-win logic, distribution and expansion geometry
- **Value creation + economic power** — magnitude of advantage and why value is captured or leaked
- **Future durability** — invariant vs fragile assumptions, commoditization and mature-market/last-mover logic
- **Economic coherence** — market, pricing, GTM, unit economics and scenarios agree
- **Falsifiability** — critical assumptions have tests, falsifiers or tripwires
- **Decision usefulness** — explicit recommendation, trade-offs and what would change it

A strong deep run should normally score at least 17/20 with no zero in thesis quality/mutation, evidence discipline, value creation/economic power, or decision usefulness. Lightweight cases should not be penalized for omitting irrelevant modules.

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
- challenge the consensus that the runtime layer is necessarily where durable value will live;
- distinguish today's "agent" implementation from invariant needs such as authorization, accountability, delegation, assurance, or workflow control where supported by evidence;
- explicitly mutate the thesis if generic runtime is becoming commoditized;
- separate OSS adoption from enterprise monetization;
- explain where value could leak to model/cloud/platform providers;
- model economics only after choosing a plausible strategic position.

### Failure modes

- produces only a feature matrix;
- concludes "competitive market" without proposing a stronger thesis;
- treats being contrarian as proof;
- assumes the employee-like agent metaphor persists indefinitely;
- jumps to TAM and €100M ARR before resolving the product layer and value-capture mechanism.

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

It should **not** force contrarian, last-mover, or full strategic-power analysis unless the facts reveal a material strategic issue.

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

The skill should generate alternatives across underserved segment, workflow-specific wedge, concentrated beachhead, distribution, business model, product layer, geography, and category framing.

It should ask whether any option changes the basis of competition enough to create economic power rather than merely becoming another slightly better tool.

It should not stop at "the market is saturated" or recommend competing head-on without a mechanism.

---

## Case 5 — Technically Novel Infrastructure Startup

### Prompt

> We have a technically differentiated infrastructure layer in a fast-moving AI market. Is the technical advantage enough to build a durable company?

### Expected behavior

The skill should:

- measure the magnitude of technical differentiation rather than just noting novelty;
- map which capabilities are likely to commoditize;
- identify platform dependencies and supplier bargaining power;
- distinguish current technical edge from accumulating assets and control points;
- run future-state and mature-market tests;
- test open-source/internal-build substitutes;
- analyze distribution and enterprise adoption, not only technical merit;
- explain why value would or would not remain with the company as technology becomes cheaper;
- state what must be true for the advantage to become durable power.

---

## Case 6 — Large Crowded TAM, Incremental Product

### Prompt

> This is a €50B software market with many established vendors. We think we can build a product that is about 20% better on usability and sell to 1% of the market. Is this attractive?

### Expected behavior

The skill should:

- reject the "1% of a huge TAM" shortcut;
- test whether 20% better is enough to change behavior or pricing;
- inspect buyer and incumbent power;
- search for a coherent beachhead where the advantage is much stronger;
- consider changing product, segment, distribution, or category rather than assuming horizontal entry;
- distinguish value creation from value capture.

### Failure modes

- accepts 1% share as conservative;
- treats any differentiation as a moat;
- calculates valuation before resolving the competitive position.

---

## Case 7 — Tiny Market With No Competitors

### Prompt

> I found a very specific niche with no software competitors. Should I build the only product for it?

### Expected behavior

The skill should not infer attractiveness from absence of competition.

It should test whether the market is coherent, pain and willingness to pay, non-software substitutes, why nobody entered, expansion potential, and whether dominance creates any accumulating asset or economic power.

---

## Case 8 — Concentrated Beachhead Versus Broad Market

### Prompt

> We can either target 100,000 generic companies or a niche of 2,000 highly connected specialist firms with a much stronger pain and a shared industry channel. Which is the better starting market?

### Expected behavior

The skill should not mechanically choose the larger TAM.

It should compare beachhead coherence, distribution concentration, depth of value, plausible penetration, learning/reputation/network effects, expansion geometry, long-term market size and value capture.

The narrow market should win only if its concentrated position creates a credible path to a larger and stronger strategy.

---

## Case 9 — Qualitatively New Capability

### Prompt

> Our product lets customers do something that was previously effectively impossible. There is no established software category or budget for it. How should we think about the opportunity?

### Expected behavior

The skill should:

- distinguish new capability from incremental improvement;
- validate that customers value the newly possible outcome;
- examine behavior change and category-education cost;
- test whether the capability creates a new market, reframes an existing budget, or remains a novelty;
- examine pricing discretion and likely competitive entry;
- identify what can compound before the capability itself commoditizes.

---

## Review Procedure

When changing the skill materially:

1. run at least Cases 1, 2, 5, 6, and 8;
2. compare conclusions and intermediate reasoning against expected behavior;
3. check that new instructions do not over-process simple cases;
4. check that "no competition" and "contrarian" are never treated as evidence by themselves;
5. add any newly discovered failure mode as a regression case.

The objective is not identical prose across runs. It is preserving the strategy behaviors that matter.