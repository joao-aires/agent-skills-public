# Scenario Modeling

## Purpose

Scenario models should expose the assumptions that drive an outcome rather than present a single impressive number.

Use at least:

- conservative
- base
- upside

Add a downside case when capital intensity or survival risk matters.

## Basic customer × ACV model

```text
ARR = customers × average contract value
```

Example:

| Scenario | Customers | ACV | ARR |
|---|---:|---:|---:|
| Conservative | 500 | €10k | €5M |
| Base | 1,500 | €20k | €30M |
| Upside | 4,000 | €30k | €120M |

The important part is explaining why each customer count and ACV is plausible.

## Segmented model

```text
ARR = Σ(customers_segment × ACV_segment)
```

Use this when SMB, mid-market, and enterprise economics differ materially.

## Usage-based model

```text
Annual revenue
= active customers
× average annual usage per customer
× price per unit
```

Then model cost of revenue separately:

```text
Gross profit
= revenue
- variable model cost
- compute
- other delivery costs
```

## Multi-year recurring-revenue model

A simplified recurring model can track:

```text
Ending ARR
= starting ARR
- churned ARR
- contracted ARR
+ expansion ARR
+ new-logo ARR
```

NRR captures the first four terms for the existing customer base.

## Growth constraints

Do not assume arbitrary exponential customer growth. Check constraints such as:

- sales reps and quota capacity
- enterprise sales-cycle length
- onboarding capacity
- product self-service
- channel reach
- market maturity
- implementation requirements
- geographic expansion

A €100M ARR target is not credible if the GTM motion could only reasonably close 30 enterprise customers per year at €50k ACV.

## ACV expansion

Model why ACV changes over time.

Possible drivers:

- more seats
- additional departments
- more workloads / transactions
- higher usage
- enterprise tier adoption
- additional products
- pricing changes

Do not increase ACV mechanically without an expansion mechanism.

## Scenario assumptions table

For important analyses, use a table like:

| Driver | Conservative | Base | Upside |
|---|---:|---:|---:|
| Reachable accounts | 10k | 20k | 50k |
| Penetration | 2% | 5% | 8% |
| Customers | 200 | 1,000 | 4,000 |
| ACV | €10k | €25k | €40k |
| ARR | €2M | €25M | €160M |
| Gross margin | 65% | 78% | 85% |
| NRR | 100% | 120% | 140% |

Values are illustrative. Replace them with evidence-backed assumptions.

## Sensitivity analysis

Identify the two or three variables with the largest impact.

For example:

```text
Revenue sensitivity:
- customer penetration: very high
- enterprise ACV: high
- SMB price: low
```

Where useful, calculate a matrix such as customer count × ACV so the user can see how outcomes change.

## What-must-be-true analysis

Work backwards from the target.

Example:

```text
Target: €100M ARR
At €50k blended ACV → 2,000 customers
At 80% enterprise mix → ~1,600 enterprise customers
Over 5 years → average net addition of ~320 enterprise customers/year
```

Then ask whether the sales motion, addressable market, and onboarding capacity can support that.

This reverse calculation often reveals implausible forecasts faster than a top-down narrative.

## Valuation scenarios

After revenue scenarios, do not apply one fixed multiple to all cases.

A better model is:

```text
Conservative revenue × conservative multiple
Base revenue × strong-company multiple
Upside revenue × category-leader multiple
```

But only use current, context-appropriate multiple ranges. Explain why each scenario warrants its multiple.