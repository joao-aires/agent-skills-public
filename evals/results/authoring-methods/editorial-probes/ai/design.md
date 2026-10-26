# AI-assisted support drafts — design proposal

Status: design only. No implementation, provider provisioning, model calls, user contact or real-ticket transmission has occurred. This proposal uses the supplied ai-development and ai-testing methods and their application-pattern, model-I/O and evaluation references. Provider, numerical operating limits and release thresholds remain decisions to make before dependent work.

## Outcome and architecture

A staff member requests a draft for one permitted ticket, reviews and edits it, then sends through the application's existing authorized action. Success means a useful, grounded draft in the requested supported language, with the staff member retaining control of the final message.

Use a bounded model call inside an application-owned workflow. Existing application code already selects the permitted ticket and relevant help articles; generation is the only inference step needed. An agent framework, agent loop, model-operated retrieval, durable agent state and new interoperability protocols have no justified role in this release. Reconsider only if a future accepted task needs the model to choose and execute varying steps. A small provider adapter is sufficient and should normalize transport errors, refusal, incomplete output and usage without erasing their distinctions.

The flow is: authorized request → existing retrieval → minimized context snapshot → bounded generation → application validation → editable draft and staff-only evidence → existing send action. The generation integration receives no customer-search or message-send tools, credentials or permissions. Neither a generated instruction nor a button can grant additional authority.

Ordinary code owns access, ticket identity, language allowlists, request lifecycle, validation, persistence and sending. The model contributes wording, synthesis and identification of missing or conflicting evidence. Generation completion never changes the ticket to sent or resolved.

## Context, result and staff interaction

The request carries the ticket's current permitted content, the selected articles with source IDs and revision information, the selected supported language and application-approved reply guidance. The actual two languages and intended locales must be named before dataset coverage or provider selection can be confirmed. Staff can correct the language choice. Do not send unrelated customer records, internal secrets or unnecessary personal details. Confirm permitted processing, retention, region, training use, licensing and contractual requirements before choosing a hosted or self-hosted provider.

Application instructions govern the task. Ticket text and help articles are evidence, including when they contain imperative text. Delimit them and preserve their provenance. Embedded requests to disclose data, ignore policy, fetch records or send mail do not alter the workflow. Do not silently drop decisive context to fit a model's limit: select relevant evidence, retain qualifications, or report that the input cannot be handled.

A small structured envelope serves the application while preserving readable prose for the staff member:

- `status`: `draft` or `needs_review`.
- `reply_text`: proposed customer-facing text; may be absent when no defensible draft is possible.
- `language`: one of the application's supported language values.
- `source_ids`: supplied article references supporting the reply.
- `review_notes`: staff-only missing information, material uncertainty or conflicts.

Provider refusal, truncation and dependency failure are application outcomes outside this content envelope; never reinterpret them as successful drafts. The ticket association and source-ID mapping belong to the request, not model-selected identifiers. Exact field names are illustrative until implementation conventions are known. Use provider-supported schema constraints where available and validate again in application code.

Show the draft as editable text, with sources and review notes visibly separate from the customer message. Never append staff-only notes automatically to the send body. Source references help review but do not prove that a claim is grounded. Render output as untrusted text; escape markup and avoid automatic activation of model-supplied links or actions.

When information is missing, a useful draft may ask the customer a relevant clarification, with a staff note explaining the gap. Conflicting policy, unsupported commitments or insufficient evidence should produce an explicit review-needed result. Do not invent refunds, account actions, diagnoses or resolutions. No numerical confidence score is needed. Staff must be able to discard a result and compose manually.

## Authority, state and recovery

Recheck permission when requesting generation and through the existing send action. Bind each request to the authenticated staff member, tenant, ticket, context revision and selected language in trusted code. Reject unauthorized source references; do not let output change the binding. Detect stale ticket/context revisions and warn or require regeneration before using a result based on superseded evidence. Preserve the application's established send permissions and duplicate-send safeguards.

Store domain ticket state, draft revisions and generation execution status separately. A draft is not an authoritative customer fact. Scope draft visibility and execution metadata to the permitted staff/tenant. Define retention and deletion for input snapshots, drafts and provider logs before launch; avoid raw ticket bodies in routine telemetry. Keep only the traceability needed to connect a draft to its effective model, prompt and context configuration. There is no need for cross-ticket conversation memory.

Use explicit pending, completed, review-needed, failed and cancelled request states. Late results must not overwrite staff edits or a newer request. Cancellation stops further application work and discards late output even if the provider cannot cancel its computation. Deduplicate accidental repeated requests where possible.

Configure a total request deadline, input/output limits, concurrency cap and total attempt/resource budget before running the integration; their values are provisional engineering decisions until latency and cost expectations are agreed. Retry transient failures only within that shared budget. A correctable representation failure can receive concrete validation feedback if a repair is likely to help; revalidate the result. Missing evidence is not repaired by repeating the same call. Permanent access/configuration failure stops. No silent provider substitution until its data handling and quality have been accepted. Failed generation leaves manual composition available and never retries the send action.

## Validation and evidence boundaries

