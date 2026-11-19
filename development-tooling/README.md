# Development tooling plugin: command, pipeline and dependency craft for selected tools

The `development-tooling` plugin carries the engineering craft around a project's toolchain: Bash and CLI design, provider-neutral CI/CD pipeline design, performance checks, selected implementation conventions and two focused security reviews.

It does not choose the toolchain or the delivery model. It separates provider-neutral pipeline design from selected-provider implementation, and separates both from security review of the selected host.

## Purpose

Use this package when the work is a script, a command surface, a pipeline shape, a load test or a dependency audit. It composes with the release activity that decides delivery, the project conventions that select tools, and the stack or platform package that owns application behavior.

## Conceptual model

Three layers answer different questions. Keeping them apart prevents a provider's syntax from becoming the delivery model and prevents a security review from becoming a redesign.

| Layer | Question | Owner |
| --- | --- | --- |
| Provider-neutral design | What must the pipeline, command or script promise, independent of vendor syntax? | `ci-cd-pipelines`, `cli-development`, `bash-engineering` |
| Selected implementation | How does this chosen tool express that promise, and what does it actually do? | `tooling-conventions`, `performance-testing`, `playwright-cli` |
| Security and supply review | Does this workflow or dependency tree carry risk its author missed? | `github-actions-hardening`, `supply-chain-risk-auditor` |

## Responsibilities

| Skill | Type | Owns | Stops at | Not for |
| --- | --- | --- | --- | --- |
| [bash-engineering](skills/bash-engineering/SKILL.md) | method | Shell interfaces, argument handling, stream and exit-code contracts, failure propagation, cleanup and portable verification | A script with a documented and tested contract | Complex state or data modeling that belongs in a structured language |
| [cli-development](skills/cli-development/SKILL.md) | method | Command grammar, input precedence, output and exit semantics, interaction, help, completion, packaging and compatibility | A reviewable command surface, independent of language | Argument parsing library choice or feature implementation |
| [ci-cd-pipelines](skills/ci-cd-pipelines/SKILL.md) | method | Stage contracts, artifact identity and promotion, environment separation, gates, branching and release flow, recovery and pipeline evidence | A provider-neutral pipeline design | Vendor syntax, GitHub trust boundaries or the release decision |
| [performance-testing](skills/performance-testing/SKILL.md) | method | Load claims, workload model, k6 scenarios, execution targets, interpretation and recovery | A measured result for the exercised workload | Capacity purchasing, SLO definition or production load without authority |
| [tooling-conventions](skills/tooling-conventions/SKILL.md) | method | Implementation and compatibility detail for selected GitHub Actions, Docker, Compose, quality tools, telemetry backends and browser drivers | A verified integration for the accepted toolchain | Tool selection, stack choice or publication |
| [github-actions-hardening](skills/github-actions-hardening/SKILL.md) | method (upstream) | Actions threat model: interpolation injection, privileged triggers, mutable references, token scope, secret exposure and runner exposure | A prioritized workflow security review | General application security or pipeline redesign |
| [playwright-cli](skills/playwright-cli/SKILL.md) | method (upstream) | Browser automation and inspection through the `playwright-cli` command surface | The interactions actually performed and observed | Journey ownership, test strategy or a substitute for real devices |
| [supply-chain-risk-auditor](skills/supply-chain-risk-auditor/SKILL.md) | method (upstream) | Version-matched advisories, lockfile tree risk, abandoned upstreams, publisher concentration and install-time scripts | A measured supply-chain report with judgment and limits | License review, exploit development or automatic dependency upgrades |

## How it materialized

| Model element | Implementation |
| --- | --- |
| Pipeline shape, promotion and recovery | [pipeline design](skills/ci-cd-pipelines/references/pipeline-design.md), [branch to production](skills/ci-cd-pipelines/references/branch-to-production.md) |
| Selected workflow and container mechanics | [workflow implementation](skills/tooling-conventions/references/workflow-implementation.md), [container builds](skills/tooling-conventions/references/container-builds.md) |
| Bash conventions and CI action boundaries | [Bash guide](skills/bash-engineering/references/bash-guide.md), [action boundaries](skills/bash-engineering/references/action-boundaries.md) |
| k6 scenarios and execution targets | [performance-testing](skills/performance-testing/SKILL.md) and its references |
| Acquired reviews and licences | `skills/github-actions-hardening/`, `skills/supply-chain-risk-auditor/`, `skills/playwright-cli/` with `UPSTREAM-LICENSE.txt` |
| Provenance and pins | The maintainer source catalogue and upstream notices |

## Reading paths

1. **New delivery pipeline** → [ci-cd-pipelines](skills/ci-cd-pipelines/SKILL.md) for stages, identity and gates → [tooling-conventions](skills/tooling-conventions/SKILL.md) for the selected provider → [github-actions-hardening](skills/github-actions-hardening/SKILL.md) on the resulting workflow.
2. **New command or script** → [cli-development](skills/cli-development/SKILL.md) for the public surface → [bash-engineering](skills/bash-engineering/SKILL.md) when the implementation is shell.
3. **Performance claim** → [performance-testing](skills/performance-testing/SKILL.md) to define workload and evidence → [tooling-conventions](skills/tooling-conventions/SKILL.md) only for the selected runner or driver integration.
4. **Dependency concern** → [supply-chain-risk-auditor](skills/supply-chain-risk-auditor/SKILL.md) for measured evidence → the project's dependency-maintenance activity for disposition.
5. **Interactive page inspection** → `playwright-cli` for the observation → the journey method for the test claim.

## Boundaries

- **Tool selection.** Which CI host, container runtime, load tool or browser driver the project uses belongs to project conventions. `tooling-conventions` and `performance-testing` are stack-specific and apply only after selection.
- **Delivery decision.** The release activity owns authorization, target verification and the served outcome. A configured pipeline, a green job or a passing load test is not a release.
- **Security scope.** `github-actions-hardening` reviews workflow trust boundaries; `supply-chain-risk-auditor` measures dependency risk. Neither replaces application security review, license analysis or incident response.
- **Evidence.** Authored, linted, built, released, deployed and outcome-verified are distinct states. A YAML parse, an image build or a synthetic benchmark proves only its own stage.
- **Acquired tools.** The three acquired skills retain upstream bodies and controls. Their presence is not provider adoption, and their commands still need installation, credentials and target authority.

## Authority and optional tools

The package declares no MCP servers. It does not install Bash, Docker, k6, Playwright, GitHub CLI or any scanner. Running a workflow, building an image, publishing an artifact or loading a non-production target requires scope from the request and access to that system. The supply-chain auditor writes a project report; it does not change dependencies by itself.

## Acquired sources

| Skill | Source | Pin | Licence |
| --- | --- | --- | --- |
| `playwright-cli` | [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | `b85c7a7` | Apache-2.0 |
| `github-actions-hardening` | [github/awesome-copilot](https://github.com/github/awesome-copilot) | `143a3d9` | MIT |
| `supply-chain-risk-auditor` | [trailofbits/skills](https://github.com/trailofbits/skills) | `82fe822` | CC-BY-SA-4.0 |

## Maintenance

Owning sources are the local `skills/*/SKILL.md` files and their references, plus the three acquired folders. Update this README when the design/implementation/security split or an acquisition changes. Validate with `scripts/validate_plugins.py`, `scripts/check_collection.py` and the repository tests; manage acquisitions through upstream maintenance.
