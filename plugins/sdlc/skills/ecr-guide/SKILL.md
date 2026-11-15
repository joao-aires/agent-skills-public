---
name: ecr-guide
description: Guide to writing an Engineering Change Record. Covers overview, problem, requirements, solution design, implementation, verification and decisions across a change.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: development
  phase: cross-phase
  scope: generic
  invocation: both
  role: support
---

# ECR guide

An Engineering Change Record (ECR) is the evolving account of one coherent change: why it exists, what it must do, how it is designed, how it is built and what evidence supports the claims. It is the coordination spine, not the only artifact.

## Reader questions

1. What is changing, for whom, and why?
2. What is in scope and out of scope?
3. What must be true for the change to be accepted?
4. What was proposed, and which alternatives were rejected?
5. What has actually been built or checked, at which revision?
6. What has been released, and what is still pending?
7. What decisions were made, by whom, and what remains open?

## Minimum content

- overview, status and change identity;
- problem, scope and non-goals;
- requirements and observable acceptance;
- solution design, alternatives and linked design artifacts;
- implementation strategy and actual changes;
- verification and review evidence, with revision and environment;
- decision history, references and open items.

## Structure and quality

- Keep the current state first in every section; put old checkpoints in a history subsection.
- Write evidence in the past tense; “will verify” is a plan.
- Link the authoritative source instead of copying it.
- Separate proposed, implemented, verified and released claims.
- Record deviations from the design and their consequence.
- Keep the record compact for a small change and detailed for a consequential one.
- Update the record as the work moves; do not leave stale sections above newer evidence.
- Use one ECR per coherent change, not one per task or phase.

## Common failures

- seven headings with no answers;
- “see issue” or “as discussed” without context;
- a status that claims more than the evidence;
- a design section with no alternatives or failure behavior;
- verification that lists commands but not results;
- a release claim based on a merge or build;
- history rewritten to make the change look cleaner than it was.

## Review

Read the ECR as a reviewer who was not in the conversation:

- Can you explain the change and its scope?
- Can you tell what is accepted, proposed, implemented and verified?
- Are the design and verification evidence sufficient?
- Are open decisions and owners visible?
- Does every claim have a revision, target or link?

## Handoff

The next phase needs the current outcome, accepted decisions, evidence and open items. A phase handoff may also use a design specification, architecture view, test result or runbook; the ECR summarizes and links them. Do not copy every artifact into the record.
