# State machine contract: states, transitions and denied paths

A **state machine** is a design or system-knowledge artifact that records the valid conditions of an entity or workflow, the events that change them, the guards and the transitions that must be denied.

It is a model, not proof that the implementation enforces it. The implementation and tests own enforcement.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). Read [state-machine-guide](../../../state-machine-guide/SKILL.md) for state naming, guards, invariants and review conventions.

## Reader questions

1. Which states exist, and what does each mean?
2. What are the initial, terminal and blocked states?
3. What event moves between states, and what guard applies?
4. Which transitions are denied, and why?
5. What invariant must hold in each state?
6. What happens on retry, duplicate event, concurrency or partial completion?
7. Is this current or proposed behavior?

## Contract

```markdown
# <Entity or workflow> — state machine

## Status and scope
Current, proposed or mixed; the entity/workflow and revision/date.

## States
Each state, its meaning and the invariant that holds there.

## Initial and terminal states
The starting condition, terminal states and blocked states.

## Transitions
Event, source state, target state, guard and observable result.

## Denied transitions
Invalid or forbidden transitions and how they are rejected.

## Concurrency and retry
Duplicate events, retries, concurrent actors and partial completion.

## Text equivalent
The main path and one denied or failure path in prose.

## Evidence
Source, contract, test or decision supporting the model.
```

## Handoff

The implementer and tester need the states, transitions, guards, invariants and denied paths. The model may be one of several artifacts in the design handoff; see [handoff](../handoff.md).

## Maturity

Use **current**, **proposed**, **mixed** and **retired**. A model does not establish that illegal transitions are rejected.

## Review

- Are states conditions rather than actions or booleans?
- Are guards and invariants explicit?
- Are denied transitions and their handling shown?
- Does the model agree with the sequence and data behavior?
- Can tests be derived from it, and is the status clear?
