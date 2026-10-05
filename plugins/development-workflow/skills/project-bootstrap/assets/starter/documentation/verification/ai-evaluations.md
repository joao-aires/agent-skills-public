# AI evaluation

Default pytest checks synthetic structured-output validation, not live model quality. Optional group ai enables ci/gemini_smoke.py --live; requires explicit GEMINI_API_KEY and GEMINI_MODEL. Audio additionally requires GEMINI_AUDIO_MODEL, --audio approved.wav and --expected-transcript approved.txt. WAV only, <=10 MiB, max output tokens and 20s timeout, no retry loop. Short approved synthetic/consented audio; never commit private recordings or credentials. WER threshold is a smoke threshold, not broad quality certification. Review current free-tier model eligibility, quota and project billing before execution; this script does not promise zero cost or change billing. No live call is made by CI.

ADK and LangChain specialist packages remain opt-in; this reference app does not add either framework when a direct SDK smoke is sufficient.
