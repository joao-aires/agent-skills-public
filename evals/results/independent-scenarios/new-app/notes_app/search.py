"""Search behavior for stored notes.

The search is a case-insensitive literal substring match. It is a pure
function so it can be tested without the command line or the data file.
"""

from __future__ import annotations

from typing import Iterable

from .errors import InputError
from .storage import Note


def search_notes(notes: Iterable[Note], term: str) -> list[Note]:
    """Return notes whose text contains ``term``, preserving input order."""

    if not isinstance(term, str) or not term.strip():
        raise InputError("search term must not be empty.")

    needle = term.casefold()
    return [note for note in notes if needle in note.text.casefold()]
