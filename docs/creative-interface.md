# Creative interface work

Use this page when a product needs a distinctive visual direction or an expressive web experience, not just a competent implementation of an existing system. Install the built `frontend-development` bundle using [installation](installation.md#load-them-in-your-client). It includes interface-design, Impeccable and UI/UX Pro Max; no separate upstream skill install is needed. Add technical expertise only for the project's actual stack.

Python 3 is needed for Pro Max's local search. Browser drivers and application libraries are separate runtime capabilities. Impeccable's optional engine is downloaded by its versioned launcher, with a documented fallback when unavailable. The [bundled-methods reference](../plugins/frontend-development/skills/interface-design/references/bundled-design-methods.md) records exact paths and limitations.

## From a reference to an implementation

Example request: "Build an image-motion workspace with the craft and responsiveness of AlignCanvas. Use our React app and owned sample images; propose a direction, implement a ring preview with accessible controls, and verify desktop, mobile and reduced motion. No export in the first slice."

1. Inspect the actual reference and product constraints. Separate observation from inferred implementation. [AlignCanvas](https://aligncanvas.com/) publicly describes live WebGL scenes and WebCodecs export; its private framework and shaders are not established here. Derive depth, continuity, hierarchy and feedback principles, with original visuals and owned assets.
2. Let interface-design recommend contrasting directions on realistic content. Choose, modify or delegate the choice. Record proposals, accepted preferences and constraints in the existing brief. Small changes inside an established product skip this round.
3. Use bundled Pro Max searches only where candidate selection helps; use Impeccable for the relevant critique or refinement method. The activity owns feedback, scope and the shared record. This is conditional orchestration through available skill and file tools, not an automatic dependency resolver.
4. Implement one complete slice. [Creative implementation](../plugins/frontend-development/skills/interface-design/references/creative-implementation.md) covers React/Next.js boundaries, Motion versus GSAP, R3F/Three.js scenes, GLSL, deterministic loops and optional WebCodecs export. An HTML/CSS page does not need all those technologies.
5. Follow [rendered QA](../plugins/frontend-development/skills/interface-design/references/rendered-qa.md): launch, capture, inspect, fix and recapture. Check keyboard, focus and failure recovery separately from screenshots. Invite feedback on the implemented result and update the brief rather than reopening every decision.

The existing [visual direction](../plugins/frontend-development/skills/interface-design/references/visual-direction.md), hierarchy and measurement guidance keep their original concerns. New references cover missing transitions and mechanisms without copying upstream design databases or playbooks.

## Acceptance protocol

The runnable suite includes a design-proportionality case and a product-feedback planning case in [`evals/cases/`](../evals/cases/), mapped through [`flows.yaml`](../evals/flows.yaml). These are defined acceptance checks, not recorded proof of improved agent performance. Use the [evaluation procedure](../evals/README.md) to retain actual execution evidence. Keep the broader baseline/candidate generation comparison below as a separate, explicitly recorded study.

For a baseline/candidate comparison, build `frontend-development` at `main` before the change and at the candidate commit in separate disposable directories. Use the same model and version, starting repository, prompt, supplied assets, tool permissions, time and token budget, browser and device profile, and user replies. Keep evaluator criteria out of actor context. Run each generation scenario at least three times per revision when resources allow; counterbalance order and have reviewers assess anonymized outputs. Record deviations and incomplete runs. Compare quality and cost together rather than treating extra work as automatic improvement.

For each run retain: source, model and tool identities; prompt and replies; actual guidance reads and routing; brief revisions; generated application diff; startup and check commands; screenshots and reviewer notes; keyboard and interaction checks; performance samples; failures and iteration counts. A baseline without bundled skills is not expected to invoke them; evaluate output and routing appropriateness separately. No paid services or publication are needed. Browser, GPU, dependency and codec availability are capability gates, not reasons to fabricate successful checks.

| Dimension | Acceptance evidence |
| --- | --- |
| Product-specific craft | Composition, type and visual focal point fit the actual content; reviewers can explain why it is more than a recolored starter. |
| Usability | The primary task and a critical recovery path work; real content and long or narrow states remain readable. |
| Discovery and continuity | Consequential feedback influences the brief and output; resumption reuses it; a small repair avoids a questionnaire. |
| Routing | The needed method is actually loaded and executed; routine work avoids gratuitous methods; direct invocation and unavailable-tool boundaries are preserved. |
| Motion | Purposeful, interruptible continuity; the reduced-motion or static path conveys equivalent content; no broken scroll or focus. |
| Accessibility | Keyboard, focus and relevant contrast or labels are measured; automated findings are triaged; untested assistive technology is disclosed. |
| Responsive and resilient behavior | Desktop and narrow captures are inspected; asset or scene failure and supported appearance modes are handled. |
| Performance | Agreed load, input, frame and memory budgets are checked on named hardware and browser; idle and background work is bounded. |
| Integrity | Complete built resources and licenses; accepted pins verify; no silent upgrades or source drift. |

Score craft, usability, motion, responsiveness, accessibility and performance from 0 to 4: 0 missing or broken, 1 major unresolved problems, 2 usable with material weaknesses, 3 meets the brief with evidence, 4 unusually strong with specific reviewer rationale. Use N/A with a reason for motion or export when the brief does not need it. Suggested adoption gate: every applicable dimension at least 3, no primary-task or accessibility blocker, no undisclosed evidence gap, and no regression against the baseline's existing product behavior. Report raw scores and reviewer disagreements; a mean cannot conceal a blocker. For an improvement claim, compare paired results and variance, include incomplete runs and show screenshots. No score guarantees AlignCanvas equivalence or taste.

## Maintenance and limits

[Source provenance](maintainers/sources.md#bundled-interface-methods) records fixed commits, licenses, resource mapping and runtime caveats. Update through Agent Depot plan, diff and update, preserving original bytes, then rebuild offline. Tests establish resource closure, labels and notices, and executable local search; they do not prove installed-client routing, engine downloads, visual quality or WebCodecs compatibility. Run those trials explicitly before making such claims. Linked inspiration is not redistributed application code or a license grant for its assets.
