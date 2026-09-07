---
name: business-strategy
description: "Develop, evaluate, compare, and continuously update business and product strategy from first principles. Use for startup ideas, business plans, market entry, wedge/beachhead selection, positioning, competitive analysis, economic power and value capture, market structure, customer behavior and culture, future-market scenarios, TAM/SAM/SOM, pricing, go-to-market, monetization, open-source commercialization, unit economics, moats, strategic control points, revenue scenarios, valuation, named strategy frameworks, or when the user wants to determine what a product or company should become. Treat the user's initial concept as a hypothesis, not the strategy."
metadata:
  version: "2.2"
---

# Business Strategy

Use this skill as a **strategy-thinking system**, not a consulting-report checklist.

The objective is to determine:

- what opportunity actually exists;
- where the business should play;
- how it can win;
- how the position becomes an economically attractive business;
- why the advantage can persist;
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

A strategy should resolve real choices about customer, market, product, distribution, business model, capabilities, sequencing, and exclusions. Frameworks are lenses for making those choices, not substitutes for them.

When the user explicitly requests a named framework, apply it explicitly and faithfully using `references/frameworks.md`. When no framework is requested, use the native strategy questions below and invoke framework logic only when it improves the decision.

### 4. Research decision-changing uncertainty

Prioritize claims approximately by:

```text
priority ≈ decision impact × uncertainty × cost of being wrong
```

Research should change confidence, options, or decisions—not maximize source count.

### 5. Generate before converging

For ambiguous strategy work, create materially different alternatives before choosing. Include different customers, buyers, jobs, layers, wedges, channels, business models, monetization models, geographies, and—when useful—different beliefs about how the market will evolve.

### 6. Make the strategy falsifiable

Critical assumptions need evidence, confidence, falsifiers, experiments, and review triggers. A strategy that cannot say what would change it is not finished.

## Modes

Infer the mode from the request; do not force the user to choose.

| Mode | Use when | Emphasis |
|---|---|---|
| `explore` | Opportunity is ambiguous | opportunity space, non-consensus insights, alternative businesses/wedges/models |
| `evaluate` | Business/product is reasonably defined | demand, competition, power, GTM, economics, durability |
| `decide` | Choosing among options | explicit criteria, trade-offs, opportunity cost, recommendation |
| `develop` | Iteratively shaping what the company should become | thesis → evidence → contradiction → revised thesis |
| `review` | Existing strategy meets new evidence | what changed, affected assumptions, reopened decisions |

### Depth

- **Light** — narrow question; answer directly and load only the relevant reference.
- **Standard** — material strategic decision; use the relevant strategy questions below.
- **Deep** — ambiguous, high-stakes, fast-moving, or explicitly comprehensive work; iterate across all material questions and maintain persistent state when possible.

Do not turn a simple revenue or pricing question into a full strategy engagement.

## Persistent Strategy State

For substantive strategy work with a writable workspace, always maintain two durable artifacts:

- `strategy-state.md` — the current source of truth, including thesis, market, evidence, assumptions, alternatives, economics, risks, experiments, and recommendation;
- `decision-log.md` — the history of material strategic choices, thesis mutations, rejected alternatives, and what would reopen them.

If they do not exist, create them from `assets/strategy-state-template.md` and `assets/decision-log-template.md` before substantive analysis. If they exist, read them before re-analyzing.

Update `strategy-state.md` whenever new evidence, assumptions, options, economics, risks, or conclusions materially change. Update `decision-log.md` whenever a material strategic decision is made, reversed, or reopened.

Do **not** create separate evidence-ledger, assumption-register, or wedge-scorecard files. Keep decision-relevant evidence and assumptions compactly inside `strategy-state.md`; compare wedges or alternatives inline when needed and persist only the current alternatives/conclusion.

If no writable workspace exists, maintain the same state conceptually in the conversation.

# Six Fundamental Strategy Questions

These questions are the primary structure of the skill. They are **not a fixed sequence or six mandatory report sections**. Strategy is iterative: evidence from one question can reopen any other question.

For a new deep analysis, start with a provisional thesis, work across the questions that can change the decision, synthesize explicit choices, define falsifiers/tests, and update persistent state.

```text
provisional thesis
      ↕
1. opportunity ↔ 2. where to play ↔ 3. how to win
      ↕                 ↕                 ↕
4. great business ↔ 5. durability ↔ 6. what must be true
      ↓
explicit choices + tests + updated state
```

## 1. What opportunity actually exists?

Establish the reality underneath the proposed business:

- who has the problem or desired outcome;
- economic buyer versus user/beneficiary;
- pain, urgency, frequency, and trigger;
- current workflow and actual alternatives, including do nothing and internal build;
- behavior change, trust, organizational norms, culture, and geography when material;
- why now and what structural change creates the opening;
- market actors, value chain, budgets, profit pools, platforms, standards, and constraints;
- current and plausible future market size when it affects the decision;
- what is fact, inference, assumption, and strategic judgment.

