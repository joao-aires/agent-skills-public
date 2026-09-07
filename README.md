# Agent Skills Repository

> 🚧 **Work in Progress:** This repository is currently under active development and the skills are subject to change.

A central repository for reusable, general-purpose skills for coding agents.

This repository serves as a collection of modular skills for my own personal use. I am sharing this publicly just in case it proves useful for other people's own use cases, which can be optimized or improved when coding agents are equipped with the right skills for the job.

## Available Skills

| Skill | Description |
| ----- | ----------- |
| `presentation-building` | Build single-file HTML presentations with a dark theme, scroll-driven slides, responsive card grids, and reveal animations. |
| `architecture-diagraming` | Build responsive, theme-aware HTML architecture diagrams using CSS grid/flexbox and CSS variables. Covers system, cloud, sequence, state, pipeline, and more. |
| `business-strategy` | Develop, evaluate, compare, and continuously update business/product strategy: decision framing, evidence, market/customer reality, wedge and beachhead selection, positioning, competitive dynamics, economic power/value capture, future-market durability, TAM/pricing/GTM/economics, moats/control points, falsifiable assumptions, and strategy review. |
| `business-opportunity-analysis` | Deprecated compatibility entry point. It uses `business-strategy` when available and retains a self-contained v1-style evaluation fallback for standalone legacy installs. |

## Business Strategy v2.1

`business-strategy` treats the initial business concept as a hypothesis rather than a fixed plan. Its core reasoning model separates **value creation, value capture, and durability**: a good product is not automatically a good business if competition, buyers, suppliers, or platforms capture the economic surplus.

The skill supports five inferred modes:

- **explore** — search the opportunity and wedge space, including non-consensus hypotheses
- **evaluate** — test a defined business or product
- **decide** — compare strategic alternatives
- **develop** — iteratively evolve what the company/product should become
- **review** — update an existing strategy when the market or evidence changes

The main `SKILL.md` is an orchestrator built around six phases: frame → ground in market reality → design the strategic position → test future/economics → decide/red-team → persist/review. Detailed methods remain in selectively loaded references.

The reference library is organized conceptually into:

- **process and evidence** — decision framing, claim-led research, stress testing
- **market reality** — market systems, customer behavior/culture, layered competition and trajectories
- **strategic position and power** — beachheads, non-comparability, positioning, economic power/value capture, moats/control points, future-market/last-mover tests
- **economics and monetization** — bottom-up sizing, business-model options, pricing, unit economics, financial scenarios, valuation, and OSS commercialization

For substantive strategy work with a writable workspace, the skill maintains two durable artifacts: `strategy-state.md` as the current source of truth and `decision-log.md` as the history of material choices. Decision-relevant evidence and critical assumptions live compactly inside the strategy state rather than in separate bookkeeping files. `evals/` contains regression cases designed to catch premature convergence, shallow competition analysis, TAM shortcuts, false "no competition" conclusions, weak value-capture reasoning, and failure to mutate the thesis.

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
