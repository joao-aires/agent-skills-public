# Review and integration

Use this reference after a draft exists. The goal is a capability that changes behavior, not a well-formed file.

## Review checklist

| Check | Question |
| --- | --- |
| Outcome | Does the skill change what the agent does compared with no skill? |
| Trigger | Do realistic prompts reach the skill, and do near-misses stay away? |
| Boundary | Is the stopping point clear, and does it differ from the nearest adjacent skill? |
| Execution | Can the agent start, act, verify and stop using the body? |
| Branching | Is every-path material inline and conditional detail disclosed behind a trigger? |
| Authority | Does the skill state what to look up, verify or execute instead of freezing it? |
| Change rate | Can the skill survive a framework, vendor or API release without a rewrite? |
| Evidence | Are completion and evidence distinct from configuration, a green build or a file write? |
| Composition | Does the core outcome work when optional plugins are absent? |
| Safety | Is the intent unsurprising, with no hidden access, destructive default or malicious payload? |
| Maintenance | Is each meaning in one authoritative place, with a validation path? |

## Test the behavior

1. **Choose realistic prompts.** Include the intended request, a near-miss that should use another skill, and a case with missing optional capabilities.
2. **Use a baseline.** For a new skill, compare with no skill. For a revision, compare with the previous version.
3. **Inspect the output and the transcript.** Did the agent select the skill, follow the method, stop correctly and produce evidence?
4. **Write negative controls.** A clear failure signal is more useful than another positive example.
5. **Vary context.** Test an existing repository, a greenfield request, a non-git workspace, an unavailable tool and a different stack where relevant.
6. **Revise the method, not the examples.** Do not overfit to the test prompts.
7. **Record the boundary.** Definition checks, local fixtures and live/provider runs establish different evidence.

A definition check proves structure. A behavioral probe proves one case. Neither proves discovery, transfer or production quality.

## Repository integration

- Place the skill at `plugins/<bundle>/skills/<name>/SKILL.md`; folder and frontmatter name must match.
- Declare the required metadata and native invocation controls.
- Add the skill to the plugin’s ownership and capabilities.
- Bump the plugin version when packaged content changes.
- Update the source catalogue, counts, generated skills map and migration notes when the inventory changes.
- Add or update evaluation cases and negative controls.
- Keep relative links inside the package. A standalone build will not contain another package’s source path.
- For an upstream acquisition, follow the upstream-maintenance policy; never edit acquired bytes.

Validation commands are in the repository maintainer guide. At minimum, a local contribution exercises metadata, maintained links, evaluation definitions, unit tests, a complete build and the built inventory/closure check. The source catalogue and generated files are part of the change, not a follow-up.

## Maintenance

- Keep one authoritative place for each meaning.
- Read the environment instead of caching scripts, layouts or generated inventories.
- Remove stale layers when the behavior or external world changes.
- Revisit the description when prompts under-trigger or collide.
- Re-run a small behavioral trial after a material rewrite; a shorter file is not evidence of better behavior.
- Preserve accepted project choices and upstream resources.

## Stop

Stop when the skill has a clear outcome, a working trigger, a method the agent can apply, evidence a reviewer can inspect and a maintenance path. More prose is not more capability. If the behavior is unmeasured, say so.
