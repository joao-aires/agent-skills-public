# Collection features: contracts and evaluation proposal

This is a design from the supplied synthetic catalog material. It preserves the existing React client and catalog API. No service, model request, import or catalog write has been executed.

## Separate the consumers

Museum visitors need a readable account of an object with enough sourcing and uncertainty to understand what the catalog supports. The import service needs validated records with stable source references. These features can share authorized catalog data, but should not be forced into the same output format or model workflow.

Use ordinary code to copy known object identity and title and resolve supplied source identities. Model judgment is useful for interpreting source statements and explaining their qualifications. Neither feature needs a new agent runtime, protocol layer, numeric alias scheme or infrastructure service for the stated slice.

## Visitor explanation

Return a short explanation in the established interface, with references to the source statements supporting consequential claims. Retain the existing object identifier as application context; it need not become the visitor's primary reading experience.

A faithful explanation of the supplied item could read:

> The catalog names this work *Study of a river*. Its maker is unconfirmed. The acquisition card describes an unsigned work and estimates a date of 1880–1890 [S1]. A later inventory tentatively attributes it to R. Vale, but that attribution has not been confirmed [S2].

This illustrates the intended treatment, not a uniquely required wording. S1 and S2 can both be true: an unsigned work can have a later tentative attribution. Do not invent a contradiction or present R. Vale as a confirmed maker. The source references should resolve through the existing catalog's supported presentation; no public URL is supplied, so none is invented here.

Follow-up questions use the same authorized evidence and preserve its qualifications. A question about the maker's biography cannot be answered from these records alone. Explain the evidence limit and, where useful, ask what the visitor wants to investigate. An unrelated canned fallback category is unnecessary. Source text is evidence, including if later records contain instruction-like text; it cannot authorize catalog changes.

Distinguish a grounded answer that acknowledges unknown information from a failure to obtain or process sources. An unavailable catalog should produce an understandable unavailable/retry state, not an invented explanation or a success-shaped empty answer. Use the application's accepted deadlines and retry policy; none is specified in the supplied material.

## Import proposal

Use a software-readable proposal that preserves the established catalog fields. Before implementation, confirm the existing importer’s field types and accepted unknown/conflict representation. The following responsibilities apply regardless of its eventual JSON/schema spelling:

| Information | Meaning and enforcement |
| --- | --- |
| Source object identity | Preserve `OBJ-1823` exactly from the input. Application code binds the proposal to that source object. |
| Title | Preserve `Study of a river`; normalization, if needed by the existing importer, must remain distinguishable from the original. |
| Canonical maker | Remain unknown/null for this input. A tentative attribution is not sufficient to fill a confirmed maker field. |
| Source claims | Preserve S1's unsigned description and estimated date, and S2's tentative attribution, with their distinct references and qualification. |
| Evidence status | Distinguish absent information, tentative support and genuinely conflicting assertions. The given sources do not establish a direct contradiction. |
| Review state | A proposal is pending editor acceptance; producing or validating it does not update the catalog. |

If the current importer cannot retain tentative claims or evidence status, keep them in an existing supported review/provenance mechanism or resolve that contract gap before applying changes. Do not silently discard the qualification or create a new persistence model without inspecting the existing API.

A supported structured-output mechanism can constrain types, required fields and expressible permitted values. The application must independently check object/source references, accepted field semantics, proposal freshness and editor authority. Source fidelity and interpretation still need quality assessment. Treat invalid, refused or incomplete generation as an unaccepted proposal. A bounded repair can use specific validation feedback if meaningful, but repeated generation will not confirm the maker.

The editor must be able to inspect the proposal and evidence before the existing authorized commit action. Revalidate against current object state and permissions at that boundary. This design request grants no mutation authority and defines no automatic-acceptance behavior.

## Evaluation approach

Prepare component checks and realistic task cases separately. The supplied record is a development example, not a held-out quality dataset.

| Property | Suitable evidence |
| --- | --- |
| Known identity/title preserved; missing maker allowed | Deterministic adapter/contract tests through the existing importer boundary. |
| References resolve only to supplied authorized sources | Exact allowed/denied reference tests, including an unknown source ID and another object's source. |
| Tentative attribution remains tentative | Reviewed expected claims and source-fidelity assessment; assertions should reject a confirmed-maker interpretation. |
| Unknown and disagreement remain distinct | Additional cases with absent sources, tentative claims and mutually incompatible supported assertions; assess their different outcomes. |
| Visitor can understand the account and uncertainty | Task-specific human review with alternative acceptable wording; source grounding separately checked. A fluent answer alone is insufficient. |
| Follow-up continuity and instruction-like source content | Conversation cases checking preserved qualification, evidence limits and authority boundaries. |
| No write before editor approval | Service-boundary tests observing no catalog mutation for mere generation/validation, plus allowed/denied acceptance and stale-proposal cases. |
| Failure behavior | Controlled unavailable, refused, truncated and invalid-output cases; preserve the distinction from a valid unknown fact. |

Keep cases and rubrics versioned in the application. Define consequential failures, such as an unsupported confirmed maker or an unauthorized write, separately from stylistic preferences. Select quality thresholds with the product/editor owner rather than inventing a passing percentage. Add held-out objects and repeated model runs before making reliability claims. Test the real interface/API and editor path when implemented; fixtures and this proposal do not establish live model quality or visitor usability.

## Remaining decisions and limits

Inspect the existing importer’s types, provenance storage and editor acceptance contract before implementation. Establish product expectations for unsupported visitor questions and source availability. This document selects no model, endpoint, retry count or service-level target. No code was changed, no provider was called and no participant study or actual import ran.
