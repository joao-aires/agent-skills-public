# Maintain upstream skill snapshots

Use Agent Depot to acquire and update third-party skills. Their unmodified files are committed under `plugins/<owner>/skills/<name>/`, alongside authored skills. Ordinary plugin builds use these files offline and apply the collection’s adaptations only to generated output.

## The records and their owners

| Record | Purpose |
| --- | --- |
| [agent-depot.json](../../agent-depot.json) `sources` | Declare each upstream repository once |
| Manifest `artifacts` | Pin each skill’s accepted commit, upstream root, local destination and external license/resource mappings |
| Each artifact’s `metadata.packaging` | Record that skill’s plugin owner, license attribution, allowlisted adaptations and usage labels beside its pin and destination |
| [agent-depot.lock.json](../../agent-depot.lock.json) | Record accepted declarations, file hashes, executable modes and inspection |
| [tooling/agent-depot.json](../../tooling/agent-depot.json) | Pin the maintenance CLI source revision, independently of acquired skills |

Several artifacts can reference one source at different commits. Every artifact has an explicit accepted `commit`. Optional `track` specifies where to look for candidates, such as `{ "branch": "main" }`, without changing the accepted pin. Artifacts without tracking remain pinned; scheduled discovery does not guess a branch or upgrade them.

Keep managed snapshots unchanged. Put the collection's methods and workflow expectations in authored companion skills or package framing, preserving the acquired method as an independently reviewable dependency. An authored activity can select compatible expertise or explain project constraints without replacing the upstream text. Do not edit a lockfile to accept local drift.

Existing builds also apply the declared output adaptations: these include framing and metadata as well as content rewrites such as tracker prerequisites. Snapshot integrity does not mean the generated skill is byte-identical to upstream. Review those transformations against each candidate update; wording-dependent replacements can fail when upstream changes. Keep new guidance in companions rather than adding another semantic rewrite. A packaging compatibility change still needs an explicit rationale, provenance and focused validation. Removing existing transformations requires preserving their applicable workflow and invocation behavior; it is a separate packaging change, not an implicit consequence of editing an authored skill.

## Prepare the maintenance CLI

Snapshot maintenance requires Git and Node.js 22.12 or newer. Agent Depot is currently used from its reviewed source commit because its npm package has not been released. In the collection root:

```bash
git clone https://github.com/joao-aires/agent-depot.git .agent-depot/tool
git -C .agent-depot/tool checkout --detach "$(node -p "require('./tooling/agent-depot.json').commit")"
npm --prefix .agent-depot/tool ci --ignore-scripts
npm --prefix .agent-depot/tool run build
node .agent-depot/tool/dist/cli.js --json verify
```

Reuse an existing tool checkout only after checking that it has no local work to lose; fetch and select the declared commit there. `.agent-depot/` is ignored local tool/cache/transaction state. Preserve its transaction records until recovery is complete. CI builds the same pinned tool through a shared setup action. Tool installation can need network access; the subsequent `verify` operation does not fetch or repair snapshots. Normal Python builds require neither this CLI nor Node.js.

To update the CLI pin, review its command and persisted-format compatibility, change `tooling/agent-depot.json`, and run CI against that exact revision. A source pin does not publish an npm package. Adoption of a released npm version can replace this bootstrap in a separate toolchain change.

## Add a skill

1. Review the upstream method, required resources, redistribution terms and its fit with the owning plugin. Reuse an existing repository source ID where applicable.
2. Declare the artifact in `agent-depot.json` with a full accepted commit and the destination `plugins/<owner>/skills/<upstream-name>`. Add an explicit resource mapping for a required external license, usually to `UPSTREAM-LICENSE.txt`. Preserve every resource inside the selected skill root.
3. Add `metadata.packaging` inside the artifact object; use the fields below. Preserve complete groups of mutually required skills. A necessary packaging compatibility exception needs an explicit rationale and focused tests; collection-specific guidance belongs in authored companions.
4. In an established collection, prepare and apply a plan. `lock` followed by `sync` is for initial acquisition, not a way to bypass reviewed changes to accepted snapshots.

