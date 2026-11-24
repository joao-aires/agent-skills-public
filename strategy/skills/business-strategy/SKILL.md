---
name: business-strategy
description: Develop, evaluate, compare, and continuously update business and product
  strategy from first principles. Use for startup ideas, business plans, market entry,
  wedge/beachhead selection, positioning, competitive analysis, economic power and
  value capture, market structure, customer behavior and culture, future-market scenarios,
  TAM/SAM/SOM, pricing, go-to-market, monetization, open-source commercialization,
  unit economics, moats, strategic control points, revenue scenarios, valuation, named
  strategy frameworks, or when the user wants to determine what a product or company
  should become. Treat the user's initial concept as a hypothesis, not the strategy.
metadata:
  kind: activity
  domain: product
  phase: planning
  version: '2.5'
  scope: generic
  invocation: user
  references: ../../references/sources.md
---

# Business Strategy

Determine the business's opportunity, playing field, advantage and value capture, and stop at an accepted strategy brief or decision. This is a **strategy-thinking system**, not a consulting-report checklist.

The objective is to determine:

- what opportunity actually exists;
- where the business should play;
- how it can win;
- how the position becomes an economically attractive business;
- why the advantage can persist;
- what evidence should cause the strategy to change.

For product scope, prioritization, first useful slices and success measures within an accepted strategy, use installed `product-direction` expertise. This skill retains business direction, competitive position, economics and value-capture decisions. Product evidence can reopen strategy without making every feature a new strategy engagement.

## Trigger Activities

This skill owns the strategy logic: the six questions, modes, evidence discipline and references. Start from the request through the thin activity that owns its stopping point and handoff. Load only the references that activity needs.

| Request | Activity |
|---|---|
| Is this idea worth more investment? | [validate-idea](../validate-idea/SKILL.md) |
| Who is the customer, and what do they do today? | [discover-customers](../discover-customers/SKILL.md) |
| What does the market, segment or competition look like? | [run-market-scan](../run-market-scan/SKILL.md) |
| What is our position, category and value claim? | [define-positioning](../define-positioning/SKILL.md) |
| How do we charge, package and make the economics work? | [design-business-model](../design-business-model/SKILL.md) |
| How do we reach and launch to the buyer? | [plan-go-to-market](../plan-go-to-market/SKILL.md) |
| What experiment would prove or disprove this? | [test-assumptions](../test-assumptions/SKILL.md) |
| What should the strategy be, and what are we excluding? | [set-strategy](../set-strategy/SKILL.md) |
| What are the strategic initiatives, OKRs and capacity? | [build-strategic-roadmap](../build-strategic-roadmap/SKILL.md) |
| Does the strategy still hold, and should we pivot or stop? | [review-strategy](../review-strategy/SKILL.md) |
| Should we raise, how much, and for which milestone? | [raise-capital](../raise-capital/SKILL.md) |
| What do the numbers, scenarios and runway say? | [model-finances](../model-finances/SKILL.md) |

The activities are entry points, not a second copy of the method. **`set-strategy` is the commit and synthesis activity**: analysis, validation and design become a strategy only when it produces the integrated choices, exclusions, falsifiers and an accepted or explicitly proposed brief.

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

When the engagement is exploratory or choosing among options, develop at least three materially different strategies or business models before converging. Include different customers, buyers, jobs, layers, wedges, channels, business models, monetization models, geographies, and—when useful—different beliefs about how the market will evolve. A feature, price or segment variant of the same business model is not a separate option. Compare the structural fields in `references/strategy-option-set.md`.

### 6. Make the strategy falsifiable

Critical assumptions need evidence, confidence, falsifiers, experiments, and review triggers. A strategy that cannot say what would change it is not finished.

## Modes

Infer the mode from the request. Do not force the user to choose. These mode names are internal to this skill. They are not SDLC activities, commands or plugin dependencies.

| Mode | Use when | Emphasis |
|---|---|---|
| `explore` | Opportunity is ambiguous | opportunity space, non-consensus insights, alternative businesses/wedges/models |
| `evaluate` | Business/product is reasonably defined | demand, competition, power, GTM, economics, durability |
| `decide` | Choosing among options | explicit criteria, trade-offs, opportunity cost, recommendation |
| `develop` | Iteratively shaping what the company should become | thesis → evidence → contradiction → revised thesis |
| `review` | Existing strategy meets new evidence | what changed, affected assumptions, reopened decisions |

