---
name: guide-readme
description: Guide to writing a repository README. Covers purpose, audience, quickstart, what it does, open-source adoption, honest claims, docs map, development, support, status and limits.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: documentation
  phase: cross-phase
  scope: generic
  invocation: both
  role: support
---

# README guide

A README is the repository's front door. It helps a new reader understand what the project is, whether it is for them, how to start and where the authoritative knowledge lives.

Read [Open-source README patterns](references/open-source-readme-patterns.md) when the repository is public and needs to earn adoption. It reviews five strong READMEs and the limits of their patterns; it is not a template.

## Reader questions

1. What is this project, and what problem does it solve?
2. Who is it for, and what is its status?
3. What do I need before I can run it?
4. How do I install, start, test, build and reset it?
5. Where do I find architecture, decisions, guides, operations and contribution notes?
6. Where do I report a problem or contribute?
7. What is explicitly unsupported or not production-ready?
8. How is this different from the alternatives I already know?

## Minimum content

- project name and one-paragraph purpose;
- audience and current status;
- prerequisites;
- quickstart: install, start, verify;
- what it does, with the useful outcome;
- documentation map with links;
- development: test, build, migrate, reset and quality checks;
- support and contribution route;
- status, limitations and unsupported paths;
- license link, without duplicating the license text; if no license is declared, say so explicitly.

## Open-source adoption

When a public repository is trying to earn users or contributors, the first screen has to answer "what is this, who is it for, and why would I choose it?" before the reader scrolls. Adoption guidance is not permission to overclaim; it is a demand for specificity.

### Above the fold

Put the project name, a one-sentence outcome, the intended audience and the current status in the first screen. "Outcome" means what the reader can do or stop doing, not the technology used. A reader should not need the feature list to decide whether to continue.

For example, a one-sentence opening names the job, the audience and the distinctive constraint: "A local-first issue tracker for small teams that need offline edits and an auditable sync history." It is more useful than "A modern, powerful platform for collaborative work."

### Demo or screenshot

Include a demo when the outcome is visual or the behavior is hard to state in prose: a short recording, a screenshot of the real interface, or a terminal capture with the command and output. The demo must be honest:

- show the current product, not a mockup presented as shipped;
- label a mockup or early prototype as such;
- show real behavior at a stated revision, without staged data that implies a capability;
- keep the file small, provide alt text and add a text description of what the demo proves;
- remove or refresh a demo that no longer matches the product.

A polished image is not evidence. If the demo is the only proof of a claim, say what version it came from.

### Install and quickstart

Give the shortest path that works from a clean checkout or a supported package manager. State prerequisites before the first command, show the install command, show how to verify success, and link the full setup guide for variants. One working path beats five incomplete ones.

If installation requires an account, a cloud service or a paid dependency, say so before the command. Do not hide a gate behind a "quick" start.

### Why this exists

Explain the problem, the constraint that made the obvious approach insufficient, and the outcome the project provides. This is not the origin story. A short paragraph or three bullets is enough; link the longer rationale or decision record.

The "why" also sets expectations. If the project exists to make a narrow workflow fast, say that, even if it can do more. A broad audience claim with a narrow feature set reads as marketing.

### Differentiation

Name the alternatives a reader is likely to know and say when each fits. A fair comparison answers "why this instead of X?" without pretending X is bad. Use a small table only when the options share comparable dimensions; otherwise use prose.

Do not invent benchmarks, adoption numbers or superiority claims. If a performance comparison matters, link the method and the environment. A comparison that attacks an alternative or hides its advantage damages trust more than it wins adoption.

### Architecture at a glance

Give a small diagram or three to five bullets showing the main components, data flow and trust boundaries. Link the architecture authority for detail. The README should help a reader place the project, not reproduce the architecture set.

### The rest of the adoption path

- **Documentation map.** Link the docs index or the artifact home map. Group links by reader need, not by folder.
- **Development.** State the test, build, lint, migration and reset commands. A contributor should be able to run them without reading CI configuration.
- **Support.** Name the issue tracker, discussion forum or support boundary and what each is best for. Do not promise a response time the project cannot keep.
- **Status and limits.** Say whether the project is a prototype, beta, internal tool or supported product, and which paths are unsupported.
- **Contribution path.** Link the contribution guide, the first-issue route and the review expectations. Keep the README to the entry point.
- **License.** Give the SPDX identifier and a link. Do not copy the license text or imply a license that is not present.

## Catchy but honest

"Catchy" earns attention through specificity, not volume. "Honest" keeps the reader after they arrive.

| Do | Don't |
| --- | --- |
| Name a concrete outcome and the reader who gets it | Use superlatives that no reader can verify |
| Show proof: a demo, a command, a revision, a measured result | Invent social proof, logos, user counts or testimonials |
| Compare with real alternatives and state when each fits | Attack a competitor or copy its marketing framing |
| Use a badge for a live signal the reader needs | Build a badge wall or use badges as decoration |
| Say what is not supported | Imply production readiness the project has not earned |
| Keep the first sentence short enough to quote | Copy the website's launch copy into the repository |

A useful first line is specific enough to be tested. "Fast" is not; "indexes a million records on a laptop in under a minute" is. If the number is not measured, do not use it.

Badges are worth including only when they answer a reader question: does the build pass, what version is this, what license applies, is the package current. Keep them near the top or in a short status block, not as a substitute for a description. Remove badges that no longer resolve.

## Structure and quality

- Lead with the useful outcome, not a feature inventory.
- Make the quickstart the shortest path that actually works from a clean checkout.
- State the expected result after the start command.
- Verify commands and links at the current revision.
- Link deep documentation instead of duplicating it.
- Use real code fences and copyable commands.
- Keep the README scannable; use headings readers will search for.
- Include a logo only if it helps recognition and has a clear source.
- Use GFM and accessible link text; avoid emoji clutter.
- Keep the README as an entry point, not a second architecture or API reference.

## Common failures

- a README that describes the vision but not how to run the project;
- prerequisites discovered only after failure;
- commands that no longer work;
- a second architecture or API reference inside the README;
- no status or limitations;
- a long feature list with no user outcome;
- license, contribution and changelog text duplicated instead of linked;
- a missing license state left ambiguous or invented;
- broken relative links or missing images;
- no mention of the supported platform or version;
- a demo that no longer matches the product or was never real;
- a comparison that names competitors without saying when they are the better choice;
- a badge wall that signals activity instead of fitness;
- an adoption claim copied from a launch page and unsupported by the repository.

## Review

Read the README as a new contributor:

- Do you know what the project is, who it is for and whether it is for you?
- Can you go from a clean checkout to a working result?
- Is the demo or screenshot current, honest and explained?
- Do you know why this exists and how it differs from the alternatives you know?
- Do you know where to find deeper knowledge?
- Are the commands and links current?
- Are unsupported paths and limits clear?
- Is the license state explicit?

## Handoff

The new contributor needs the purpose, quickstart, documentation map, development path, support and limitations. Update the README when setup, commands, supported status, the demo or the competitive landscape change; link the canonical docs rather than copying them.

## Sources and fit

This guide is original repository guidance informed by [GitHub: about READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) and [GitHub: best practices for repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories) for the README's reader questions and repository context; [Google Technical Writing One: documents](https://developers.google.com/tech-writing/one/documents) for audience, scope and the opening summary; and [Write the Docs: documentation principles](https://www.writethedocs.org/guide/writing/docs-principles/) for skimmable, current content.

The adoption guidance is a local synthesis. The [open-source README pattern review](references/open-source-readme-patterns.md) records the source observations and their limits; it is not an endorsement or a template. The repository README contract owns required content.
