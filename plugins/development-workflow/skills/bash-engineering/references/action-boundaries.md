# Bash behind reusable CI interfaces

Use a thin wrapper to map typed CI inputs into environment variables and quoted script arguments. Script logic remains locally runnable; host outputs/grouping belong to an explicit adapter. If the skill is used outside CI, none of these host details are required.

## Action and workflow choices

| Construct | Appropriate role |
| --- | --- |
| Composite action | Compose existing steps/tools with small local glue |
| Reusable workflow | Coordinate jobs, identity/permissions, runners and outputs |
| Node/code action | Substantial host API logic and structured data |
| Container action | Packaged runtime/tools with declared platform constraints |
| Standalone Bash | Reusable command orchestration invoked by local/CI callers |

Document action input/output/default/failure behavior and dependencies. Workflow interfaces are public contracts: additive optional changes, compatibility checks and deliberate versioning. Check all callers before renaming outputs or changing defaults.

## Adapter example

```yaml
- name: Validate target
  shell: bash
  env:
    ACTION_PATH: ${{ github.action_path }}
    TARGET_DIRECTORY: ${{ inputs.directory }}
  run: |
    set -euo pipefail
    bash "$ACTION_PATH/validate.sh" --directory "$TARGET_DIRECTORY"
```

A step fragment for a composite action. Environment mapping prevents event/input content becoming generated shell syntax; the script still validates path scope and options. Do not interpolate an action path or user expression directly into shell, or use `eval` to reconstruct arguments.

Keep machine results distinct from log lines. For GitHub file-command outputs validate keys and use the documented multiline protocol when necessary; an untrusted newline can otherwise introduce unintended assignments. Do not emit raw user content as workflow commands. Mask secrets as defense in depth, but never deliberately print/export them as public outputs.

## Reusable validation chain

Discover targets -> render -> schema validation -> policy audit -> semantic/behavior tests. Track counts and skipped targets/schemas. Failures from every producer/consumer must propagate. A YAML file syntactically valid or a linter passing does not establish safe runtime behavior.

For bundled code actions, build/test with the declared lockfile and ensure published bundles match source. Align local builder, action runtime and supported runner platforms. A validation helper must include untracked/deleted/generated changes relevant to the artifact; looking only for modified tracked files can miss drift.

Use `build-delivery-pipelines` for pipeline/release design. This skill owns shell behavior and the shell/host boundary, not the full delivery lifecycle.
