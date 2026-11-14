# Guide contract: help a reader complete or learn a task

A **guide** is a how-to or tutorial that helps a reader complete a bounded task or learn a workflow. It is entry-and-knowledge-first and is not a reference, an architecture explanation or an ECR.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). The default home is `docs/guides/`; a docs site may be the established alternate.

## Reader questions

A reader who was not in the conversation must be able to answer:

1. Is this the right guide for my task or learning goal?
2. What do I need before I start?
3. What are the ordered steps, and what should I see after each one?
4. What do I do if a step fails or my environment differs?
5. How do I know I succeeded?
6. Where do I go next, and where is the reference detail?

## Contract

```markdown
# <Task or learning outcome>

## Outcome
What the reader will be able to do, and the intended audience.

## Prerequisites
Access, tools, versions, configuration and starting state.

## Steps
Ordered actions with the expected observation after each consequential step.

## Verification
The observable result that establishes success.

## Recovery
Common failures, how to diagnose them and how to return to a safe state.

## Next
Related guides, reference, architecture or decisions.
```

Guidance:

- **Outcome.** State whether this is a how-to (complete a task) or a tutorial (learn by doing). Do not mix a reference manual into the steps.
- **Prerequisites.** Name versions, access, configuration and starting state. Link setup or reference material instead of repeating it.
- **Steps.** Use numbered steps when later steps depend on earlier ones. Explain what the reader should see, not only what to type.
- **Verification.** Give the observable result. "The command exits zero" is weaker than "the page loads and the saved item persists after reload."
- **Recovery.** Include the common failure branches and how to return to a safe state. Do not invent errors or fixes that were not observed or documented.
- **Next.** Link the related guide, reference, architecture view or decision. Keep the guide focused on one reader job.

## Maturity and evidence

A guide should be **current**, **draft** or **retired**. If a step was not actually exercised, say so. Do not present a plausible command sequence as verified.

## Home and maintenance

Keep guides discoverable from the docs index and the README documentation map. Update a guide when a command, prerequisite, UI flow or supported version changes. If a guide becomes obsolete, mark it retired and link the replacement rather than leaving a stale path.

## Review

Can a reader with the stated prerequisites complete the task and verify success without leaving the guide for basic steps? If the guide only lists commands or repeats the reference, it is not a guide.
