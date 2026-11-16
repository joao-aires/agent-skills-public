#!/usr/bin/env python3
"""Command-line interface for the local notes application.

The CLI owns argument parsing, text normalisation for input, output
formatting and exit codes. Persistence lives in ``notes_store`` and matching
lives in ``notes_search``.

Exit codes: 0 success, 1 runtime or data error, 2 usage error.
"""

from __future__ import annotations

import argparse
import sys

import notes_search
import notes_store

PROG = "notes.py"


def _positive_int(value: str) -> int:
    try:
        number = int(value, 10)
    except ValueError:
        raise argparse.ArgumentTypeError(f"invalid note id {value!r}: expected an integer")
    if number < 1:
        raise argparse.ArgumentTypeError(f"invalid note id {value!r}: expected a positive integer")
    return number


def _single_line(parts) -> str:
    """Join argument words and collapse whitespace into one line."""

    return " ".join(" ".join(parts).split())


def _store() -> notes_store.NoteStore:
    return notes_store.NoteStore(notes_store.resolve_path())


def _print_note(note: dict) -> None:
    print(f"{note['id']}\t{note['text']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=PROG,
        description="Store, list, search and delete notes in a local JSON file.",
        epilog='example: python3 notes.py add "buy milk"',
    )
    commands = parser.add_subparsers(dest="command", required=True, metavar="command")

    add = commands.add_parser("add", help="store a note and print its id")
    add.add_argument("text", nargs="+", metavar="text", help="note text")

    commands.add_parser("list", help="list notes in id order")

    find = commands.add_parser("search", help="find notes containing a term")
    find.add_argument("term", nargs="+", metavar="term", help="text to look for")

    remove = commands.add_parser("delete", help="delete a note by id")
    remove.add_argument("id", type=_positive_int, metavar="id", help="note id")

    return parser


def _add(parts) -> int:
    text = _single_line(parts)
    if not text:
        print(f"{PROG}: error: note text is empty", file=sys.stderr)
        return 2
    note = _store().add(text)
    print(note["id"])
    return 0


def _list() -> int:
    for note in _store().list_notes():
        _print_note(note)
    return 0


def _search(parts) -> int:
    term = _single_line(parts)
    try:
        notes_search.normalize_term(term)
    except notes_search.EmptySearchTerm as exc:
        print(f"{PROG}: error: {exc}", file=sys.stderr)
        return 2

    for note in notes_search.search(_store().list_notes(), term):
        _print_note(note)
    return 0


def _delete(note_id: int) -> int:
    note = _store().delete(note_id)
    print(f"deleted {note['id']}")
    return 0


def main(argv=None) -> int:
    options = build_parser().parse_args(argv)
    try:
        if options.command == "add":
            return _add(options.text)
        if options.command == "list":
            return _list()
        if options.command == "search":
            return _search(options.term)
        return _delete(options.id)
    except notes_store.StoreError as exc:
        print(f"{PROG}: error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