For novel markets, test whether an apparently new category represents real new demand, a shift of an existing budget, or only technical novelty.

Use as relevant:

- `references/decision-framing.md`
- `references/research-protocol.md`
- `references/market-system-mapping.md`
- `references/customer-behavior-and-culture.md`
- `references/competitive-dynamics.md`
- `references/market-sizing.md`

## 2. Where should we play?

Choose the part of the opportunity where the company should concentrate first.

Compare genuine alternatives across:

- customer segment and economic buyer;
- job / use case / workflow;
- geography;
- product layer or place in the value chain;
- channel or ecosystem;
- beachhead market;
- high-touch versus self-serve motion;
- proprietary versus open-source boundary where relevant.

Prefer a coherent beachhead that can be won deeply over an arbitrary small niche or a thin presence in a huge TAM. Ask whether customers share enough pain, workflow, buying criteria, willingness to pay, and distribution for one product/GTM motion to become strongly preferred.

Separate the **first market** from the **long-term destination**.

Use as relevant:

- `references/wedge-selection.md`
- `references/market-system-mapping.md`
- `references/customer-behavior-and-culture.md`
- `references/market-sizing.md`

## 3. How can we win?

Define why customers choose this company and why the position is strategically advantaged.

Test:

- magnitude of customer value versus the best alternative: incremental, meaningful, dramatic, or qualitatively new;
- whether the difference is large enough to change behavior or the comparison set;
- positioning and category frame;
- distribution advantage and route to the buyer;
- beachhead dominance potential;
- capabilities the company must uniquely perform well;
- competitor response, bundling, internal build, and future entrants;
- expansion geometry: why winning the first market makes the next move easier;
- what the company intentionally will **not** do.

For novel or `explore`/`develop` work, test non-consensus hypotheses:

```text
What does the market broadly believe?
What might it be wrong about?
What do we believe instead?
Why might we be right?
If true, what opportunity follows?
What evidence would falsify the belief?
```

Contrarianism is not evidence.

Use as relevant:

- `references/wedge-selection.md`
- `references/positioning-and-category.md`
- `references/competitive-dynamics.md`
- `references/economic-power-and-value-capture.md`

## 4. How does this become a great business?

Treat business model, monetization, market size, and unit economics as part of strategy—not merely downstream calculations.

Explore materially different models when plausible. Ask:

- who pays, for what outcome, and why;
- what pricing metric aligns with value;
- willingness to pay and pricing discretion;
- subscription, usage, transaction, marketplace, services, licensing, OSS/commercial, or hybrid alternatives as relevant;
- whether the monetization model changes the product, buyer, wedge, or distribution motion;
- bottom-up TAM / SAM / realistically obtainable market;
- GTM and distribution economics;
- gross margin and variable-cost exposure;
- retention, expansion, concentration, and revenue quality;
- customer-count × ACV/usage paths and sensitivities;
- capital intensity and implementation burden when material;
- which actors can capture or leak the economic surplus;
- valuation only when it is part of the user's decision.

A monetization model that weakens adoption, power, distribution, or durability can be strategically inferior even if near-term ARPU is higher.

Use as relevant:

- `references/economic-power-and-value-capture.md`
- `references/market-sizing.md`
- `references/revenue-quality-and-unit-economics.md`
- `references/financial-scenario-modeling.md`
- `references/valuation-framework.md`
- `references/open-source-commercialization.md`

Do not jump from a large market number to obtainable revenue or from revenue to valuation.

## 5. Why does the advantage persist?

Test whether today's advantage becomes durable economic power rather than being competed away.

Ask:

- what accumulates with customers, scale, usage, ecosystem, or time;
- what creates switching costs, network effects, economies of scale, trust/brand, proprietary data/context, standards influence, unique distribution, scarce resources, process advantages, or other barriers;
- whether a strategic control point develops;
- what technology or capability is likely to commoditize;
- whether suppliers or platforms can capture the margin;
- whether customers can multi-home or switch easily;
- what incumbents can bundle or copy;
- whether expansion strengthens or dilutes the power mechanism;
- which customer need is invariant even if the current technical implementation disappears.

For fast-moving or novel markets, build plausible future states and run the mature-market / last-mover test:

> If the company succeeds and the market matures, what has commoditized, what has compounded, and why does the company still earn attractive returns?

Use as relevant:

- `references/economic-power-and-value-capture.md`
- `references/moats-and-control-points.md`
- `references/future-market-scenarios.md`
- `references/competitive-dynamics.md`

## 6. What must be true, and what changes our mind?

Turn the strategy into falsifiable beliefs and decisions.

For each critical assumption, keep compactly in `strategy-state.md`:

- importance;
- confidence;
- strongest supporting and contradicting evidence;
- falsifier or tripwire;
- next test;
- review trigger.

Then attack the strategy:

