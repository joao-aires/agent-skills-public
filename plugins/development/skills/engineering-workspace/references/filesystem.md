# Filesystem engineering workspace — first-class, optional Git-backed

Choose this when the project has an authorized directory separate from the application's source tree. It may be a sibling folder, a subfolder of a wider parent work area **outside the app repository**, or a standalone Git repository. Do not infer an arbitrary path and create it without authorization.

## Discovery and placement

1. Read the supplied working directory, applicable repository/project instructions, explicit artifact links, project docs and any already defined engineering root.
2. If an ECR exists, update it; never regenerate it under a new name because the title changes. Follow established folder conventions over the example below.
3. If creating a workspace is within scope but no root is known, propose a path and get authorization rather than writing outside the allowed working tree. If only a read-only task is authorized, deliver the structured result inline without persistence.
4. Preserve source-control separation: application `docs/` represents canonical implemented knowledge, not the draft ECR. The engineering workspace can be versioned independently (Git preferred for collaboration). A file in an untracked folder has no automatic revision history.

Example layout, **not a required schema**:

```text
work/
├── app/                     # application's repository: code/tests/current docs
└── engineering/             # independent artifact workspace, optionally a Git repo
    ├── product/
    │   └── product-brief.md
    └── changes/
        └── async-exports/
            ├── ecr.md       # seven standard sections
            ├── design.md    # optional deeper RFC
            └── diagrams/
                ├── target-containers.mmd
                └── export-sequence.mmd
```

Small changes may need only `changes/<name>/ecr.md`. Do not create empty stubs or placeholder diagrams. Use established project naming, Markdown linking and index/navigation where present; add the smallest discoverable index needed when creating a new workspace. Keep diagram source editable and render/verify with available tools.

## Identity and updates

A stable folder path or existing change slug can serve as the change identity. For a large project use a parent document linked to feature ECRs, not a forest of duplicate copies. Link application baseline using repo/ref + actual path/commit when available; a relative path between unrelated roots is not a durable cross-system identifier.

On edit, inspect current content/working changes and update the existing sections, preserving concurrent edits. In a Git-backed workspace, respect branch/isolation conventions, revision, and publication authority; do not push merely because a file was saved. If filesystem access is unavailable, say so and provide inline artifact content suitable for later saving.

## Example practice

A `design` activity reads `app/docs/architecture/containers.md` at the actual base revision, reads the ECR, then updates its `4. Solution design` with an accepted/proposed distinction and a link to `diagrams/target-containers.mmd`. It does not edit canonical implemented documentation until implementation actually changes the application and that change is authorized.
