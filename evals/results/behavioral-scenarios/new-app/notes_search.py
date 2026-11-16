"""Matching rules for note search.

Search is deliberately small: a case-insensitive substring test where every
run of whitespace counts as a single space. Ranking, tokenisation and prefix
operators are out of scope; results keep the caller's order (id order, as
produced by the store).
"""

from __future__ import annotations


class EmptySearchTerm(ValueError):
    """The search term has no searchable text."""


def _fold(value: str) -> str:
    return " ".join(value.split()).casefold()


def normalize_term(term: str) -> str:
    """Return the term to match with, or raise ``EmptySearchTerm``."""

    folded = _fold(term)
    if not folded:
        raise EmptySearchTerm("search term is empty")
    return folded


def search(notes, term: str):
    """Return the notes whose text contains ``term``, preserving input order."""

    needle = normalize_term(term)
    return [dict(note) for note in notes if needle in _fold(note["text"])]
