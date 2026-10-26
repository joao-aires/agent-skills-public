---
name: job-failure-diagnosis
description: Investigate recurring failures in background jobs using supplied code, configuration and execution records.
user-invocable: true
---

# Diagnose failed jobs

Explain the recurring failure as far as the supplied evidence supports, and identify the next check that would resolve the most important remaining uncertainty. Only supplied artifacts and local analysis are authorized. No live job replay, data access, notification or deployment. Do not claim that a repair was executed.

## Reconstruct the failure

Establish what the job should do and what counts as completion from the supplied code and configuration. Distinguish a logical job from its individual execution attempts so retries do not inflate the apparent number of affected jobs.

Connect execution records using the identifiers and timestamps they actually contain. Follow the job from scheduling or enqueueing through execution and completion where evidence exists. Identify the first observed departure from expected behavior; a final failure message may describe a later consequence. Mark missing stages and conflicts between records instead of filling them in.

Compare failed attempts with other supplied failures and, when available, successful attempts. Look for differences in code or configuration versions, input characteristics, duration, dependency responses and workload. Describe the recurring pattern and any exceptions. Report user-visible impact only where the records support it, such as delayed output or repeated side effects.

## Test explanations against the records

Trace the failing path through the supplied code and the configuration that applies to those executions. For each plausible explanation, state what mechanism would produce the observed failure, which evidence supports it, and what contradicts it or remains unknown. A matching timestamp or error label alone does not establish a cause.

Choose checks that distinguish the leading explanations. For a timeout, compare the recorded duration with the configured deadline and inspect any supplied evidence of progress, dependency waits or cancellation. A timeout establishes that a deadline was reached; it does not by itself establish insufficient worker capacity. If failures occur under higher workload, use supplied queue, concurrency or resource records to assess whether capacity explains the pattern before recommending more workers.

Inspect retry behavior when it affects the failure or its consequences: determine what triggers another attempt and whether partially completed work can be repeated safely. Keep the initiating cause separate from factors that amplify it, such as retries repeating a side effect. Missing execution records limit what can be concluded; they do not prove that a stage never ran.

## Return the diagnosis and next check

Lead with the supported cause, or the leading hypotheses if the cause remains unresolved. Link findings to supplied file locations or record identifiers, explain the causal chain, and state the evidence gaps that limit confidence.

Recommend changes only where they address an evidenced mechanism, with the expected effect and relevant tradeoff. For the next useful check, specify the artifact or observation needed and how its possible results would change the diagnosis. If that check requires live access, replay or unsupplied data, describe it as a follow-up without performing it. Keep proposed remedies, completed local analysis and unverified outcomes distinct.
