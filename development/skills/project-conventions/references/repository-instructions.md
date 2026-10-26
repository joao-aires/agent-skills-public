# Maintain repository instructions

Use this method when creating, auditing or pruning AGENTS.md, CLAUDE.md or an equivalent project instruction file, or when a change makes its existing commands and conventions stale. Keep the work inside the requested repository and files. General documentation upkeep does not require a repository-wide instruction audit.

## Establish what the next contributor needs

Inspect the applicable instructions before editing them. Check the repository's manifests, lockfiles, command definitions, CI and canonical contributor, architecture and security documentation. Follow the development path far enough to identify its prerequisites and the conventions that are easy to miss. Existing code can show a pattern; an isolated workaround does not establish that it is required.

Evaluate each candidate instruction by asking what future action it changes. Useful content includes a working command, an unusual prerequisite, an ownership boundary, a generated-file rule or a pointer that saves reconstructing the project. Keep enough context to understand when it applies. General quality advice and facts obvious at the point of use seldom earn space in broadly loaded instructions.

## Choose the scope and canonical home

| Information | Appropriate home |
| --- | --- |
| Durable rules and working-command pointers applicable throughout the repository | Root project instructions. |
| Different commands or conventions for a component | Scoped instructions near that component, preserving applicable parent rules. |
| A substantial setup, architecture, testing or release procedure | Its existing canonical document, linked from instructions where needed. |
| Personal preferences or machine-specific details | The user's established local mechanism, only when that location is in scope. |
| Temporary investigation, work status or a proposed decision | The existing work record or conversation until it becomes durable accepted knowledge. |

Confirm the actual client's supported filenames, discovery and instruction precedence before changing compatibility entry points. Do not assume that all clients load the same files or interpret nested files identically. Preserve existing compatibility files and their additional content; introduce a link, import or shared source only when the host supports it and the request needs it. Keep one maintained source for each shared rule where practical.

## Audit and revise the existing guidance

Read each in-scope file against the repository, then decide whether its information is current, useful, correctly scoped and sufficiently precise. Follow linked procedures as needed; a missing command in AGENTS.md may already have a good canonical home. Identify contradictions and resolve them against accepted project decisions rather than silently selecting whichever statement is shorter.

For a command, check the executable definition, working directory and prerequisites. Run appropriate authorized local checks when that is useful and feasible. Label static inspection separately from execution; deployment commands, account access and destructive operations do not become authorized merely because they appear in a document. Verify referenced paths and keep secrets out of examples.

Make targeted changes: correct stale facts, move detailed procedures to their owner, consolidate repetition and remove superseded guidance. Explain the reason for consequential changes in the reviewable diff or change description. Preserve required project constraints while shortening; line limits and sample sections are editing aids, not reasons to discard useful knowledge. Use tables or bullets for lookup and short explanations where a rule's condition or rationale would otherwise be unclear.

## Decide which session learnings should persist

Before promoting a discovery or correction into project instructions, establish:

- **Evidence:** the command, behavior or accepted decision is supported by the repository or an actual check.
- **Durability:** it is likely to remain true beyond the current task or environment.
- **Usefulness:** it changes how future contributors work or prevents a recurring misunderstanding.
- **Ownership:** it belongs in this scope and is not better expressed by existing documentation, configuration or an executable check.

A recurring failure may reveal a missing prerequisite or a general invariant. Record that cause and its applicability, rather than the incident history or an instruction to repeat a one-off workaround. Keep proposed preferences separate from accepted policy. Update existing guidance instead of appending another competing rule.

## Check the result

Trace an ordinary contributor task through the revised instructions and their links. Confirm that required commands and constraints remain findable, scoped rules do not unnecessarily repeat their parents, and compatibility entry points agree where they share information. Return the files changed, important rationale, checks actually performed and unresolved contradictions. An assessment-only request ends with findings; an authorized editing request can apply the targeted corrections without another approval ceremony.
