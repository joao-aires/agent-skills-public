# Capital and Finance

## Purpose

Capital is a strategic constraint. The amount, timing and terms of financing determine what the company can attempt, how long it can learn and who controls the outcome.

Use this reference for fundraising readiness, round sizing, instruments, investor process and financial-model sanity. Use [financial scenario modeling](financial-scenario-modeling.md) for revenue and cost paths, [revenue quality and unit economics](revenue-quality-and-unit-economics.md) for the metrics investors evaluate, and [valuation framework](valuation-framework.md) for valuation logic.

## Readiness before fundraising

Investors buy evidence of a future, not effort. Readiness is stage-specific, but the common core is:

- a credible market and a coherent wedge;
- evidence that the customer problem is real and worth paying for;
- a repeatable or plausibly repeatable route to the customer;
- unit economics that improve with scale, or a clear path to them;
- a team whose capability matches the plan;
- a use of funds tied to specific milestones;
- honest knowledge of what is not yet proven.

Do not raise to avoid deciding. A round bought without a plan buys time and dilution, not clarity.

### Milestone logic

State what the round is meant to prove:

```text
Current evidence:
Milestone this round buys:
Evidence that milestone produces:
Next round's likely requirements:
Time and cost to reach it:
```

The milestone should be the one that most changes the company's risk profile — retention, a repeatable channel, a technical proof, a regulatory approval — not simply revenue growth.

## Size the round from the cash model

Work bottom-up.

```text
Required cash
= operating plan cost to the milestone
+ working capital and payment timing
+ contingency for delay and surprise
− expected receipts
```

Then check:

- **Hiring plan** — roles, start dates, ramp time, fully loaded cost.
- **Go-to-market** — sales capacity, marketing programs, partner costs, support.
- **Product and infrastructure** — engineering, compute, inference, tooling.
- **Compliance and operations** — legal, audit, security, insurance, facilities.
- **Contingency** — a stated buffer, not a hidden margin.

Convert to runway in months and to dilution at the expected price. If you have twelve months of runway and the raise takes nine months to close, you have three months left at close; the round must fund from that point, not from today.

Common sizing errors:

- sizing to a headline rather than to the plan;
- omitting hiring ramp and severance risk;
- assuming revenue that the sales capacity cannot produce;
- ignoring working capital in usage-based or enterprise businesses;
- funding the plan but not the next fundraise's evidence;
- raising more than the milestone can absorb productively, which creates pressure to spend.

## Instruments

### Safe

A simple agreement for future equity converts into equity at a later priced round, usually with a valuation cap and sometimes a discount.

Use when speed and low legal cost matter, and the amount is modest relative to the eventual round.

Consider:

- the cap sets an effective price and can create a difficult conversion if the next round is lower;
- multiple safes with different caps create a stack that must be reconciled;
- pro rata rights, most-favored-nation clauses and side letters add complexity;
- the instrument is not standardized across jurisdictions; the actual document governs.

### Priced round

A priced equity round sets a valuation, share price and terms: liquidation preference, participation, anti-dilution, board composition, protective provisions, vesting and information rights.

Use when:

- the amount is material;
- a lead investor is setting terms and governance;
- the company wants a clean cap table and a priced reference for employees and later investors.

Consider:

- preference and participation affect founder and employee outcomes more than the headline valuation;
- governance terms can constrain future financing or acquisitions;
- the round's terms should be compared on economic and control effects, not valuation alone.

### Convertible notes and other instruments

Notes add maturity and interest, which can create pressure if the next round is delayed. Revenue-based financing and venture debt trade future cash for non-dilutive capital and usually require a predictable revenue base and covenants.

Match the instrument to the risk and the timeline. A bridge should be sized to reach a specific milestone, not to postpone a decision indefinitely.

## Investor pipeline

Treat fundraising as a pipeline with stages, conversion and timing.

| Stage | Evidence | Typical failure |
|---|---|---|
| Target list | Thesis fit, stage, sector, check size, geography | Generic list with no partner-level fit |
| Warm introduction | Mutual contact, portfolio founder, operator | Cold outreach at seed and later stages |
| First meeting | Clear narrative, traction, ask | Long pitch without a decision question |
| Deep dive | Data, model, references, customer calls | Unprepared data or inconsistent numbers |
| Partner meeting | Conviction, terms discussion | No internal champion |
| Term sheet | Valuation, terms, governance | Terms discovered late |
| Close | Legal, wiring, announcements | Timeline slip and re-trading |

Pipeline rules:

