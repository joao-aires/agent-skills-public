# Prose review: sentence-level pass for any document

Run this before committing prose this repository authors: documentation, READMEs, skill bodies, artifact contracts, commit messages and pull requests. [Writing for agents](../../writing-for-agents/SKILL.md) owns the instruction-writing principles; this reference applies them to any reader.

## The pass

- **Open with the action.** The first sentence says what the document does and who it serves. For a skill, it also says where the skill stops.
- **One idea per sentence.** Split semicolon chains and clauses that carry two rules. A sentence that needs the previous one to make sense is two sentences.
- **Positive before prohibition.** State the behaviour to produce. Keep a prohibition only as a hard guardrail, and pair it with the action that replaces it.
- **Delete sediment.** Remove "formerly", "retired", "was once", version archaeology and sentences that explain the repository to itself. Keep the rule, not the history.
- **Do not restate an owner.** If another skill, contract or reference already states a rule, link it once at the branch instead of repeating it.
- **Keep the obligations.** Compression must not remove an acceptance criterion, authority boundary, evidence limit, caveat or link.

## Form-specific checks

| Writing | Add |
| --- | --- |
| Skill | The first sentence states the job and stopping point; declarations stay in `## Composition` |
| Documentation | The reader's question comes first; the artifact contract still owns required content |
| README | State what the package does and does not own before the skill table |
| Contract or guide | Never drop a required record field to make the prose shorter |
| Commit or PR | The subject says why; the body states what changed, what was checked and what is open |

## File mechanics

Markdown conventions — one paragraph per line, blank lines between blocks, headings, lists, tables, code fences and links — live in [Formatting and layout](formatting-and-layout.md#markdown-file-conventions). A project config such as `.markdownlint.*` or `.editorconfig` overrides them.
