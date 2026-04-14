# Agent Skills Repository

> 🚧 **Work in Progress:** This repository is currently under active development and the skills are subject to change.

A central repository for reusable, general-purpose skills for coding agents.

This repository serves as a collection of modular skills for my own personal use. I am sharing this publicly just in case it proves useful for other people's own use cases, which can be optimized or improved when coding agents are equipped with the right skills for the job.

## Available Skills

| Skill | Description |
| ----- | ----------- |
| `presentation-building` | Build single-file HTML presentations with a dark theme, scroll-driven slides, responsive card grids, and reveal animations. |
| `architecture-diagraming` | Build responsive, theme-aware HTML architecture diagrams using CSS grid/flexbox and CSS variables. Covers system, cloud, sequence, state, pipeline, and more. |

## Installation

To make these skills available to your coding agents, you can use one of the two methods below:

### Option 1: Using the Vercel Skills CLI

The easiest way to integrate is using the official Vercel-Labs [skills](https://github.com/vercel-labs/skills) CLI tool, which natively supports fetching skills from GitHub repositories directly into your supported agents (like Cursor, Claude Code, or Antigravity):

```bash
# Install all skills from this repository
npx skills add joao-aires/skills

# Or to install a specific skill (e.g., presentation-building)
npx skills add joao-aires/skills --skill presentation-building
```

### Option 2: Using the Sync Script

Alternatively, you can use the included `sync-skills.sh` script to symlink the tools into a global `~/.agents/skills` directory, making them accessible to any custom agent that reads from that path.

First, you'll need to clone this repository to your local machine:

```bash
git clone git@github.com:joao-aires/skills.git
cd skills
```

Then, you can use the sync script:

```bash
# Sync all skills
./scripts/sync-skills.sh sync

# Sync a specific skill
./scripts/sync-skills.sh sync my_skill
# Or simply:
./scripts/sync-skills.sh my_skill
```

To view the current sync status of skills:

```bash
./scripts/sync-skills.sh status
```

To remove all symlinks managed by this repo:

```bash
./scripts/sync-skills.sh remove
```

## Contributing

When adding a new skill:

1. Create a new directory under `skills/` with an intuitive name.
2. Include the necessary scripts, dependencies, and a localized README if needed.
3. Keep the skill modular and self-contained so that agents can easily ingest and run it.

## License

MIT
