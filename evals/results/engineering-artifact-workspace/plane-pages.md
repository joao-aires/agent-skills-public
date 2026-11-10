# Plane Pages as ECR storage — bounded connected integration checks

**Observed:** 2026-11-10 · Plane workspace `Baryet`, existing demo project `Baryet` · connected OAuth Plane MCP tools.

## Scope and controls

- Real connected Plane project Pages API; no external production application, independent agent/subagent, actual source implementation or user-facing release.
- Created **one private, clearly marked temporary project Page** with an artificial scheduled-export revocation ECR. No other existing Page or work item was modified. Archived and deleted the temporary Page at the end; confirmed it is absent from project Page listing.
- The connected Plane MCP `page` action exposes `create`, `retrieve`, `update`, `archive`, `delete` and project/workspace listing. `update` takes whole-document `description_html`, not a patch or conditional revision token.
- No private user content was required for the fixture; the sample data was invented for this test.

## Test 1 — Create, scope and read back

**Observed pass.** A private project Page was created containing seven numbered ECR headings and the accepted requirements R1 (authorized scheduling) and R2 (execution-time permission revalidation). A separate `retrieve` returned its ID, the intended project membership, private access, all seven headings and both requirements. The project Page list included the test Page; workspace Page listing did not include it, consistent with project scope.

## Test 2 — Update and preserve prior decisions

**Observed pass, with HTML normalization.** Read the existing Page first, then updated its full `description_html`: a deliberately contradictory scheduling-only proposal was corrected to require an access check before execution; a bounded plan was added; implementation and release were still marked **pending**, not executed. A new retrieval confirmed the same Page identity and scope, seven headings, both original accepted requirements, the revised proposed design, and no loss of unchanged scope/history.

Plane serialized the updated Page into editor-specific HTML such as `<h2 class="editor-heading-block" ...>` and annotated paragraph tags. A naive exact match of `<h2>` initially produced a **false negative**; parsing real heading elements with attributes confirmed all seven persisted. Integrations should compare semantically relevant content, not raw byte-for-byte HTML.

## Test 3 — Stale sequential writes / lost update

**Confirmed limitation.** Simulated two editors that both read the same initial Page:
1. Writer A updated the record with a unique temporary note; a fresh read confirmed it persisted.
2. Writer B submitted a **stale complete HTML body** based on the earlier snapshot, with a different note but without A's note.
3. Plane accepted B's update **without a conflict error**. On retrieval, B's note was present and A's newer note had disappeared.
4. Restored the intended V2 ECR body and reread to confirm clean content; removed the test Page afterward.

The observed Plane MCP API did **not** expose an ETag, expected revision or other conditional-write argument on `page update`. `updated_at` is returned by reads but cannot be used as a server-enforced compare-and-swap condition via this connector. A last-second read and three-way merge can reduce accidental overwrites; **they cannot eliminate a race without an atomic guard or serialized single-writer process**.

## Assessment relative to PR #44

| Capability | Result | Evidence limit |
| --- | --- | --- |
| Real provider storage and retrieval | Pass | One private project Page, one workspace/project |
| Seven-section ECR and long-form HTML preservation | Pass | Plane normalizes editor HTML |
| Incremental continuity and accepted requirements | Pass | Whole-body read/edit/write; no automatic partial patch |
| Current/proposed/implemented status fidelity | Pass in test content | These were authored statuses, not code execution evidence |
| Concurrent or stale-edit safety | **Failed / last-write-wins observed** | No exposed conditional-update guard |
| Authorized cleanup | Pass | Page archived, deleted and absent from project list |
| Independent agent skill adherence | **Not tested** | Direct MCP calls, not a blind actor given the skills |

**Implication:** Plane Pages are a viable ECR *document home* in a controlled, single-writer or otherwise coordinated workflow. The agent must resolve actual Page identity and project scope, retrieve the current body before editing, preserve accepted content, reread after updates, and **not promise race-safe multi-agent collaboration**. For simultaneous writers or consequential concurrent updates, the workflow must choose an authority with server-enforced versioning or an explicit serialized edit policy.

This is a real **connected provider integration probe**, not an independent end-to-end behavioral evaluation or certification of Plane's editor and API across versions.
