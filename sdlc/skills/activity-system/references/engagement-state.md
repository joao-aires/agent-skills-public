# Engagement state: focus, threads and re-entry

Real design and development work does not move through phases in a straight line. A person may design a UI, implement part of it, return to design when the implementation reveals a missing state, and keep a backend contract and a data question open at the same time.

The engagement state is a small record of what is actually happening. It keeps the agent from losing the plot without turning the lifecycle into a gate ceremony.

## When to use it

Use it when:

- the work spans several activities or sessions;
- the user moves back and forth between design and implementation;
- requirements and design, or two software types, are active together;
- a side topic could silently change the design;
- implementation starts before the design is settled;
- another agent or person may pick up the work.

Do not use it for a one-shot question or a small fix. A single-line note is enough there, if anything.

## State block

Keep it in the conversation or at the top of the ECR. For long work, the ECR is the durable home.

```markdown
## Engagement state

Focus: <the thread receiving attention now>

Threads:
- <activity> — <software type> — <stopping point> — <status>
- <activity> — <software type> — <stopping point> — <status>

Decisions:
- <accepted decision>
- <open decision and owner>

Parked:
- <aside> — return after <condition>

Next transition:
- <what must be decided or produced before the focus changes>

Authority:
- <what the work may currently read, write, publish or implement>
```

For a short engagement, compress it:

```text
Focus: frontend saved-searches design. Backend contract accepted; AI not affected.
```

## Rules

1. **One focus, many threads.** Attend to one thread at a time, but do not pretend the others are finished.
2. **Switching is explicit.** Say what you are switching to and why.
3. **Returning is a reopen, not a reset.** Check what evidence changed and which dependent decisions must be revisited.
4. **Parallel phases are allowed.** Requirements and design, or frontend and backend design, can be active together. Each thread has its own stopping point and artifact.
5. **Transitions are announcements, not gates.** "Moving from design to implementation preparation" is a state change; it does not require a ceremony.
6. **Side topics are classified.** In-scope aside, blocking decision, new activity or out of scope. Park nonblocking asides with a return point.
7. **Static labels are not runtime state.** A skill's `phase` says where it primarily belongs; the engagement state says what is happening now.
8. **One thread does not silently change another.** If a frontend decision changes the API contract, reopen the backend/seam thread explicitly.

## Threads

A thread is one line of work with its own id, current phase, stopping point and evidence. A thread may carry a software type:

```markdown
Threads:
- T1 Saved searches — backend — implementation — running
- T2 Export panel — frontend — testing — waiting on T1
- T3 Seam: error and pagination — shared — design — open
```

A thread moves through phases; it is not a phase and not a session.

Read [software types](../../artifact-system/references/software-types.md) for the type evidence. A thread does not need a type when the design evidence is the same regardless of type.

## Delegated execution

Work divides along two axes: the **thread** and the **phase**. A delegate is one thread in one phase — `T1 · implementation`, `T2 · testing` — and it starts from artifacts rather than from another delegate's context. Two threads can sit at different phases at once; the coordinator tracks which is where.

When work is delegated, the thread line carries its phase and the active delegate:

```markdown
Threads:
- T1 Saved searches — implementation — impl delegate — running
- T2 Export panel — testing — test delegate — waiting on T1
```

The phase boundary is what makes the handoff testable: if the next delegate can only work by inheriting the previous one's reasoning, the artifacts are incomplete. Reusing a context across phases hides that gap.

A repair loop stays inside its phase. A new phase, or a decision reopened by later evidence, starts a new delegate for the affected phase.

Use a single session end-to-end when the work is small or the client has no separate contexts; record that the phases shared context. [Delegation](delegation.md) owns the envelope, independence and degradation.

## Reopen protocol

When new evidence invalidates an earlier decision:

1. Name the decision that changed and the evidence that changed it.
2. Reopen the owning thread and its artifact; do not rewrite history silently.
3. Identify dependent decisions, artifacts and implementation slices.
4. Update or mark them superseded, and recheck the seam.
5. State what implementation, if any, must pause or be revised.
6. Record the new decision owner and the next evidence needed.

A reopen is not a full restart. Keep accepted decisions that the new evidence does not touch.

## Side topics

Classify an interruption before following it:

| Kind | Response |
| --- | --- |
| In-scope aside | Answer briefly and return to the focus |
| Blocking decision | Pause only dependent work; record the owner |
| New activity | State the activity, its stopping point and whether it replaces or follows the current work |
| Out of scope | Record it as parked or deferred; do not expand scope silently |

Do not let an aside silently change the phase. If it changes a design premise, say so and reopen design explicitly.

## Transition announcement

At a transition, state:

```text
Current: design
Next: implementation preparation
Carried forward: accepted design X, requirements Y, evidence Z
Open: decision A, owner B
Parked: aside C, return point D
Authority: implementation is / is not authorized
```

This matters when work is interleaved, handed off or resumed. It does not matter for a single bounded task.

## Anti-ceremony

- Do not create a state block for a small fix.
- Do not require every thread to have a software type.
- Do not use the state block as an approval gate.
- Do not repeat accepted decisions in every thread; link the authority.
- Do not turn a parked aside into a backlog item unless the user wants it tracked.

The state block is a reading aid. If it is longer than the work it describes, cut it.
