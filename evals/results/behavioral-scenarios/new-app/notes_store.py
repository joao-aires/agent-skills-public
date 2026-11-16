"""Durable JSON storage for the notes application.

This module owns the on-disk format and every read and write of the notes
file. It knows nothing about command-line arguments or search matching.

File format (single JSON object)::

    {
      "version": 1,
      "next_id": 3,
      "notes": [
        {"id": 1, "text": "buy milk", "created_at": "2026-11-15T09:12:03Z"},
        {"id": 2, "text": "call Ana", "created_at": "2026-11-15T09:13:40Z"}
      ]
    }

Writes replace the file atomically so an interrupted write cannot truncate an
existing notes file. There is no cross-process locking; two writers that
overlap can lose one update (a documented limitation, not a silent one).
"""

from __future__ import annotations

import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = 1
DEFAULT_PATH = "~/.notes.json"
ENV_VAR = "NOTES_DATA"
_TEMP_PREFIX = ".notes-"
_TEMP_SUFFIX = ".tmp"


class StoreError(Exception):
    """The notes file could not be read, parsed, or written."""


class NoteNotFound(StoreError):
    """No note with the requested id exists."""


def resolve_path(environ=None) -> Path:
    """Return the notes file path, honouring ``NOTES_DATA``.

    An unset or empty ``NOTES_DATA`` falls back to ``~/.notes.json``. The
    result is expanded for ``~`` but not resolved to an absolute path, so a
    relative override stays relative to the caller's working directory.
    """

    source = os.environ if environ is None else environ
    raw = source.get(ENV_VAR) or DEFAULT_PATH
    return Path(raw).expanduser()


def _now() -> str:
    """Return the current UTC time as an ISO 8601 ``...Z`` string."""

    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def _validate(data, path: Path) -> dict:
    """Return a normalised store document or raise ``StoreError``."""

    if not isinstance(data, dict):
        raise StoreError(f"{path}: expected a JSON object at the top level")

    version = data.get("version")
    if version is not None and version != SCHEMA_VERSION:
        raise StoreError(
            f"{path}: unsupported schema version {version!r}; expected {SCHEMA_VERSION}"
        )

    raw_notes = data.get("notes")
    if not isinstance(raw_notes, list):
        raise StoreError(f"{path}: 'notes' must be a JSON array")

    notes = []
    seen = set()
    for index, item in enumerate(raw_notes):
        if not isinstance(item, dict):
            raise StoreError(f"{path}: note {index} is not a JSON object")
        note_id = item.get("id")
        if isinstance(note_id, bool) or not isinstance(note_id, int) or note_id < 1:
            raise StoreError(f"{path}: note {index} has an invalid id {note_id!r}")
        if note_id in seen:
            raise StoreError(f"{path}: duplicate note id {note_id}")
        text = item.get("text")
        if not isinstance(text, str):
            raise StoreError(f"{path}: note {note_id} has a non-string text")
        created_at = item.get("created_at")
        seen.add(note_id)
        notes.append(
            {
                "id": note_id,
                "text": text,
                "created_at": created_at if isinstance(created_at, str) else None,
            }
        )

    notes.sort(key=lambda note: note["id"])
    next_id = data.get("next_id")
    if isinstance(next_id, bool) or not isinstance(next_id, int) or next_id < 1:
        next_id = max(seen, default=0) + 1
    else:
        next_id = max(next_id, max(seen, default=0) + 1)

    return {"version": SCHEMA_VERSION, "next_id": next_id, "notes": notes}


class NoteStore:
    """Read and write notes in one JSON file."""

    def __init__(self, path):
        self.path = Path(path).expanduser()

    def _load(self) -> dict:
        try:
            raw = self.path.read_text(encoding="utf-8")
        except FileNotFoundError:
            return {"version": SCHEMA_VERSION, "next_id": 1, "notes": []}
        except OSError as exc:
            raise StoreError(f"cannot read {self.path}: {exc}") from exc

        if not raw.strip():
            raise StoreError(f"{self.path}: file is empty; expected a JSON object")

        try:
            data = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise StoreError(f"{self.path}: invalid JSON: {exc}") from exc

        return _validate(data, self.path)

    def _save(self, data: dict) -> None:
        parent = self.path.parent
        try:
            parent.mkdir(parents=True, exist_ok=True)
            descriptor, temporary = tempfile.mkstemp(
                dir=str(parent), prefix=_TEMP_PREFIX, suffix=_TEMP_SUFFIX
            )
        except OSError as exc:
            raise StoreError(f"cannot prepare a write to {self.path}: {exc}") from exc

        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                json.dump(data, handle, ensure_ascii=False, indent=2)
                handle.write("\n")
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, self.path)
        except BaseException as exc:
            try:
                os.unlink(temporary)
            except OSError:
                pass
            if isinstance(exc, OSError):
                raise StoreError(f"cannot write {self.path}: {exc}") from exc
            raise

    def list_notes(self):
        """Return every note, ordered by id."""

        return [dict(note) for note in self._load()["notes"]]

    def add(self, text: str) -> dict:
        """Append a note and return it. Ids increase and are never reused."""

        if not isinstance(text, str):
            raise TypeError("note text must be a string")
        data = self._load()
        note = {"id": data["next_id"], "text": text, "created_at": _now()}
        data["notes"].append(note)
        data["next_id"] = note["id"] + 1
        self._save(data)
        return dict(note)

    def delete(self, note_id: int) -> dict:
        """Remove one note and return it, or raise ``NoteNotFound``."""

        data = self._load()
        for index, note in enumerate(data["notes"]):
            if note["id"] == note_id:
                removed = data["notes"].pop(index)
                self._save(data)
                return dict(removed)
        raise NoteNotFound(f"no note with id {note_id}")
