# Market Sizing

## Principle

Prefer a bottom-up estimate grounded in customers and spend. Use top-down market reports as a ceiling or cross-check, not as the main calculation.

## Core equations

```text
TAM = total plausible buyers × plausible annual spend
SAM = reachable buyers × reachable annual spend
SOM = realistically won buyers × expected annual spend
```

For multiple segments:

```text
TAM = Σ(segment buyers × segment ACV)
```

## Step-by-step

1. Define the economic buyer and purchasing unit.
2. Count plausible buyers by segment, geography, or industry.
3. Estimate annual spend based on value, current substitutes, and budget ownership.
4. Remove buyers that cannot realistically use the current product to derive SAM.
5. Apply realistic market-share, GTM-capacity, and adoption constraints to derive obtainable revenue.
6. Cross-check against industry reports and adjacent public-company revenue pools.

## Segmenting examples

### B2B SaaS

```text
20,000 SMB × €3k ACV      = €60M
5,000 mid-market × €20k   = €100M
1,000 enterprise × €100k = €100M
TAM                       = €260M
```

### Usage infrastructure

```text
Customers × annual workloads × price per workload
```

### Marketplace

```text
GMV × take rate = revenue opportunity
```

Do not confuse GMV with company revenue.

## Useful sanity checks

- Does the TAM exceed the total spend of the relevant budget category?
- Is assumed ACV consistent with the value created?
- Is the obtainable customer count feasible for the sales motion?
- If enterprise-heavy, can the company realistically support procurement and implementation?
- If usage-based, is usage expansion assumed or evidenced?

## Avoid the 1% fallacy

Do not say:

```text
Market = €100B
1% share = €1B revenue
```

unless there is a defensible reason the company could reach that share and the market definition corresponds to actual company revenue.

Instead model:

```text
Target accounts
× penetration rate
× ACV
=
plausible revenue
```

## Market evolution

When the category is new, model both current and future TAM. A business can be small today but strategically valuable if the underlying budget category is growing rapidly.

Keep current-state and future-state estimates separate.

For new categories, tie future TAM to explicit adoption or budget-shift assumptions and include them in the assumption register.