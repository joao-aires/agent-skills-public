---
name: open-source-readme
description: Create or improve the public README for an open-source repository so readers can judge fit and reach a verified first result. Use for repository landing pages, quickstarts, demos and contributor navigation.
license: MIT
user-invocable: true
metadata:
  scope: generic
  invocation: both
  role: support
---

# Write the open-source README

Read the manifest, public entry points, examples and existing docs. Identify the primary reader, their job and the first result the current project can deliver. Open with a concrete promise and proof. For example, “Convert a folder of CSV exports into one Parquet file” gives a reader a task they can recognize and try.

| Repository | Show early | First result |
| --- | --- | --- |
| Library | Supported environment and a short example of the public API | Input, callable and expected output |
| CLI | One representative command and what it produces | Install, run with sample input and recognize success |
| Application | A representative task or screenshot with context | Open the app or start it locally and complete the task |

Start with prerequisites that change whether the quickstart can work. Keep commands in copyable order, identify required values and show the expected result. Say when the reader needs an account or credentials. Run the documented path from a clean environment when feasible and record what you verified. For existing projects, preserve supported entry points and accurate claims.

After the first result, help readers find deeper usage, configuration, limitations, support and contributing. Link to canonical docs and the license. Use a diagram when it clarifies how packages fit together. Use badges when they convey meaningful status and screenshots when they demonstrate actual behavior.

Review the rendered README from the perspective of a first-time reader. Can they explain what the project does, recognize whether it fits, and reach a first result? Check commands, relative links and captions. Use [documentation writing](../documentation-writing/SKILL.md) for deeper prose and structure decisions.

See [GitHub’s README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) for repository landing page conventions.
