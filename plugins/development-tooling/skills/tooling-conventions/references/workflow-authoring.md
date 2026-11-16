# Workflow authoring

Use this reference when creating or changing a CI workflow: naming, data flow, shell boundaries and the execution features that determine reliability. It assumes GitHub Actions syntax but keeps the decisions applicable to another host. For adapter/trust details read [workflow implementation](workflow-implementation.md); for a focused security review load the installed `github-actions-hardening` skill.

A workflow is orchestration. Build, test, package and deployment logic belongs in commands and scripts that can also run outside CI. Keep the workflow responsible for selecting work, connecting identities, enforcing gates and recording evidence.

## Name the unit of work

- Name the workflow by purpose and component, with a deployment target when applicable: `ci-api.yml` / `CI / API`, `release-api.yml` / `Release / API`, `deploy-api.yml` / `Deploy / API`. Put target identity in the display name or `run-name`: `Deploy / API / production / eu-west-1`.
- Use descriptive lowercase job IDs. The ID is for maintainers and expressions; the job `name` is for the checks UI. Avoid `build1`, `job2` and IDs that restate the workflow name.
- Use short verb-object step names: `Run unit tests`, `Build image`, `Publish chart`, `Smoke test target`. Let the command, not the step name, carry flags and implementation detail.
- Make deployment identity visible without opening the log: environment, account/project/subscription, region/cluster/namespace, service and artifact version or digest. An environment name alone does not prove which target changed.
- Preserve a coherent existing convention. Renaming workflows, jobs or required checks is an interface change; update branch protection and callers deliberately.

## Give each value one owner

| Source | Use for | Do not use for |
| --- | --- | --- |
| `inputs` | Typed parameters from a caller or manual run | Secrets or ambient repository configuration |
| `env` | Values a process needs, scoped to workflow, job or step | Shared configuration owned outside the workflow; secret storage by default |
| `vars` | Non-secret configuration shared across workflows | Credentials, tokens or values that must stay out of logs |
| `secrets` | Credentials and tokens | Configuration; direct use in `if:` conditionals |
| Job outputs | Small results passed between jobs | Large files, artifacts or untrusted payloads used as trusted data |

- Prefer typed reusable-workflow inputs (`boolean`, `number`, `string`) with explicit defaults. Validate allowlisted values before they select a target, command or path; an input is data even when only trusted users can trigger the workflow.
- Scope `env` as narrowly as the step allows. Mapping a secret into `env` makes it available to that process, so do not place credentials at workflow scope merely for convenience.
- `vars` are readable configuration, not a secret store and not proof of authorization. A change outside the repository can change them.
- Treat `secrets` as credentials: do not echo them, pass them as command-line arguments where avoidable, or expose them to arbitrary change code. Secret masking is a safeguard, not permission to print.
- Secrets are not available to fork pull requests (apart from the read-only `GITHUB_TOKEN`), are not inherited by reusable workflows automatically, and cannot be referenced directly in `if:`. Map a secret to a job or step environment variable, then test that variable.
- Do not use `GITHUB_ENV`, `GITHUB_OUTPUT` or `GITHUB_STEP_SUMMARY` as a general data bus. Validate keys and use the documented multiline delimiter protocol; an untrusted newline can otherwise create unintended assignments. Prefer a file when the value is arbitrary.
- Keep `GITHUB_TOKEN` permissions separate from environment data. A token in `env` is still a credential, and its scopes come from `permissions:`.

## Map expressions before the shell sees them

`${{ ... }}` is expanded into the workflow definition before the runner starts the shell. It is textual substitution, not a variable reference. A value interpolated directly into `run:` can therefore become shell syntax.

```yaml
# Unsafe: the event value becomes part of the script
- run: echo "Reviewing ${{ github.event.pull_request.title }}"
```

Map the value into `env` and quote the shell expansion:

