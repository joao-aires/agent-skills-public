# Design the exchange around the task

Use this for consequential output contracts, context construction or inference recovery. Begin with the accepted outcome and existing architecture. A small text-generation feature may need only a brief assessment; it does not require all the mechanisms below.

## Establish what the consumer can rely on

Follow the result from model output to its next consumer. Identify which information the consumer needs, what it can calculate itself and what happens if the model supplies an incomplete or incorrect result. This determines the useful contract before an API format is selected.

| Consumer need | Suitable approach to assess | Consequence to resolve |
| --- | --- | --- |
| A person needs to understand or judge an answer | Readable prose, citations, uncertainty or a justified explanation | Useful meaning is not established by field shape; assess grounding and the person's task. |
| Software needs records or bounded decisions | Structured data with appropriate schema and application validation | Preserve required distinctions, field limits and invalid-result handling; verify the selected service's actual enforcement. |
| A service may execute an operation | A supported tool/function contract with trusted authorization and effect handling | A syntactically valid call does not establish permission, target freshness or safe retry. |

These approaches can compose. An application may need both a structured record and a readable explanation. Do not remove the latter merely because a compact machine response benchmarks faster.

Distinguish the properties being checked:

- Representation checks establish that the received content can be interpreted as intended.
- Schema and application checks establish expressible field constraints, references and domain rules. Select the appropriate layer for each property; some domain semantics can be encoded in a schema.
- Authority checks establish which effects the caller may perform on which resources in their current state.
- Quality assessment establishes whether the result serves the task, using exact checks, grounded references, rubrics or human review as appropriate.

A model's refusal, incomplete response or unavailable dependency needs its own interpretation. Do not force those states into a success-shaped object or assume a successful HTTP request completed the task. Verify required capabilities against the chosen API/model/version and transport, without assuming that a compatible endpoint or catalog entry proves every optional feature.

## Allocate work between the model and application

Ask which parts require inference and which follow mechanically from available data. Keeping deterministic transformations in code can reduce generated content and remove opportunities for inconsistent repetition. The tradeoff is whether reconstruction makes the result harder to validate, interpret or diagnose.

For large software-consumed outputs, compare explicit records with compact references or positional forms. Compact aliases can avoid repeating long identifiers. Positional forms can make some relationships structural, but increase reliance on order, count and correct mapping. Use them only when those responsibilities can be enforced and the result remains useful. Keep mappings bound to the input they describe; an identifier's shorter spelling does not establish its validity or authority. Duplicate content may still represent distinct resources.

Do not prescribe abbreviated keys or numeric IDs as general defaults. Measure actual usage and accepted quality when representation is a performance decision. Preserve human-readable provenance or explanations when they are part of the task.

## Construct context with understood authority

Identify what is an application instruction, a user goal, a prior decision and supporting evidence. Treat documents, retrieved text, external messages and tool results according to their actual trust and purpose. Serialize or delimit them so content cannot accidentally become application syntax. The supported instruction roles communicate priority; trusted checks remain responsible for constraints that must hold despite a different response.

Select context for relevance and sufficient evidence. Preserve provenance, meaning and freshness where they affect interpretation. A recorded signal may be only a proxy for the fact the task needs; do not silently strengthen it. Earlier model output can be useful context but is not independent confirmation of its own correctness.

Use retrieval, summarization, memory or larger context according to the task's knowledge and continuity needs. Compression can remove a qualification or source relationship even while preserving keywords. Inspect the resulting evidence, not only its token count. If stable context may be reused, retain isolation and freshness requirements; caching behavior and measurements belong with operating guidance.

No fixed number of prompt layers or provider-specific message-role recipe is required. Organize the exchange so the agent can explain which content governs behavior, which content is evidence and how conflicting or missing information is handled.

## Choose uncertainty and recovery behavior

Establish what the consumer should receive when the evidence is insufficient. Asking a question, returning a qualified partial result, abstaining, escalating or stopping can each fit different failure costs. A classification fallback category is one possible product policy; it is not an AI-wide requirement. Preserve accepted behavior rather than inventing a fallback that merely makes a schema easy to satisfy.

Choose recovery from the cause and current state:

| Observed condition | Next action to assess |
| --- | --- |
| A correctable representation or validation failure | Use concrete validation feedback when another generation has a reasonable prospect of correction. Preserve required evidence and revalidate the accepted result. |
| Missing, conflicting or unreliable evidence | Obtain better evidence, clarify, qualify or abstain according to the task. Repeating the same request does not itself supply missing facts. |
| A transient dependency failure | Retry only within the task's duration, attempt and resource limits and the provider's operating constraints. |
| A permanent configuration, access or unsupported-capability failure | Correct the configuration or use an already accepted alternative. Unchanged retries are unlikely to help. |
| An external effect may have occurred | Observe or reconcile actual state before another mutation; inference recovery does not replace effect recovery. |

Set bounds across the complete workflow so nested generation, repair and tool retries do not multiply work unintentionally. The actual limits follow from risk and budget; there is no universal retry count. A smaller repair request must retain the context needed for the original meaning. Independently solving arbitrary chunks may be a different task and needs an explicit composition strategy.

Apply fallbacks within accepted quality, authority and data-handling constraints. Automatic substitution can be legitimate when the product already defines it; an unresolved consequential change needs a decision. Report remaining failure or uncertainty honestly rather than silently accepting a result that violates the contract.

Return the selected consumer contract, consequential constraints, uncertainty/recovery behavior and evidence needed to verify them. Keep these decisions in existing project records and tests; this method does not require another document format or service.