| Boundary | Checks and evidence required |
| --- | --- |
| Deterministic application checks | Current access and tenant isolation; permitted source binding; supported language value; schema, size and status consistency; escaping; no model tools; separate notes/body; cancellation, timeout, duplicate requests and stale-result handling. Fixtures can verify these without a model. |
| Meaning and draft quality | Grounded factual claims, correct source support, relevance, completeness, appropriate uncertainty, absence of unsupported promises, language fluency and practical editing effort. Human assessment is required; schema success cannot establish these properties. |
| Existing retrieval | On evaluation inputs, inspect whether the supplied articles contain the necessary evidence and whether they are current and permitted. Record retrieval omissions separately from generation failures; existing retrieval does not guarantee adequate evidence. |
| Provider integration | Later, use the actual chosen API/version to verify schema behavior, refusal, truncation, rate limits, transport failures, timeout and cancellation semantics. Mocks establish application handling only. |
| Staff journey | Later, verify request → review → edit → authorized send in a test environment with synthetic tickets and a test recipient/sink. Assert persisted edited body and correct ticket, current send authorization, no automatic send, and usable loading/error states and keyboard interaction. This requires a real integrated application journey, not an attractive draft. |

Include ticket/article prompt injection, fake article IDs, attempts to cross tenants, unsupported language, empty and conflicting articles, very long tickets, malformed output, provider refusal and timeouts. Exact checks cover mechanically knowable facts; semantic language and grounding still require review. There is no agent trajectory or remote-agent interoperability to evaluate in this architecture.

## Comparing two candidates

First inventory the forty sanitized historical tickets by language/locale, issue type, evidence availability, difficulty and approved-reply availability. Sanitization alone does not establish permission for external evaluation: review residual identifiers and permitted data use before any later provider calls. Preserve inputs, expected outcomes/rubrics and actual candidate outputs as separate versioned records. Approved historical replies are reference evidence, not text to copy into model context; verify they remain correct under the supplied article revisions.

Propose a fixed twenty-ticket development set and twenty-ticket held-out set, stratified across languages and important failure slices. Aim to distribute the twenty approved replies across both sets while keeping related/duplicate tickets together to avoid leakage. Inspect actual counts before fixing the split; coverage may require more cases. Do not claim every language/issue intersection is covered by forty tickets.

For the twenty tickets without approved replies, have qualified support reviewers annotate required facts, relevant evidence, unacceptable claims and acceptable uncertainty before seeing candidate outputs. Multiple good replies are valid. If these annotations cannot be obtained, report those cases as exploratory and keep them outside claims requiring approved expected outcomes. Even the twenty approved replies need a rubric rather than exact string matching.

On development cases, refine a shared prompt and contract, then freeze them and the rubric before held-out evaluation. Compare candidate A and B on the same context snapshots, language instructions, output limits and recovery policy. Record model/version, sampling and reasoning settings, adapter, prompt, article revisions, dataset split and evaluator revisions. Interleave runs and blind/randomize reviewer presentation. Provider-specific changes should be recorded as confounders: a bundled model-and-prompt change supports a candidate comparison, not a causal claim about the model alone.

A proposed bounded comparison is three independently generated drafts per candidate per held-out ticket: 120 initial generations, plus separately accounted permitted recovery attempts. This is an experiment plan requiring later authorization and a cost cap, not an executed benchmark. If the approved budget supports fewer trials, disclose that limitation. Repeated outputs from one ticket are not independent tickets.

Use bilingual human support reviewers as the primary graders. Rate grounding/correctness, task completeness, fluency/tone and editing effort separately; classify each output as usable unchanged, usable with minor edits, major rewrite, or unusable. Review borderline and consequential disagreements with an additional qualified reviewer. Measure acceptable-draft coverage alongside abstention/review-needed behavior so refusing everything cannot appear successful. Report both all-case usefulness and answerable-case usefulness with explicit denominators. Reference comparison supports grading but does not penalize valid alternate wording. A model judge is optional only after calibration against accepted human judgments, including failures and borderline cases; no live judge is assumed.

Before running, agree release criteria. Proposed provisional criteria are no observed cross-tenant disclosure, unauthorized effect or materially unsupported commitment, plus at least 80% usable drafts with at most minor edits in each supported language. Human reviewers must agree what minor editing means before scoring. These are suggested decision rules, not accepted commitments or population reliability guarantees. A critical failure blocks a favorable aggregate; unrepresented language slices remain unverified.

Report paired case outcomes, disagreements, critical failures and performance by language and important issue/evidence slices, with denominators and variability across repeats. Retain case-level results; twenty held-out tickets give limited confidence, especially after slicing. Measure request-to-validated-result latency, failure/timeout rate, token usage, cost per requested draft and cost per acceptable draft. Include failed calls and repairs in totals; report per-attempt and total-job measurements. Cost and latency have no agreed pass/fail threshold yet, so present measured tradeoffs and estimated pricing separately. A quality/cost/latency tradeoff may remain a product decision rather than yield a universal winner.

## Delivery and current limits

Keep cheap authority and recovery tests in routine CI. Later rerun affected deterministic checks after integration changes and a frozen held-out quality comparison after consequential model, prompt or context changes. Add reviewed failure cases as regressions without repeatedly tuning to the held-out set. After separately authorized release, privacy-reviewed staff feedback and edit/discard rates can reveal problems; these are proxies, not direct proof of correctness, and should be checked with sampled human review.

This work produced a design and evaluation plan only. No ticket dataset was inspected, no cases annotated, no checks executed against an application, and neither candidate's quality, cost, latency nor integration behavior has been measured. The two language identities, available slice coverage, reviewer availability, provider/data-use constraints, numerical operating budgets and accepted release criteria remain unresolved. Design and future passing evaluations do not authorize provisioning, deployment or external communications.
