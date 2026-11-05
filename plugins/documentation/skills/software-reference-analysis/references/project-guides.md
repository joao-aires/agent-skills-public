# Write an account a newcomer can follow

Use this reference when creating or substantially revising a reference-product guide. The guide owns the evidence-backed account of that product. It can define concepts and interpret consequences; general practitioner advice and exercises belong in teaching material.

## Give each subject a predictable home

Start with one entry point per project. For a substantial guide, the following subject split is useful; smaller products can keep sections together. Preserve existing names and split only independently useful explanations.

| Subject | Reader's question | Typical content |
| --- | --- | --- |
| Introduction | What is it, who uses it and what do its terms mean? | Category/classifications, principal capabilities, a running task and compact evidence scope. |
| Product/business | Why does this offer exist and how is it sustained? | Public positioning, requirements, outcomes, packaging/adoption, support and company-operation evidence. |
| Experience | How do visitors understand it and users accomplish their work? | Separate website and product sections; objects/scopes, journeys, states, visuals, interaction and accessibility. |
| Architecture | Which responsibilities and boundaries make it work? | Context, execution, state/data, external systems, AI, authority and privacy. |
| Engineering | How is the implementation changed and released? | Repository/modules, contracts, stack idioms, local development, tests, CI and artifact promotion. |
| Operations | How is useful service maintained and recovered? | Configuration, signals, overload, migrations, lifecycle, retention and recovery; native updates/permissions where relevant. |

Colocate relevant assets and observations. Keep implementation pins in an existing identity record if one exists; avoid repeating source inventories in every chapter. Unknown company research or production measurements belong as specific limits beside the affected conclusion.

## Build explanation in a useful order

Introduce the users' work and principal capabilities before tracing a helper or rare failure. Define unfamiliar domain objects when first needed. Explain normal behavior, name its actual owners, then follow an important interruption through those same owners. Finish with the consequence and a plausible alternative under stated constraints.

A trace product, for example, needs to establish what a trace represents and how investigators use it before discussing queued ingestion. The queue enters because acceptance and searchable visibility have different lifetimes. That relationship explains the architecture more effectively than a technology inventory.

For an annotated walkthrough, link initiating route/command, domain/service entry, permission/state decision, persistence/external effect and result projection. Say what each selected passage establishes and what it leaves open. Include configuration/mode differences that select another path. One lifecycle diagram should not merge mutually exclusive engines into a fictitious implementation.

Describe observed coupling and mixed responsibilities accurately. An idealized layered diagram can misrepresent a handler that actually coordinates several stores. Label alternative designs as proposals and source-team rationale only when supported by primary evidence.

## Select diagrams for a specific question

| Question | Useful view |
| --- | --- |
| Who uses it and what lies outside the system? | Context view. |
| Which applications/stores collaborate? | Container view with responsibilities and labeled relationships. |
| What happens in order, including failure? | Sequence diagram. |
| Which objects and identities relate? | Domain map, or a physical ERD when schema evidence supports it. |
| How do users move through scopes and tasks? | Navigation/task flow. |
| What changes state and what resumes or cancels? | State diagram. |
| Which checks and promotions produce the artifact? | Delivery flow. |

Use the subset that makes the mechanism intelligible. Keep editable sources, declare scope/current-versus-proposed status, introduce unfamiliar boxes and explain the result in nearby text. Render and inspect the changed diagrams. A structural validator cannot detect a misleading arrow or clipped label.

[C4's diagram guidance](https://c4model.com/diagrams), consulted 5 November 2026, distinguishes structural zoom levels and supporting dynamic/deployment views. A C4 container is an application or data store, not a requirement to use Docker. No fixed diagram quota follows from choosing C4.

## Review the finished account

Ask the text concrete questions: What is the user's next action? Who authorizes it? Which fact commits, which result can lag, and what does failure look like? Where would a contributor change this behavior? Can the reader explain its consequence without repeating a library name?

Review website narrative/navigation and product objects/journeys separately. A landing-page capture cannot support claims about a dashboard's keyboard behavior. Source inspection can explain intended interactions, while actual focus, native effects and task completion require their own observations.

Split paragraphs at changes of subject; preserve causal links and technical conditions. Replace unexplained abbreviations and compressed ownership labels with explicit actors/actions. Keep source links near the claims without making a long function signature the reader's first explanation.

Remove misplaced practitioner instructions from the product account. “This layout retains the prior editor during a session refresh” can be an observed mechanism. “Preserve drafts in your own application and test revalidation” is transferable guidance for a study chapter. Citing project code does not change that distinction.
