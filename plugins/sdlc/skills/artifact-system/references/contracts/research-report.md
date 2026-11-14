# Research report contract: a decision-oriented answer

A research report owns a **bounded inquiry and its recommendation**. It is not an ECR, a PRD or an implementation plan. It may end at a recommendation or a decision request. If implementation follows, the ECR owns that change and its release evidence.

Apply the [artifact quality bar](../quality-bar.md). The report is complete when a reader can find the question, the recommendation, the strongest evidence, the alternatives and the remaining decision without reading the raw probe.

## Contract

```markdown
# Question

## Recommendation
The recommended option, its confidence, and what would change it.

## Evidence
What was observed, at which revision and environment, with links to the
probe source, output or primary sources.

## Alternatives
Credible options compared on the same dimensions, with the main limit of each.

## Limits
What the evidence does not establish, and which assumptions remain.

## Open decision
The decision still needed, the owner, and the next evidence that would settle it.

## References
Primary sources, runnable evidence, and the ECR if work follows.
```

Guidance:

- **Question.** State the decision the report is meant to support. A report that answers "tell me about X" without a decision is usually a note, not a research report.
- **Recommendation.** Separate the recommendation from the evidence. State confidence and the condition that would reverse it. Do not present a proposed recommendation as accepted.
- **Evidence.** Distinguish documented capability, observed behavior and interpretation. Give the exact revision, environment, command or probe, and result. Link the runnable evidence or place it after the decision material.
- **Alternatives.** Compare viable options on the same dimensions. Explain the main limit of each and why the recommendation fits the stated constraints.
- **Limits.** State what the probe does not establish. A local single-host experiment does not establish multi-host behavior; a simulated receiver does not establish the real provider contract.
- **Open decision.** Name the decision, its owner and the evidence that would settle it. Do not invent approval.
- **References.** Link primary sources and the probe source/output. Use the [link rules](../quality-bar.md#4-resolvable-navigation).

Do not add implementation, verification or release sections merely to look complete. If the inquiry turns into a change, create or update the ECR and link the report.

## Maturity

A research report normally moves from **question** to **recommendation proposed** to **decision requested** to **accepted**. It does not claim implementation, release or production behavior. The recommendation remains proposed until its owner accepts it.

## Reader test

A reader who was not in the conversation must be able to answer:

1. What question was investigated, and why now?
2. What is recommended, and how confident is it?
3. What was actually observed, and what is only documented or assumed?
4. Which alternatives were rejected, and on what dimension?
5. What remains unresolved, who owns it, and what evidence would settle it?

If the reader must open the raw probe to find the recommendation or the main limit, the report is not complete.

## Example

> **Question.** Can the webhook consumer deduplicate work across process restarts and independent workers on a modest single host, without committing to a new external service?
>
> **Recommendation.** Use a durable local receipt and a dispatch intent in SQLite for a single-host installation. The recommendation is proposed; the real receiver's idempotency and lookup contract must be confirmed before acceptance.
>
> **Evidence.** In a local probe at fixture `consumer@<full-sha>` ([commit](https://example.invalid/consumer/commit)), an in-process map lost identity after restart. Replaying an unkeyed send produced two effects. A durable SQLite claim with a unique event key produced one effect across eight concurrent attempts and a reopen. A simulated receiver that enforced a stable key reduced two delivery attempts to one effect. The probe source and output are linked below.
>
> **Alternatives.**
>
> | Option | Fit | Main limit |
> | --- | --- | --- |
> | In-process map | One disposable worker | Restart and independent workers lose shared identity |
> | SQLite on one host | Durable local volume, modest concurrency | Writer contention, volume recovery and multi-host coordination need testing |
> | Existing relational database | Multiple hosts and managed recovery | Availability, failover and operational ownership depend on the actual deployment |
>
> **Limits.** The probe is local and single-host. It does not establish the real receiver's idempotency-key scope, retention or conflict behavior, PostgreSQL performance, power-loss behavior or restore guarantees. The simulated receiver is not the production provider.
>
> **Open decision.** The integration owner must confirm key scope, expiry and lookup semantics. The service owner must decide the ambiguous-send outcome if the receiver cannot deduplicate. The recommendation remains proposed until those decisions are recorded.
>
> **References.** [Probe source](https://example.invalid/probe), [raw output](https://example.invalid/output), [receiver idempotency documentation](https://example.invalid/docs). If implementation follows, the ECR will own the change and release evidence.
