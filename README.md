# Agent Skills Repository

> 🚧 **Work in Progress:** This repository is currently under active development and the skills are subject to change.

A central repository for reusable, general-purpose skills for coding agents.

This repository serves as a collection of modular skills for my own personal use. I am sharing this publicly just in case it proves useful for other people's own use cases, which can be optimized or improved when coding agents are equipped with the right skills for the job.

## Available Skills

| Skill | Description |
| ----- | ----------- |
| `presentation-building` | Build single-file HTML presentations with a dark theme, scroll-driven slides, responsive card grids, and reveal animations. |
| `architecture-diagraming` | Build responsive, theme-aware HTML architecture diagrams using CSS grid/flexbox and CSS variables. Covers system, cloud, sequence, state, pipeline, and more. |
| `business-strategy` | Develop, evaluate, compare, and continuously update business/product strategy: decision framing, claim-led research, market systems, customer behavior and culture, layered competitive dynamics, wedge selection, positioning, future-market scenarios, TAM/pricing/GTM/economics, moats/control points, falsifiable assumptions, and strategy review. |
| `business-opportunity-analysis` | Deprecated compatibility entry point. It uses `business-strategy` when available and retains a self-contained v1-style evaluation fallback for standalone legacy installs. |

## Business Strategy v2

`business-strategy` treats the initial business concept as a hypothesis rather than a fixed plan. For deep work it can maintain a living strategy state, evidence ledger, assumption register, decision log, and wedge scorecard across sessions.

It supports five modes that are inferred from the request:

- **explore** — search the opportunity and wedge space
- **evaluate** — test a defined business or product
- **decide** — compare strategic alternatives
- **develop** — iteratively evolve what the company/product should become
- **review** — update an existing strategy when the market or evidence changes

The skill uses progressive disclosure: the main `SKILL.md` contains the operating loop and routes to focused reference files only when those modules matter.

### Strategy v2 modules

The reference system covers:

- decision framing and claim-led research
- market-system and profit-pool mapping
- customer behavior, organizational culture, and geography
- product, capability, and whole-vision competition plus competitor trajectory
- wedge generation, scoring, and sequencing
- positioning and category framing
- future-market scenarios and invariant/structural/transitional/fragile assumptions
- moats, accumulating assets, and strategic control points
- red-teaming and falsifiable tripwires
- bottom-up market sizing, OSS commercialization, unit economics, financial scenarios, and valuation

The `assets/` directory contains templates for persistent strategy state, evidence, assumptions, decisions, and wedge comparisons. The `evals/` directory contains regression cases designed to catch premature convergence, shallow competitive analysis, and failure to mutate the thesis.

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
