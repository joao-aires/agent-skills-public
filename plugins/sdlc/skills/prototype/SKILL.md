---
name: prototype
description: Build a throwaway probe that answers one design question about logic, state or
  a user interface. Use when design validation needs observed behavior or a rendered
  choice, not more discussion.
user-invocable: true
metadata:
  kind: method
  domain: design
  phase: design
  scope: generic
  invocation: both
---

# Prototype: build a throwaway probe

Read [activity system](../activity-system/SKILL.md) for scope and stopping point.

A prototype is disposable code that answers **one framed question**. It is not a first implementation, a design proposal or a demo worth keeping. [Design](../design/SKILL.md) owns the question, the option set, the evidence needed and the decision. This method owns the build craft: turn that question into the smallest runnable thing that produces an observation, then report what it showed.

Read [design validation](../design/references/design-validation.md) for the validation mode and evidence rules. Prototype covers the interactive or rendered part of that method; it does not replace the design record.

## Boundaries

| Question | Owner |
| --- | --- |
| What are we deciding, and which options are credible? | [Design](../design/SKILL.md) |
| What would count as evidence, and what does the result mean? | Design validation and the design owner |
| How do we build the throwaway probe and observe it? | This method |
| How do we implement and verify the accepted direction? | Implementation and `test` |

Do not use a prototype to settle a decision design has not framed, or to claim implemented behavior. If the question is missing, return to design or refine rather than inventing a question through code.

## Choose the probe

| Question | Probe | Read |
| --- | --- | --- |
| Does this rule, state model or data shape survive realistic cases? | Logic probe | [Logic probe](references/logic-probe.md) |
| Which structure, hierarchy or interaction direction is right? | UI probe | [UI probe](references/ui-probe.md) |

The two produce different artifacts, so choosing wrongly wastes the whole build. Use the question, the surrounding code and the accepted design record. A backend rule or data model usually points to a logic probe; a page, flow or component points to a UI probe. If the question is genuinely ambiguous and the user is unavailable, pick the better match, state the assumption at the top of the probe, and keep it visible.

## Rules that apply to both

1. **Throwaway from day one, and clearly marked.** Build it to be deleted. Put it near the work it informs so its context is obvious, but outside the production path, and name it so a casual reader sees it is a prototype. A UI route follows the project's existing routing convention instead of inventing a new top-level structure.
2. **One command to run.** A logic probe opens as one self-contained file or runs through one project command. A UI probe starts from one existing task-runner command. There is no setup sequence, package installation or secret hunt between the owner and the running probe.
3. **No persistence by default.** Keep state in memory. Persistence is the thing being checked, not a dependency of the check. If the question involves a database, use a scratch database or a clearly named "PROTOTYPE, wipe me" local file.
4. **No production polish.** No tests, no abstractions, no error handling beyond what makes the probe runnable, no migration, no production hardening. Polish hides the question and makes the throwaway look keepable.
5. **Surface the state.** After every action, show the full relevant state. On every UI variant switch, show which variant is active and what data or state drives it. The observation is the product; hidden state turns the probe into a guessing game.
6. **Capture the answer, not the build.** Record the question, what was observed, the verdict, its confidence and the condition that would reverse it. Put it in the design record, ECR validation section or conversation that owns the decision. Do not create an artifact type for the prototype.
7. **Keep it out of the main line.** Fold only the validated decision into the real code. Remove the probe shell, switcher and losing variants from the main branch. If the probe must be retained as evidence, put it in the project's scratch or throwaway branch and link it from the decision; never let it become a parallel implementation.

## Work sequence

1. **State the question and the observable answer.** Write one paragraph at the top of the probe: the decision it informs, the claim being checked and what result would change the design. If the user is away, this paragraph is how they check later that the right thing was built.
2. **Pick the smallest shape.** Choose logic or UI, then the least machinery that can produce the observation. A static rendered slice beats a full flow; a pure reducer beats a service; one route beats a navigation system.
3. **Build with real content and the states that matter.** Use realistic names, values, volumes and permissions from the project. Cover the happy path plus the empty, busy, error, denied, stale, duplicate or conflicting cases the question actually reaches.
4. **Run it yourself first.** Confirm it starts with one command and that the state or variant is visible. Fix only what prevents observation; do not turn the run into a test suite.
5. **Hand it over or drive it.** Give the owner the command, URL and the scenarios worth trying. Ask for the moments where they say "that shouldn't be possible" or "I assumed it worked differently"; those are findings about the idea, not the code.
6. **Record and dispose.** Write the answer where the decision lives, mark the probe as evidence or delete it, and return to design or implementation. The next step is not "polish the prototype."

## Stop

Stop when the question has an answer, or when the probe cannot answer it and the limit is explicit. State what was observed, what was not, and what would settle the remainder. Do not extend the probe to cover a second question, and do not promote its code because it happens to run.

## Anti-patterns

- building before the question is framed, or answering a different question than the design asked;
- leaving the prototype in the production path, or letting its shell become the implementation;
- tests, abstractions, migrations or error handling that make the throwaway expensive;
- real persistence, production credentials or writes to shared data when the question did not require them;
- a UI that hides its variant identity, or a logic probe that hides its state;
- calling a happy-path click-through evidence of failure, denial or recovery behavior;
- reporting a plan, a build or an opinion as an observation;
- keeping the probe because deleting it feels wasteful.
