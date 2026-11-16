# Script and action selection

Choose the smallest form that keeps the behavior testable and the trust boundary visible. The workflow step should be an adapter; the logic should have a home where it can run, fail and be tested outside CI.

## Options

| Form | Strength | Cost and constraint |
| --- | --- | --- |
| Inline shell in a step | Fewest moving parts; easy to inspect | Poor home for branching, cleanup, data modeling or reuse; runner shell differences |
| Checked-in shell script | Runs locally; ShellCheck and fixture tests; stable interface | Requires a shell and the tools it assumes; portability is limited |
| Checked-in Python or Node/TypeScript script | Structured data, parsers, HTTP clients, unit tests | Adds a runtime and dependency lock; startup and packaging matter |
| Composite action | Packages shared steps with declared inputs/outputs | Runs in the caller's job and token; no independent permissions; every `run:` needs a shell |
| JavaScript/TypeScript code action | Typed inputs, host API client, tested packaged logic | Bundling and Node runtime constraints; action code is privileged code |
| Container action | Reproducible toolchain and OS dependencies | Linux-only for Docker actions; image pull/build latency; image pinning and architecture |

## Decision criteria

| Criterion | Prefer | Reason |
| --- | --- | --- |
| Host API work (checks, PR comments, releases, pagination) | Code action, or `actions/github-script` for a genuinely small script | Token handling, typed responses and retries belong in code; scraping CLI text or HTML is brittle |
| JSON/YAML manipulation | Structured parser: `jq` for a simple query, Python/Node when logic or schema validation grows | Quoting, escaping and nested data break ad hoc `grep`/`sed` pipelines |
| Cross-platform behavior | Node/Python script, or a composite action with explicit per-OS steps | Bash and GNU coreutils are not portable to Windows runners |
| Testability | Checked-in script first; action wrapper second | The script can run with fixtures locally; the wrapper only maps inputs and outputs |
| Reuse across jobs | Composite action for steps; reusable workflow for jobs, permissions and environments | Reuse the boundary that actually repeats; do not wrap a whole job in a composite action |
| Dependency surface | Shell for orchestration; a locked runtime for real logic | Every runtime and third-party action adds supply-chain and upgrade work |
| Trust boundary | Code you own and pin; third-party actions only after review | An action executes with the caller's token, workspace and secrets |
| Startup/latency | Shell or code action before a container action | Container pull/build cost is justified by environment fidelity, not convenience |
| Output contract | Emit a small machine-readable result; keep logs separate | Downstream jobs and summaries need stable values, not parsed prose |

## Defaults that hold up

- One to three commands with no branching can stay inline. Move to a checked-in script when the step grows branches, loops, traps, structured data or a second caller.
- Do not implement API pagination, release creation or comment management in shell. Use an action or a small tested program with the host API.
- Do not parse JSON with `grep`, `cut` or `sed`. Use a parser and validate the expected shape before acting on it.
- Prefer one portable script over parallel Bash/PowerShell implementations unless the platform behavior genuinely differs. When it does, keep the platform split explicit and test both.
- A composite action is a packaging boundary, not a security boundary. It inherits the job's permissions; it cannot reduce them.
- A reusable workflow is the right boundary for job-level permissions, environments, secrets and outputs. Its interface is public to callers, so evolve it additively.
- Pin third-party actions and container images. Vendor or lock the dependencies of code actions and verify the published bundle matches source.
- If the logic needs a secret, pass it as an environment variable or typed input to the smallest unit that needs it. Do not put credentials in command arguments, logs or generated scripts.

## Safe shell step

Map expressions into `env`, validate selectors and quote the expansion. This is a step fragment, not a complete workflow.

```yaml
- name: Publish selected artifact
  shell: bash
  env:
    TARGET_ENVIRONMENT: ${{ inputs.environment }}
    ARTIFACT_PATH: ${{ inputs.artifact-path }}
    RELEASE_TOKEN: ${{ secrets.RELEASE_TOKEN }}
  run: |
    set -euo pipefail
    case "$TARGET_ENVIRONMENT" in
      staging|production) ;;
      *) echo "Unsupported environment: $TARGET_ENVIRONMENT" >&2; exit 2 ;;
    esac
    case "$ARTIFACT_PATH" in
      /*|*..*) echo "Artifact path must stay inside the workspace" >&2; exit 2 ;;
    esac
    if [[ ! -f "$ARTIFACT_PATH" ]]; then
      echo "Artifact not found: $ARTIFACT_PATH" >&2
      exit 1
    fi
    ./scripts/publish.sh --environment "$TARGET_ENVIRONMENT" --artifact "$ARTIFACT_PATH"
```

`RELEASE_TOKEN` is available to the publish script through the environment; it is not interpolated into the command line. The script owns validation, the HTTP contract and exit semantics. The step owns input mapping and the human-readable name.

## Verify the chosen form

- Run the script locally with representative and invalid inputs, including empty values, spaces, a missing file and an expected nonzero status.
- Run ShellCheck for shell, the language's tests and type checks for a program, and `actionlint` for the workflow or action wrapper.
- Test the installed entrypoint and the actual caller, not only a sourced helper. For a composite or code action, verify declared inputs/outputs and the metadata table against behavior.
- Exercise the target runner OS and architecture when portability is claimed. A local macOS run does not establish a Linux container action or a Windows PowerShell step.
- For a security-sensitive action, review it with `github-actions-hardening` and run `zizmor` on its workflow/action definitions; a linter pass is not execution evidence.

## Sources

- GitHub, [About custom actions](https://docs.github.com/en/actions/concepts/workflows-and-actions/custom-actions) and [Metadata syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).
- GitHub, [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use).
- [actionlint](https://github.com/rhysd/actionlint) and [zizmor audit rules](https://docs.zizmor.sh/audits/).
- Repository guidance: [Bash engineering](../../bash-engineering/SKILL.md) and [workflow authoring](workflow-authoring.md).
