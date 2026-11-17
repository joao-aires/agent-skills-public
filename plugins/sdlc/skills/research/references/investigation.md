# Investigation notes: sources, claims and stopping

Read this when a wrong claim would change the decision, when the available sources disagree, or when the question spans documentation, code and observed behavior. The [research method](../SKILL.md) owns the sequence; this reference supplies the source hierarchy, the claim record and the stopping test.

## Source hierarchy

Match the claim to the source that owns it. The nearest authority wins.

| Claim about | Owning authority | Retain with the finding |
| --- | --- | --- |
| Current project behavior | Code, configuration, schema and tests at a revision; an observed command or journey | Paths, command, revision, environment |
| Library or framework behavior | Source and tests at the pinned version; first-party reference | Version, revision, relevant test |
| External API, protocol or provider behavior | First-party specification or reference, plus a probe against the real endpoint | Document date, API version, request and response |
| Standards, regulation or policy | The standard, regulation or policy text | Clause, version, effective date |
| Commercial terms, quotas or prices | The current vendor document or quote | Retrieval date, region, plan |
| Prior decision or constraint | The accepted decision record | Status, date, supersession link |
| Team intent or priority | The decision owner or accepted product artifact | Person or artifact, date |

A blog post, generated overview, Q&A answer or model summary can locate authority but cannot settle a claim. If the authority is inaccessible, record the claim as unverified and name what would settle it.

A **primary source** is the artifact that owns the fact: the specification, the code, the schema, the signed policy or the observed run. A source that merely reports on it is secondary, however accurate it looks. Prefer the version that was actually in force for the decision, not the newest page on the same topic.

## Evidence and citation table

Use a compact table when several claims compete. It keeps observation, inference and limits from collapsing into one confident sentence.

| Claim | Authority | Directly establishes | Kind | Revision or date | Limit |
| --- | --- | --- | --- | --- | --- |
| Webhook replay is safe | Provider idempotency reference | Duplicate delivery with the same key returns the original result | documented | API v3, retrieved 2026-11-17 | Key scope and retention not stated |
| A second delivery does not duplicate the effect | Local probe against a sandbox endpoint | One stored effect after two sends with the same key | observed | `consumer@<full-sha>`, sandbox | Sandbox is not the production provider |
| The consumer can deduplicate locally | Source and tests | A unique receipt row rejects the second event | observed | `consumer@<full-sha>`, test run | Single host, no concurrent deploy |

Rules for the table:

- One claim per row. Split a compound sentence.
- Put the source that owns the claim in **Authority**, not the source that mentioned it.
- Mark **Kind** as documented, observed or inferred. Inference gets its premises in the claim.
- A limit is not a disclaimer. State the exact scope the evidence does not cover.
- Prefer a revision or retrieval date over "current" or "latest".
- Do not let two rows imply independent confirmation when both trace to the same underlying source.

## Stopping conditions

Stop when all of these hold:

1. The decision owner can state the recommendation, its confidence and the condition that would reverse it.
2. Every claim that could change the decision points to an authority at a revision, or is visibly marked unverified.
3. The strongest contrary evidence is represented and either answered or left as an open decision.
4. Remaining unknowns have an owner or a named next probe.
5. Further work would improve phrasing or confidence without changing the decision.

Do not stop at the first plausible answer, because the budget ran out, or because several secondary sources agree with each other. Agreement among summaries is not independent evidence.

## Anti-patterns

- **Summary as source** — citing an article about the API instead of the API reference or a probe.
- **Undated authority** — "the docs say" with no version or retrieval date for a fast-moving external system.
- **Probe as production** — a local or sandbox result presented as provider or deployment behavior.
- **Single path confidence** — testing the happy path and inferring the failure, denial or retry behavior.
- **Averaged disagreement** — smoothing over a contradiction between code, documentation and observation.
- **Reading list** — collecting sources without a recommendation or a decision.
- **Artifact first** — creating a report before the question and the audience are clear.
- **Habitual home** — placing the report in the repository because it is convenient, without resolving authority.
- **Delegated certainty** — accepting a background agent's conclusion without checking its cited source.
- **Research after the decision** — continuing an investigation whose answer can no longer change the choice.
- **Certainty by effort** — treating a long investigation as evidence that the answer is right.

## Worked example: is webhook replay safe?

**Question.** Can the new payment integration retry a webhook delivery without charging the customer twice?

**Evidence.**

| Claim | Authority | Kind | Limit |
| --- | --- | --- | --- |
| The provider accepts an idempotency key on delivery | Provider API reference, v3 | documented | Key retention period is not stated |
| A repeated key returns the original response in the sandbox | Probe at `integration@<full-sha>` | observed | Sandbox behavior may differ from production |
| The consumer stores a unique receipt before applying the effect | Source and test at `consumer@<full-sha>` | observed | Single-process test; concurrent workers untested |

**Recommendation.** Retry with a stable idempotency key derived from the event identity, and keep the local receipt. Confidence is moderate: the provider contract and the local probe agree, but production retention and concurrent-worker behavior are unverified.

**Would reverse it.** Evidence that the provider scopes keys per request rather than per event, or that the receipt is written after the effect.

**Limit and open decision.** The retention window and the production key scope belong to the integration owner. The retry policy should not be treated as accepted until that owner confirms them.

This is enough to inform a design or refinement decision; it is not an implementation plan or a claim that production is safe.
