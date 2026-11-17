# Strategy package: reviewed sources and original synthesis

The `strategy` package is original local material. No upstream skill, template, prompt, canvas, report scaffold or book text is redistributed here.

During the strategy capability audit, a set of public strategy and startup repositories was read to understand what practitioners commonly expect from this kind of guidance and which conventions are worth adopting or rejecting. Those sources were inspiration for coverage and vocabulary only. Every reference and asset in this package was written for this repository, and the method differences are deliberate: decision-first and evidence-graded rather than a fixed workshop output.

## Revisions

The audit was read-only. The table records the exact revision reviewed for provenance. No snapshot is vendored, so the revision documents what was inspected; it is not an acquired artifact or lock entry. If a later change needs to quote, adapt or redistribute a source, it must start a new review and pin the exact revision at acquisition.

## Reviewed-source matrix

| Source | Revision reviewed | License finding relevant to use | What it informed | Not copied | Decision |
|---|---|---|---|---|---|
| [gstack](https://github.com/garrytan/gstack/tree/dd4266dc4b5acb72772c32e4aec32835d659a094) | `dd4266dc4b5acb72772c32e4aec32835d659a094` | MIT repository; mixed `NOTICE.md` for Apache-2.0/MIT design material | Breadth of startup-strategy topics; sequencing from idea to launch | Prompts, role-play instructions, fixed scores, report scaffolds, engineering/runtime layer | Do not acquire |
| [gstack-distilled](https://github.com/0xabrar/gstack-distilled/tree/c06c32e84b1ac42f020677277ca9b2c8e3181844) | `c06c32e84b1ac42f020677277ca9b2c8e3181844` | MIT text with dual copyright; GitHub reports `NOASSERTION` because the file is non-standard | Distillation of common strategy questions; concise framing | Condensed prose, checklists and templates | Do not acquire |
| [startup-skills](https://github.com/bwerneckm/startup-skills/tree/5645be0892925dddab2e64b7b91c90f86c6530d2) | `5645be0892925dddab2e64b7b91c90f86c6530d2` | **No LICENSE file at review**; README claims MIT but GitHub reports `NONE` | Topic coverage for validation and go-to-market | All files and wording | Do not acquire; no clear redistribution grant |
| [founder-stack](https://github.com/ajstars1/founder-stack/tree/b50957716e1aade4335e2a8b9ec63063a4ab1c5d) | `b50957716e1aade4335e2a8b9ec63063a4ab1c5d` | MIT; `where-to-play` links to CC BY-NC-SA 4.0 worksheets | Founder-facing order of decisions; capital and operating concerns | Founder narratives, scripts, canvases, linked worksheets | Do not acquire |
| [stratarts](https://github.com/maigentic/stratarts/tree/aea77df147c02445e2e10ece7ae771fcf47009b4) | `aea77df147c02445e2e10ece7ae771fcf47009b4` | MIT | Strategy-artefact conventions and workshop sequence | Canvases, worksheets, visual templates, fixed scores | Do not acquire |
| [playing-to-win](https://github.com/paultaki/playing-to-win/tree/94b295250dea4e5fb430517c9107907ea54d860d) | `94b295250dea4e5fb430517c9107907ea54d860d` | MIT text for the implementation; **Playing to Win framework IP is not MIT** | Names and canonical logic of the Playing to Win choice cascade | Book text, examples, diagrams, exercise formats | Do not acquire; cite the framework, write original guidance |
| [pm-skills](https://github.com/phuryn/pm-skills/tree/9af7bfd0bc47fdad43c2eaa7a43cd13918e7aaef) | `9af7bfd0bc47fdad43c2eaa7a43cd13918e7aaef` | MIT | Product/strategy boundary; discovery and prioritisation vocabulary | PRD templates, prioritisation scores, roadmaps | Do not acquire |
| [magnus919/agent-skills](https://github.com/magnus919/agent-skills/tree/84831c587aabe754915b8af70ae6e3ab85274804) | `84831c587aabe754915b8af70ae6e3ab85274804` | MIT; optional Python utility | Skill structure and progressive-disclosure conventions; financial and experimentation coverage | Skill bodies, prompts, metadata, scripts | Do not acquire |
| [market-skills](https://github.com/trinity-ai-labs/market-skills/tree/0a9194765a283f71446f2a134d4c6e8ae1df3a62) | `0a9194765a283f71446f2a134d4c6e8ae1df3a62` | MIT | Market and competitor analysis coverage | Market maps, sizing worksheets, competitor grids | Do not acquire |
| [emotixco](https://github.com/emotixco/claude-skills-founder/tree/ea6864c05c2f4a3666b9d6c14c550b20f35a04c9) | `ea6864c05c2f4a3666b9d6c14c550b20f35a04c9` | MIT | Customer and emotional-job framing | Interview scripts, persona templates, scoring | Do not acquire |

The pins above are provenance for the read-only review. The package contains none of their files, excerpts or templates. A permissive license on one file does not cover a repository's book-derived or third-party material; where the framework or worksheet has separate terms, the source was treated as reference-only.

## What was used as inspiration

Only the problem list and the shape of the discipline were carried across. The mapping is approximate because the resulting guidance is a synthesis, not a translation.

| Area | Resulting local reference |
|---|---|
| Idea screening, premise challenge and early kill criteria | [idea validation](../skills/business-strategy/references/idea-validation.md) |
| Interview practice, ICP and commitment signals | [customer discovery](../skills/business-strategy/references/customer-discovery.md) |
| Market selection and competitor profiling | [market entry](../skills/business-strategy/references/market-entry.md) |
| Positioning, value and switching resistance | [value proposition](../skills/business-strategy/references/value-proposition.md) |
| Pricing, packaging and unit economics | [pricing and packaging](../skills/business-strategy/references/pricing-and-packaging.md) |
| Motion selection, launch and funnel metrics | [go-to-market](../skills/business-strategy/references/go-to-market.md) |
| Test design, decision bars and PMF interpretation | [experiments and PMF](../skills/business-strategy/references/experiments-and-pmf.md) |
| Integrated choices and the strategy brief | [choice cascade and strategy brief](../skills/business-strategy/references/choice-cascade-and-strategy-brief.md) |
| Operating cadence and handoff | [operating plan](../skills/business-strategy/references/operating-plan.md) |
| Review, tripwires and pivot decisions | [strategy review and pivot](../skills/business-strategy/references/strategy-review-and-pivot.md) |
| Fundraising and financial-model sanity | [capital and finance](../skills/business-strategy/references/capital-and-finance.md) |

## What was not copied

No upstream material is reproduced here:

- upstream skill bodies, descriptions or metadata;
- role-play prompts, personas or simulated investor/mentor dialogues;
- upstream fixed scores, point systems, readiness ratings or "pass/fail" thresholds presented as universal;
- proprietary canvases, worksheets, matrices or report scaffolds;
- HTML report templates, dashboards or visual layouts;
- book text, examples, diagrams or exercise formats;
- customer-interview scripts, survey instruments or pricing calculators;
- any upstream repository structure or file naming.

The local assets are plain Markdown starting points written for this repository. They are not adaptations of an upstream template, and they do not create new artifact contracts.

## Named frameworks and public methods

Some references name established frameworks and public methods because the user may ask for them or because the logic is useful. These are attributed where used, in [frameworks](../skills/business-strategy/references/frameworks.md) and in the relevant reference:

- Porter's Five Forces and strategic positioning;
- April Dunford's positioning sequence;
- the Playing to Win choice cascade (A. G. Lafley and Roger L. Martin);
- Rumelt's strategy kernel;
- Jobs to Be Done;
- Crossing the Chasm;
- Zero to One;
- 7 Powers;
- Blue Ocean Strategy;
- Wardley Mapping;
- scenario planning and pre-mortem;
- the Y Combinator style of forcing questions;
- the "disappointed without the product" product-market-fit survey heuristic.

The names and canonical logic belong to their authors. The explanations, examples, tables and decision rules in this package are original synthesis. A framework structures reasoning; it does not prove a market fact, and this package does not treat it as evidence.

## Decision not to acquire

The audit concluded that none of the reviewed sources should be acquired. Reasons:

1. **License gaps.** At least one source had no license file, and at least one carried framework or book IP rather than an MIT-style grant. Acquisition would create a redistribution obligation the repository cannot satisfy cleanly.
2. **Duplication and drift.** The existing `business-strategy` references already own market reality, competition, positioning, economics and durability. Vendoring overlapping guides would create two authorities and a maintenance burden.
3. **Method mismatch.** Several sources are workshop kits: canvases, fixed scores and report scaffolds. This repository's convention is decision-first guidance with explicit evidence and completion criteria, not a mandated output shape.
4. **Ownership.** Strategy judgment must remain local and reviewable. A copied playbook would import assumptions and vocabulary that do not match this repository's artifact system, evaluation approach or product/strategy boundary.
5. **No need.** The capability gap was coverage of validation, discovery, entry, pricing, GTM, experiments, operating planning and capital. That is now authored locally.

## Maintenance

- Re-run a source review only if the repository decides to acquire or quote a source. Do not add a source here merely because it is popular.
- Keep the matrix aligned with what the package actually contains. If a future reference is derived from a specific source, name that source and its license at that point.
- Record the reviewed revision for every source. A review pin is provenance; an acquisition pin also identifies vendored bytes and a lock entry.
- Framework names and attributions belong in the reference that uses them, not in this file, which owns the source and license record.
