---
name: guide-rfc
description: Guide to writing a request for comments or technical proposal. Covers problem, current state, affected components, proposal, alternatives, impact and open decision.
user-invocable: true
metadata:
  kind: guide
  domain: development
  phase: design
  scope: generic
  invocation: both
---

# RFC guide

An RFC proposes a consequential technical change and asks for a decision. It is written for reviewers who need enough context to agree, reject or request changes without reconstructing the conversation.

## Reader questions

1. What problem or opportunity does this address?
2. What exists today, at which revision or in which state?
3. Which components, teams or users are affected?
4. What exactly is proposed, including the denied and failure paths?
5. Which alternatives were considered, and why were they rejected?
6. What are the compatibility, migration, security, reliability, cost and operating consequences?
7. What decision is requested, from whom, and what remains open?

## Minimum content

- status, owner and date;
- problem and constraints;
- current state and evidence;
- affected components and interfaces;
- proposal and behavior, including failure and denial;
- alternatives and tradeoffs on the same dimensions;
- impact: compatibility, migration, security, reliability, performance, cost and operations;
- open questions and decision owner;
- links to evidence, prior decisions and related changes.

## Structure and quality

- Open with the decision you want, not the history of the idea.
- Separate current state from the proposal.
- Compare alternatives on dimensions that could change the decision.
- State the failure and migration consequences, not only the happy path.
- Make the scope and non-goals explicit.
- Link evidence; do not assert “this will scale” without a basis.
- Keep the proposal stable enough to review; record material changes.
- If accepted, link the decision record and any implementation follow-up.

## Common failures

- a proposal with no problem or current state;
- alternatives that are straw men;
- hiding migration, compatibility or operational cost;
- proposing a technology because it is popular;
- no named decision owner;
- an RFC that keeps changing during review without a change log;
- treating an accepted RFC as implemented behavior.

## Review

Read the RFC as a reviewer:

- Can you state the problem and the proposed change in one paragraph?
- Do you know what exists today and what would change?
- Are the alternatives real and fairly compared?
- Are failure, migration and operational consequences covered?
- Is the requested decision clear and owned?
- Is the evidence sufficient for the risk?

## Handoff

The design and implementation reader needs the problem, current state, affected components, proposal, alternatives, impact and open decision. An accepted RFC is a decision, not proof of implementation; link the implementation and verification separately.
