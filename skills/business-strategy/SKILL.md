---
name: business-strategy
description: "Develop, evaluate, compare, and continuously update business and product strategy from first principles. Use for startup ideas, business plans, market entry, wedge selection, positioning, competitive analysis, market structure, customer behavior and culture, future-market scenarios, TAM/SAM/SOM, pricing, go-to-market, monetization, open-source commercialization, unit economics, moats, strategic control points, revenue scenarios, valuation, or when the user wants to determine what a product or company should become. Treat the user's initial concept as a hypothesis, not the strategy."
metadata:
  version: "2.0"
---

# Business Strategy

Use this skill as a reusable strategy-thinking system, not a report template.

The objective is to help determine **what the business should be, where it should play, how it can win, what must be true, and what evidence should cause the strategy to change**.

## Core Mandate

Do **not** treat the user's initial product or business concept as the strategy.

Treat it as the first hypothesis in a search process:

```text
initial thesis
  → expose assumptions
  → research decision-changing claims
  → map the market system
  → generate alternatives
  → choose a wedge and strategy
  → stress-test against competitors and future markets
  → validate economics
  → define falsifiers and experiments
  → update the thesis as evidence changes
```

A strong analysis may conclude that the original idea is good, but it must earn that conclusion. If evidence points toward a materially better formulation, **mutate the thesis explicitly** and record why.

## Modes

Infer the mode from the request. Do not force the user to select one.

| Mode | Use when | Primary emphasis |
|---|---|---|
| `explore` | The opportunity is still ambiguous | problem spaces, market structure, alternative concepts, wedges |
| `evaluate` | The user has a reasonably defined business | demand, competition, TAM, GTM, economics, defensibility |
| `decide` | The user is choosing among options | explicit criteria, trade-offs, opportunity cost, recommendation |
| `develop` | The user wants to iteratively shape what the company/product should become | hypothesis → research → contradiction → revised thesis loops |
| `review` | A strategy already exists and new information has arrived | what changed, which assumptions moved, whether strategy should change |

### Depth

Adapt depth to the decision rather than mechanically running the full workflow.

- **Light** — narrow question; answer directly using only relevant steps.
- **Standard** — material strategic decision; use a structured subset of the workflow.
- **Deep** — ambiguous, high-stakes, fast-moving, or explicitly comprehensive strategy work; use the full loop and persistent artifacts when possible.

A revenue-potential question should not trigger a 15-stage strategy engagement. A novel market or company-formation question usually should.

## State and Continuity

For deep `develop` or `review` work, maintain a current strategy state.

If a writable workspace exists, create or update:

- `strategy-state.md`
- `evidence-ledger.md`
- `assumption-register.md`
- `decision-log.md`
- `wedge-scorecard.md` when multiple wedges matter

Use the templates in `assets/`.

If no writable workspace exists, maintain the same information in the conversation and summarize the current state at meaningful checkpoints.

When a prior strategy state exists, **read it before re-analyzing from scratch**. Review should begin with: what changed, which assumptions are affected, and whether any prior decision should be reopened.

## Strategy Workflow

### 0. Frame the decision

State the actual decision being made, the time horizon, scope, constraints, and what success means.

Distinguish questions such as:

- Is this opportunity attractive?
- Which customer or geography should we enter first?
- Which wedge best opens the broader platform?
- Should we build, buy, partner, or not enter?
- What should this product become as the market evolves?

Read `references/decision-framing.md` when the decision is ambiguous or alternatives matter.

### 1. State the current thesis

Before researching deeply, write a provisional thesis in concrete terms:

- target user and economic buyer
- job/problem
- proposed product or capability
- initial wedge
- long-term destination
- why now
- how it wins
- business model
- most important assumptions

Mark it **provisional**. Do not disguise guesses as conclusions.

### 2. Surface assumptions and research claims

Identify assumptions that could materially change the decision.

Prioritize research using:

```text
research priority ≈ decision impact × uncertainty
```

Turn the highest-priority assumptions into explicit claims to test. Use stable IDs for deep work.

Read `references/research-protocol.md` for claim-led research, evidence handling, contradiction rules, and stop conditions.

### 3. Map the market as a system

Do more than list competitors.

Map:

- users, buyers, beneficiaries, and blockers
- value chain and workflow
- budget owners and profit pools
- platforms, complements, channels, and standards
- direct substitutes, internal build, and "do nothing"
- bottlenecks and control points
- which layers are differentiating versus commoditizing
- likely market evolution

