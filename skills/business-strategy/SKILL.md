---
name: business-strategy
description: "Develop, evaluate, compare, and continuously update business and product strategy from first principles. Use for startup ideas, business plans, market entry, wedge/beachhead selection, positioning, competitive analysis, economic power and value capture, market structure, customer behavior and culture, future-market scenarios, TAM/SAM/SOM, pricing, go-to-market, monetization, open-source commercialization, unit economics, moats, strategic control points, revenue scenarios, valuation, or when the user wants to determine what a product or company should become. Treat the user's initial concept as a hypothesis, not the strategy."
metadata:
  version: "2.1"
---

# Business Strategy

Use this skill as a **strategy-thinking system**, not a consulting-report checklist.

The objective is to determine:

- what the business should be;
- where it should play and how it can win;
- why customers will change behavior;
- why the company can capture part of the value it creates;
- what remains durable as the market changes;
- what evidence should cause the strategy to change.

## Core Principles

### 1. The initial idea is a hypothesis

Do not optimize the user's first concept by default. Expose its assumptions, compare genuine alternatives, and mutate the thesis when evidence supports a better formulation.

### 2. Separate value creation, value capture, and durability

Use this as a reasoning model, not a literal equation:

```text
business quality ≈ value creation × value capture × durability
```

A large useful market can still produce a weak business if competition, buyers, suppliers, or platforms capture the surplus. Apparent pricing power without meaningful customer value can be fragile.

### 3. Strategy is a set of choices

Frameworks are lenses, not required sections. Use Jobs to Be Done, Playing to Win, positioning, Five Forces, Wardley mapping, scenario planning, pre-mortems, or other frameworks only when they improve the decision.

### 4. Research decision-changing uncertainty

Prioritize claims approximately by:

```text
priority ≈ decision impact × uncertainty × cost of being wrong
```

Research should change confidence, options, or decisions—not maximize source count.

### 5. Generate before converging

For ambiguous strategy work, create materially different alternatives before choosing. Include different customers, buyers, jobs, layers, wedges, channels, business models, geographies, and—when useful—different beliefs about how the market will evolve.

### 6. Make the strategy falsifiable

Critical assumptions need evidence, confidence, falsifiers, experiments, and review triggers. A strategy that cannot say what would change it is not finished.

## Modes

Infer the mode from the request; do not force the user to choose.

| Mode | Use when | Emphasis |
|---|---|---|
| `explore` | Opportunity is ambiguous | opportunity space, non-consensus insights, alternative wedges |
| `evaluate` | Business/product is reasonably defined | demand, competition, power, GTM, economics, durability |
| `decide` | Choosing among options | explicit criteria, trade-offs, opportunity cost, recommendation |
| `develop` | Iteratively shaping what the company should become | thesis → evidence → contradiction → revised thesis |
| `review` | Existing strategy meets new evidence | what changed, affected assumptions, reopened decisions |

### Depth

- **Light** — narrow question; answer directly and load only the relevant reference.
- **Standard** — material strategic decision; use the relevant phases below.
- **Deep** — ambiguous, high-stakes, fast-moving, or explicitly comprehensive work; use the full loop and persistent artifacts when possible.

Do not turn a simple revenue or pricing question into a full strategy engagement.

## The Strategy Loop

The six phases are a routing model, not mandatory report sections. Skip phases that cannot change the decision.

### Phase 1 — Frame the decision and provisional thesis

Clarify:

- decision, objective, horizon, constraints, reversibility;
- customer/user and economic buyer;
- problem/job and why now;
- proposed product/capability;
- initial wedge and long-term destination;
- business model and provisional way to win;
- highest-risk assumptions.

Mark the thesis **provisional**.

Use `references/decision-framing.md` when the decision or alternatives are ambiguous.

### Phase 2 — Ground the thesis in market reality

Research the claims that could most change the choice.

Understand, as relevant:

