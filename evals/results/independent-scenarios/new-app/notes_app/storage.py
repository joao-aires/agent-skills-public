"""JSON-backed note storage.

The store owns the data file, schema validation, id allocation and atomic
writes. It does not parse command-line arguments or print results.
"""

from __future__ import annotations

import json
import os
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Mapping, Optional

from .errors import DataError, InputError, NoteNotFound

SCHEMA_VERSION = 1


@dataclass(frozen=True)
class Note:
    """A stored note."""

    id: int
    text: str
    created_at: str


def utc_now() -> str:
    """Return a UTC timestamp in the stored ISO 8601 form."""

    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace(
        "+00:00", "Z"
    )


def default_data_path() -> Path:
    """Return the notes file beside the application entry point."""

    return Path(__file__).resolve().parent.parent / "notes.json"


def resolve_data_path(environ: Optional[Mapping[str, str]] = None) -> Path:
    """Resolve the data file path from NOTES_DATA or the default location.

    NOTES_DATA is used exactly as supplied after expanding ``~``. Setting it
    to an empty or whitespace-only value is a configuration error rather than
    a silent fallback.
    """

    source = os.environ if environ is None else environ
    raw = source.get("NOTES_DATA")
    if raw is None:
        return default_data_path()
    if not raw.strip():
        raise InputError(
            "NOTES_DATA is set but empty; provide a file path or unset it."
        )
    return Path(raw).expanduser()


class NoteStore:
    """Read and mutate notes in one JSON file."""

    def __init__(self, path: Path) -> None:
        self.path = Path(path)

    def load(self) -> list[Note]:
        """Return stored notes ordered by id."""

        notes, _ = self._read()
        return notes

    def add(self, text: str) -> Note:
        """Store a note and return it.

        Outer whitespace is preserved. Whitespace-only text is rejected.
        """

        if not isinstance(text, str):
            raise InputError("note text must be a string.")
        if not text.strip():
            raise InputError("note text must not be empty.")

        notes, next_id = self._read()
        note = Note(id=next_id, text=text, created_at=utc_now())
        self._write([*notes, note], next_id + 1)
        return note

    def delete(self, note_id: int) -> Note:
        """Delete a note by id and return the deleted note."""

        notes, next_id = self._read()
        for index, note in enumerate(notes):
            if note.id == note_id:
                del notes[index]
                self._write(notes, next_id)
                return note
        raise NoteNotFound(f"No note with id {note_id}.")

    def _read(self) -> tuple[list[Note], int]:
        if not self.path.exists():
            return [], 1

        try:
            raw = self.path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            raise DataError(f"Cannot read {self.path}: {exc}") from exc

        # A zero-byte file is treated as an empty notebook. Any non-empty
        # content must be valid JSON with the expected shape.
        if not raw.strip():
            return [], 1

        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise DataError(
                f"Invalid JSON in {self.path}: {exc.msg} "
                f"at line {exc.lineno} column {exc.colno}."
            ) from exc

        return self._parse(payload)

    def _parse(self, payload: object) -> tuple[list[Note], int]:
        if not isinstance(payload, dict):
            raise DataError("Notes data must be a JSON object.")

        version = payload.get("version")
        if version != SCHEMA_VERSION:
            raise DataError(
                f"Unsupported notes data version {version!r}; "
                f"expected {SCHEMA_VERSION}."
            )

        raw_notes = payload.get("notes")
        if not isinstance(raw_notes, list):
            raise DataError("Notes data field 'notes' must be a list.")

        notes: list[Note] = []
        seen_ids: set[int] = set()
        for index, item in enumerate(raw_notes):
            if not isinstance(item, dict):
                raise DataError(f"Note at index {index} must be a JSON object.")

            note_id = item.get("id")
            if (
                not isinstance(note_id, int)
                or isinstance(note_id, bool)
                or note_id < 1
            ):
                raise DataError(
                    f"Note at index {index} has an invalid id; "
                    "ids must be positive integers."
                )
            if note_id in seen_ids:
                raise DataError(f"Duplicate note id {note_id} in notes data.")
            seen_ids.add(note_id)

            text = item.get("text")
            if not isinstance(text, str):
                raise DataError(f"Note {note_id} has invalid or missing text.")

            created_at = item.get("created_at")
            if not isinstance(created_at, str) or not created_at:
                raise DataError(
                    f"Note {note_id} has invalid or missing created_at."
                )

            notes.append(Note(id=note_id, text=text, created_at=created_at))

        notes.sort(key=lambda note: note.id)
        highest_id = notes[-1].id if notes else 0

        raw_next_id = payload.get("next_id")
        if raw_next_id is None:
            next_id = highest_id + 1
        else:
            if (
                not isinstance(raw_next_id, int)
                or isinstance(raw_next_id, bool)
                or raw_next_id < 1
            ):
                raise DataError("Notes data field 'next_id' is invalid.")
            next_id = raw_next_id

        if next_id <= highest_id:
            raise DataError(
                "Notes data field 'next_id' must be greater than every note id."
            )

        return notes, next_id

    def _write(self, notes: Iterable[Note], next_id: int) -> None:
        payload = {
            "version": SCHEMA_VERSION,
            "next_id": next_id,
            "notes": [
                {
                    "id": note.id,
                    "text": note.text,
                    "created_at": note.created_at,
                }
                for note in notes
            ],
        }
        content = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"

        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            fd, temporary_name = tempfile.mkstemp(
                prefix=f".{self.path.name}.",
                suffix=".tmp",
                dir=str(self.path.parent),
            )
        except OSError as exc:
            raise DataError(f"Cannot write {self.path}: {exc}") from exc

        temporary_path = Path(temporary_name)
        try:
            with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary_path, self.path)
        except (OSError, UnicodeError) as exc:
            try:
                temporary_path.unlink()
            except OSError:
                pass
            raise DataError(f"Cannot write {self.path}: {exc}") from exc