- Research the investor's actual thesis, portfolio and stage; do not pitch a consumer fund on infrastructure.
- Create competition without manufacturing urgency. A genuine parallel process is credible; an invented deadline is not.
- Track conversion and cycle time by stage, and fix the weakest stage rather than adding more top-of-funnel.
- Prepare for diligence before the first meeting: metrics definitions, cohort data, contracts, cap table.
- Decide in advance which terms are acceptable and which are not.
- Keep a single source of truth for metrics. Inconsistent numbers across conversations end processes.

## Monthly updates

A short, consistent update builds trust and reduces diligence friction.

```text
Subject: [Company] — [Month] update

1. Headline: what changed and what it means
2. Metrics: revenue, growth, retention, pipeline, cash, runway — same definitions each month
3. Product and customer: one meaningful learning, not a feature list
4. Team: hires, departures, key open roles
5. Risks and misses: what did not go to plan and why
6. Asks: specific introductions, hiring, customer access
7. Next month's focus
```

Rules:

- Send on a predictable cadence, including in bad months.
- Do not change metric definitions without saying so and restating prior periods.
- State misses plainly; investors discover them anyway and the delay costs credibility.
- Keep asks concrete enough to act on.
- Do not use the update as a fundraising pitch until you are fundraising.

## Data room

Maintain a current, organized data room before it is requested.

| Section | Typical contents |
|---|---|
| Corporate | Incorporation, cap table, shareholder agreements, board minutes |
| Financials | Historical statements, current model, budget versus actual, bank statements |
| Metrics | Cohort and retention data, pipeline, definitions and source |
| Product and technology | Architecture overview, security posture, key contracts, IP assignment |
| Customers | Contracts, pipeline, references, churn analysis |
| People | Org chart, key employment agreements, option plan, contractors |
| Legal and compliance | Material contracts, litigation, regulatory status, insurance |
| Fundraising | Deck, memo, round terms, use of funds |

The data room is evidence, not marketing. Accuracy and consistency with the model matter more than volume.

## Financial-model sanity

A model is a set of arguments, not a forecast.

Check:

- **Revenue build** — customers × ACV, or usage × price, tied to actual sales capacity and funnel conversion.
- **Growth constraints** — hiring, onboarding, implementation, market maturity.
- **Gross margin** — including infrastructure, inference, support and third-party costs.
- **Retention and expansion** — cohort-based, with churn and contraction visible.
- **Cost structure** — fully loaded headcount, programs, tools, facilities, compliance.
- **Cash timing** — collections, payment terms, prepayments, seasonality.
- **Runway** — cash, burn, and the month the next raise must close, not the month cash reaches zero.
- **Sensitivity** — the two or three variables that most change the outcome.
- **Scenario logic** — down case tied to a strategic failure, not only modest underperformance.

Red flags:

- revenue that grows faster than any plausible acquisition capacity;
- gross margin that excludes a material variable cost;
- retention assumptions that improve without a mechanism;
- a hiring plan with no ramp time;
- a model with no down case;
- a valuation that assumes a multiple rather than a business.

Use [financial scenario modeling](financial-scenario-modeling.md) for the structure and [valuation framework](valuation-framework.md) for how quality and growth affect value.

## Founder economics

Company value is not founder wealth. Keep separate:

- dilution from each round and instrument;
- option pool and vesting;
- liquidation preferences and participation;
- taxes and jurisdiction;
- secondary sales and their terms.

Model the founder outcome at a realistic exit range, not only at the headline valuation. A high valuation with heavy preference can produce a worse founder outcome than a lower valuation with cleaner terms.

## Failure modes

- Raising without a milestone.
- Sizing the round to a headline instead of the plan.
- Treating a safe as free of governance or economic consequences.
- Discovering terms during legal instead of before the term sheet.
- A pipeline that is a list of names rather than a process.
- Metrics that change between conversations.
- Updates that appear only when there is good news.
- A data room assembled during diligence.
- A model that cannot be reconciled to the bank account.
- Confusing valuation with liquidity.

## Output

End with:

- the capital need and the milestone it buys;
- the instrument and its economic and control implications;
- the investor pipeline and the next actions;
- the data room and metrics readiness;
- the model's key assumptions and sensitivities;
- the runway and the date by which the next raise must close;
- the main risks and what would change the plan.

The useful result is capital that funds a specific proof, on terms the company can live with.

Starting structure: [`assets/capital-plan.md`](../assets/capital-plan.md). Adapt or omit sections; do not fill it with invented evidence.