Read `references/market-system-mapping.md` when market structure affects the strategy.

### 4. Understand behavior and culture

When adoption depends on people changing behavior, team practices, trust, delegation, status, workflow, or geography, analyze those factors explicitly.

Ask:

> Does the wedge fit an existing behavior, or does it require creating a new behavior?

Consider current workflow, trigger events, trust, loss of control, social and organizational norms, procurement behavior, developer culture, geographic differences, and change-management burden.

Read `references/customer-behavior-and-culture.md`.

### 5. Analyze competition at three levels

Always include alternatives and internal build where relevant.

For strategic markets, distinguish:

1. **Product competitors** — who sells the same outcome today?
2. **Capability competitors** — who owns pieces of the envisioned stack or workflow?
3. **Whole-vision competitors** — who could combine existing assets and make the company unnecessary?

Then evaluate competitor **trajectory**, not just today's feature list:

> What can this competitor plausibly bundle or launch in 12–36 months given the assets it already controls?

Read `references/competitive-dynamics.md`.

### 6. Generate strategic alternatives before converging

Do not optimize only the user's first idea.

Generate genuinely different alternatives such as:

- different customer segment
- different buyer
- narrower wedge
- broader problem definition
- different product layer
- different business model
- different distribution channel
- open-source versus proprietary boundary
- application versus platform versus infrastructure/control plane
- geographic beachhead

Include the status quo / do-not-enter option when it is a real choice.

### 7. Select the wedge

For each credible wedge, evaluate:

- pain intensity and urgency
- trigger clarity
- time-to-value
- adoption friction
- buyer and budget clarity
- distribution advantage
- competitive density
- incumbent/bundling risk
- asset accumulation
- expansion surface
- path to a strategic control point
- economics
- future resilience

Use scores to expose trade-offs, not to outsource judgment to arithmetic.

Read `references/wedge-selection.md` and use `assets/wedge-scorecard-template.md` for deep comparisons.

### 8. Position the product and category

Clarify:

- competitive alternatives in the customer's mind
- unique capabilities
- value those capabilities create
- best-fit customers
- category or frame that makes the value obvious
- what the company deliberately will **not** be

Read `references/positioning-and-category.md` when category framing or differentiation is material.

### 9. Stress-test against future market states

For novel or fast-moving markets, this step is mandatory.

Build a small set of plausible futures rather than one forecast:

- current/base continuation
- likely structural evolution
- meaningful alternative
- extreme but decision-relevant scenario

Classify important assumptions as:

- **invariant** — likely valuable across futures
- **structural** — likely durable for years
- **transitional** — useful during this market phase
- **fragile** — depends heavily on today's architecture or behavior

Prefer strategies whose value rests on invariants and structural needs rather than fragile implementation details.

Read `references/future-market-scenarios.md`.

### 10. Choose where to play and how to win

Synthesize the strategy as explicit choices:

- ambition / objective
- where to play
- how to win
- initial wedge
- sequence of expansion
- capabilities required
- control point / accumulating asset
- business model
- strategic exclusions

Frameworks such as Jobs to Be Done, Playing to Win, positioning frameworks, Five Forces, Wardley mapping, scenario planning, and pre-mortems are **lenses**, not mandatory sections. Use only the ones that improve the decision.

### 11. Validate the business economics

Only run the modules relevant to the question.

Use:

- `references/market-sizing.md` — bottom-up TAM/SAM/SOM
- `references/open-source-commercialization.md` — OSS adoption and monetization boundary
- `references/revenue-quality-and-unit-economics.md` — margins, retention, NRR, variable costs
- `references/financial-scenario-modeling.md` — conservative/base/upside paths and sensitivities
- `references/valuation-framework.md` — valuation and strategic acquisition value

Do not jump from a large market number to obtainable revenue, or from revenue to valuation.

### 12. Test defensibility and control

Ask both:

- Why is this hard to copy or displace?
- If this becomes the default layer, what valuable downstream activity passes through it?

Distinguish a temporary feature advantage from durable power, ecosystem position, switching costs, data advantage, distribution, standards, scale, workflow lock-in, or operational complexity customers do not want to own.

Read `references/moats-and-control-points.md`.

### 13. Red-team the strategy

Before recommending the strategy, attack it.

Test:

