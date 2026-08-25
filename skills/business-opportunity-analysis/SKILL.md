---
name: business-opportunity-analysis
description: "Compatibility alias for the business-strategy skill. Use for legacy requests about TAM/SAM/SOM, revenue potential, pricing, GTM, monetization, SaaS/AI economics, valuation, competitive positioning, open-source commercialization, and business opportunity analysis. The full v2 methodology now lives in ../business-strategy/SKILL.md."
metadata:
  version: "2.0"
  deprecated: "true"
---

# Business Opportunity Analysis — Compatibility Alias

The v1 opportunity-analysis methodology has evolved into the broader `business-strategy` v2 skill.

For any matching request:

1. Read `../business-strategy/SKILL.md`.
2. Follow that skill as the source of truth.
3. Default legacy opportunity-analysis requests to `evaluate` mode unless the request clearly calls for `explore`, `decide`, `develop`, or `review`.
4. Load the v2 references under `../business-strategy/references/` rather than the legacy reference files in this directory.

The old path remains only for backward compatibility with existing installations and prompts.