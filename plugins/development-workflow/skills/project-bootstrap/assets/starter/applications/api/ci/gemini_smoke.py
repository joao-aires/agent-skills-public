"""Explicit live smoke tests, never included in ordinary CI."""

import argparse
import json
import os
from pathlib import Path

from google import genai
from google.genai import types

from notes.ai import IdeaSummary, validate_summary

parser = argparse.ArgumentParser()
parser.add_argument("--live", action="store_true", required=True)
parser.add_argument("--audio", type=Path)
parser.add_argument("--expected-transcript", type=Path)
args = parser.parse_args()
if bool(args.audio) != bool(args.expected_transcript):
    parser.error("Audio and expected transcript must be supplied together")
client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"],
    http_options=types.HttpOptions(timeout=20000, retry_options=types.HttpRetryOptions(attempts=1)),
)
model = os.environ["GEMINI_MODEL"]
response = client.models.generate_content(
    model=model,
    contents="Summarize this synthetic note: Build a simple private project notebook.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json", response_schema=IdeaSummary, max_output_tokens=256
    ),
)
validate_summary(response.text or "")
result = {"model": model, "llm_schema": "passed", "audio": "not-run"}
if args.audio:
    if args.audio.stat().st_size > 10 * 1024 * 1024:
        parser.error("Smoke audio must be <=10 MiB")
    audio_model = os.environ["GEMINI_AUDIO_MODEL"]
    output = client.models.generate_content(
        model=audio_model,
        contents=[
            "Transcribe this audio verbatim. Return only the transcript.",
            types.Part.from_bytes(data=args.audio.read_bytes(), mime_type="audio/wav"),
        ],
        config=types.GenerateContentConfig(max_output_tokens=512),
    )
    expected = args.expected_transcript.read_text().lower().split()
    actual = (output.text or "").lower().split()
    # Levenshtein word error rate; never an exact live-output equality assertion.
    row = list(range(len(actual) + 1))
    for i, word in enumerate(expected, 1):
        nxt = [i]
        for j, other in enumerate(actual, 1):
            nxt.append(min(nxt[-1] + 1, row[j] + 1, row[j - 1] + (word != other)))
        row = nxt
    wer = row[-1] / max(1, len(expected))
    result.update(
        audio_model=audio_model, audio="passed" if wer <= 0.2 else "failed", word_error_rate=wer
    )
    if wer > 0.2:
        raise SystemExit(json.dumps(result))
print(json.dumps(result))
