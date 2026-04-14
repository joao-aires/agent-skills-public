# Agent Skills Repository

> 🚧 **Work in Progress:** This repository is currently under active development and the skills are subject to change.

A central repository for reusable, general-purpose skills for coding agents.

This repository serves as a collection of modular skills for my own personal use. I am sharing this publicly just in case it might be useful for other people looking to extend the capabilities of their AI coding assistants and autonomous agents.

## Available Skills

| Skill | Description |
| ----- | ----------- |
| `presentation-builder` | Build single-file HTML presentations with a dark theme, scroll-driven slides, responsive card grids, and reveal animations. |

## Installation

To make these skills available to your coding agents, you can use one of the two methods below:

### Option 1: Using the Vercel Skills Tool

The easiest way to integrate is using the official Vercel-Labs [skills](https://github.com/vercel-labs/skills) repository tool:

1. Ensure your agents are configured to recognize tools from the Vercel-Labs framework.
2. Link or include this repository's `skills/` folder so the framework can automatically discover and bind them.

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
