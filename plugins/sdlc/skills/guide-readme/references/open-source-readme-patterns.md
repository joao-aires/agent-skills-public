# Open-source README patterns: a small source review

This is a bounded review of five widely used open-source READMEs, read on 16 November 2026 at the revisions linked below. It describes structure and rhetorical moves only. No README text is reproduced, and no project is ranked. The patterns are observations, not requirements; a small library, an internal tool and a language ecosystem need different entries.

## Sources reviewed

| Project | Revision reviewed | What the README optimizes |
| --- | --- | --- |
| [FastAPI](https://github.com/fastapi/fastapi/blob/6847b5dacdc37340157520dd47fb4a3657439796/README.md) | `6847b5d` | Time from arrival to a running API example |
| [Supabase](https://github.com/supabase/supabase/blob/364b5968be15bbafdc182bc43b9779efaf9c9607/README.md) | `364b596` | Capability map and docs routing for a multi-product platform |
| [shadcn/ui](https://github.com/shadcn-ui/ui/blob/ef399795482e91e814695b82a0df681cdd02e548/README.md) | `ef39979` | Deliberate handoff to a documentation site |
| [Rust](https://github.com/rust-lang/rust/blob/f0f849d96ff7c1ea57eca1de63a966e8f832baf5/README.md) | `f0f849d` | Scope of the repository plus a canonical learning path |
| [Vercel](https://github.com/vercel/vercel/blob/c628be7835e03a965b93e9cf9e2bd5ac2acbf5eb/README.md) | `c628be7` | Product entry plus a detailed contributor workflow |

## What each README does

### FastAPI

- Opens with a wordmark, a short tagline, live build/coverage/version/runtime badges, and direct links to documentation and source. The identity and the health signals fit in one screen.
- Defines the product in one sentence and immediately lists a small set of differentiating qualities. Each quality is specific enough to test, and the performance claim links to a section with method and context.
- Moves into installation and a complete example: create a file, run it, check it, open the generated docs. The reader reaches a visible result before the README explains the wider feature set.
- Keeps deeper material, dependency variants and deployment behind headings or links, so the long README remains navigable.
- Labels estimated performance figures as internal estimates rather than presenting them as independent measurement.

**Limit:** sponsor blocks and a large badge cluster consume attention that a smaller project cannot justify. The long-form README works because the headings, anchors and docs links are strong; copying the length without the navigation produces a wall.

### Supabase

- Opens with a theme-aware logo, a single-sentence category definition and a comparison to a known product. The reader can place it before reading the feature list.
- Uses a capability checklist, with each capability linked to its own documentation. This is a map of what the platform covers, not an attempt to teach each feature in the README.
- Shows a screenshot of the real dashboard, then links to full documentation.
- Routes support by channel and states what each channel is best for. That is more useful than a generic "join our community" link.
- Adds a "How it works" section that explains the composition philosophy and the open-source foundation, then places badges, translations and license material later.

**Limit:** a capability checklist dates quickly and can read as a completeness claim. The screenshot and links need maintenance at the same cadence as the product.

### shadcn/ui

- Stays extremely short: a name, a one-paragraph position, a directive about intended use, a hero image, a documentation link, a contribution link and a license.
- Treats the documentation site as the authority and does not duplicate installation, components or examples in the README.
- States the license and contribution route plainly, without a policy wall.

**Limit:** this pattern depends on an established brand and a documentation site that carries the onboarding. A new or unfamiliar project that copies the length leaves the reader without a reason to trust it or a path to a first result.

### Rust

- Uses a centered wordmark and a compact navigation row to the website, getting-started page, learning material, documentation and contribution guide.
- Separates "what this repository contains" from "why use the language." The repository scope is one sentence; the value case is three short qualities linked to deeper explanations.
- Sends the reader to the canonical installation and learning path instead of reproducing the book in the README.
- Keeps installation from source available but marked as not recommended, which is an honest routing decision.
- Ends with license detail and a trademark policy, both linked rather than copied.

**Limit:** there is no inline install command. That is appropriate for a mature language with an authoritative book, and inappropriate for a library whose reader expects one copyable command.

### Vercel

- Opens with a centered logo, a short tagline and a small set of primary links: documentation, changelog, templates and CLI.
- Defines the platform in a sentence, then gives three concrete ways to start: import a project, choose a template or use the CLI. Each is a route, not a feature claim.
- Separates installation of the standard CLI from optional native binaries, including the tradeoff of replacing existing commands.
- Spends substantial space on the contributor path: package manager, running local changes, verification, pull-request process and interpreting test errors.
- Asks contributors to discuss a change before opening a pull request, making the social contract explicit.

**Limit:** product entry and deep contributor instructions share one file. Many projects should keep the README entry short and move the contributor detail to a contribution guide; Vercel can sustain it because contribution is a major use of the repository.

## Cross-cutting patterns

1. **The first screen answers three questions.** What is it, who is it for, and what can I do next? Identity, a one-sentence outcome, a proof signal and a path appear before the history or the feature inventory.
2. **Specific beats superlative.** The stronger claims name a mechanism, a constraint or a measurable outcome. Qualitative value claims work when they are tied to a concrete property, not when they rely on adjectives.
3. **Proof sits near the claim.** A demo, a badge, a benchmark method or a link to a working example accompanies the assertion it supports. A badge is treated as a live claim, not decoration.
4. **The shortest working path is visible.** FastAPI and Vercel put a runnable route near the top. Rust routes to a canonical getting-started page. shadcn/ui routes to the docs because that is where its working path lives.
5. **Capability maps link out.** Supabase lists capabilities with a documentation link for each. It does not attempt to document the platform in the README.
6. **Support channels state their purpose.** "Best for" guidance reduces misrouted questions and sets an honest service boundary.
7. **Contribution is a path, not a policy wall.** Setup, local verification and review expectations appear as steps; the full policy is linked.
8. **License and status are explicit.** Four of the five reviewed READMEs name or link their license; Supabase relies on repository metadata and the licenses of its component tools. A public project should state its license directly rather than leave the reader to infer it. Status or maturity is stated where it affects adoption.
9. **Visual identity is restrained.** Logos and screenshots support recognition. None of the reviewed READMEs uses a decorative image where a command, a result or a capability map would answer the reader's question.

## Where the patterns mislead

- **Credibility by logo and badge.** A new project can reproduce the visual signals without the proof behind them. Badges and wordmarks do not replace a working quickstart.
- **The one-line README.** It works when the documentation site is the product's front door and the project is already known. Otherwise it withholds the orientation a reader needs.
- **The exhaustive capability checklist.** It becomes a maintenance liability and can imply coverage the project does not have. State the few capabilities that decide fit and link the rest.
- **The comparison section.** It requires fairness and upkeep. Naming an alternative without saying when it wins reads as an attack; leaving the section stale is worse than omitting it.
- **The long README.** Length is not a virtue. It works when headings, anchors and links let a reader skip; otherwise the same material belongs in docs.
- **The demo.** A recording or screenshot ages faster than text. Caption it, date the revision when it is evidence and remove it when it stops being true.
- **The contributor appendix.** Deep contributor process in the README can crowd out the user path. Link a contribution guide unless contribution is the repository's primary audience.

## Fit for this repository

Use these patterns as design options, not a checklist. The local [README guide](../SKILL.md) and [repository README contract](../../artifact-system/references/contracts/repository-readme.md) own the required entry content. The strongest transferable moves are: a specific first screen, one honest proof near the adoption claim, a shortest working path, capability and documentation maps that link out, explicit support routing and an explicit license.

Do not import:

- sponsor blocks or badge walls as a default;
- superlative claims or copied launch copy;
- a one-line README without an authoritative docs site;
- competitor comparisons without a maintenance owner;
- contributor process that belongs in a contribution guide.

## Sources and fit

Primary sources reviewed: the five READMEs linked in the table, read at the pinned revisions above. General guidance cross-checked: [GitHub: about READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes), [GitHub: best practices for repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories), [Google Technical Writing One: documents](https://developers.google.com/tech-writing/one/documents) and [Write the Docs: documentation principles](https://www.writethedocs.org/guide/writing/docs-principles/).

This review is a local interpretation. It describes patterns visible at one point in time; it does not claim that any project endorses this guidance, and it does not reproduce their text.
