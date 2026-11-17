# Experiments and Product-Market Fit

## Purpose

An experiment buys information. It is justified when the information could change a decision and the cost is lower than the cost of being wrong.

This reference covers test design, precommitted decision bars, evidence grading, and how to read product-market fit and retention signals. Use [idea validation](idea-validation.md) for premise-level triage and the assumption ledger, and [strategy stress testing](strategy-stress-testing.md) for adversarial review of the thesis.

## From assumption to test

Work down this ladder until the test is cheap enough and strong enough for the decision.

| Rung | Method | Produces | Typical limit |
|---|---|---|---|
| 1 | Existing evidence — analytics, support, sales records, prior attempts | Observed behavior at scale | Not specific to the new offer |
| 2 | Behavioral interviews | Current workaround, trigger, cost | Stated, not purchased |
| 3 | Artifact test — prototype, sample output, mockup | Comprehension and reaction | No commitment |
| 4 | Manual delivery — concierge, service, internal tool | Whether the outcome is valuable | Not scalable |
| 5 | Priced pilot or deposit | Economic commitment | Small n, selection bias |
| 6 | Live experiment — A/B, staged rollout, price test | Causal effect in a population | Needs volume and clean design |
| 7 | Scaling test — more segments, channels, geographies | Repeatability | Expensive, confounded |

Choose the lowest rung that can produce a decision-grade answer. Moving up costs money and time; moving down risks learning something that does not transfer.

### Test specification

Every test states:

```text
Assumption tested:
Decision it informs:
Hypothesis:
Population and eligibility:
Treatment and control (if any):
Primary metric and definition:
Baseline and source:
Pass / partial / fail thresholds:
Observation window:
Sample or power consideration:
Known confounds and how they are handled:
Cost and owner:
Result and interpretation:
Decision taken:
```

If the pass/fail thresholds are missing, the test will be interpreted after the fact.

## Precommitted bars

A precommitted bar is what makes an experiment falsifiable.

Define three outcomes before running:

- **Pass** — evidence supports the assumption at the stated strength; proceed to the next assumption or stage.
- **Partial** — direction is right but magnitude, segment or mechanism is uncertain; the next test is specified.
- **Fail** — the assumption is not supported within the window; the decision is reconsidered, not deferred by default.

Rules:

- **Thresholds are set from the decision, not from what feels achievable.** "Ten paying customers" is meaningful only if ten implies the economics or learning the next step requires.
- **Record changes to the bar.** If the threshold moves after seeing data, log the change, the reason and who approved it. Unexplained movement is goalpost shifting.
- **Do not run a test whose result cannot change anything.** Confirmation has a cost.
- **Avoid multiple comparisons without adjustment.** Testing many variants and reporting the best one produces false confidence.
- **Respect sample limits.** With small samples, report the observation and its uncertainty instead of a precise conversion rate.
- **Distinguish statistical from practical significance.** A measurable difference that is too small to change the business is not a pass.

### Choosing a threshold

Use one of:

- an economic threshold — the level at which unit economics or payback work;
- a strategic threshold — the level at which the next commitment is justified;
- a comparative threshold — a stated improvement over baseline or the alternative;
- a learning threshold — the evidence needed to choose between named options.

Do not set a threshold by benchmarking a competitor whose segment, price and motion differ.

## Evidence grades

Grade evidence so a recommendation cannot borrow certainty it does not have.

| Grade | Description | Example |
|---|---|---|
| A | Direct, repeated behavior at meaningful scale, independently observed | Cohort retention across multiple periods |
| B | Direct behavior in a small or selected population | Paid pilot with five customers |
| C | Stated preference, expert judgment or one observed case | Interview consensus, single reference |
| D | Inference, analogy or model output | Market analogy, extrapolated usage |

Rules:

- State the grade next to the claim it supports.
- Do not upgrade a grade because several people repeated the same opinion; that is one evidence origin.
- Grade the claim, not the confidence of the person making it.
- A critical decision on grade C or D evidence is allowed, but must be named as a bet with a test and a tripwire.
- Keep contrary evidence at the same grade as supporting evidence.