### Option-set gate

In the exploratory and decision modes described below, do not converge until you have at least three materially different strategies or business models. Compare them across customer/segment, wedge, product layer, channel, monetization, capital intensity, time-to-value, profitability, risk, defensibility and leading indicators. Use `references/strategy-option-set.md` for the matrix, material-difference test, decision record and revisit triggers.

A different feature set, price point or segment label is not a separate option unless it also changes the customer or buyer, wedge, product layer, channel or monetization enough to alter the economics, required capabilities and risks. A light engagement can keep the comparison compact. It does not reduce the minimum to one. End with a recommendation that states the opportunity cost and why each rejected alternative was rejected.

### Depth

- **Light** — narrow question; answer directly and load only the relevant reference.
- **Standard** — material strategic decision; use the relevant strategy questions below.
- **Deep** — ambiguous, high-stakes, fast-moving, or explicitly comprehensive work; iterate across all material questions and maintain persistent state when possible.

Do not turn a simple revenue or pricing question into a full strategy engagement.

## Persistent Strategy State

For substantive ongoing strategy work, preserve a durable current thesis and the history of consequential decisions. Reuse the project's authoritative records when they serve these roles. Keep decision-relevant evidence, assumptions, alternatives, economics, tests and review triggers with the thesis rather than creating parallel registers.

The names `strategy-state.md` and `decision-log.md` below denote those roles. If no suitable records exist, use those filenames and the templates in `assets/` as starting points. Adapt structure to the decision. A bounded question can remain in the conversation. Read existing state before re-analysis, update the thesis when evidence changes and record material choices, reversals and reopening conditions in the decision history. If no writable workspace exists, maintain the same distinctions in the conversation.

## Durable Outputs

A strategy engagement may leave durable records such as the **strategy brief** — the current choices, economics, exclusions, assumptions and falsifiers — and the **market and competitive analysis** that supports it. Keep them consistent with the persistent state. Use `assets/strategy-brief.md` as a starting structure when no accepted brief exists. A bounded question can stay in the conversation. For the craft and review of the brief, use [craft-strategy-brief](../craft-strategy-brief/SKILL.md). For competitive analysis, use [craft-competitive-analysis](../craft-competitive-analysis/SKILL.md). When a market or competitive analysis needs a durable, reviewable record, use the SDLC `research-report` contract rather than inventing a second artifact type. Until an artifact contract exists, keep the brief in `strategy-state.md`.

Product requirements, product roadmaps and engineering change records belong to the development lifecycle (SDLC). Strategy-level outcome and economic measures belong to the operating plan. Product success measures within an accepted strategy belong to `product-direction` in `sdlc`. This skill supplies the direction those artifacts must remain consistent with. It does not produce a second copy of them.

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

For novel, exploratory or development work, test non-consensus hypotheses:

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
- opportunity cost and rejected alternatives, with the reason each was not chosen;
- current recommendation and what would change it.

Do not hide unresolved contradictions behind a polished narrative.

## Named Strategy Frameworks

When the user names a framework, school of strategy, or thinker, read `references/frameworks.md` and apply that lens explicitly.

Rules:

- **Be faithful to the framework.** Use its canonical logic rather than merely labeling generic analysis with the framework name.
- **Keep framework and evidence separate.** A framework structures reasoning; it does not prove a market fact.
- **Integrate the result.** Map framework insights back into the six strategy questions, `strategy-state.md`, and `decision-log.md` when they change the strategy.
- **Do not create framework soup.** Combine frameworks only when each answers a different material question.
- **Respect the user's request.** If the user asks specifically for Five Forces, Playing to Win, Zero to One, Wardley Mapping, 7 Powers, etc., show the analysis through that framework rather than silently translating it into another one.
- **Verify unfamiliar frameworks.** If a requested named framework is not covered in `references/frameworks.md`, research its canonical method before applying it instead of improvising from the name.

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

Classify the evidence and reasoning:

| Kind | Meaning |
| --- | --- |
| Fact | Directly supported by evidence |
| Derived calculation | Computed from stated inputs |
| Inference | Conclusion drawn from evidence |
| Assumption | Unverified belief required by the thesis |
| Strategic judgment | Recommendation under uncertainty |

