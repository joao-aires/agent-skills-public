# Focused quality checks

Use the tools matching the repository, preserving established alternatives. Author configuration in the target application; this collection does not install hooks or wrap Super-Linter.

| Concern | Starting point | When |
| --- | --- | --- |
| Python | [Ruff](https://docs.astral.sh/ruff/), chosen type checker | Affected files during implementation; required project checks in CI |
| JavaScript/TypeScript | [ESLint](https://eslint.org/docs/latest/use/), project formatter, TypeScript | Affected files and relevant type/build boundary |
| YAML | [yamllint](https://yamllint.readthedocs.io/en/stable/) | Changed YAML, preserving workflow/template semantics |
| GitHub Actions | [actionlint](https://github.com/rhysd/actionlint) | Workflow changes and CI validation |
| Shell | [ShellCheck](https://www.shellcheck.net/) | Actual shell scripts; account for the selected shell |
| Secrets | [Gitleaks](https://github.com/gitleaks/gitleaks) | Staged changes locally; defined diff/full-history boundary in CI |
| Local hook orchestration | [prek](https://prek.j178.dev/quickstart/) | Fast commit-stage checks and explicit whole-project runs |

For a repository already configured with prek, `prek run` checks staged files; `prek run --all-files` checks the configured whole-project boundary. Verify installed-version semantics before setup. Keep remote hook revisions pinned. A secret scan must include the intended staged/new files and redact values; verify scope with synthetic fixtures rather than real credentials. Report pre-existing findings separately and review narrow exceptions.

A failure should identify the tool, affected file/rule and command to reproduce without exposing secret content. Fix intended changes, rerun, inspect formatter diffs and preserve partial staging. Installing guidance does not authorize changing global hook settings or disabling CI protections.
