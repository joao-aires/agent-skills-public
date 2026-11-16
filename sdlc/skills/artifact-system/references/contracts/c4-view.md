# C4 view contract: the boundary, responsibilities and dependencies

A **C4 view** is a system-knowledge artifact at context, container or component level. It explains the system boundary, the actors and external systems, the major elements and the dependencies that cross a consequential boundary.

It may be a current-state view in the architecture set or a proposed-target view in a design record. It is not the architecture itself and does not claim implementation by existing.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). Read [guide-c4-view](../../../guide-c4-view/SKILL.md) for notation, level selection, text equivalents and review conventions.

## Reader questions

1. What is inside the system boundary, and what is outside it?
2. Who are the actors and external systems?
3. What are the major elements, and what does each own?
4. Which dependencies cross a trust, data or deployment boundary?
5. Is this the current system or a proposed target?
6. What evidence supports the view, and what is unknown?

## Contract

```markdown
# <System or scope> — C4 <level> view

## Status and scope
Current, proposed or mixed; the system boundary and the revision/date.

## Actors and external systems
Who uses the system, what external systems it depends on and why.

## Elements and responsibilities
Each element, what it owns and the relationship that matters.

## Dependencies
Directed dependencies, protocols or relationships, and the boundaries they cross.

## Text equivalent
A short prose explanation of the important relationships for non-rendering readers.

## Evidence and uncertainty
Source, contracts, runtime observation, decisions and unknown or inferred edges.
```

## Handoff

The design, implementation or operations consumer needs the boundary, elements, responsibilities, directed dependencies, current/proposed status and the evidence. The view may be one of several artifacts in the architecture handoff; see [handoff](../handoff.md).

## Maturity

Use **current**, **proposed**, **mixed** and **retired**. A proposed view is not current architecture. A mixed view labels its parts.

## Review

- Can a reader identify the boundary and the elements that matter?
- Does each element have a responsibility?
- Are the important dependencies labeled and directed correctly?
- Are current and proposed states unmistakable?
- Is there a text equivalent and supporting evidence?
