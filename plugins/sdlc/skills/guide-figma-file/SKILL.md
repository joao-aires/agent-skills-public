---
name: guide-figma-file
description: Guide to structuring and reviewing a Figma design file as a durable artifact. Use for pages, frames, components, tokens, source-of-truth, revision, permissions and design handoff.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: frontend
  phase: design
  scope: generic
  invocation: both
  role: support
---

# Figma file guide

Read [activity system](../activity-system/SKILL.md) for scope and the [design proposal contract](../artifact-system/references/contracts/design-proposal.md) for authority. Use the optional Figma MCP only within its granted read/write access.

A Figma file is a **view artifact and design workspace**, not automatically the design authority. Its authority depends on what it contains: a proposal view, an accepted design, or the canonical design system.

## Reader question

Can a designer, engineer or reviewer find the current frames, understand what is proposed versus accepted, and know which file or component is authoritative?

## When to use

- a UI design needs a shared, inspectable file;
- several directions must be compared in one place;
- components, tokens or design-system state need a durable home;
- a design-to-implementation handoff needs frame links and revisions.

## Minimum content

- file purpose and owner;
- page structure: current, proposed, archive, exploration;
- frames for the affected task and its important states;
- components and tokens used, with links to the accepted design system;
- annotations for behavior and unresolved decisions;
- revision or file link and access boundary;
- the related design proposal or ECR.

## Structure and quality

- Separate current, proposed and archived work so no one mistakes a proposal for the accepted system.
- Name pages, frames and components by meaning, not by date or author.
- Reuse the accepted component and token system; do not fork a parallel one.
- Keep exploration visually distinct from accepted design.
- Record the file revision or frame link used in the design proposal.
- Use a text summary for readers who cannot open the file.

## Common failures

- treating a Figma file as the only record of a decision;
- mixing current and proposed frames in one page;
- a component or token fork that implementation cannot follow;
- an unversioned link that changes after review;
- assuming read access implies write authority;
- copying secrets or sensitive customer content into the file.

## Authority, home and review

- **Authority:** the design proposal/ECR decision, or the accepted design system when the file is canonical.
- **Home:** Figma workspace; link it from the design proposal or repository docs.
- **Access:** record view/edit permissions and whether the link is public, workspace-only or private.
- **Review:** use the [design review](../design/references/design-review.md) and preserve the accepted design system.

## Specialist route

Use available `interface-design` for design decisions and `frontend-*` conventions for component and token implementation. The Figma MCP is an access mechanism, not a design method.

## Handoff

Record the file link, frame or page, revision, permissions and the design-system authority. Do not claim that a frame is implemented or approved merely because it exists in Figma.