## Product-market fit

Product-market fit is not a single number. It is a pattern of behavior suggesting the product has become the customer's preferred way to make progress, and that the company can reach and retain them.

Signals that carry weight:

- **Retention** — cohorts flatten rather than decay to zero.
- **Organic pull** — new users arrive without proportional acquisition spend.
- **Usage depth** — the product becomes part of a recurring workflow, not an occasional tool.
- **Willingness to pay and expand** — price resistance falls, expansion appears without heavy selling.
- **Word of mouth** — customers refer comparable customers without incentive.
- **Complaint quality** — complaints shift from "this does not work" to "this is missing for my job", a sign of adoption.

Signals that carry less weight than commonly assumed:

- satisfaction scores and NPS;
- waitlist size and launch attention;
- a single cohort's early usage;
- founder-led sales success;
- a survey question about disappointment if the product disappeared (the Sean Ellis test). The often-cited 40% threshold from that survey is a heuristic from a particular sample, not a law; use it as one input with the segment and method stated.

PMF is segment-specific. A product can have fit with early adopters and none with the mainstream buyer it needs for the strategy. State which segment the evidence covers.

## Reading retention

Retention is the strongest single behavioral signal, and the easiest to misread.

Check:

- **Cohort shape** — flattening is better than a high initial number that decays.
- **Definition** — what counts as active, and whether the action reflects value or habit.
- **Mix** — a blended curve can improve while every segment worsens, or the reverse.
- **Survivorship** — churned customers often leave the data entirely.
- **Seasonality and lifecycle** — usage tied to a quarterly process looks like churn monthly.
- **Expansion vs retention** — revenue retention can hide logo churn.
- **Small samples** — a few accounts can dominate a percentage.

Useful cuts:

- by acquisition channel and segment;
- by activation behavior in the first period;
- by use case or job;
- by buyer type;
- by cohort age.

If retention is weak, diagnose before adding acquisition: more users into a leaking product produces a larger leak.

## Pivot or persevere

Pivot decisions are strategic, not emotional. Distinguish:

| Change | What changes | Typical trigger |
|---|---|---|
| Persevere | Nothing material; continue the plan | Evidence supports the thesis; next assumption is the binding one |
| Narrow | Segment, use case or geography | Fit exists in a subset, not the target |
| Repackage | Price, packaging, motion | Value exists but the commercial model is wrong |
| Pivot | Problem, customer, solution, channel or model | Core assumption failed; adjacent evidence points elsewhere |
| Park or stop | The bet no longer justifies its cost | Premise failed, economics impossible, window closed |

A pivot should preserve what was learned. State:

- what evidence caused the change;
- which assumption failed and which survived;
- what is being kept — customers, capability, data, distribution, team;
- what is being abandoned and the cost of abandoning it;
- the new thesis and its first test;
- why this is not simply a rebrand of the same failing plan.

Perseverance is legitimate when the evidence is early but directionally supportive and the next test is cheap. It is not legitimate when the only argument is prior investment.

## Avoiding fake certainty

- Do not report a point estimate where the data supports only a range.
- Do not describe a pilot as a market result.
- Do not use statistical language for a convenience sample.
- Do not imply causality from a before-and-after comparison without a control or a plausible mechanism.
- Do not hide a failed primary metric behind a successful secondary one.
- Do not treat absence of evidence as evidence of absence when the test could not detect the effect.
- Do not let a model output stand in for observed behavior.
- Do not present a plan to test as if the test ran.

## Completion evidence

An experiment program is complete enough to decide when:

- each test maps to a named assumption and decision;
- thresholds and windows were set before the result;
- results are reported with population, method, grade and limits;
- failed and partial results remain visible;
- the decision — persevere, narrow, repackage, pivot, park or stop — is stated with its evidence;
- the next test is the cheapest one that could change the next decision;
- the state and decision log reflect what changed.

The goal is not more experiments. It is a decision that is cheaper to defend because the evidence was designed for it.

Starting structure: [`assets/bet-record.md`](../assets/bet-record.md). Adapt or omit sections; do not fill it with invented evidence.
