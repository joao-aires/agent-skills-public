---
name: business-opportunity-analysis
description: "Analyze a business, startup, product, or market opportunity from first principles. Use when the user asks about TAM/SAM/SOM, revenue potential, pricing, go-to-market, monetization, business-model quality, SaaS or AI economics, valuation, revenue multiples, strategic value, competitive positioning, open-source commercialization, or scenario-based company outcomes. Produces a structured, evidence-aware analysis that distinguishes market size from obtainable revenue, revenue from revenue quality, and valuation from simple revenue multiples."
metadata:
  version: "1.0"
---

# Business Opportunity Analysis

Analyze business opportunities as systems, not as isolated market-size or revenue-multiple exercises.

The goal is to answer questions such as:

- How large can this business realistically become?
- What could it charge, and to whom?
- What revenue is plausible under conservative, base, and upside scenarios?
- What makes the revenue high- or low-quality?
- What go-to-market strategy best matches the product and buyer?
- How should an open-source product be commercialized?
- What valuation range could the business command, and why?
- Which assumptions matter most, and what would have to be true for the upside case?

## Core Principle

Do **not** jump directly from a large market number to a revenue forecast, or from revenue to valuation.

Use this chain instead:

```text
Problem / job to be done
        ↓
Target customer + buyer
        ↓
Value created / budget unlocked
        ↓
Addressable units × plausible spend
        ↓
TAM / SAM / obtainable market
        ↓
GTM + adoption constraints
        ↓
Customers × ACV / usage
        ↓
Revenue scenarios
        ↓
Gross margin + retention + expansion
        ↓
Revenue quality
        ↓
Growth + market position + strategic importance
        ↓
Valuation range
```

## Required Analysis Workflow

### 1. Define the business precisely

State:

- product or service
- primary user
- economic buyer
- core job to be done
- competing alternatives, including "do nothing" and internal build
- whether it is an application, platform, infrastructure layer, marketplace, service, or hybrid

Avoid analyzing an ambiguous label such as "AI agent company" without identifying the layer it owns.

### 2. Separate product wedge from long-term platform

Many companies enter through a narrow product and monetize a broader layer later.

For example:

```text
Easy-to-understand wedge
        ↓
Distribution / adoption
        ↓
Underlying platform or control point
        ↓
Expansion into more workflows
        ↓
Higher ACV + stronger moat
```

Explicitly distinguish:

- **wedge** — the initial product people adopt
- **core asset** — what accumulates value as usage grows
- **expansion surface** — adjacent workflows, teams, geographies, or products
- **strategic control point** — if one exists, the layer through which other activity must pass

### 3. Build TAM bottom-up before using top-down market reports

Prefer bottom-up market sizing:

```text
Number of plausible customers
×
Plausible annual spend per customer
=
Addressable annual revenue
```

Segment when necessary:

```text
SMB customers × SMB ACV
+
Mid-market customers × Mid-market ACV
+
Enterprise customers × Enterprise ACV
```

Then use top-down industry reports only as a sanity check or ceiling.

Always distinguish:

- **TAM** — total theoretical addressable revenue
- **SAM** — market reachable with the product, geography, channel, and capabilities under consideration
- **SOM / obtainable revenue** — realistic share given competition, sales capacity, adoption friction, and time

Read `references/market-sizing.md` for the detailed methodology.

### 4. Derive pricing from value and deployment model

Do not choose pricing by copying competitors alone.

Consider:

- value created or cost avoided
- buyer budget
- frequency / intensity of usage
- marginal cost to serve
- procurement preferences
- predictability of customer spend
- how customer value scales

Evaluate pricing metrics such as:

- per seat
- per organization / workspace
- per transaction
- per API call / token / compute unit
- per workflow / agent / deployment
- platform fee + usage
- enterprise annual contract
- BYO-infrastructure or BYO-model arrangements

For infrastructure and AI products, explicitly model who pays underlying compute/model costs.

### 5. Model revenue with scenarios

Use at least three scenarios when the user asks about potential outcomes:

- conservative
- base
- upside

A useful model is:

```text
Revenue = customers × average annual revenue per customer
```

or, for usage businesses:

```text
Revenue = active customers × average usage × price per unit
```

For multi-segment businesses:

```text
Revenue = Σ(customers in segment × segment ACV)
```

Do not hide assumptions. Surface the variables that drive the result.

When useful, model a multi-year path using:

- starting customers
- customer growth
- ACV expansion
- churn
- NRR
- gross margin
- sales capacity

### 6. Evaluate revenue quality

Two companies with identical revenue can have radically different valuations.

Assess:

- gross margin
- recurring vs transactional revenue
- customer concentration
- logo retention
- net revenue retention (NRR)
- expansion dynamics
- CAC and sales efficiency where data exists
- implementation / services burden
- dependence on third-party infrastructure
- pricing power
- predictability

For AI products, pay special attention to inference, sandbox, browser, storage, and human-operations costs.

A company with high pass-through model costs should not automatically receive the economics of high-margin SaaS.

Read `references/revenue-quality-and-unit-economics.md` when detailed unit economics matter.

### 7. Analyze go-to-market as part of the business model

Do not treat GTM as an afterthought.

Determine:

- who discovers the product
- who tries it
- who approves it
- who pays for it
- what adoption event creates habit or lock-in
- what converts free / OSS usage into paid usage

Common motions include:

- product-led growth
- developer-led adoption
- open-source-led growth
- founder-led enterprise sales
- top-down enterprise sales
- channel / marketplace distribution
- embedded / OEM distribution
- community-led growth