```yaml
- name: Verify selected scope
  shell: bash
  env:
    TARGET_SCOPE: ${{ inputs.scope }}
    SOURCE_REF: ${{ github.head_ref }}
  run: |
    set -euo pipefail
    case "$TARGET_SCOPE" in
      application|infrastructure) ;;
      *) echo "Unsupported scope: $TARGET_SCOPE" >&2; exit 2 ;;
    esac
    printf 'Verifying %s at %s\n' "$TARGET_SCOPE" "$SOURCE_REF"
    make verify SCOPE="$TARGET_SCOPE"
```

- Never interpolate attacker-influenced event data into `run:`, `script:` or a generated command. This includes PR titles and bodies, branch and tag names, commit messages, issue/comment text, review bodies, release names, `workflow_dispatch` inputs and outputs from jobs that processed untrusted code.
- Mapping into `env` prevents the value from becoming script syntax. It does not make the value trustworthy: validate it, quote it, and reject values that do not match the expected shape.
- Use allowlists for values that select a target or command. Resolve paths against a known root and reject escapes; do not let an input choose an arbitrary command.
- Do not use `eval`, reconstruct an argument string, or build a command by concatenation. Pass values as separate arguments and use arrays or `"$@"`.
- Values in `with:` are action arguments rather than shell syntax, which is safer, but the receiving action may still use them in a shell. Validate the contract and pin/review the action.
- `run-name` and `if:` are display or expression contexts, not shell sinks. They still must not expose secrets or let untrusted text masquerade as trusted status.

## Make shell steps fail honestly

- Select the shell explicitly when the workflow depends on it (`shell: bash`). Do not assume Bash on Windows or a particular default shell across runners.
- Use `set -euo pipefail` for Bash entrypoints, then account for the cases it does not cover: substitutions, pipelines, conditionals and commands whose nonzero status is expected.
- Quote expansions (`"$value"`), use `"$@"`, use arrays, and put `--` before paths that may begin with `-`. Keep stdout for the documented result and send diagnostics to stderr.
- Preserve the original failure through cleanup. A trap that removes owned temporary work should re-exit with the captured status rather than ending successfully:

```bash
tmp_dir="$(mktemp -d)"
trap 'status=$?; rm -rf "$tmp_dir"; exit "$status"' EXIT
```

- Check expected failures with `if ! command; then ... fi` rather than relying on `set -e` to produce the right message. Decide whether the next action remains valid after a failed command.
- Never enable `set -x` in a step that handles secrets. Do not upload shell traces or diagnostic bundles without reviewing their contents.
- Keep inline shell short. Move branching, cleanup, structured data and reusable behavior into a checked-in script, then call it through a thin step. Use [script selection](script-selection.md) to choose the implementation form and `bash-engineering` for the shell contract.

## Choose execution features deliberately

| Feature | Rule |
| --- | --- |
| Matrix | Vary real dimensions such as OS, runtime or supported version. Name the expanded jobs with their values, choose `fail-fast` from whether one failure invalidates the rest, bound `max-parallel` against shared resources, and keep required checks present for every required combination. |
| Concurrency | Group by the mutable resource (source line, environment, deployment target or infrastructure state), not merely by workflow name. Cancel superseded validation; serialize releases, migrations and deployments. Workflows that mutate the same resource need the same group. |
| Permissions | Declare a minimal top-level default (`permissions: {}` or `contents: read`) and grant per job. Add `id-token: write` only to the OIDC job. Separate validation, publication and deployment identities. |
| Caching | Key on runner OS, toolchain version and lockfile content. Treat restore keys as fallback, not proof of freshness. Prevent untrusted changes from writing a cache consumed by a privileged release; disable cache reads in release workflows where supported. Caches are disposable. |
| Artifacts | Upload only the files another stage needs, with a unique name and bounded retention. Fail when expected files are missing. Verify a digest before promotion. Treat an artifact downloaded across a trust boundary as untrusted input. |
| Job summaries | Record revision, artifact digest, gate results, target and skipped coverage. Summaries are for humans and are not a gate. Keep untrusted content out of rendered Markdown; a summary upload failure does not fail the job. |
| Timeouts | Set `timeout-minutes` on jobs and long steps. Align the bound with real workload duration and network waits; an unbounded step can hold a runner and a concurrency slot indefinitely. |
| Safe retries | Retry only operations that are idempotent or explicitly reconciled. Do not blindly retry a deployment, migration or publication that may have partially applied. A rerun reuses the original revision and event payload; reconcile tags, artifacts and target state before resuming. |

