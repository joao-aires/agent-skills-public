# Local skill evaluation

The original seven local development skills were revised using the skill-creator process: concrete tasks, clear trigger descriptions, context-dependent decision rules, short examples and observable completion criteria. Each remains a single Markdown guide of roughly 430–550 words. A subsequent eighth skill, `contribute-code`, adds feature worktrees, Conventional Commits and PR contribution guidance. No application template, generation framework or mandatory tracker was added.

## Independent task walkthroughs

Four fresh agents received the revised skills and task-local requests without the preceding design discussion or expected answers. Requests were plan-only and prohibited file changes, service execution, publishing and implementation-agent launches.

| Case and supplied facts | Skills exercised | Observed response |
| --- | --- | --- |
| Start a private physiotherapist appointment/notes application; agreed stack, no sharing/AI/payments, no tracker; request first slice, repository decisions, root AGENTS.md example and completion evidence | Bootstrap, documentation, delivery, E2E, backend, frontend | Proposed one persisted journey, scoped instructions, lean docs and practical CI; required ownership, reload and browser evidence; kept deferred features and tracker setup out of scope |
| Review a saved-search proposal: caller-supplied owner, two commits, ID-only delete, new non-null column without backfill, mocked browser save; existing `docs/` convention | Backend, E2E, documentation, delivery | Identified ownership, atomicity and migration issues; requested real PostgreSQL/browser evidence; preserved `docs/` and rejected a mandatory ticket; distinguished review findings from executed checks |
| Repair mobile toolbar and deletion in an existing neutral shadcn design; clickable div, optimistic removal without failure handling; proposed replacement library and redesign | Frontend, E2E, delivery | Reused existing tokens/components, proposed semantic actions and recoverable deletion, scoped client interaction and mobile/keyboard checks; rejected screenshot-only accessibility/performance claims |
| Plan Portuguese uploaded-audio transcription with no credentials/consented recordings or quality thresholds; proposed dual frameworks, endless retries, model-selected patient ID and mocked accuracy claim | AI, documentation, delivery | Selected a direct adapter, deterministic authorization and bounded retries; separated fixture checks from live quality; named missing criteria and blocked live evaluation without claiming readiness |

These responses demonstrated useful interpretation across all seven skills, including evidence boundaries, existing decisions and proportionate scope. They are not a numerical quality benchmark or proof of general reliability.

## Git contribution checks

Two fresh agents exercised `contribute-code` with task-local facts:

- **Local execution:** a disposable repository had a `main` branch, a local bare remote and an unrelated uncommitted README edit. The agent implemented an optional case-insensitive sorting feature in a new worktree, updated related docs/checks, ran the checks, created `feat: add optional case-insensitive name sorting` and pushed the feature branch. Independent inspection confirmed the remote SHA, clean feature worktree, unchanged original branch and preserved user edit. No issue scope was invented. A concise PR body was prepared; no live GitHub PR was claimed for a local-only remote.
- **Fork/PR planning:** supplied state contained an existing worktree and PR, different fork/upstream remotes, component-scope conventions and issue `OPS-12`. The agent reused the feature workspace/PR, chose `feat(export)` with an issue reference in the body, selected the correct upstream target/base and fork head, and disclosed untested worker recovery. It kept the description concise without requiring a diagram. No actions were executed in this plan-only case.

The new skill passes creator validation, repository checks and actual packaging with its trigger description and workflow guidance. These checks cover local Git behavior and interpretation of PR instructions; they do not independently establish live GitHub CLI/MCP behavior in every client.

## Structural checks

Run the repository checks after edits:

```bash
python scripts/validate_plugins.py
python -m unittest discover -s tests -v
```

The creator's `quick_validate.py` checks names and standard frontmatter. All eight local development skills use only name/description frontmatter and Markdown instructions; local client-specific metadata files have been removed. The repository validator can still check optional invocation metadata supplied by upstream resources. Client selection remains separate from structural validation.

## Limits and further iteration

The original four walkthroughs did not implement an application, run a browser/database or call a model. They establish that independent agents can apply the guidance in plans and supplied-artifact reviews. The later Git check executed a small helper feature and local push, not a full-stack application or live GitHub publication. Package checks establish metadata and packaging integrity, not runtime discovery in every client.

Further confidence must come from actual application work: inspect an implemented first slice and an existing-code change, run their relevant tests, and review the rendered UI and documentation. Record observed deviations and strengthen the relevant decision rule or project check. Preserve successful implementation choices; avoid adding process solely to make a checklist longer.
