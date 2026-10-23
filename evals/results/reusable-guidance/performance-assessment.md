# Research-assistant performance assessment

This assessment uses only the three supplied synthetic trace records. No model, retrieval service or client was run. The accepted outcome remains an answer with supported citations under the existing rubric.

## What the observations establish

| Run | Input | Retrieval | Provider elapsed | Validation/client | Sum of recorded stages | Recorded quality |
| --- | --- | --- | --- | --- | --- | --- |
| A1, baseline | P1 | 7,400 ms | 1,400 ms | 250 ms | 9,050 ms | Pass |
| A2, baseline | P2 | 9,100 ms | 1,600 ms | 250 ms | 10,950 ms | Pass |
| B1, proposal | P3 | 5,200 ms | 800 ms | 250 ms | 6,250 ms | Missing required citation |

The sums are arithmetic over the recorded components. Without an independent end-to-end timer or confirmation that stages never overlap, they should not be presented as directly measured user latency.

Retrieval is the largest recorded stage in each case. In the two baseline records, its mean is 8,250 ms, compared with 1,500 ms for provider elapsed and 250 ms for validation/client work. Under a serial-stage interpretation it accounts for 82.5% of the mean summed time. That makes retrieval the first place to investigate, while leaving the precise cause inside retrieval unknown.

The proposal changed the model, answer limit and input set together. Its shorter recorded stages cannot establish a causal model speedup or a fair improvement over baseline. It also failed the accepted citation criterion. A faster deficient answer is not a useful completed outcome. Two baseline passes and one failure are not reliable estimates of either candidate's quality rate.

Provider elapsed is opaque: no data separates queueing, prefill, reasoning and visible generation. Cache usage and provider cost are unknown. Do not infer cache hits, token savings, billed cost or the effect of a reasoning setting from these records.

## Recommended next experiment

Investigate retrieval on the unchanged accepted model/prompt/output configuration before reducing answer content or reasoning. The bounded next step below is a proposed local fixture experiment; the supplied artifacts alone cannot execute it.

1. Retain the current answer rubric and the same fixed query/evidence set for both arms. Include P1 and P2 if their underlying queries and permitted corpora can be recovered, plus a small reviewed set that exercises the relevant retrieval paths. If those inputs are unavailable, create a new comparable local set and label it as a new baseline.
2. Record an end-to-end timer and retrieval substage timing at existing local boundaries. Inspect query dispatch, network/dependency waiting, result assembly and any repeated work where the code provides observations. Keep unobservable internals unknown. Use authorized fixture data and no raw private content logging.
3. Run five paired local repetitions per query as an initial bounded diagnostic, interleaving baseline and candidate where practical. Record order and warm/cold conditions. This is enough to discover a large repeatable issue, not to claim a production percentile or reliability rate.
4. Choose one retrieval intervention only after that diagnosis. For example, eliminate a demonstrated duplicate read or test an existing indexed query path. If no supported intervention is found, return the bottleneck evidence rather than manufacturing an optimization.
5. Compare the same requested evidence, source access, freshness and downstream rubric for each arm. Preserve failed attempts, recovery time and actual useful completions. Keep retrieval-only timings separate from the full task.

The experiment should run in an owned local environment with external service calls replaced where necessary. A fixture can compare local orchestration or query behavior; it cannot establish remote production retrieval or model performance. Use an existing project experiment time/work ceiling if one exists; otherwise agree one before expensive execution. No such execution is authorized or performed here.

## Decision and stop conditions

Retain a candidate only if it preserves required evidence/citations and shows a meaningful comparable improvement at the boundary it actually changes. A source-access or correctness regression blocks adoption regardless of speed. Keep the current configuration if no candidate meets those conditions.

Stop the bounded diagnostic when its scheduled runs finish, the environment cannot reproduce comparable inputs, required evidence changes, or the allowed resource ceiling is reached. Report unavailable data and failures explicitly. Additional runs or live-service trials should answer a specific unresolved question rather than repeat indefinitely.

Caching is a later option if the observed work repeats and the service supports reuse with acceptable freshness and isolation. Establish actual eligibility, hits and invalidation before claiming a benefit. A stable prompt prefix does not show that the retrieval stage is cached. Input compression, a model change or lower reasoning likewise needs its own quality-controlled comparison if later evidence makes it relevant.

## Needed evidence

The next diagnostic needs underlying query/corpus fixtures, existing retrieval boundaries, independent task timers and the accepted answer rubric. Token usage, actual prices and cache observations are required for monetary or cache claims. Real-user latency and production-scale conclusions remain unmeasured. This assessment is a recommendation from supplied records, not an implemented optimization or a live benchmark.
