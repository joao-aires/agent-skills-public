# Create and evaluate a distinctive interface

Install the built `frontend-development` bundle using [installation](installation.md). It includes interface-design, Impeccable and UI/UX Pro Max; users need no separate upstream skill install. Add technical expertise only for the project's actual stack. Python 3 is needed for Pro Max's local search; browser drivers and application libraries are separate runtime capabilities. Impeccable's optional engine is downloaded separately by its versioned launcher, with a documented fallback when unavailable. See [bundled methods](../plugins/frontend-development/skills/interface-design/references/bundled-design-methods.md) for exact paths and limitations.

## From a reference to an implementation

For example: “Build an image-motion workspace with the craft and responsiveness of AlignCanvas. Use our React app and owned sample images; propose a direction, implement a ring preview with accessible controls, and verify desktop/mobile and reduced motion. No export in the first slice.”

1. Inspect the actual reference and product constraints. Separate what is observed from inferred implementation. [AlignCanvas](https://aligncanvas.com/) publicly describes live WebGL scenes and WebCodecs export; its private framework and shaders are not established here. Derive depth, continuity, hierarchy and feedback principles, with original visuals and owned assets.
2. Let interface-design recommend contrasting directions on realistic content. Choose or modify one, or delegate the choice. Record proposals, accepted preferences and constraints in the existing brief. Small changes within an established product skip this round.
3. Use bundled Pro Max searches only where candidate selection helps; use Impeccable for the relevant critique/refinement method. The activity owns feedback, scope and the shared record. This is conditional agent orchestration through available skill/file tools, not an automatic dependency resolver.
4. Implement one complete slice. [Creative implementation](../plugins/frontend-development/skills/interface-design/references/creative-implementation.md) covers React/Next.js boundaries, Motion versus GSAP, R3F/Three.js scenes, GLSL, deterministic loops and optional WebCodecs export. An HTML/CSS page does not need all those technologies.
5. Follow [rendered QA](../plugins/frontend-development/skills/interface-design/references/rendered-qa.md): launch, capture, inspect, fix and recapture. Check keyboard/focus and failure recovery separately from screenshots. Invite feedback on the implemented result and update the brief rather than reopening every decision.

The existing [visual direction](../plugins/frontend-development/skills/interface-design/references/visual-direction.md), hierarchy and measurement guidance still own their original concerns. New references cover missing transitions and mechanisms, without copying the upstream design databases or playbooks.

## Acceptance protocol

The [evaluation specification](../evals/development-workflows.json) includes `creative-premium-landing`, `creative-existing-dashboard`, `creative-motion-workspace`, `design-feedback-resumption`, and `bundled-design-routing`. These are defined acceptance scenarios, not recorded proof of improved agent performance. Use the [evaluation procedure](maintainers/evaluations.md) to retain actual execution evidence.

For a baseline/candidate comparison, build `frontend-development` at main before this change and at the candidate commit in separate disposable directories. Use the same model/version, starting repository, prompt, supplied assets, tool permissions, time/token budget, browser/device profile and user replies. Keep evaluator criteria out of actor context. Run each generation scenario at least three times per revision when resources allow; counterbalance order and have reviewers assess anonymized outputs. Record deviations and incomplete runs. Compare quality and cost together rather than accepting extra work as automatic improvement.

For each run retain: source/model/tool identities, prompt and replies, actual guidance reads/routing, brief revisions, generated app diff, startup/check commands, screenshots and reviewer notes, keyboard/interaction checks, performance samples, failures and iteration/time counts. A baseline without bundled skills is not expected to invoke them; evaluate output and routing appropriateness separately. No paid services or publication are needed. Browser, GPU, dependency and codec availability are capability gates, not reasons to fabricate successful checks.

| Dimension | Acceptance evidence |
| --- | --- |
| Product-specific craft | Composition, type and visual focal point fit actual content; reviewers can explain why it is more than a recolored starter. |
| Usability | Primary task and a critical recovery path work; actual content and long/narrow states remain readable. |
| Discovery and continuity | Consequential feedback influences the brief and output; resumption reuses it; a small repair avoids a questionnaire. |
| Routing | Needed method is actually loaded/executed; routine work avoids gratuitous methods; direct invocation and unavailable-tool boundaries are preserved. |
| Motion | Purposeful, interruptible continuity; reduced-motion/static path conveys equivalent content; no broken scroll or focus. |
| Accessibility | Keyboard/focus and relevant contrast/labels measured; automated findings triaged; untested assistive technology disclosed. |
| Responsive and resilient behavior | Desktop/narrow captures inspected; asset/scene failure and supported appearance modes handled. |
| Performance | Agreed load/input/frame/memory budgets checked on named hardware/browser; idle/background work bounded. |
| Integrity | Complete built resources and licenses; accepted pins verify; no silent upgrades or source drift. |

Score craft, usability, motion, responsiveness, accessibility and performance from 0–4: 0 missing/broken, 1 major unresolved problems, 2 usable with material weaknesses, 3 meets the brief with evidence, 4 unusually strong with specific reviewer rationale. Use N/A with a reason for motion/export when the brief does not need it. Suggested adoption gate: all applicable dimensions at least 3, no primary-task/accessibility blocker, no undisclosed evidence gap, and no regression against the baseline's existing product behavior. Report raw scores and reviewer disagreements; a mean score cannot conceal a blocker. For an improvement claim, compare paired results and variance, include incomplete runs and show screenshots. No score guarantees AlignCanvas equivalence or taste.

## Maintenance and limits

[Source provenance](maintainers/sources.md#bundled-interface-methods) records fixed commits, licenses, resource mapping and runtime caveats. Update through Agent Depot plan/diff/update, preserving original bytes, and rebuild offline. Tests establish resource closure, labels/notices and executable local search; they do not prove installed-client routing, engine downloads, visual quality or WebCodecs compatibility. Run those trials explicitly before making such claims. Linked inspiration is not redistributed application code or a license grant for its assets.
