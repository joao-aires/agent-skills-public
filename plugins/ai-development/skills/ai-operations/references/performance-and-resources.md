# Diagnose performance and resource use

Use this when a user's wait, service limit or cost affects the accepted task. Reuse existing operating measurements and project tools. A simple feature need not acquire a tracing platform or a benchmark framework.

## Locate the constraint

Follow one representative task from the user's action to its useful result. Identify stages that can explain its elapsed time: admission or quota waiting, retrieval, provider work, generation, repeated tools, validation/recovery and client delivery. Measure only distinctions the available system can observe. A first-token delay may combine queueing, input processing and internal computation; do not invent an internal breakdown from one opaque duration.

Define whether first useful output, final completion or both matter. Streaming may improve perceived progress without reducing completion time and may complicate a consumer that needs the entire result before validation. Choose transport from the task and supported contract, then report the boundary timed. A CLI inference measurement does not include an unmeasured client journey.

Include representative workload size and variability. Distinguish cold/warm or cached/uncached paths where they matter, and preserve time spent waiting for quotas separately from provider response time. A configuration that is fast for a small request may not serve large inputs or concurrent use.

## Select an intervention from evidence

| Candidate | Useful when | Tradeoff to resolve |
| --- | --- | --- |
| Reduce generated content or reconstruct deterministic information in code | Generation or repetitive output is material | Preserve needed explanation/provenance and account for mapping, validation and consumer complexity. |
| Curate, retrieve or summarize input | Irrelevant or repetitive context consumes resources | Retain qualifications and sufficient evidence; measure retrieval/compression errors separately. |
| Reuse cached work | Equivalent authorized work repeats with acceptable freshness | Verify service support, eligibility, hit behavior, isolation and invalidation; stable text alone does not establish a cache hit. |
| Recompute only affected work | Dependencies and state let the unchanged result remain valid | Establish what changes invalidate prior work and how partial results compose. This is not valid for every task. |
| Change the model or reasoning configuration | Evaluation shows the task can retain accepted quality | Verify selected capabilities and compare relevant cases; fewer reasoning tokens are not a correctness argument. |
| Parallelize independent work | Serial dependency waiting dominates | Bound concurrency, quotas and total spend; account for merge consistency and additional failure paths. |

These options can compose, but change enough variables separately to understand the result. A service or model switch changes more than advertised token speed. Use evaluation evidence for usefulness and operating evidence for what ran; preserve both when recommending a configuration.

## Budget the complete workflow

Identify the actual limiting unit and window. Context capacity, output allocation, account request/token limits and concurrent-work limits are different constraints. Reasoning may share an output budget depending on the selected API. Verify current provider semantics rather than translating all limits into one input-size cap.

Include material retries, repair, tool calls, retrieval, judges and supporting services in job-level budgets. Choose admission, concurrency and stopping behavior from the deployment and accepted user outcome. Useful provider headers can inform scheduling but may be absent or incomplete and do not reveal every account-wide limit. Permanent access/configuration failures need correction; quota rejection needs appropriate waiting or a controlled result, not busy retries.

Account for every attempted operation in total cost and user-visible duration. Distinguish reported usage, estimates, published list prices and actual billed cost. Cached-token prices, discounts and free quotas need their own evidence. Compare cost per useful completed task alongside total spend and demand; an efficiency improvement can coexist with a larger bill.

## Preserve diagnosis and operating decisions

Record enough application/configuration identity, timing, usage and stable error categories to locate a regression. Capture raw content only for an accepted purpose under the project's collection policy. Bound buffers and metric dimensions; content-free operational metadata is often sufficient for routine diagnosis.

Separate a failure to execute, an invalid result, poor task quality and an uncertain external effect. These may require different owners and recovery. An inexpensive successful request can still yield no useful outcome. Conversely, a rejected unsafe operation may be correct application behavior while leaving the user's goal unfinished.

Return the observed constraint, proposed intervention, comparable evidence, costs and unresolved limits. Adopt operating targets and automatic fallbacks only within the project's accepted policy. No fixed latency goal, model, cache TTL, token quota or retry count follows from this method.
