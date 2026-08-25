---
name: business-opportunity-analysis
description: "Deprecated legacy compatibility skill. Use only when explicitly invoked as business-opportunity-analysis or when the newer business-strategy skill is unavailable. Provides a self-contained fallback for TAM/SAM/SOM, pricing, GTM, revenue scenarios, OSS commercialization, unit economics, moats, and valuation. Prefer business-strategy for all new strategy work."
metadata:
  version: "2.0-compat"
  deprecated: "true"
---

# Business Opportunity Analysis — Legacy Compatibility

The primary skill is now `business-strategy`.

## Preferred behavior

If `../business-strategy/SKILL.md` is available, read it and use it as the source of truth. A legacy opportunity-analysis request normally maps to its `evaluate` mode.

If the sibling skill is **not** available because this legacy skill was installed by itself, use the standalone fallback below. This preserves old installations without duplicating the entire v2 strategy system.

## Standalone Fallback

Analyze the business opportunity as a system rather than jumping from a large market number to a revenue or valuation claim.

Use this sequence:

```text
problem / job
→ target user + economic buyer
→ wedge + long-term product
→ addressable buyers × plausible spend
→ GTM + adoption constraints
→ customers × ACV / usage
→ revenue quality + unit economics
→ defensibility / strategic value
→ valuation scenarios
→ what must be true
```

### 1. Define the business precisely

State:

- product or service
- primary user
- economic buyer
- core job / pain
- alternatives, including internal build and do nothing
- product layer: application, platform, infrastructure, marketplace, service, or hybrid

### 2. Separate wedge from destination

Distinguish:

- **wedge** — first product/use case adopted
- **core asset** — what accumulates value
- **expansion surface** — adjacent workflows, teams, products, or geographies
- **strategic control point** — if one exists, the layer other valuable activity passes through

### 3. Size the market bottom-up

Read `references/market-sizing.md`.

Prefer:

```text
plausible buyers × plausible annual spend
```

before top-down market reports. Keep TAM, SAM, and realistically obtainable revenue separate.

### 4. Derive pricing and GTM from value

Determine:

- value created / cost avoided
- budget owner
- pricing metric
- procurement preference
- who discovers, tries, approves, and pays
- what creates habitual adoption or expansion

For open-source businesses, read `references/open-source-commercialization.md`.

### 5. Model revenue scenarios

Read `references/scenario-modeling.md`.

Use conservative, base, and upside scenarios when outcomes matter. Tie customer counts to realistic sales/channel capacity and tie ACV growth to an explicit expansion mechanism.

### 6. Evaluate revenue quality

Read `references/revenue-quality-and-unit-economics.md`.

Assess gross margin, retention, NRR, expansion, concentration, pricing power, variable cost exposure, implementation burden, and predictability.

### 7. Assess defensibility

Evaluate relevant mechanisms such as:

- workflow lock-in
- proprietary data
- network / ecosystem effects
- distribution
- standards
- switching costs
- integrations
- operational complexity customers do not want to own
- regulatory or scale advantage

Ask:

> If this became the default layer for the workflow, what valuable downstream activity would pass through it?

### 8. Value the company contextually

Read `references/valuation-framework.md`.

Do not apply a universal SaaS multiple. Use current comparables when valuation matters and separate standalone value from strategic acquisition value.

### 9. State what must be true

End important analyses with the assumptions that determine whether the upside case works.

For example:

```text
For the target ARR case to work:
- reachable customer count must be plausible;
- ACV must match customer value and budget;
- GTM capacity must support the required new logos;
- margins and retention must support scalable growth;
- the wedge must expand into the intended strategic position.
```

## Evidence Rules

When current data matters, research it.

Always distinguish:

- reported facts
- derived calculations
- assumptions
- inference / strategic judgment

Prefer primary sources for pricing, product capabilities, filings, regulation, and official usage/customer statistics.

## Upgrade Path

For wedge selection, layered competitor trajectories, customer culture/behavior, future-market scenarios, claim-led research, strategy mutation, persistent assumption registers, decision logs, or ongoing strategy review, install and use `business-strategy`.