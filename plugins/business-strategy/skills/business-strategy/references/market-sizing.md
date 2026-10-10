# Market Sizing

## Principle

Prefer bottom-up market sizing tied to real buyers, usage, and spend. Use top-down market reports as context or a cross-check, not as the primary logic.

## Define the market before sizing it

State:

- customer / buyer
- geography
- use case / workflow
- product layer
- pricing unit
- time horizon

Avoid mixing different definitions under one TAM number.

## Bottom-up TAM

Choose the model that matches the business.

### Account-based

```text
TAM = number of plausible customer accounts × annual spend per account
```

### Seat-based

```text
TAM = addressable users × annual revenue per user
```

### Usage-based

```text
TAM = addressable usage volume × price per unit
```

### Transaction-based

```text
TAM = addressable transaction value × take rate
```

Segment when spend differs materially by company size, geography, or use case.

## SAM

SAM should account for practical scope such as:

- geography / regulation
- target customer size
- integrations / platform compatibility
- language / workflow
- product maturity
- delivery model

## Obtainable market / SOM

Do not use an arbitrary percentage of TAM.

Model obtainable revenue from constraints such as:

```text
reachable accounts
× conversion rate
× annual contract value
```

or:

```text
sales capacity × productivity × conversion × ACV
```

For self-serve:

```text
qualified traffic / distribution reach
× signup rate
× paid conversion
× ARPU
```

## Pricing assumptions

Tie spend assumptions to customer value, alternatives, budget, and buying model rather than copying competitor list prices.

If the business model is not yet chosen, size multiple monetization options where they produce materially different markets or economics.

## Market evolution

When the category is new, model both current and future TAM. A business can be small today but strategically valuable if the underlying budget category is growing rapidly.

Keep current-state and future-state estimates separate.

For new categories, tie future TAM to explicit adoption or budget-shift assumptions and record the decision-critical ones in the **Critical Assumptions** section of `strategy-state.md`.

## Sanity checks

Cross-check:

- implied customer spend versus current budgets
- implied market share versus competitive structure
- implied penetration versus adoption friction
- implied sales volume versus GTM capacity
- top-down reports with compatible definitions

## Output

State:

- market definition
- bottom-up TAM
- SAM
- realistically obtainable market / revenue
- key pricing / adoption assumptions
- sensitivity to the most important assumptions
- current versus future market where relevant

The useful output is not the biggest credible number; it is the market size consistent with the chosen strategy and business model.