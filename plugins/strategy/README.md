# Strategy plugin: business direction, evidence and commercial choices

The `strategy` plugin turns an ambiguous business or product idea into explicit, testable choices: who the customer is, where to play, how to win, how value is captured, why the advantage lasts and what would change the strategy.

It owns business strategy as a discipline. It deliberately does not own product requirements, product roadmaps, engineering change records, release plans or execution delivery.

## Purpose

Use this package when the question is what the business or product should become, or whether a direction is worth committing to. It composes with the product direction work that follows an accepted strategy, and with research and delivery activities that supply or consume its evidence.

`business-strategy` is the logic owner. The activities are thin entry points: they own the request, inputs, work, output, stopping point and handoff, then load only the references the question needs.

## Conceptual model

| Concept | Question it answers |
| --- | --- |
| Strategy logic | What are the six questions, modes, evidence rules and failure modes? Owned by [business-strategy](skills/business-strategy/SKILL.md). |
| Entry point | Which requested activity owns this question, and where does it stop? One of the `validate-*`, `discover-*`, `run-*`, `define-*`, `design-*`, `plan-*`, `set-*`, `build-*`, `review-*` activities. |
| Durable record | What survives the conversation: the strategy brief, competitive analysis, GTM plan, operating plan, capital plan, unit economics, models, reviews and decision history? |
| Evidence posture | Is this a fact, derived calculation, inference, assumption or strategic judgment — and what would falsify it? |

Strategy is iterative, not a fixed sequence. The entry points are ordered by dependency only where a real dependency exists; evidence from any of them can reopen an earlier choice.

## Entry points

Start from the user's question, not from the reference tree.

| User question | Activity | Typical output |
| --- | --- | --- |
| Is this idea coherent enough to pursue? | [validate-idea](skills/validate-idea/SKILL.md) | Premise, evidence, assumption ledger, go/investigate/stop |
| Who has the problem, and what do they do today? | [discover-customers](skills/discover-customers/SKILL.md) | ICP, status quo, jobs, evidence limits |
| What does the market or competition look like? | [run-market-scan](skills/run-market-scan/SKILL.md) | Market, segment, competitor profiles, opening |
| What is our position and value claim? | [define-positioning](skills/define-positioning/SKILL.md) | Category, alternatives, value, proof, switching anxiety |
| How do we capture value and make the economics work? | [design-business-model](skills/design-business-model/SKILL.md) | Model, pricing, packaging, unit economics, durability |
| How do we reach and launch to the buyer? | [plan-go-to-market](skills/plan-go-to-market/SKILL.md) | Motion, channels, launch sequence, funnel, first plan |
| What evidence would change our mind? | [test-assumptions](skills/test-assumptions/SKILL.md) | Test design, precommitted bars, evidence grade, decision |
| What should the strategy be? | [set-strategy](skills/set-strategy/SKILL.md) | Integrated choices, exclusions, falsifiers, brief |
| What are the strategic initiatives and OKRs? | [build-strategic-roadmap](skills/build-strategic-roadmap/SKILL.md) | Outcomes, initiative portfolio, capacity, cadence |
| Does the strategy still hold? | [review-strategy](skills/review-strategy/SKILL.md) | Tripwires, challenge, continue/narrow/park/pivot/kill |
| Should we raise, and how much? | [raise-capital](skills/raise-capital/SKILL.md) | Readiness, round size, instrument, pipeline, runway |
| What do the numbers say? | [model-finances](skills/model-finances/SKILL.md) | Driver model, scenarios, sensitivities, runway |

`set-strategy` is the commit and synthesis activity. Analysis elsewhere becomes strategy only when it produces integrated choices, exclusions, falsifiers and an accepted or explicitly proposed brief.

## Responsibilities

| Skill | Type | Owns | Stops at | Not for |
| --- | --- | --- | --- | --- |
| [business-strategy](skills/business-strategy/SKILL.md) | activity | Strategy logic: six questions, modes, evidence discipline, references | Strategy analysis and recommendation | The execution plan or product scope |
| [craft-strategy-brief](skills/craft-strategy-brief/SKILL.md) | method | Craft and review of the strategy brief | A defensible brief | PRD, roadmap or pitch deck |
| [craft-competitive-analysis](skills/craft-competitive-analysis/SKILL.md) | method | Competitor set, profile, trajectory, bundle risk, response craft | A decision-relevant competitive argument | A category directory or feature matrix |
| Trigger activities | activity | One requested decision each, with its inputs, output and handoff | The named stopping point | Strategy logic they link to instead of restating |
| `product-direction` (sdlc) | method | Product problems, slices, success measures within an accepted strategy | The product decision | Business direction, pricing or market choice |

## How it materialized

