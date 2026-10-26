# Skill draft revisions

Revised instructions are in [job-failure-diagnosis/SKILL.md](job-failure-diagnosis/SKILL.md) and [component-spacing/SKILL.md](component-spacing/SKILL.md). Both retain their original names, descriptions and `user-invocable: true` metadata. The input drafts are unchanged.

## Material changes

The job-failure-diagnosis draft named broad concerns and asked for a robust solution without explaining how to investigate. The revision supplies a diagnosis method: reconstruct expected and observed execution, distinguish jobs from retry attempts, compare failures with available successes, trace the failing code path, and weigh causal explanations against supporting and contradictory evidence. Timeout and workload checks make the difference between a symptom and a cause concrete. Retry guidance separates the initiating failure from repeated side effects. The output now connects each conclusion and proposed remedy to evidence, and describes what a next check would resolve. All analysis remains confined to supplied artifacts; live replay, data access, notification and deployment remain prohibited, and a proposed repair cannot be reported as executed.

The component-spacing draft already explained what to inspect, how to choose spacing and how to verify it. The revision keeps that compact craft method. It clarifies how spacing conveys grouping, uses comparable components as context for existing roles, and explains what to look for during narrow-layout, content-growth and focus checks. It makes the report distinguish applied edits, proposals, checked states and outstanding visual verification. Accepted type, color and interaction behavior, the rendering fallback and the component-library migration boundary are preserved. No numeric spacing defaults, new design system or migration procedure were introduced.

## Guidance read and applied

All paths below are within the named documentation bundle. These files were opened and read during this task; their external source links were not followed.

| Guidance | Read evidence and application |
| --- | --- |
| `skills/documentation-writing/SKILL.md` | Read the full entry point. Applied "When writing instructions, explain the work behind abstract labels" to replace the diagnosis concern list with an evidence-to-conclusion method. Used its purpose, precision and reader-question review guidance to retain the spacing draft's useful workflow and separate proposals from verified outcomes. |
| `COMPOSITION.md` | Read the full composition guidance linked by documentation-writing. Applied "The requested activity owns its outcome and stopping point" by producing only revised skill instructions and this rationale, without carrying out either skill's application work or expanding discovery. |
| `skills/documentation-writing/references/structured-instructions.md` | Read the full reference, including "Teach the method before compressing it", "Keep the rule and its conditions together" and "Review the reader's path". Used diagnosis guidance for competing explanations and discriminating checks; used craft guidance for grouping, rationale and critique. Kept conditional checks conditional and retained the narrow spacing skill rather than giving both drafts the same structure. |
| `skills/humanizer/SKILL.md` | Read the full skill in a separate untruncated read after the initial batched output was truncated. Applied its embedded prose-editing process and meaning check: removed vague assurance language, used direct verbs, retained uncertainty and authority limits, and avoided decorative formatting. Used the authored drafts' neutral technical voice. |
| `skills/humanizer/AGENTS.md` | Read the package guidance alongside humanizer. Its plain-language advice supports active voice and exact technical meaning. Its package synchronization, version and publication rules were not applicable because no Humanizer package files were changed. |

## Review and limits

Performed an author reader-question review and compared both revisions against the supplied drafts. The diagnosis instructions now answer where to start, what evidence changes the next action, how to avoid treating an error as its own cause, and what to return when evidence is incomplete. The spacing instructions answer how to assess grouping and alignment, what to inspect with long content and focus, and what to report when rendering is unavailable.

This was an instruction review, not an independent behavioral trial. No jobs were diagnosed, application components edited, renders produced or repair outcomes verified. No application implementation, upstream edits, new tooling, subagents or external calls were performed. Source reads were limited to the two input drafts and named documentation bundle; the output files were read back for review.

Input SHA-256 values, checked before and after writing the revisions:

- `component-spacing/SKILL.md`: `d15edfac00a0740e31d77a53c41e327d8bc22d5efd7d83d92e7a24ec0c101fbd`
- `job-failure-diagnosis/SKILL.md`: `662837e923fc0fd4ed694f49264d99ea11579854b7cc0abc7e30118f4f6488fb`
