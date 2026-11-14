# README contract: the repository's front door

A **README** is the entry artifact for a repository. It helps a new reader understand what the project is, whether it is for them, how to start and where the authoritative knowledge lives. It is entry-and-knowledge-first, but it must describe the actual system accurately.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). The default home is the repository root; component READMEs live beside their component.

## Reader questions

A reader who has just arrived must be able to answer:

1. What is this project, and what problem does it solve?
2. Is it for me, and what is its current status?
3. What do I need before I can run it?
4. How do I install, start, test, build and reset it?
5. Where do I find the architecture, product intent, decisions, guides and runbooks?
6. Where do I report a problem or contribute?
7. What is explicitly not supported or not production-ready?

## Contract

```markdown
# <Project>

One paragraph: purpose, audience and status.

## Quickstart
Prerequisites, install, start and verify in the fewest correct steps.

## What it does
The useful user or system outcome, without marketing claims.

## Documentation map
Links to product, architecture, decisions, guides, reference, operations and contribution docs.

## Development
Test, build, migrate, reset and quality-check commands.

## Support and contribution
Issue route, contribution guide and support boundary.

## Status and limits
Current maturity, unsupported paths and known limitations.
```

Guidance:

- **Purpose and audience.** Explain the problem and who the project serves. Avoid vague claims such as "seamless" or "production-ready."
- **Quickstart.** Give the shortest path that actually works from a clean checkout. State prerequisites and expected result. Verify the commands at the current revision.
- **What it does.** Describe the useful outcome, not a feature inventory. Link deeper explanation; do not duplicate it.
- **Documentation map.** Link the repository artifact home map or docs index. The README should be the front door, not the entire documentation set.
- **Development.** Include test, build, migration, reset and quality-check commands with ownership where useful. Keep secrets out of examples.
- **Support and contribution.** Link the contribution guide and issue route. Do not invent a support commitment.
- **Status and limits.** Say whether the project is a prototype, internal tool, beta or production service, and what is explicitly unsupported.

## Home and maintenance

Keep the root README focused on the repository entry path. Use component READMEs for component-specific commands and exceptions. Update the README when the startup path, prerequisites, documentation map or supported status changes.

Do not let the README become a stale copy of the architecture, API reference or runbooks. Link the authorities and keep only the entry-level summary here.

## Review

Can a new contributor reach a running system and find the authoritative docs without asking? If the README only lists technologies or repeats starter text, it is not a front door.

Verify the commands, paths and links. A README that documents a command that no longer works is worse than a short README that points to the current setup guide.
