# Workflow authoring

Use this reference when creating or changing a CI workflow: naming, data ownership, expression boundaries, shell failure behavior and the execution-feature decisions that determine reliability. It assumes GitHub Actions but keeps the decisions applicable to another host. Exact syntax, available settings and current feature behavior belong to the [workflow syntax reference](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax); for adapters and trust read [workflow implementation](workflow-implementation.md); for a security review load the installed `github-actions-hardening` skill. A workflow is orchestration: build, test, package and deployment logic belongs in commands and scripts that can also run outside CI. Keep the workflow responsible for selecting work, connecting identities, enforcing gates and recording evidence.

## Name the unit of work

- Name the workflow by purpose and component, with a deployment target when applicable: `ci-api.yml` / `CI / API`, `release-api.yml` / `Release / API`, `deploy-api.yml` / `Deploy / API`. Put target identity in the display name or `run-name`: `Deploy / API / production / eu-west-1`. An environment name alone does not prove which target changed, so make account/project, region, service and artifact digest visible without opening the log.
- Use descriptive lowercase job IDs and short verb-object step names: `Run unit tests`, `Build image`, `Publish chart`, `Smoke test target`. The job ID is for maintainers and expressions, the job `name` is for the checks UI, and the command carries flags and implementation detail rather than the step name. Avoid `build1`, `job2` and names that restate the workflow.
- Preserve a coherent existing convention. Renaming workflows, jobs or required checks is an interface change; update branch protection and callers deliberately.

## Give each value one owner

| Source | Use for | Do not use for |
| --- | --- | --- |
| `inputs` | Typed parameters from a caller or manual run | Secrets or ambient repository configuration |
| `env` | Values a process needs, scoped to workflow, job or step | Shared configuration owned outside the workflow; secret storage by default |
| `vars` | Non-secret configuration shared across workflows | Credentials, tokens or values that must stay out of logs |
| `secrets` | Credentials and tokens | Configuration; direct use in `if:` conditionals |

- Prefer typed reusable-workflow inputs with explicit defaults. Validate allowlisted values before they select a target, command or path; an input is data even when only trusted users can trigger the workflow.
- Pass only small results between jobs as job outputs. Large files belong in artifacts, and an output from a job that processed untrusted code is untrusted input.
- Scope `env` as narrowly as the step allows. Mapping a secret into `env` makes it available to that process, so do not place credentials at workflow scope merely for convenience.
- `vars` are readable configuration, not a secret store and not proof of authorization. A change outside the repository can change them.
- Treat `secrets` as credentials: do not echo them, pass them as command-line arguments where avoidable, or expose them to arbitrary change code. Secret masking is a safeguard, not permission to print. Token permissions are separate from environment data: a token in `env` is still a credential, and its scopes come from the workflow's `permissions`.
- Do not use workflow command files as a general data bus. Validate keys and use a file when the value is arbitrary; embedded delimiters can otherwise create unintended assignments.

## Map expressions before the shell sees them

`${{ ... }}` is expanded into the workflow definition before the runner starts the shell. It is textual substitution, not a variable reference, so interpolating event data directly into `run:` (for example a pull-request title) makes that value part of the script.

Map the value into `env`, validate it, then quote the shell expansion:

```yaml
- name: Verify selected scope
  shell: bash
  env:
    TARGET_SCOPE: ${{ inputs.scope }}
  run: |
    set -euo pipefail
    case "$TARGET_SCOPE" in
      application|infrastructure) ;;
      *) echo "Unsupported scope: $TARGET_SCOPE" >&2; exit 2 ;;
    esac
    make verify SCOPE="$TARGET_SCOPE"
```

- Never interpolate attacker-influenced event data into `run:`, `script:` or a generated command: PR titles and bodies, refs, commit messages, issue or review text, release names, dispatch inputs and outputs from jobs that processed untrusted code. Mapping into `env` prevents the value from becoming script syntax but not from being untrusted: validate it, quote it and reject values that do not match the expected shape.
- Use allowlists for values that select a target or command. Resolve paths against a known root and reject escapes; do not let an input choose an arbitrary command.
- Do not use `eval`, reconstruct an argument string or build a command by concatenation. Pass values as separate arguments and use arrays or `"$@"`.
- Values in `with:` are action arguments rather than shell syntax, but the receiving action may still use them in a shell. `run-name` and `if:` are expression contexts. None of these makes untrusted text trusted, so validate the contract, pin the action, and keep secrets out of rendered output.

## Make shell steps fail honestly

- Select the shell explicitly when the workflow depends on it. Do not assume Bash on Windows or a particular default shell across runners.
- Use `set -euo pipefail` for Bash entrypoints, then account for the cases it does not cover: substitutions, pipelines, conditionals and commands whose nonzero status is expected. Check expected failures with `if ! command; then ... fi` rather than relying on `set -e` to produce the right message.
- Quote expansions (`"$value"`), use `"$@"` and arrays, and put `--` before paths that may begin with `-`. Keep stdout for the documented result and send diagnostics to stderr.
- Preserve the original failure through cleanup. A trap that removes owned temporary work should re-exit with the captured status:

```bash
tmp_dir="$(mktemp -d)"
trap 'status=$?; rm -rf "$tmp_dir"; exit "$status"' EXIT
```

