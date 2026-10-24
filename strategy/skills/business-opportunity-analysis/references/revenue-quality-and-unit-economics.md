# Revenue Quality and Unit Economics

## Why revenue quality matters

Revenue is not equally valuable across companies. Two businesses can report the same ARR while having very different gross profit, retention, predictability, and capital needs.

## Core metrics

### Gross margin

```text
Gross margin = (Revenue - cost of revenue) / Revenue
```

For software and AI companies, include the costs required to deliver the service, such as:

- inference / model API spend
- cloud compute
- sandbox or browser infrastructure
- storage and bandwidth
- third-party API costs
- customer-facing operations required for delivery

Do not automatically treat pass-through infrastructure spend as high-margin software revenue.

### Logo retention

Measures how many customers remain customers.

```text
Logo retention = retained customers / starting customers
```

### Net Revenue Retention (NRR)

```text
NRR = (starting recurring revenue - churn - contraction + expansion) / starting recurring revenue
```

NRR above 100% means the existing customer base grows even before new customer acquisition.

Indicative interpretation for B2B recurring software, not universal rules:

```text
<100%      weak expansion / meaningful contraction
100-110%   modest
110-120%   good
120-140%   excellent
140%+      exceptional, if durable
```

Always compare against the company's segment and pricing model.

## Expansion economics

Identify the natural expansion axis:

- more seats
- more workloads
- more agents
- more data
- more business units
- more geographies
- higher-tier features
- additional products

A strong infrastructure product may enter with one team and expand across the organization.

Example:

```text
Year 1: 20 workloads  → €20k ARR
Year 2: 100 workloads → €70k ARR
Year 3: 500 workloads → €220k ARR
```

The importance is not the example numbers; it is whether usage creates a credible expansion mechanism.

## AI-specific economics

AI companies often combine software economics with material variable costs.

Model contribution economics explicitly:

```text
Customer revenue
- model inference
- runtime compute
- storage / network
- third-party tools
- variable support / operations
=
contribution profit
```

Consider whether model costs decline over time and whether savings accrue to the vendor, customer, or competitors through price pressure.

## BYOK economics

If the customer pays model providers directly:

```text
Customer → model provider: inference spend
Customer → company: runtime / software spend
```

This may improve reported gross margin and reduce exposure to model price volatility, but can reduce revenue scale compared with bundling inference.

Always distinguish economic value from accounting optics.

## Customer concentration

A company with €20M ARR where one customer represents €8M has materially different risk from one with hundreds of diversified customers.

Check:

- largest customer share
- top 5 / top 10 share
- renewal timing
- whether large accounts have unusual pricing

## Services burden

High implementation or consulting requirements can reduce scalability.

Ask:

- How long until customer value?
- How many professional-services hours are needed?
- Can partners eventually perform implementation?
- Is customization reusable product work or bespoke work?

## CAC and payback

When data is available:

```text
CAC payback ≈ CAC / monthly gross profit from new customer
```

Shorter payback generally supports faster, less capital-intensive growth.

For developer-led or open-source-led businesses, distinguish community acquisition from enterprise sales cost.

## Revenue-quality checklist

Score qualitatively:

- recurring: low / medium / high
- gross margin: low / medium / high
- retention: weak / good / exceptional
- expansion: weak / good / exceptional
- concentration: high / moderate / diversified
- pricing power: weak / moderate / strong
- variable cost exposure: high / moderate / low
- implementation burden: high / moderate / low
- predictability: low / medium / high

Then explain which dimensions most influence valuation and scalability.