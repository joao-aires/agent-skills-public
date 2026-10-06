---
name: build-evaluated-ai
description: Guide AI features with Google ADK or LangChain/LangGraph when useful, Gemini LLM and speech-to-text testing, and explicit evaluation boundaries.
---

# Build evaluated AI features

- Start with the product task and a clear way to judge success. Use a direct model SDK for simple calls; choose Google ADK or LangChain/LangGraph when their orchestration or integrations help. Avoid introducing both by default.
- Prefer Gemini for low-cost LLM and speech-to-text experiments. Check the chosen model's capabilities, free-tier availability, quota and pricing rather than assuming every call is free. Keep model/provider configuration and secrets outside prompts.
- Use relevant first-party framework skills for implementation details. Keep application logic and data access independent enough to test without the model.
- Validate structured output. Keep authorization, budgets and side-effect policy deterministic outside the model; treat retrieved content as untrusted input.
- Bound tool loops, tokens, retries and execution time. Keep prompts and representative evaluation examples versioned; avoid logging private prompts or recordings.
- Use deterministic fixtures for routine CI and explicit live evaluations for model quality. Check useful outcomes, failure handling, latency and cost; assess transcription with representative audio and the languages the product needs.
- Distinguish uploaded-audio transcription from live voice requirements. Keep product correctness separate from model quality, and report limitations honestly.
