# Future-Market Scenarios

## Principle

Do not pretend to forecast a novel market precisely. Build a small set of plausible future states and test whether the strategy remains valuable.

The objective is **robustness**, not prediction theater.

## When this is mandatory

Use future-market stress testing when:

- technology is evolving rapidly
- standards are unsettled
- platform boundaries are moving
- regulation could reshape the market
- the product depends on a new behavior or metaphor
- the wedge may be transitional
- the company has a 5–10 year platform ambition

## Build 3–4 scenarios

### 1. Current/base continuation

What if today's market structure largely persists and adoption grows?

### 2. Likely structural evolution

What changes appear likely because of economics, technology, regulation, or platform incentives?

### 3. Meaningful alternative

What if an important assumption develops differently?

Examples:

- customers consolidate onto one platform instead of remaining multi-vendor
- a new standard removes integration friction
- users reject a new interaction model
- open source commoditizes the proposed paid layer

### 4. Extreme but decision-relevant scenario

Use only if it could invalidate the long-term thesis.

The point is not science fiction; it is to expose hidden dependencies.

## Classify assumptions

For important assumptions, assign:

### Invariant

Likely valuable across very different futures.

Examples may include accountability, trust, coordination, resource allocation, or authorization, depending on the market.

### Structural

Likely to persist for several years because it follows from durable incentives or constraints.

### Transitional

Valuable during a migration or immature market phase but likely to decline.

### Fragile

Depends heavily on today's architecture, vendor landscape, terminology, or user behavior.

A strategy dominated by fragile assumptions deserves a lower confidence level even if it fits today's market well.

## Invariant-value test

Ask:

> If the implementation model changes radically, what customer need remains?

Then separate the enduring need from the current technical abstraction.

Example pattern:

```text
today's object: "AI employee directory"
possible invariant: identity, authority, delegation, accountability
```

The invariant may be the stronger strategic foundation.

## Scenario matrix

For each strategy or wedge evaluate:

- customer value
- distribution
- competitor pressure
- monetization
- moat
- required capabilities
- risk of obsolescence

Use simple ratings such as strong / viable / weak / invalidated.

## Option value

Prefer early moves that create learning, distribution, data, standards influence, or customer relationships while preserving the ability to pivot as the market resolves.

Avoid irreversible bets on fragile assumptions unless expected advantage is large enough to justify the risk.

## Signals and tripwires

For each future-state uncertainty, identify observable signals:

- standards adoption
- vendor consolidation
- new platform launches
- customer architecture choices
- price compression
- regulation
- behavior change

Record which strategic decision each signal would reopen.

## Output

End with:

1. scenarios considered
2. assumptions classified as invariant / structural / transitional / fragile
3. which strategy is most robust
4. which current opportunity is intentionally transitional
5. signals to monitor
6. decisions to revisit if those signals occur

Do not choose the most futuristic scenario simply because it is interesting.