# Delegation: hand work to another context

Delegation starts a second context, gives it bounded work and takes back a result. It is the [hand-off](../../artifact-system/references/handoff.md) move inside a phase: a unit of work changes hands, while the requested activity keeps accountability, scope and stopping point. [Composition](composition.md) is the other case — expertise is consulted, but no work changes hands.

It exists for three reasons: work that would otherwise flood the current context with logs, diffs or search results; depth that needs a specialist pass; and review that must not share the author's reasoning.

## When to delegate

| Delegate | Keep |
| --- | --- |
| Independent slices, investigations, and searches that would flood the context | Focus, decisions, integration and final verification |
| A fresh-context review of work already produced | The judgment about which findings are valid |
| Repetitive verification across revisions, targets or environments | The claim about what the evidence supports |
| Background work that can proceed while you continue elsewhere | The stopping point and the report to the user |

Split by thread and phase. A delegate is one thread in one phase: the phase owns its repair loop, and the next phase is a new delegate with a new context. One exception: a repair that changes production behavior belongs to the phase managing that behavior, so testing reopens implementation instead of repairing and certifying its own fix. Handing a phase's internal loop to someone else creates a context that must rebuild state it never had; reusing a phase's context for the next phase hides what the handoff is supposed to prove.

Fresh context per phase is also the test of the handoff. If testing can only proceed by asking the implementer what it meant, the artifacts are incomplete; fix the handoff rather than the delegate.

Do not delegate an acceptance, a scope change, the authorization for a merge or release, work that writes the same files as an active writer, or a task whose only output would be a transcript.

## The envelope

Send pointers and permissions, not a transcription. The delegate reads the sources itself.

| Field | Content |
| --- | --- |
| Thread | The work item and its current phase, not the delegate's identity |
| Outcome | What is true when the work is done, in observable terms |
| Inputs | Accepted artifacts, their paths and the revision checked |
| Acceptance | The checks that will judge the result |
| Workspace | Worktree or branch, write scope, and the files or decisions not to touch |
| Return | The artifact, commit or PR, plus evidence, deviations and open questions |

An envelope that says "the latest artifact is here" is incomplete: it must name the revision, the acceptance and the write scope. [Handoff](../../artifact-system/references/handoff.md#delegation-envelope) owns the record side of the same fields.

## Context the delegate needs

A delegate starts empty, so context has to be given deliberately. Two rules keep it manageable:

- **Point, do not paste.** Copying a diff, a log or a comment thread into a prompt produces a second copy that goes stale. Name the path or reference and the revision; let the delegate read the source.
- **Give a map, not a dump.** A short index of where the accepted decisions, requirements, standards and evidence live is worth more than a long summary, because the delegate can follow it to whatever detail the finding requires.

The review delegate needs the accepted decision, the standards and the diff, and should not be given the author's reasoning: an argument for the change invites agreement with it.

Delegates that continue the work inside a phase need the opposite: the author's *record*, not the author's *reasoning*. A failing check, a review comment and the repair that follows all sit inside one phase, so the context that produced the change keeps them; a context that has to rebuild the state is slower and less accurate. What that executor keeps, and returns, is the implementation state:

| Field | Why the delegate needs it |
| --- | --- |
| Revision | So a diagnosis is attached to the code it describes |
| Slice statement | What must become true, what must not change and what is deferred |
| Commands run and results | Which checks already passed, so nothing is repeated or assumed |
| Environment and known-flaky checks | Whether a failure is code, configuration, environment or noise |
| Attempts | What was already tried for a failing check or a review comment, and what happened |

Keep that state append-only and small, in the change record or the pull-request description. It is what stops a second agent from repeating the first one's failed fix, and it lets the delegate report at the same revision the orchestrator is reasoning about.

## What comes back

A result, not a narrative: the output, the evidence at a named revision, deviations from the envelope, open questions and the next decision the work exposes. Keep it short enough to act on without reading the whole transcript.

When the delegate is blocked by a decision, it returns a **decision request**: the question, the options with their trade-offs, a recommendation and what is blocked. It stops there. It does not choose, and it does not implement the option it prefers.

## Independence

Review and verification are worth delegating only when the delegate did not produce the work and does not share its reasoning. A second pass in the same context is a re-read, not assurance; say which one happened.

The same delegate must not both find and fix the same defect, or both write and certify the same check. When one agent does both, the evidence is self-assessment.

## Degradation

The contract needs one host capability: a context that can be started without the current conversation and that returns a result. Everything else adapts.

| Missing | Adaptation |
| --- | --- |
| Subagent surface | Run the pass in the current context and record that it shares context |
| Nesting beyond the first level | The delegate runs its own sub-steps instead of starting further agents |
| Background execution | Run it in the foreground and keep the current work stopped |
| Separate workspace | Narrow the write scope and serialize writers by file set |

A missing capability changes the evidence, not the acceptance standard. Record the adaptation where the result is recorded.

## Limits

Delegation does not create authority. The delegate inherits the delegator's scope and cannot accept a decision, widen scope, or decide to merge, deploy or publish. Commit and push happen only when the envelope grants them; executing an authorized release can be delegated, authorizing it cannot. One writer per file set. The delegator stays accountable for the result.