- market actors, workflow, budgets, profit pools, platforms, standards and substitutes;
- actual customer behavior, trust, organizational norms, geography and change burden;
- product competitors, capability owners, whole-vision competitors and 12–36 month trajectories;
- internal build, open source and doing nothing.

Do not confuse a feature matrix with competitive analysis.

Use:

- `references/research-protocol.md`
- `references/market-system-mapping.md`
- `references/customer-behavior-and-culture.md`
- `references/competitive-dynamics.md`

### Phase 3 — Design the strategic position

Generate alternatives before convergence.

For novel markets, ask whether the market consensus itself is wrong:

```text
What does the market believe?
What might it be wrong about?
What do we believe instead?
If true, what opportunity follows?
What evidence would falsify this belief?
```

Contrarianism is not evidence.

Then choose the strongest position by testing:

- **wedge / beachhead** — can a coherent initial market be won deeply?
- **magnitude of value** — incremental, meaningful, dramatic, or qualitatively new?
- **distribution** — can the company reach and convert the buyer efficiently?
- **positioning** — does the customer compare the product on the right dimensions?
- **economic power** — why will competition, customers, suppliers, or platforms not erase the surplus?
- **expansion geometry** — does each adjacency become easier and strengthen the strategic position?
- **accumulating assets / control points** — what gets stronger with use, scale, or time?

Use:

- `references/wedge-selection.md`
- `references/positioning-and-category.md`
- `references/economic-power-and-value-capture.md`
- `references/moats-and-control-points.md`

### Phase 4 — Test the future and the economics

For fast-moving or novel markets, build plausible future states instead of pretending to forecast one exact future.

Separate:

- invariant needs;
- structural assumptions;
- transitional opportunities;
- fragile dependencies.

Run the **mature-market / last-mover test** when the long-term position matters:

> If the company succeeds and the market matures, what has commoditized, what has compounded, and why does the company still earn attractive returns?

Then validate only the economics relevant to the decision:

- bottom-up TAM / SAM / obtainable market;
- pricing and GTM;
- revenue scenarios and sensitivities;
- gross margin, retention, expansion and variable costs;
- valuation when requested;
- OSS adoption-to-monetization boundary when applicable.

Use:

- `references/future-market-scenarios.md`
- `references/market-sizing.md`
- `references/revenue-quality-and-unit-economics.md`
- `references/financial-scenario-modeling.md`
- `references/valuation-framework.md`
- `references/open-source-commercialization.md`

Do not jump from a large market number to obtainable revenue or from revenue to valuation.

### Phase 5 — Decide, red-team, and falsify

Synthesize explicit choices:

- ambition / objective;
- where to play;
- how to win;
- wedge / beachhead;
- expansion sequence;
- required capabilities;
- economic-power / moat mechanism;
- business model;
- strategic exclusions.

Then attack the strategy:

- strongest incumbent reaction / bundling;
- customer non-adoption;
- distribution failure;
- pricing or unit-economic failure;
- supplier/platform dependency;
- commoditization;
- regulatory/cultural friction;
- future-state obsolescence;
- team/capability constraints when relevant.

For each critical assumption record confidence, supporting/contradicting evidence, falsifier, next test, and review trigger.

End with the cheapest evidence-producing actions that test the highest-impact uncertainty.

Use `references/strategy-stress-testing.md` plus the assumption/evidence templates for deep work.

### Phase 6 — Persist and review

For deep `develop` or `review` work, maintain a living strategy state when a writable workspace exists:

- `strategy-state.md`
- `evidence-ledger.md`
- `assumption-register.md`
- `decision-log.md`
- `wedge-scorecard.md` when alternatives matter

Use the templates in `assets/`.

When prior state exists, read it before re-analyzing from scratch.

A review loop is:

```text
what changed
→ which assumptions are affected
→ which decisions should reopen
→ rerun only the affected modules
→ mutate or reaffirm the thesis
→ update state + decision log
```

Every material strategy change should record the old belief, new choice, reason/evidence, rejected alternatives, and what would reopen the decision.