- strongest incumbent response;
- customer non-adoption;
- distribution failure;
- pricing / unit-economic failure;
- supplier or platform dependency;
- commoditization;
- regulatory/cultural friction;
- future-state obsolescence;
- team/capability constraints when relevant.

End with the cheapest evidence-producing actions that test the highest-impact uncertainty.

A review loop is:

```text
what changed
→ which evidence / assumptions are affected
→ which of the six questions should reopen
→ rerun only the affected analysis
→ mutate or reaffirm the thesis
→ update strategy-state + decision-log
```

Use as relevant:

- `references/research-protocol.md`
- `references/strategy-stress-testing.md`
- `references/future-market-scenarios.md`

## Synthesize the Strategy

After working the relevant questions, make the choices explicit:

- strategic ambition / objective;
- customer and economic buyer;
- where to play;
- wedge / beachhead;
- how to win and positioning;
- distribution / GTM;
- business model and monetization;
- expansion sequence;
- required capabilities;
- economic-power / durability mechanism;
- strategic exclusions;
- critical assumptions and tests;
- current recommendation and what would change it.

Do not hide unresolved contradictions behind a polished narrative.

## Named Strategy Frameworks

When the user names a framework, school of strategy, or thinker, read `references/frameworks.md` and apply that lens explicitly.

Rules:

1. **Be faithful to the framework.** Use its canonical logic rather than merely labeling generic analysis with the framework name.
2. **Keep framework and evidence separate.** A framework structures reasoning; it does not prove a market fact.
3. **Integrate the result.** Map framework insights back into the six strategy questions, `strategy-state.md`, and `decision-log.md` when they change the strategy.
4. **Do not create framework soup.** Combine frameworks only when each answers a different material question.
5. **Respect the user's request.** If the user asks specifically for Five Forces, Playing to Win, Zero to One, Wardley Mapping, 7 Powers, etc., show the analysis through that framework rather than silently translating it into another one.
6. **Verify unfamiliar frameworks.** If a requested named framework is not covered in `references/frameworks.md`, research its canonical method before applying it instead of improvising from the name.

## Strategy Mutation Protocol

When evidence materially weakens the current thesis:

1. say so explicitly;
2. identify which assumption broke;
3. generate at least one revised thesis, not merely a lower confidence score;
4. compare the revised and current theses;
5. change the recommendation if warranted;
6. update `strategy-state.md` and `decision-log.md` in persistent work.

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

Persist only decision-relevant evidence in `strategy-state.md`; citations and detailed research can remain in the analysis/output rather than becoming a separate bookkeeping artifact.

## Reference Map

Load references selectively.

### Framework routing

- `references/frameworks.md` — named strategy lenses, canonical logic, when to use them, and how to integrate them

### Process and evidence

- `references/decision-framing.md` — clarify the decision, options, criteria and reversibility
- `references/research-protocol.md` — claim-led research, compact evidence tracking, contradiction handling
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

### Economics and monetization

- `references/market-sizing.md` — bottom-up TAM/SAM/SOM
- `references/revenue-quality-and-unit-economics.md` — margins, retention, NRR, AI/variable costs
- `references/financial-scenario-modeling.md` — revenue paths, sensitivities, what-must-be-true
- `references/valuation-framework.md` — contextual multiples and strategic acquisition value
- `references/open-source-commercialization.md` — OSS adoption, commercial boundary, monetization and GTM

## Recommended Deep Output

Adapt to the decision; do not mechanically output every section.

1. **Decision / recommendation** — what should be done and why
2. **Current thesis and alternatives** — including any thesis mutation
3. **Opportunity reality** — decisive customer, market and competitive evidence
4. **Where to play + how to win** — beachhead, positioning, distribution, value creation, expansion
5. **Business model + economics** — monetization, market size, pricing, GTM, unit economics and scenarios as relevant
6. **Durability** — economic power, accumulating assets, future-market robustness
7. **Risks / assumptions** — what could break the thesis
8. **Experiments / tripwires** — what to learn next and what would change the recommendation
9. **State changes** — for ongoing `develop` / `review` work

## Anti-Patterns

Avoid:

- accepting the user's first idea as fixed;
- treating "no competitors" or a contrarian opinion as evidence of opportunity;
- optimizing for a huge TAM while ignoring the ability to win a coherent beachhead;
- treating any differentiation as economic power;
- feature-matrix-only competitive analysis;
- researching broad topics instead of decision-changing claims;
- name-dropping frameworks without using their actual logic;
- forcing every framework or every strategy question into every answer;
- assuming today's technical architecture or user behavior is permanent;
- copying competitor pricing without value analysis;
- confusing OSS popularity with monetization;
- assuming AI or novelty is itself a moat;
- applying one universal SaaS valuation multiple;
- hiding assumptions inside confident prose;
- producing polished strategy when decisive evidence is missing;
- ending without specifying what would change the recommendation.

The goal is not maximum analytical coverage. It is a better strategic decision with the minimum analysis needed to earn it.