# Sequence view contract: the order and the failure path

A **sequence view** is a system-knowledge artifact that explains how one operation, event or job moves between participants: the order, the synchronous and asynchronous work, the branches and the failure or recovery path.

It is not a contract, a state model or proof that an integration works. It is a view of behavior at a named scope.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). Read [guide-sequence-view](../../../guide-sequence-view/SKILL.md) for participant selection, ordering and review conventions.

## Reader questions

1. What starts the operation?
2. Which participants are involved, and what does each own?
3. What happens in what order?
4. Which work is synchronous, asynchronous or fire-and-forget?
5. What changes on rejection, timeout, retry, cancellation or partial failure?
6. Where does completion become authoritative?
7. Is this current or proposed behavior?

## Contract

```markdown
# <Operation or scenario> — sequence view

## Status and scope
Current, proposed or mixed; the operation, trigger and revision/date.

## Participants
Each participant and its responsibility.

## Main path
Ordered calls, events or state changes with intent labels.

## Branches and failure
Success, rejection, timeout, retry, cancellation, partial failure and recovery.

## Completion
The observable result and where completion becomes authoritative.

## Text equivalent
The main path and one consequential failure path in prose.

## Evidence
Contract, source, test, runtime observation or decision supporting the view.
```

## Handoff

The implementer or operator needs the scenario, participants, ordering, async behavior, failure path and completion point. The view may be one of several artifacts in the design or architecture handoff; see [handoff](../handoff.md).

## Maturity

Use **current**, **proposed**, **mixed** and **retired**. A sequence does not establish deployed behavior.

## Review

- Can a reader follow the operation from trigger to result?
- Are participants and responsibilities clear?
- Is sync/async behavior explicit?
- Does the failure path change the decision?
- Is the current/proposed status clear and evidenced?
