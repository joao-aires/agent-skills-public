# README contract: the repository's front door

A **README** is the entry artifact for a repository. It helps a new reader understand what the project is, whether it is for them, how to start and where the authoritative knowledge lives. It is entry-and-knowledge-first, but it must describe the actual system accurately.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). The default home is the repository root; component READMEs live beside their component.

Read the [README guide](../../../guide-readme/SKILL.md) for writing conventions, examples and review checks. Read the [open-source README pattern review](../../../guide-readme/references/open-source-readme-patterns.md) when the repository is public and adoption matters.

## Reader questions

A reader who has just arrived must be able to answer:

1. What is this project, and what problem does it solve?
2. Is it for me, and what is its current status?
3. What do I need before I can run it?
4. How do I install, start, test, build and reset it?
5. Where do I find the architecture, product intent, decisions, guides and runbooks?
6. Where do I report a problem or contribute?
7. What is explicitly not supported or not production-ready?
8. How does it differ from the alternatives I already know?

## Contract

```markdown
# <Project>

One paragraph: purpose, audience, status and the outcome the project provides.

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

## License
SPDX identifier and link, or an explicit statement that no license is declared.
```

Guidance:

- **Purpose and audience.** Explain the problem and who the project serves. Avoid vague claims such as "seamless" or "production-ready."
- **Quickstart.** Give the shortest path that actually works from a clean checkout. State prerequisites and expected result. Verify the commands at the current revision.
- **What it does.** Describe the useful outcome, not a feature inventory. Link deeper explanation; do not duplicate it.
- **Documentation map.** Link the repository artifact home map or docs index. The README should be the front door, not the entire documentation set.
- **Development.** Include test, build, migration, reset and quality-check commands with ownership where useful. Keep secrets out of examples.
- **Support and contribution.** Link the contribution guide and issue route. Do not invent a support commitment.
- **Status and limits.** Say whether the project is a prototype, internal tool, beta or production service, and what is explicitly unsupported.
- **License.** Give the SPDX identifier and a link to the license file. Do not copy the license text into the README, and do not imply a license that is absent. If the repository has no declared license, say so explicitly.

## Open-source adoption

A public repository that seeks users or contributors has a second job: help the right reader choose it, and help them start without a guided tour. Add the material below where it is true and useful. It is not required for an internal or component README, and it does not relax the evidence rules above.

```markdown
<One honest demo image or short recording, with a caption and a text description.
Omit it when the outcome is not visual.>

## Why this exists
The problem, the constraint that made the obvious approach insufficient, and the
outcome the project provides. Link the longer rationale or decision record.

## How it compares
The real alternatives a reader is likely to know, when each fits, and the
tradeoff the reader accepts by choosing this project. No disparagement and no
unsupported benchmark.

## Architecture at a glance
A small diagram or three to five responsibility and flow bullets, with a link to
the architecture authority.
```

Placement is a judgment, not a fixed order. Purpose, demo and quickstart usually belong above the fold; "why this exists" can follow the quickstart when a reader's first need is to run the project. Keep the README scannable and link the deep explanation instead of reproducing it.

- **Above the fold.** Put the project name, one-sentence outcome, intended audience and current status in the first screen. The outcome is what the reader can now do or stop doing, not the technology used.
- **Demo or screenshot.** Show current behavior, not a mockup presented as shipped. Label prototypes, state the revision when the demo is evidence, remove staged data that implies an unavailable capability, and give the image alt text plus a short description of what it proves.
- **Why this exists.** Explain the problem and the constraint. Keep the origin story out unless it changes the reader's understanding.
- **Differentiation.** Name real alternatives and say when each is the better choice. If performance matters, link the method, environment and revision. Do not invent adoption numbers, testimonials or superiority claims.
- **Architecture at a glance.** Show the main responsibilities, data flow and trust boundaries at a level that helps a reader place the project. The architecture authority owns the detail.
- **Catchy but honest.** Specificity earns attention; proof keeps it. Prefer a testable outcome and a named audience over superlatives. Do not copy launch marketing into the README, manufacture social proof or use a badge as evidence of quality.
- **Badges.** Include a badge only when it answers a reader question, such as build state, released version, supported runtime or license. Use a live, resolvable signal, keep the set short and remove stale badges. A badge is a claim, not decoration.

## Handoff

The new contributor must know the purpose, quickstart, documentation map, development path, support and status/limits. For a public repository, they must also be able to judge fit and find an honest demonstration. See [handoff](../handoff.md).

## Home and maintenance

Keep the root README focused on the repository entry path. Use component READMEs for component-specific commands and exceptions. Update the README when the startup path, prerequisites, documentation map, demo, supported status or the relevant alternatives change.

Do not let the README become a stale copy of the architecture, API reference or runbooks. Link the authorities and keep only the entry-level summary here.

## Review

Can a new contributor reach a running system, judge whether the project fits and find the authoritative docs without asking? If the README only lists technologies, repeats starter text or presents a demo that no longer matches the product, it is not a front door.

Verify the commands, paths, links, images and comparison claims. A README that documents a command that no longer works is worse than a short README that points to the current setup guide. An honest limitation is more useful than a polished claim the repository cannot support.

## Sources and fit

This contract is original to the repository. Its reader questions and entry-level scope are informed by [GitHub: about READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) and [GitHub: best practices for repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories). The adoption guidance is informed by the [open-source README pattern review](../../../guide-readme/references/open-source-readme-patterns.md) and [Google Technical Writing One: documents](https://developers.google.com/tech-writing/one/documents) for audience, scope and opening with the key point. It is a local contract, not a GitHub requirement.
