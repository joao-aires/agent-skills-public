# Guidance audit: capability, detail and authority

Audit date: 2026-11-16. Scope: 143 skills in 21 plugins at audit time, with 104 local and 39 acquired skills; `skill-authoring` now applies the same rule to future changes. The rule applied is [own the capability, disclose the detail, link the authority](../maintainer-reference.md#own-the-capability-disclose-the-detail-link-the-authority).

## Method

1. Scan every local skill for body length, reference volume, code blocks, table density, external links, flag-like strings and version-like strings.
2. Review the highest-risk local skills manually against the rule: does the content help choose, verify, recover or recognize a failure, or does it restate external documentation?
3. Exclude the 39 acquired snapshots from editing. Preserve their bytes; audit only whether a local wrapper or handoff is misleading.
4. Record a disposition rather than treating length alone as a failure. A long local contract, decision table or evidence checklist can be correct.

The scan is a prioritization aid, not a quality score. A short skill can still duplicate a framework tutorial, and a long local contract can be entirely decision-relevant.

## Summary

| Priority | Meaning | Skills |
| --- | --- | --- |
| **Fixed in this branch** | Clear external-detail duplication or conceptual overlap | `ai-deepeval-testing`, `release`/`ci-cd-pipelines`, `interface-design`/`design-research`, `business-strategy` mode wording |
| **P1** | Fixed in this pass | `architecture-patterns` body table now points to the full reference matrix |
| **P2** | Fixed in this pass | `cli-development`, `rest-api-design`, `graphql-design`, `event-driven-design` Kafka reference, `tooling-conventions` workflow authoring |
| **P3** | Review opportunistically; mostly local method or contract | `business-strategy` references, `artifact-system` references |
| **Keep** | Decision-focused local guidance | `explain`, `technical-writing`, `design-research`, `ai-evaluation`, `distributed-systems`, `design-system`, `guide-*` |
| **Exempt** | Acquired snapshots; never edit bytes | 39 upstream skills |

## Findings

| Skill or area | Evidence | Disposition |
| --- | --- | --- |
| `ai-deepeval-testing` | Was 89/229/113 lines across skill/playbook/CI; contained constructor examples, metric-name tables, flag inventories, tracing-helper inventories and version-specific storage notes. | **Fixed.** Now 82/95/80. Keeps the decision map, one evidence-boundary example, local reporting, CI gates and failure triage; links exact APIs, parameters and flags. |
| `release` and `ci-cd-pipelines` | `release` carried both the authorized action and a 109-line pipeline manual. | **Fixed.** `release` is the action/verification activity; `ci-cd-pipelines` owns provider-neutral stages, promotion, gates, branching and recovery. Pipeline detail was trimmed to decisions and evidence. |
| `interface-design`, `design-research` | “UI/UX Pro Max is always used” treated one optional method as a mandatory baseline while `impeccable` and other methods compete. | **Fixed.** No method is mandatory. Select by the decision, treat methods as optional inputs, reconcile conflicts against the brief and evidence. |
| `business-strategy` | `explore`/`decide` wording looked like external activities or plugin dependencies. | **Fixed.** Modes are explicitly internal; exploratory and decision language replaces ambiguous code terms. |
| `architecture-patterns` | The skill body carried a full eight-pattern fits/costs table while `references/pattern-selection.md` carries the force checklist, comparison matrix and evidence table. | **Fixed.** The body now has a short pattern-family table; the full comparison and evidence matrix remain in the reference. |
| `cli-development` | 209-line body and 895 lines of references; exact flag conventions, exit-code tables, XDG/platform details and packaging mechanics duplicated clig.dev, POSIX, XDG and package-manager docs. | **Fixed.** Now 152/462. Kept caller model, grammar, precedence, stream/JSON/exit decisions, interaction, compatibility and verification; linked exact conventions and compressed the references. |
| `rest-api-design` | 199-line body with exhaustive method, status, header and error tables; much of it is normative HTTP semantics. | **Fixed.** Now 150/277. Kept resource modeling, operation meaning, idempotency, collections, authorization, compatibility and evidence; condensed the status catalogue to client-facing decisions and linked RFC 9110/6585. |
| `graphql-design` | 204-line body with GraphQL specification, Apollo directive and federation details. | **Fixed.** Now 150/269. Kept schema contract, nullability, connections, errors, mutations, N+1, authorization, cost, federation, evolution and public/private decisions; removed exact directive/API catalogues and linked the spec/Relay/Apollo. |
| `event-driven-design/references/kafka-patterns.md` | 155 lines with broker configuration and delivery details that Kafka documentation owns. | **Fixed.** Now 110. Kept design decisions, ordering, idempotency, outbox/replay, schema evolution and failure modes; removed setting inventories and version mechanics, linked Kafka/Schema Registry. |
| `tooling-conventions/references/workflow-authoring.md` | 132 lines with GitHub Actions-specific naming, expression, permissions, caching and reusable-workflow mechanics. | **Fixed.** Now 110. Kept naming, data ownership, expression boundary, shell failure, execution decisions, reuse, identity and evidence; removed provider flag inventories and linked GitHub syntax/security docs. |
| `business-strategy` references | 3,052 reference lines across frameworks, market systems, economics and research methods. | **P3.** Large but mostly local synthesis. Audit for passages that merely summarize a named framework; keep the decision rules, comparison matrices and source pointers. Do not rewrite the strategy method wholesale. |
| `artifact-system` references | 3,388 reference lines of contracts, registry, homes, quality and storage guidance. | **P3, mostly keep.** These are local contracts and decision rules, not external documentation. Review only for repeated contract content when a contract is next changed. |
| `distributed-systems` | 185-line body with consistency, replication, failure and capacity reasoning. | **Keep.** It is a decision method with stable concepts; the external sources are linked. |
| `design-system`, `ai-evaluation`, `explain`, `technical-writing`, `design-research` | Decision-oriented method bodies with conditional references. | **Keep.** No clear documentation-shadow problem. |
| `guide-*` artifact guides | Local artifact structure and review methods. | **Keep.** They are the local standard for artifact shape, not a copy of a vendor doc. |
| Acquired skills | 39 snapshots including framework, design and platform guidance. | **Exempt.** Preserve bytes and native resources. A local skill may name the acquired capability; it must not pretend the upstream snapshot is current or complete. |

## Examples of correct boundaries

| Skill | Correctly externalized |
| --- | --- |
| `ai-deepeval-testing` | Exact API fields, metric parameters, runner flags and local storage paths are links; the skill owns selection, evidence and failure boundaries. |
| `release` | Provider syntax and pipeline mechanics are outside the activity; `release` owns target identity, authorization, served-outcome verification and recovery claims. |
| `design-research` | Mobbin/Refero endpoints, plans and rate limits are links; the method owns question framing, source quality, observation/inference separation and privacy. |
| `architecture-patterns` | Pattern definitions and sources are linked; the method owns force identification, pattern comparison, costs and migration constraints. |

## Next pass

1. Review `business-strategy` references only where a framework summary has replaced local judgment.
2. Review `artifact-system` contracts when they are next changed, not as a standalone rewrite.
3. Re-run the audit after a material skill rewrite; shorter text alone is not evidence of better behavior.

This audit does not establish that the remaining local guidance is behaviorally effective. It records documentation shape and ownership; behavioral evaluation remains separate.
