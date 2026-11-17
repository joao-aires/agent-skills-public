# Synthesizing a conversation into a spec

Use this checklist when the material already exists. The aim is an accurate, reviewable spec, not a new discovery cycle.

## Conversation-to-spec checklist

1. **Locate the decision.** What did the participants actually agree? Quote or paraphrase the decision, and name the evidence: a message, meeting note, accepted ADR, brief or current behavior.
2. **Name the actor and the job.** Who is the change for, what can they do afterward, and what can they not yet do? Use the user's terms before introducing system terms.
3. **State the problem.** Describe the observed present behavior and its consequence. Distinguish a verified defect from a hypothesis or a preference.
4. **Draw the boundary.** Include what changes and exclude adjacent work explicitly. Note behavior that must remain unchanged.
5. **Derive requirements.** Turn each promised behavior into an observable requirement. Include denial, partial, timeout, retry and recovery behavior where it changes what the actor can rely on.
6. **Name quality constraints only where they bind.** Capture a target, its population or conditions and how it will be observed. Leave an unresolved target as an open decision.
7. **Write acceptance.** For each acceptance case, state the action, the condition, the result a reader can observe and the evidence that will show it.
8. **Record decisions and assumptions.** Give each an owner and the phase by which it is needed. Do not hide a disagreement inside a requirement.
9. **Check the seam.** If implementation follows, agree where the behavior will be tested: an existing seam, the highest useful seam and the fewest seams.
10. **Read it cold.** A contributor who was not in the conversation should be able to explain what is promised, what is excluded and what is still open.

## What to omit

- a user-story catalogue or persona inventory unless the existing record already uses one;
- a tracker item, epic tree or label scheme created only to hold the spec;
- code snippets, file paths or a folder-by-folder implementation plan;
- a fixed frontend/backend taxonomy the target does not justify;
- invented SLOs, owners, dates, regulatory commitments or customer promises;
- a design mechanism presented as a requirement;
- a copy of a linked authority instead of a reference to it;
- status language that claims acceptance, implementation or release without evidence.

## Acceptance and evidence mapping

| Spec claim | Acceptance to write | Evidence that fits |
| --- | --- | --- |
| An actor can complete an action | The action from a stated starting condition, with the observable result | A test or journey run at a named revision |
| A denied action stays denied | The denial case and what the actor can see instead | An authority test or recorded interaction |
| The result survives | Reload, reread or reconnect after the action | Persistence or integration observation |
| A quality target holds | The population, workload or failure condition and the observation point | Benchmark, monitor, probe or measured run |
| A surface behaves or communicates correctly | The state, content, error and next action the user or consumer sees | Linked design artifact and rendered review |
| A failure recovers | The failure, the recovery action and the independent proof | Failure-path test or exercise evidence |

A check may cover several requirements. A requirement with no mapped check remains open. Do not substitute a successful command or a green dashboard for the promised user-visible result.

## Anti-patterns

- **Interview replay.** Re-asking what the conversation already settled.
- **Spec as design.** Choosing modules, schemas or algorithms that the participants did not decide.
- **Spec as backlog.** A long list of stories with no observable acceptance.
- **Silent decision.** Resolving an open product or boundary question by writing the preferred answer as fact.
- **ID drift.** Renumbering requirements after tests or release refer to them.
- **Acceptance theatre.** Cases that only prove a function ran, not that the promised result occurred.
- **Seam sprawl.** A new test boundary per component because no one agreed the highest useful seam.
- **Publication by accident.** Treating a written spec as authorization to create or publish a tracker item.
