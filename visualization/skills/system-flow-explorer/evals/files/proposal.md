# Supplied design brief (synthetic)

A reader uses a client to request and display a document from the lookup API.
After reading, they may request an optional explanation using the returned text.
Propose POST /documents/explain for this extension. The API calls an external
model provider through an in-process adapter; provider selection and wire URL
are undecided. The original document remains visible on failure. Correlate the
explanation with documentId and requestId, and discard updates for stale selections.
Prompt/tool examples are conceptual, not provider wire captures. Assess prose
support against supplied facts separately from schema validation. No durable
store is requested: the synthetic lookup catalog is an in-process dictionary.