Keep recommendations and user-accepted commitments distinct in every persistent artifact. Mark proposed pivots, pricing, buyers and business models as provisional until the user accepts them. A decision log cannot manufacture that acceptance. Carry only accepted commitments into system design and implementation.

For decision-changing competitor, adoption, pricing, licensing or protocol-support claims, verify current primary evidence and cite the supporting page. Describe untested vendor claims as such. A missing feature in a page is not proof a competitor lacks it. Examples and SDKs can have different licenses. Do not invent evidence IDs, customer research, purchase intent or certainty such as zero architectural drift to fill a strategy template. Leave unknowns explicit and label numeric scenarios as assumptions with inputs and sensitivity.

Prefer primary sources where possible and match source type to claim type. Actively search for counter-evidence. Multiple pages repeating one origin are not independent confirmation.

When evidence conflicts, examine definition, geography, time period, methodology, accounting basis, incentives, and source independence rather than averaging automatically.

Persist only decision-relevant evidence in `strategy-state.md`. Citations and detailed research can remain in the analysis or output rather than becoming a separate bookkeeping artifact.

## Reference Map

Load references selectively.

### Framework routing

- `references/frameworks.md` — named strategy lenses, canonical logic, when to use them, and how to integrate them

### Process and evidence

- `references/decision-framing.md` — clarify the decision, options, criteria and reversibility
- `references/strategy-option-set.md` — minimum three-option comparison, matrix, anti-patterns, decision record and revisit triggers
- `references/research-protocol.md` — claim-led research, compact evidence tracking, contradiction handling
- `references/strategy-stress-testing.md` — pre-mortem, failure mechanisms, coherence and verdict

### Validation and discovery

- `references/idea-validation.md` — premise challenge, assumption ledger, validation plan and precommitted continue/pivot/kill criteria
- `references/customer-discovery.md` — ICP, status quo, behavioral interviews, commitment signals and discovery evidence limits

### Entry and commercial design

- `references/market-entry.md` — beachhead and mode selection, entry sequencing, competitor profiles and monitoring triggers
- `references/value-proposition.md` — alternatives, unique attributes, value proof, best-fit customer and switching anxieties
- `references/pricing-and-packaging.md` — value-based pricing, willingness-to-pay evidence, packaging, margins and payback
- `references/go-to-market.md` — motion and channel selection, launch gates, growth loops, funnel metrics and a 90-day plan

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

### Decisions, execution and capital

- `references/experiments-and-pmf.md` — assumption-to-test ladder, precommitted bars, evidence grades and retention interpretation
- `references/choice-cascade-and-strategy-brief.md` — Playing to Win and Rumelt structures, exclusions, falsifiers and the strategy brief
- `references/operating-plan.md` — outcome OKRs, initiative portfolio, capacity, cadence, decision rights and product handoff
- `references/strategy-review-and-pivot.md` — review cadence, tripwires, steelman and attack, continue/narrow/park/kill
- `references/capital-and-finance.md` — fundraising readiness, round sizing, instruments, investor process and model sanity

### Templates and sources

- `assets/` — compact starting templates for a validation plan, interview guide, strategy brief, GTM plan, operating plan, review, capital plan, unit-economics record and bet record; adapt or omit sections rather than filling them with invented evidence
- [Source and license record](../../references/sources.md) — reviewed sources, license findings and the decision not to acquire

## Recommended Deep Output

Adapt to the decision. Do not mechanically output every section.

- **Decision / recommendation** — what should be done, why, its opportunity cost and the rejected alternatives
- **Current thesis and alternatives** — including the option set and any thesis mutation
- **Opportunity reality** — decisive customer, market and competitive evidence
- **Where to play + how to win** — beachhead, positioning, distribution, value creation, expansion
- **Business model + economics** — monetization, market size, pricing, GTM, unit economics and scenarios as relevant
- **Durability** — economic power, accumulating assets, future-market robustness
- **Risks / assumptions** — what could break the thesis
- **Experiments / tripwires** — what to learn next and what would change the recommendation
- **State changes** — for ongoing `develop` / `review` work

## Anti-Patterns

Avoid:

- accepting the user's first idea as fixed;
- converging on the first plausible strategy without three materially different options in exploratory or decision work;
- presenting feature or price variants as separate strategies;
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
