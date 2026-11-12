# Author GitHub Actions workflows

Name workflows for their purpose, jobs for the outcome they produce and authored steps for their action and object. For example, use “Verify pull request”, “Test Python package” and “Upload failure logs”. Check required status checks and reusable callers before renaming exposed checks or identifiers.

Use workflow expressions in declarative fields such as conditions, matrices and action inputs. For context values used inside a shell command, bind the expression through step-level environment variables and quote the shell expansion.

```yaml
- name: Record the source ref
  env:
    SOURCE_REF: ${{ github.ref_name }}
  shell: bash
  run: printf '%s\n' "$SOURCE_REF"
```

Treat each value as data. Use narrow environment scope and avoid logging secrets. Apply the repository's Actions hardening guidance when defining triggers, permissions or release jobs.

Keep short orchestration inline. Move reusable shell operations into checked-in Bash scripts with explicit inputs, checked failures and local invocation. Prefer JS or TS for complex structured data or API operations when the project can test and run that code locally. Use existing package scripts for project commands.

For PR verification, use the same build and test entry points as local development, keep names stable and preserve useful failure output. For a release, identify the exact artifact, promote it after required checks and verify the target. Run workflow validation and exercise the affected success and failure paths on an authorized runner. Use [GitHub workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) and [secure use guidance](https://docs.github.com/en/actions/reference/security/secure-use).
