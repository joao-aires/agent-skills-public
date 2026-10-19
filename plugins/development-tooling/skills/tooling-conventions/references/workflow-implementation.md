# Workflow implementation conventions

CI is orchestration; task runners own reusable build logic. These conventions generalize existing CI authoring practice. Check current host/runtime documentation when implementing a provider-specific adapter.

## Trust, interfaces and permissions

- Give each job only the permissions needed; separate checks, publication, release writing and deployment identities.
- Prefer supported short-lived federation/workload identity. Never expose release secrets to untrusted source, forks or privileged workflows checking out arbitrary PR code.
- Treat input values, branch names, PR titles and other event data as untrusted. Map GitHub expressions into environment variables and quote them in shell; use allowlists when values select targets or commands.
- Do not pass secrets through build arguments/layers, unrestricted artifacts or diagnostic command output. Secret masking is a final safeguard, not permission to print a secret.
- Pin action revisions, toolchains and dependency locks according to the supply-chain policy. Verify updates; `latest` and floating internal branches are not immutable references.
- Scope caches by trust/toolchain/lock inputs and prevent untrusted caches from poisoning privileged builds.

## Names and source locations

Keep GitHub Actions entrypoints in `.github/workflows/` and application scripts/Dockerfiles beside their owner. For new workflows, prefer `<activity>-<application>.yml` such as `ci-api.yml`, `release-api.yml` and `deploy-api.yml`, with display names such as `CI / API` and `Deploy / API`. Use descriptive lowercase job IDs and short verb-object step names; include target/artifact identity in deployment runs. Preserve a consistent existing convention.

## Workflow structure

Document typed inputs, defaults, secrets, outputs and failure semantics. Optional additive inputs are easier to evolve; renaming/removing/changing a default can break consumers. Reusable workflows orchestrate jobs; composite actions usually suit shared steps; code actions suit substantial host API logic; container actions suit packaged tool environments.

Use a dependency DAG and explicit outputs. A release must depend on all required gates rather than just the build job. Path filtering must not leave a required check permanently pending or skip changes to shared build/dependency files.

For GitHub shell glue:

```yaml
- name: Verify selected scope
  env:
    TARGET_SCOPE: ${{ inputs.scope }}
  run: |
    set -euo pipefail
    case "$TARGET_SCOPE" in
      application|infrastructure) ;;
      *) exit 2 ;;
    esac
    make verify SCOPE="$TARGET_SCOPE"
```

This is a step fragment, not a standalone workflow. Resolve the build contract before use. Do not interpolate values directly into generated shell/JavaScript commands. Test script exit codes, quoting and cleanup paths with the project's linters.

## Concurrency and reliability

Group by the shared mutable resource: source release line, config branch, deployment target or infrastructure state. Different workflow names may mutate the same resource and therefore need the same lock/group. Use non-cancelling serialization for active mutations. Keep timeouts, retries and runner choices aligned with workload duration and side effects; retry only safe or idempotent operations.

Use job summaries and artifacts to show inputs, source revision, artifact digest, checks and target. Do not rely on scraping a log for the last SHA-shaped string. Capture task/tool metadata directly.

## Validation

Run the same native verification locally, host-specific lint (for example actionlint), format/schema checks and workflow-interface tests. Exercise dry-run version calculation, existing-tag handling, hotfix propagation, untrusted-PR behavior and partial-failure resumption. Only call a gate enforced when its outcome actually blocks promotion/merge under the project's policy.

Provider-specific CI configuration belongs in the target repository and uses its selected host; the portable skill does not require GitHub Actions or Make.

## Reusable implementation patterns

Use thin composite adapters around locally runnable scripts, shared tool checks/setup steps with declared capabilities, and reusable workflow chains that render, validate and audit resources. Data-heavy host API operations suit code actions; packaged tools can use container actions with explicit architecture/runtime constraints. Keep action metadata and README input/output/default/failure tables synchronized.

Bundled code-action artifacts need locked dependency installation, source tests and generated-bundle consistency in CI. Check untracked/deleted changes as well as modified tracked files and align builder/runtime versions. Reusable workflow defaults such as skipping unavailable schemas can preserve compatibility but must expose coverage limitations; they are not a universal validation standard.

For shell implementation and adapter contracts use `bash-engineering`; for rendered-resource semantics use `kubernetes-resource-engineering`. These tasks remain separate from overall release/branching design.
