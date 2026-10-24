# GDPR questions that change system design

Use this reference for the affected processing operation, not as an automatic requirement to create every artifact. Consult the regulation and relevant regulator guidance through the [source guide](../../../references/sources.md).

| Context or proposed change | Investigate | Potential system consequence |
| --- | --- | --- |
| Customers/people in multiple locations | Establishment, targeting/monitoring and actual processing scope; Article 3 guidance | Applicable responsibilities, representation and legal decision ownership |
| SaaS provider, customer and AI/analytics vendors | Who determines purposes/means for each operation; controller/processor relationships | Instructions, contracts, subprocessors, assistance, access and provider-change handling |
| New personal-data field or event | Purpose, accepted basis, necessity, sensitivity and retention | Minimized schema/event payload, default visibility and bounded retention |
| Behavioral analytics, tracking or automated decisions | Actual tracking technology, profiling/consequences, applicable ePrivacy/national rules and risk | Purpose separation, controls, transparency and assessment requirements |
| Access/export/correction/deletion request | Identity/authority, applicable rights/exceptions and locating relevant data | Search across stores, scoped export, correction propagation and deletion/recovery handling |
| New region/provider/support path | Actual access/transfer route and applicable mechanism/contract | Architecture/provider choice and enforceable operating restrictions |
| Higher-risk processing | Applicable DPIA trigger, risks to people and mitigations | Assessment before dependent processing and revisiting design where risk remains |
| Incident | Breach facts, roles, impact, notification/recording duties and timing | Escalation, evidence preservation and authorized response; avoid a universal notification rule |

For a proposed deletion flow, trace the subject's authoritative and derived data, provider obligations, retention exceptions and backup reactivation risks. Verify representative scope and recovery behavior. Keep pending legal interpretation explicit; do not invent an exception or guarantee merely to complete the design.