| Model element | Implementation |
| --- | --- |
| Strategy logic and reference routing | [business-strategy](skills/business-strategy/SKILL.md) |
| Entry-point routing | The twelve activity skills under `skills/`, plus the entry-point table above |
| Strategy records and templates | `business-strategy/assets/` |
| Brief and competitive craft | The two `guide-*` skills |
| Source and licence record | [references/sources.md](references/sources.md) |

## Artifacts

These are local working records, not contracts in the SDLC artifact system. Adapt them to the project's existing authority.

| Record | Template | Guide | Home |
| --- | --- | --- | --- |
| Strategy brief | [strategy-brief.md](skills/business-strategy/assets/strategy-brief.md) | [craft-strategy-brief](skills/craft-strategy-brief/SKILL.md) | Project strategy records |
| Competitive analysis | [competitive-analysis.md](skills/business-strategy/assets/competitive-analysis.md) | [craft-competitive-analysis](skills/craft-competitive-analysis/SKILL.md) | Alongside the market scan or strategy brief |
| Validation plan and bet record | [validation-plan.md](skills/business-strategy/assets/validation-plan.md), [bet-record.md](skills/business-strategy/assets/bet-record.md) | [test-assumptions](skills/test-assumptions/SKILL.md) | Strategy state or decision log |
| GTM plan | [gtm-plan.md](skills/business-strategy/assets/gtm-plan.md) | [plan-go-to-market](skills/plan-go-to-market/SKILL.md) | Commercial planning record |
| Operating plan | [operating-plan.md](skills/business-strategy/assets/operating-plan.md) | [build-strategic-roadmap](skills/build-strategic-roadmap/SKILL.md) | Operating record for the period |
| Capital plan | [capital-plan.md](skills/business-strategy/assets/capital-plan.md) | [raise-capital](skills/raise-capital/SKILL.md) | Finance and fundraising records |
| Unit economics | [unit-economics-record.md](skills/business-strategy/assets/unit-economics-record.md) | [design-business-model](skills/design-business-model/SKILL.md) | Finance record by segment and period |
| Strategy state, review, decision log | [strategy-state-template.md](skills/business-strategy/assets/strategy-state-template.md), [strategy-review.md](skills/business-strategy/assets/strategy-review.md), [decision-log-template.md](skills/business-strategy/assets/decision-log-template.md) | [review-strategy](skills/review-strategy/SKILL.md) | Project strategy records |

## Reading paths

1. **Early idea** → [validate-idea](skills/validate-idea/SKILL.md) → [discover-customers](skills/discover-customers/SKILL.md) → [test-assumptions](skills/test-assumptions/SKILL.md) → [set-strategy](skills/set-strategy/SKILL.md).
2. **Strategy decision** → [run-market-scan](skills/run-market-scan/SKILL.md) → [define-positioning](skills/define-positioning/SKILL.md) → [design-business-model](skills/design-business-model/SKILL.md) → [set-strategy](skills/set-strategy/SKILL.md) → [build-strategic-roadmap](skills/build-strategic-roadmap/SKILL.md).
3. **Launch** → [plan-go-to-market](skills/plan-go-to-market/SKILL.md) → [model-finances](skills/model-finances/SKILL.md) → [test-assumptions](skills/test-assumptions/SKILL.md).
4. **Ongoing strategy** → [review-strategy](skills/review-strategy/SKILL.md) → [set-strategy](skills/set-strategy/SKILL.md) when a choice changes.
5. **Fundraising** → [model-finances](skills/model-finances/SKILL.md) → [raise-capital](skills/raise-capital/SKILL.md).

## Boundaries

- **SDLC boundary.** Product direction, the PRD, the product roadmap, engineering change records and release plans are outside this plugin. They must remain consistent with an accepted strategy; they are not produced here.
- **Product boundary.** `product-direction` in `sdlc` decides which product problem and slice to pursue within accepted strategy. It can supply evidence that reopens a strategy question but does not choose the business direction.
- **No artifact contracts.** The records in `assets/` are starting shapes. This package adds no artifact types, homes or evidence contracts to the SDLC model.
- **No fabricated evidence.** Customer quotes, market sizes, purchase intent, competitor capability and unit economics must be observed, cited or labelled as assumptions. A framework structures reasoning; it does not prove a market fact.
- **No permission implied.** A recommendation is not an accepted commitment. Only the decision owner's acceptance makes a strategy or a price change authoritative.

## Authority and optional tools

The package declares no MCP servers and no external data sources. Reading a repo, contacting customers, running a pilot, changing prices, contacting investors or publishing a strategy requires action scope from the request and the relevant account or system access. Legal, tax and securities advice, valuation opinions and formal compliance determinations are outside its authority.

## Maintenance

Owning sources are `plugins/strategy/skills/*/SKILL.md`, the shared references under `business-strategy/references/` and the templates under `business-strategy/assets/`. Update this README when the entry-point set, responsibility map or boundary with product direction changes. Validate with `scripts/validate_plugins.py`, `scripts/check_collection.py` and the repository tests; record source decisions in [references/sources.md](references/sources.md).