For open-source businesses, read `references/open-source-commercialization.md`.

### 8. Identify moats and strategic value

Evaluate both conventional defensibility and strategic control.

Potential moats:

- proprietary data
- workflow lock-in
- network effects
- ecosystem / marketplace
- developer mindshare
- standards adoption
- distribution
- switching costs
- embedded integrations
- operational complexity customers do not want to own
- regulatory / compliance advantage
- scale economics

Also ask:

> If this company became the default layer for this workflow, what downstream activity would pass through it?

This helps distinguish a feature from a platform or control point.

### 9. Value the company using scenario multiples, not a single heuristic

Never imply that a revenue multiple applies equally to all companies.

Use:

```text
Valuation ≈ Revenue or ARR × context-dependent multiple
```

but explain that the multiple is determined by factors including:

- growth rate and acceleration
- gross margin
- retention / NRR
- market size and remaining runway
- category position
- scarcity / strategic importance
- competitive intensity
- capital efficiency
- public-market comparables
- acquisition synergies

Use ranges instead of fake precision.

A useful conceptual model is:

```text
Revenue
  × quality of revenue
  × growth / future expectations
  × market / category premium
  × strategic premium
≈ company value
```

The multipliers above are conceptual, not independently quoted financial multiples.

Read `references/valuation-framework.md` for the detailed framework and examples.

### 10. Distinguish standalone valuation from strategic acquisition value

For acquisitions, ask what the asset is worth **to the buyer**, not only what it is worth independently.

Examples of strategic value:

- drives cloud consumption
- protects an existing franchise
- accelerates entry into a strategic market
- acquires distribution or developers
- controls an emerging standard
- removes a future competitor
- creates cross-sell opportunities
- improves proprietary models or data

An acquirer can rationally pay more than standalone financial multiples suggest if the synergies are large enough.

### 11. State what must be true

End important analyses with the assumptions that determine whether the upside case materializes.

For example:

```text
For the €100M ARR case to work:
1. Enterprise ACV must exceed €50k.
2. NRR must remain above 120%.
3. Gross margin must remain above 75%.
4. The product must expand beyond its initial Slack wedge.
5. The company must become a default runtime rather than one of many interchangeable frameworks.
```

This is more useful than presenting an upside number without its prerequisites.

## Evidence and Research Rules

When current data matters, research it.

Prefer primary sources where possible:

- company pricing pages
- company announcements
- regulatory filings
- investor presentations
- official usage / customer statistics
- credible reporting for private-company revenue or valuation

For market-size reports, treat consultancy estimates as directional rather than exact truth.

Always separate:

- **reported facts**
- **derived calculations**
- **assumptions**
- **judgment / inference**

When the user provides no geography or currency, use the geography most appropriate to the business and state it. When the user specifies one, respect it consistently.

## Recommended Output Structure

Adapt depth to the question, but for a full opportunity analysis prefer:

1. **Executive view** — what the business could become and why
2. **Business definition** — customer, buyer, job, product layer
3. **Market structure** — wedge, platform, competitors, substitutes
4. **TAM / SAM / SOM** — bottom-up with explicit assumptions
5. **Pricing & monetization** — proposed model and rationale
6. **GTM** — wedge, acquisition channel, conversion path
7. **Revenue scenarios** — conservative / base / upside
8. **Revenue quality & economics** — margin, retention, cost structure
9. **Moat & strategic value** — why this can or cannot become a control point
10. **Valuation scenarios** — ordinary / strong / exceptional outcomes
11. **Key risks** — what could break the thesis
12. **What must be true** — conditions for the upside case

## Anti-Patterns

Avoid these common mistakes:

### "The market is $100B, so 1% is a $1B business"

This ignores buyer count, achievable ACV, GTM, competition, and adoption friction.

### "SaaS trades at 10× revenue"

There is no universal SaaS multiple. Multiples vary dramatically with growth and revenue quality.

### "AI companies get higher multiples"

AI is not itself a moat or valuation methodology. High multiples require exceptional growth, economics, market position, or strategic value.

### Confusing GMV, bookings, ARR, revenue, and gross profit

Use the correct denominator and state it explicitly.

### Treating pass-through spend as high-quality software revenue

If most revenue immediately pays model providers or infrastructure vendors, analyze gross profit and contribution margin.

### Using current revenue while ignoring acceleration

For hypergrowth companies, investors may price expected forward revenue. Explain this rather than claiming that the observed multiple is inexplicable.

### Treating acquisition price as a normal market multiple

Strategic transactions may include substantial synergy premiums.

## Fast Analysis Mode

For a lightweight question, use this compressed sequence:

```text
1. Who pays and why?
2. How many plausible buyers exist?
3. What can they plausibly spend?
4. How do customers discover and adopt it?
5. What does a realistic customer-count × ACV scenario produce?
6. What are gross margins and expansion dynamics?
7. What makes this defensible?
8. What multiple range fits those characteristics?
9. What must be true for the upside case?
```

## Reference Files

Use the supporting references selectively:

- `references/market-sizing.md` — TAM, SAM, SOM and bottom-up sizing
- `references/open-source-commercialization.md` — OSS wedges, open-core boundaries, monetization, GTM
- `references/revenue-quality-and-unit-economics.md` — margins, retention, NRR, AI cost structures
- `references/valuation-framework.md` — revenue multiples, growth, strategic premiums, acquisition logic
- `references/scenario-modeling.md` — revenue and multi-year scenario construction

Only load the references relevant to the user's question.