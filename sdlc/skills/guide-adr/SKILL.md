---
name: guide-adr
description: Guide to writing an architecture or product decision record. Covers context, options, decision, consequences, status and supersession.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: development
  phase: design
  scope: generic
  invocation: both
  role: support
---

# ADR guide

An architecture decision record (ADR) or product decision record (PDR) captures one consequential decision, the context that made it necessary, the alternatives and the consequences. It is a durable memory for future maintainers, not a design document or a meeting note.

## Reader questions

1. What decision was made?
2. What context, constraints and forces shaped it?
3. Which alternatives were considered, and why were they rejected?
4. What are the consequences, including the negative ones?
5. Who decided, and when?
6. Is the decision still active, or has it been superseded?

## Minimum content

- title, status, date and decision owner;
- context and forces;
- options considered and the reason for the choice;
- the decision, stated in the active voice;
- consequences: positive, negative, risks and follow-up;
- links to the proposal, requirements, code or related decisions;
- supersession link when the decision changes.

## Structure and quality

- One decision per record.
- State the decision plainly; do not bury it after a long history.
- Keep the context sufficient for a future reader who was not there.
- Record the real alternatives, not just the chosen one.
- Include the consequences you do not like; they are why the record matters.
- Do not rewrite an accepted ADR when the decision changes; supersede it and link the replacement.
- Keep it short enough to read in a few minutes.

## Common failures

- a record that documents a meeting rather than a decision;
- no alternatives or consequences;
- a decision hidden in a long narrative;
- rewriting history after the fact;
- multiple unrelated decisions in one record;
- no owner or date;
- an ADR that claims implementation or verification.

## Review

Read the record as a future maintainer:

- Can you state the decision and why it was made?
- Do you understand the alternatives and the tradeoff?
- Are the consequences, including the bad ones, explicit?
- Is the status and supersession clear?
- Does it link the evidence and the affected work?

## Handoff

The implementation and operations reader needs the decision, context, alternatives, consequences and supersession relation. A decision record does not prove the decision was implemented; link the work and its evidence.