- Never enable `set -x` in a step that handles secrets. Do not upload shell traces or diagnostic bundles without reviewing their contents.
- Keep inline shell short. Move branching, cleanup, structured data and reusable behavior into a checked-in script, then call it through a thin step. Use [script selection](script-selection.md) for the form and `bash-engineering` for the shell contract.

## Choose execution features deliberately

| Feature | Decision |
| --- | --- |
| Matrix | Vary real dimensions such as OS, runtime or supported version. Name expanded jobs with their values, choose failure isolation from whether one failure invalidates the rest, bound parallelism against shared resources, and keep required checks present for every required combination. |
| Concurrency | Group by the mutable resource (source line, environment, deployment target or infrastructure state), not workflow name. Cancel superseded validation; serialize releases, migrations and deployments. Workflows that mutate the same resource need the same group. |
| Permissions | Declare a minimal top-level default and grant per job. Give token-minting rights only to the identity job. Separate validation, publication and deployment identities. |
| Caching | Key on runner OS, toolchain version and lockfile content. Treat restore keys as fallback, not proof of freshness. Prevent untrusted changes from writing a cache consumed by a privileged release; disable cache reads there. Caches are disposable. |
| Artifacts | Upload only files another stage needs, with a unique name and bounded retention. Fail when expected files are missing. Verify a digest before promotion. Treat an artifact crossing a trust boundary as untrusted input. |
| Timeouts | Bound jobs and long steps against real workload duration and network waits. An unbounded step can hold a runner and a concurrency slot indefinitely. |
| Retries | Retry only operations that are idempotent or explicitly reconciled. Do not blindly retry a deployment, migration or publication that may have partially applied. A rerun reuses the original revision and payload; reconcile target state before resuming. |

## Reuse at the right boundary

| Construct | Owns | Use when |
| --- | --- | --- |
| Reusable workflow | Jobs, permissions, environments, secrets, outputs | Several workflows need the same job graph or deployment contract |
| Composite action | Steps inside the caller's job | Several jobs need the same sequence of steps and tools |
| Code action | Substantial host API or structured-data logic | Shell would become a program; the action needs typed inputs and tests |
| Container action | A packaged runtime and tools | The tool environment must be reproducible and Linux execution is acceptable |

- Reusable workflows declare typed inputs, outputs and named secrets. `secrets: inherit` is broad; pass only what the called workflow needs. Permissions can be maintained or reduced through the chain, not elevated. Environment protection belongs to the called workflow's own job; caller inputs are data, not authorization.
- Composite actions run with the caller's job identity and token and cannot grant their own permissions. Give each `run:` step an explicit `shell`, declare inputs and outputs, and keep local scripts thin and testable.
- Keep reusable-workflow interfaces stable. Add optional inputs rather than renaming or changing defaults; check callers before changing an output or failure behavior.
- Pin third-party actions and reusable workflows to an immutable revision under the project policy. A tag or branch is mutable. A local action is still code in the trust boundary; review it like application code.

## Make identity and recovery explicit

- Use `environment:` for protection rules, environment-scoped secrets and variables, and deployment records. Approval is an authorization control for that job, not a substitute for least privilege or target validation.
- Prefer OIDC or another short-lived federation mechanism to long-lived cloud keys. Restrict the cloud trust policy by repository, ref, environment and audience; verify the provider's current subject-claim format, and mint the token only in the job that needs it.
- Identify the artifact and the target separately. Promote the same artifact; keep configuration and credentials with the environment. A successful deployment job is not proof that the target serves the intended revision.
- Design recovery before promotion: retain the previous artifact and configuration, identify compatibility constraints, expose a rollback or roll-forward input, and verify the recovery path in a safe environment.

## Verify with distinct evidence

- Run `actionlint` on changed workflows for syntax, expression types, action and reusable-workflow interfaces and some injection patterns, and `zizmor` for static security audits such as template injection, excessive permissions, mutable references and cache poisoning. Pin the versions CI uses. Neither linter executes the workflow; linting, resolving expressions and rendering the graph establish only those stages.
- Execute at a representative boundary: a branch run, a manual dispatch in a safe environment, or a dry run with the same inputs. Inspect status, logs, outputs, artifacts, summaries and cleanup. Exercise failure, cancellation and rerun behavior where those are the claim.
- Verify identity separately: the scopes actually granted, the OIDC claims the provider received, and the target revision served. A permissions block or trust policy in source proves configuration, not the effective grant. Record authored, linted, executed-on-host and outcome-verified states separately. When security is material, use `github-actions-hardening` for the threat-model review rather than treating a linter pass as a security assessment.

## Sources

- GitHub, [workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [variables](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/store-information-in-variables) and [workflow commands](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands).
- GitHub, [using secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets), [secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) and [OpenID Connect](https://docs.github.com/en/actions/concepts/security/openid-connect).
- GitHub, [reuse workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows), [deployment environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments) and [custom actions](https://docs.github.com/en/actions/concepts/workflows-and-actions/custom-actions); [actionlint](https://github.com/rhysd/actionlint) and [zizmor audit rules](https://docs.zizmor.sh/audits/).
