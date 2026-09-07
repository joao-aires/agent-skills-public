# Agent Skills Repository

> 🚧 **Work in Progress:** This repository is currently under active development and the skills are subject to change.

A central repository for reusable, general-purpose skills for coding agents.

This repository serves as a collection of modular skills for my own personal use. I am sharing this publicly just in case it proves useful for other people's own use cases, which can be optimized or improved when coding agents are equipped with the right skills for the job.

## Available Skills

| Skill | Description |
| ----- | ----------- |
| `presentation-building` | Build single-file HTML presentations with a dark theme, scroll-driven slides, responsive card grids, and reveal animations. |
| `architecture-diagraming` | Build responsive, theme-aware HTML architecture diagrams using CSS grid/flexbox and CSS variables. Covers system, cloud, sequence, state, pipeline, and more. |
| `business-strategy` | Develop, evaluate, compare, and continuously update business/product strategy: opportunity, where-to-play/how-to-win, beachheads, positioning, competition, monetization/economics, economic power, durability, falsifiable assumptions, and named strategy frameworks. |
| `business-opportunity-analysis` | Deprecated compatibility entry point. It uses `business-strategy` when available and retains a self-contained v1-style evaluation fallback for standalone legacy installs. |

## Business Strategy v2.2

`business-strategy` treats the initial business concept as a hypothesis rather than a fixed plan. Its core reasoning model separates **value creation, value capture, and durability**: a good product is not automatically a good business if competition, buyers, suppliers, or platforms capture the economic surplus.

The skill supports five inferred modes:

- **explore** — search the opportunity, business-model, and wedge space, including non-consensus hypotheses
- **evaluate** — test a defined business or product
- **decide** — compare strategic alternatives
- **develop** — iteratively evolve what the company/product should become
- **review** — update an existing strategy when the market or evidence changes

The main `SKILL.md` is organized around six fundamental questions rather than a fixed procedural workflow:

1. **What opportunity actually exists?**
2. **Where should we play?**
3. **How can we win?**
4. **How does this become a great business?**
5. **Why does the advantage persist?**
6. **What must be true, and what changes our mind?**

These questions are iterative: evidence from any one can reopen the others. Detailed methods remain in selectively loaded references.

The reference library is organized conceptually into:

- **framework routing** — explicit support for named lenses such as Jobs to Be Done, Playing to Win, Porter, Zero to One/Thiel, Blue Ocean, Wardley Mapping, Crossing the Chasm, 7 Powers, Rumelt, scenario planning, and others
- **process and evidence** — decision framing, claim-led research, stress testing
- **market reality** — market systems, customer behavior/culture, layered competition and trajectories
- **strategic position and power** — beachheads, non-comparability, positioning, economic power/value capture, moats/control points, future-market/last-mover tests
- **economics and monetization** — bottom-up sizing, business-model options, pricing, unit economics, financial scenarios, valuation, and OSS commercialization

For substantive strategy work with a writable workspace, the skill maintains two durable artifacts: `strategy-state.md` as the current source of truth and `decision-log.md` as the history of material choices. Decision-relevant evidence and critical assumptions live compactly inside the strategy state rather than in separate bookkeeping files.

Named frameworks are applied explicitly when requested, but their conclusions feed back into the same integrated strategy state rather than creating parallel strategy systems.

`evals/` contains regression cases designed to catch premature convergence, shallow competition analysis, TAM shortcuts, false "no competition" conclusions, weak value-capture reasoning, framework name-dropping, and failure to mutate the thesis.

## Installation

To make these skills available to your coding agents, you can use one of the two methods below.

### Option 1: Using the Vercel Skills CLI

```bash
# Install all skills from this repository
npx skills add joao-aires/agent-skills-public

# Install only business-strategy
npx skills add joao-aires/agent-skills-public --skill business-strategy
```

### Option 2: Using the Sync Script

Alternatively, use the included `sync-skills.sh` script to symlink tools into a global `~/.agents/skills` directory.

```bash
git clone git@github.com:joao-aires/agent-skills-public.git
cd agent-skills-public

# Sync all skills
./scripts/sync-skills.sh sync

# Sync a specific skill
./scripts/sync-skills.sh business-strategy

# Check status
./scripts/sync-skills.sh status

# Remove managed symlinks
./scripts/sync-skills.sh remove
```

## Contributing

When adding a new skill:

1. Create a new directory under `skills/` with an intuitive name.
2. Include the necessary scripts, dependencies, assets, and references as needed.
3. Keep the main `SKILL.md` concise and use progressive disclosure for detailed methodologies.
4. Keep the skill modular and self-contained so agents can ingest and run it in different environments.
5. Add regression cases for important behavior when a skill contains a multi-step reasoning workflow.

## License

MIT