```bash
node .agent-depot/tool/dist/cli.js plan --output /tmp/upstream-candidate.json
node .agent-depot/tool/dist/cli.js diff /tmp/upstream-candidate.json --patch
node .agent-depot/tool/dist/cli.js update --plan /tmp/upstream-candidate.json
node .agent-depot/tool/dist/cli.js verify
```

Use a new plan filename each time. Add a `-text` rule for the managed destination in `.gitattributes` so Git preserves upstream bytes across platforms. Update catalogue entries, ownership and package versions when distributed content changes. Commit the declaration, lock, snapshots, attributes and consumer changes together.

## Packaging annotations

Each artifact owns its packaging annotations. These fields are this collection's contract, not a schema interpreted by Agent Depot:

| Field inside `artifacts.<id>.metadata.packaging` | Meaning |
| --- | --- |
| `plugin` | Owning plugin; must match the destination |
| `license` | Nonempty attribution used in generated notices |
| `license_path` | Upstream license location, or `null` when the skill frontmatter provides it |
| `adaptations` | Names of the builder's allowlisted output transformations |
| `labels` | String-valued usage labels applied to generated skills |

Keep unrelated artifact annotations alongside `packaging`, and reserve root `metadata` for repository-wide information. The builder validates the packaging fields it consumes and ignores unrelated annotations; Agent Depot preserves both without interpreting their semantics. Do not maintain a second root packaging map.

For a metadata-only change, edit the artifact, prepare a plan, inspect its `metadataChange` before/after values, then apply it and run verification and packaging checks. Verified snapshots are reused without fetching or rewriting their files; accepted commits and content digests stay unchanged. Tracking discovery for other unchanged artifacts can still need upstream access, so select the edited artifact when appropriate. Metadata can alter labels, adaptations and notices in the distributed plugin: inspect the effective output and bump its version if that output changes. Moving existing annotations without changing output does not require a package version bump.

## Review an update

For a chosen artifact, request an exact candidate without editing its accepted snapshot:

```bash
node .agent-depot/tool/dist/cli.js plan \
  --artifact development--code-review \
  --to <full-candidate-commit> \
  --output /tmp/upstream-candidate.json
```

For artifacts with tracking policies, use `outdated --json` to discover changes and `plan --artifact <id>` or `plan --source <id>` to prepare candidates. These filters control tracking discovery; existing declaration edits still appear in the plan. Review the exact commit and diff, including resource removals, license changes, invocation controls and changed instructions or assumptions. An unchanged skill should not advance merely because unrelated upstream files changed.

Apply the reviewed plan, bump the owning plugin version, and run snapshot verification plus the [collection checks](../maintainer-reference.md#maintaining-the-collection). Build into a new directory and inspect the effective adapted output, not only raw upstream Markdown. Integrity and packaging checks cannot decide whether new instructions are suitable or whether agent behavior improved. Run behavioral evaluations when that change warrants them; keep runtime/client setup within the requested scope.

Commit and review changes before merging. Revert the declaration, lock and snapshots together if an accepted update must be undone. `sync` restores missing locked snapshots; it does not upgrade or overwrite edited directories. For an interrupted operation, stop the earlier process and use `recover`; preserve subsequent edits if recovery reports a conflict.

## CI maintenance

Regular CI builds the pinned CLI and verifies committed snapshots offline before the existing package checks. Python packaging independently checks selected snapshot bytes, executable flags where supported, inventories and declaration alignment. Raw upstream metadata is preserved; the generated adapted skills receive the collection’s full metadata validation.

The upstream-maintenance workflow runs from trusted `main` on a schedule or manual dispatch. With no inputs, it checks only declared tracking policies. The initial collection uses fixed commits, so scheduled runs report pinned artifacts without preparing upgrades. Manual dispatch can supply an artifact ID and full candidate commit; this path skips tracking discovery for unrelated sources. Eligible updates produce an exact plan, update snapshots, bump owning package patch versions, run checks and prepare a review PR. The job never auto-merges or installs plugins into a coding agent.

Discovery and plans are retained as workflow artifacts. GitHub Actions must be allowed to create PRs. A PR created with the default `GITHUB_TOKEN` may not trigger another CI run; candidate validation in the maintenance workflow is required, and branch-policy checks must still be satisfied before merge. Inspect semantic and licensing changes yourself. This workflow does not automatically classify breaking instruction changes or claim that deterministic checks replace behavioral review.
