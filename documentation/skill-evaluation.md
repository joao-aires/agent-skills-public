# Local skill evaluation

The original seven local development skills were revised using the skill-creator process: concrete tasks, clear trigger descriptions, context-dependent decision rules, short examples and observable completion criteria. Each remains a single Markdown guide of roughly 430–550 words. A subsequent eighth skill, `contribute-code`, adds feature worktrees, Conventional Commits and PR contribution guidance. No application template, generation framework or mandatory tracker was added.

## Adversarial review follow-up

On 2026-10-10, the review's five findings were addressed: standard string metadata for upstream PR credits, inline differential adversarial review, persistence-neutral E2E criteria for existing applications, the missing operations license notice, and readable CI with full-SHA action pins, weekly Dependabot updates and a job timeout. The contribution skill now explicitly confines remote publication to the requested or established scope.

The seven helper regression tests pass, including rejection of malformed optional frontmatter in source/shared validation and final build validation, attribution-preserving adaptation, and removal of unsupported agent dispatch. All seven bundles built with the same 44 upstream pins; all 62 local/upstream skills passed the shared metadata checks. Every package includes its local license notice.

An actual installation/discovery smoke test used GitHub Copilot CLI 1.0.95 in a separate `COPILOT_HOME`, without changing the user's client settings or starting an authenticated model session. Each built directory was installed using `copilot plugin install <absolute-directory>`. `copilot plugin list --json` reported all seven plugins enabled; `copilot skill list --json` exposed all expected plugin-sourced skills:

| Plugin | Discovered skills |
| --- | --- |
| development-workflow | 39 |
| python-backend | 3 |
| web-frontend | 4 |
| ai-development | 7 |
| application-operations | 4 |
| business-strategy | 3 |
| visual-communication | 2 |

Every supplied package file was compared with its installed copy and preserved byte-for-byte, including workflow framing, upstream references, scripts, invocation metadata and license/source notices. The installer warns that direct local/repository installs are deprecated. Reinstalling the workflow bundle from a new build path in the first test configuration dropped the frontend entry from its inventory. A fresh configuration reproduced successful installation/discovery of all seven final bundles. Session-local loading with seven repeated `--plugin-dir` arguments also exposed all 62 skills without persistent installation. Usage guidance records the reinstallation limitation, recommends session-local loading for rebuilt bundles and provides the documented VS Code local-registration route.

This establishes real CLI installation, inventory discovery and supporting-file preservation. It does not establish model selection, enforcement of invocation boundaries, live tool execution or application quality. The VS Code example follows its official documentation and was not executed in this environment.

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

The creator's `quick_validate.py` checks names and standard frontmatter. The original eight local development skills use only name/description frontmatter and Markdown instructions; local client-specific metadata files have been removed. The repository validator can still check optional invocation metadata supplied by upstream resources. Client selection remains separate from structural validation.

## Limits and further iteration

The original four walkthroughs did not implement an application, run a browser/database or call a model. They establish that independent agents can apply the guidance in plans and supplied-artifact reviews. The later Git check executed a small helper feature and local push, not a full-stack application or live GitHub publication. Package checks establish metadata and packaging integrity, not runtime discovery in every client.

Further confidence must come from actual application work: inspect an implemented first slice and an existing-code change, run their relevant tests, and review the rendered UI and documentation. Record observed deviations and strengthen the relevant decision rule or project check. Preserve successful implementation choices; avoid adding process solely to make a checklist longer.

## Delivery, operations, security and feedback additions

Six focused Markdown guides add CI/CD, security/privacy, data recovery, capacity, cost and product feedback. They use standard name/description frontmatter, contextual decisions and evidence boundaries; no client metadata or application templates. All six passed creator metadata validation. Existing bootstrap/backend guidance now brings security, recovery, cost, bounded concurrency and latency into architecture decisions.

Two fresh task walkthroughs received only the relevant skills and scenario facts, without the preceding discussion or expected answers. Both were plan-only: no file changes, service access, purchases, deployment or outreach.

| Case and supplied facts | Observed response |
| --- | --- |
| FastAPI on EKS/RDS with S3 uploads; separate environment builds, mutable image tag, destructive column drop, enabled but untested backups | Chose one immutable artifact for promotion, held the destructive drop in favor of staged compatibility, separated application recovery from data restore, proposed readable workflow/job/step names and an isolated restore with measured RPO/RTO and side effects disabled; did not claim recoverability |
| GKE with 4 replicas × 4 workers × pool 20, database maximum 200, a short 5% CPU snapshot, peak tail-latency growth, 20 registered users/5 savers/2 reopeners, 8 naming mentions from 2 accounts, private sharing request | Identified a potential 320-connection ceiling before rollout, rejected blind rightsizing/commitments from a short snapshot, kept AKS commands out of GKE advice, deduplicated feedback and qualified cohort denominators, proposed a small usability decision and server-side sharing/revocation checks; used no new platform or outreach |

All seven plugin bundles built successfully with 44 pinned upstream skills, including complete AKS references and the Trail of Bits dependency-auditor scripts/lockfile. Repository metadata/containment checks and all three helper regression tests passed. Local Markdown links and whitespace checks passed; the SVG was rendered and visually inspected for legibility and lifecycle direction.

These checks establish packaging and useful interpretation of supplied cases. They do not demonstrate a deployed application, restore rehearsal, measured cloud savings, live analytics integration or complete security/privacy assessment. Observability, incident/SLO/monitoring and load/failure-testing workflows await the user's operating instructions.

## Project foundations and migration refinement

`project-bootstrap` was renamed to `project-conventions` and broadened to focused upkeep of repository conventions. Full setup/reorganization remains explicitly requested; routine feature work applies existing conventions and updates only affected foundations. Usage examples and workflow selection reflect that boundary.

The diagram now places foundations outside the repeating cycle and research/explicit clarification in a full-width band across discovery, development and feedback. The README migration note distinguishes same-checkout managed links, manually copied/linked skills and plugin installation, including the four unchanged original skill paths and the renamed early-PR skill.

Creator metadata validation, repository checks and the three existing helper tests passed. The sync regression verifies repair of a broken old-layout link and preservation of an unrelated link in an isolated home directory; it does not modify the user's installation. Local links were checked and the revised SVG was rendered and inspected. No new application-runtime evidence is claimed for this refinement.