## Strategy Mutation Protocol

When evidence materially weakens the current thesis:

1. say so explicitly;
2. identify which assumption broke;
3. generate at least one revised thesis, not merely a lower confidence score;
4. compare the revised and current theses;
5. change the recommendation if warranted;
6. update the decision log in persistent work.

Do not defend the initial concept for conversational consistency.

## Evidence Discipline

Always distinguish:

- **Fact** — directly supported by evidence
- **Derived calculation** — computed from stated inputs
- **Inference** — conclusion drawn from evidence
- **Assumption** — unverified belief required by the thesis
- **Strategic judgment** — recommendation under uncertainty

Prefer primary sources where possible and match source type to claim type. Actively search for counter-evidence. Multiple pages repeating one origin are not independent confirmation.

When evidence conflicts, examine definition, geography, time period, methodology, accounting basis, incentives, and source independence rather than averaging automatically.

## Reference Map

Load references selectively.

### Process and evidence

- `references/decision-framing.md` — clarify the decision, options, criteria and reversibility
- `references/research-protocol.md` — claim-led research, evidence ledger, contradiction handling
- `references/strategy-stress-testing.md` — pre-mortem, failure mechanisms, coherence and verdict

### Market reality

- `references/market-system-mapping.md` — actors, value chain, budgets, profit pools, bottlenecks
- `references/customer-behavior-and-culture.md` — workflow, trust, behavior change, organizational/geographic context
- `references/competitive-dynamics.md` — three competition levels, trajectories, bundling, internal build/OSS

### Strategic position and power

- `references/wedge-selection.md` — beachhead, dominance potential, non-comparability, expansion geometry
- `references/positioning-and-category.md` — comparison set, category, magnitude of advantage, exclusions
- `references/economic-power-and-value-capture.md` — value creation vs capture, bargaining power, pricing/cost power
- `references/moats-and-control-points.md` — accumulating assets, control points, durability, commoditization
- `references/future-market-scenarios.md` — future states, invariant/fragile assumptions, last-mover test

### Economics

- `references/market-sizing.md` — bottom-up TAM/SAM/SOM
- `references/revenue-quality-and-unit-economics.md` — margins, retention, NRR, AI/variable costs
- `references/financial-scenario-modeling.md` — revenue paths, sensitivities, what-must-be-true
- `references/valuation-framework.md` — contextual multiples and strategic acquisition value

### Specialized business model

- `references/open-source-commercialization.md` — OSS adoption, commercial boundary, monetization and GTM

## Recommended Deep Output

Adapt to the decision; do not mechanically output every section.

1. **Decision / recommendation** — what should be done and why
2. **Current thesis and alternatives** — including any thesis mutation
3. **Market reality** — decisive customer, market and competitive evidence
4. **Strategic position** — beachhead, positioning, value creation, economic power, expansion
5. **Future + economics** — durability and financial implications as relevant
6. **Risks / assumptions** — what could break the thesis
7. **Experiments / tripwires** — what to learn next and what would change the recommendation
8. **State changes** — for ongoing `develop` / `review` work

## Anti-Patterns

Avoid:

- accepting the user's first idea as fixed;
- treating "no competitors" or a contrarian opinion as evidence of opportunity;
- optimizing for a huge TAM while ignoring the ability to win a coherent beachhead;
- treating any differentiation as economic power;
- feature-matrix-only competitive analysis;
- researching broad topics instead of decision-changing claims;
- listing frameworks instead of making choices;
- assuming today's technical architecture or user behavior is permanent;
- copying competitor pricing without value analysis;
- confusing OSS popularity with monetization;
- assuming AI or novelty is itself a moat;
- applying one universal SaaS valuation multiple;
- hiding assumptions inside confident prose;
- producing polished strategy when decisive evidence is missing;
- ending without specifying what would change the recommendation.

The goal is not maximum analytical coverage. It is a better strategic decision with the minimum analysis needed to earn it.