## Reuse at the right boundary

| Construct | Owns | Use when |
| --- | --- | --- |
| Reusable workflow | Jobs, permissions, environments, secrets, outputs | Several workflows need the same job graph or deployment contract |
| Composite action | Steps inside the caller's job | Several jobs need the same sequence of steps and tools |
| Code action | Substantial host API or structured-data logic | Shell would become a program; the action needs typed inputs and tests |
| Container action | A packaged runtime and tools | The tool environment must be reproducible and Linux execution is acceptable |

- Reusable workflows declare typed inputs, explicit outputs and named secrets. `secrets: inherit` is broad; prefer passing only the secrets the called workflow needs. Permissions can be maintained or reduced through the chain, not elevated. Set `environment` on the job inside the called workflow; the caller cannot supply it.
- Composite actions run with the caller's job identity and token. They cannot grant their own permissions. Give each `run:` step an explicit `shell`, declare inputs/outputs in `action.yml`, and keep local scripts thin and testable.
- Keep reusable-workflow interfaces stable. Add optional inputs rather than renaming or changing defaults; check callers before changing an output or failure behavior.
- Pin third-party actions and reusable workflows to an immutable revision under the project policy. A tag or branch is mutable. A local action is still code in the trust boundary; review it like application code.

## Make identity and recovery explicit

- Use `environment:` for protection rules, environment-scoped secrets/variables and deployment records. Approval is an authorization control for that job, not a substitute for least privilege or target validation.
- Prefer OIDC or another short-lived federation mechanism to long-lived cloud keys. Restrict the cloud trust policy by repository, ref, environment and audience; verify the provider's current subject-claim format. Request `id-token: write` only where the token is minted.
- Separately identify the artifact and the target. The same artifact should be promoted; configuration and credentials stay with the environment. A successful deployment job is not proof that the target serves the intended revision.
- Design recovery before promotion: retain the previous artifact/configuration, identify compatibility constraints, expose a clear rollback or roll-forward input, and verify the recovery path in a safe environment.

## Verify with distinct evidence

- Run `actionlint` on changed workflows. It checks workflow syntax, expression types, action and reusable-workflow interfaces, shell fragments and some injection patterns. Run `zizmor` for static security audits such as template injection, excessive permissions, mutable references, credential persistence and cache poisoning. Pin the tool versions used by CI.
- Neither linter executes the workflow. Linting a YAML file, resolving expressions and rendering a workflow graph establish only those stages.
- Execute the workflow at a representative boundary: a branch run, a manual dispatch in a safe environment, or a dry run that exercises the same inputs. Inspect job status, logs, outputs, artifacts, summaries and cleanup. Exercise failure, cancellation and rerun behavior where those are the claim.
- Verify identity separately: confirm the token scopes actually granted, the OIDC claims the provider received, and the target revision that was served. A permissions block or a trust policy in source proves configuration, not the effective grant.
- Record authored, linted, executed on the host, and outcome-verified states separately. When security is material, use `github-actions-hardening` for the threat-model review rather than treating a linter pass as a security assessment.

## Sources

- GitHub, [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) and [Store information in variables](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/store-information-in-variables).
- GitHub, [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) and [Using secrets in GitHub Actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets).
- GitHub, [Workflow commands](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands), [Reuse workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows) and [OpenID Connect](https://docs.github.com/en/actions/concepts/security/openid-connect).
- GitHub, [Dependency caching](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching) and [About custom actions](https://docs.github.com/en/actions/concepts/workflows-and-actions/custom-actions).
- [actionlint](https://github.com/rhysd/actionlint) and [zizmor audit rules](https://docs.zizmor.sh/audits/).
- Martin Fowler, [Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html), for fast feedback, a single verified mainline and a staged build.
