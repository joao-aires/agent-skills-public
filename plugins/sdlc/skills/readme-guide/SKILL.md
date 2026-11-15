---
name: readme-guide
description: Guide to writing a repository README. Covers purpose, audience, quickstart, what it does, docs map, development, support, status and limits.
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

## Reader questions

1. What is this project, and what problem does it solve?
2. Who is it for, and what is its status?
3. What do I need before I can run it?
4. How do I install, start, test, build and reset it?
5. Where do I find architecture, decisions, guides, operations and contribution notes?
6. Where do I report a problem or contribute?
7. What is explicitly unsupported or not production-ready?

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
- license link, without duplicating the license text.

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

## Common failures

- a README that describes the vision but not how to run the project;
- prerequisites discovered only after failure;
- commands that no longer work;
- a second architecture or API reference inside the README;
- no status or limitations;
- a long feature list with no user outcome;
- license, contribution and changelog text duplicated instead of linked;
- broken relative links or missing images;
- no mention of the supported platform or version.

## Review

Read the README as a new contributor:

- Do you know what the project is and whether it is for you?
- Can you go from a clean checkout to a working result?
- Do you know where to find deeper knowledge?
- Are the commands and links current?
- Are unsupported paths and limits clear?

## Handoff

The new contributor needs the purpose, quickstart, documentation map, development path, support and limitations. Update the README when setup, commands or supported status change; link the canonical docs rather than copying them.