- strongest incumbent response
- bundling and platform risk
- customer non-adoption
- distribution failure
- unit-economics failure
- dependency risk
- regulatory or cultural friction
- commoditization
- future-state obsolescence
- founder/team capability constraints when relevant

Read `references/strategy-stress-testing.md`.

### 14. Make assumptions falsifiable

For every critical assumption, record:

- assumption
- type
- importance
- current confidence
- supporting and contradicting evidence
- falsifier / tripwire
- next test
- review trigger

Avoid vague statements such as "enterprises will probably want this." Define what evidence would make that belief stronger or weaker.

### 15. Define experiments and monitoring

End strategy formation with the next evidence-producing actions, not merely a document.

Prioritize experiments that cheaply test high-impact uncertainties:

- customer interviews
- landing-page or demand tests
- concierge/manual delivery
- design-partner commitments
- pricing tests
- prototype usage
- channel experiments
- OSS adoption/conversion metrics
- procurement/security discovery

For evolving markets, define external signals to monitor and the decision they would reopen.

### 16. Persist strategy changes

For deep work, update the state artifacts.

Every material strategy change should record:

- old belief / option
- new choice
- evidence or reasoning that changed it
- rejected alternatives
- what evidence would reopen the decision

This prevents long brainstorming sessions from losing accumulated strategic knowledge.

## Strategy Mutation Protocol

When new evidence materially weakens the current thesis:

1. Say so explicitly.
2. Identify which assumption broke.
3. Generate at least one revised thesis rather than merely lowering confidence.
4. Compare the revised thesis with the current one.
5. Update the decision log if the strategy changes.

Do not defend the initial concept for conversational consistency.

## Evidence Rules

When current or external data matters, research it.

Prefer primary sources where possible and match source type to claim type. For deep research, maintain an evidence ledger.

Always distinguish:

- **Fact** — directly supported by a source
- **Derived calculation** — computed from stated inputs
- **Inference** — conclusion drawn from evidence
- **Assumption** — unverified belief required by the thesis
- **Strategic judgment** — recommendation or choice under uncertainty

Actively look for counter-evidence. Multiple pages repeating one original source are not independent corroboration.

Do not force contradictory evidence into a single number; explain differences in definition, geography, time period, methodology, or incentives.

## Recommended Output for Deep Strategy Work

Adapt to the question, but a strong final synthesis often contains:

1. **Executive decision** — recommendation and why
2. **Current thesis** — what the business should be
3. **What changed** — especially in `develop` or `review` mode
4. **Market system** — customers, layers, profit pools, substitutes
5. **Customer behavior and culture** — adoption realities
6. **Competitive dynamics** — current and future
7. **Strategic alternatives** — including rejected options
8. **Wedge and sequencing** — entry → expansion → control point
9. **Positioning** — category, differentiation, exclusions
10. **Future-state robustness** — what survives market evolution
11. **Economics** — market size, pricing, GTM, scenarios, unit economics as relevant
12. **Moat / control point** — why value can be captured
13. **Risks and red-team** — what could break the thesis
14. **Critical assumptions** — confidence and falsifiers
15. **Experiments and tripwires** — what to learn next

## Anti-Patterns

Avoid:

- accepting the user's first idea as fixed
- feature-matrix-only competitive analysis
- researching topics without decision-changing claims
- listing frameworks instead of making choices
- "the market is €100B, so 1% is €1B"
- treating today's market architecture as permanent
- assuming cultural adoption is the same across workflows or geographies
- copying competitor pricing without value analysis
- confusing popularity with monetization in open source
- assuming AI or novelty is itself a moat
- applying one universal SaaS valuation multiple
- hiding assumptions inside confident prose
- producing a polished strategy when critical evidence is missing
- ending without specifying what would change the recommendation

## Reference Routing

Load references selectively and only when they are relevant:

- `references/decision-framing.md`
- `references/research-protocol.md`
- `references/market-system-mapping.md`
- `references/customer-behavior-and-culture.md`
- `references/competitive-dynamics.md`
- `references/wedge-selection.md`
- `references/positioning-and-category.md`
- `references/future-market-scenarios.md`
- `references/moats-and-control-points.md`
- `references/strategy-stress-testing.md`
- `references/market-sizing.md`
- `references/open-source-commercialization.md`
- `references/revenue-quality-and-unit-economics.md`
- `references/financial-scenario-modeling.md`
- `references/valuation-framework.md`

Do not load every reference by default. Progressive disclosure is part of the design.