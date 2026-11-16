"""Command-line interface for the local notes application."""

from __future__ import annotations

import argparse
import sys
from typing import Optional

from .errors import DataError, InputError, NoteNotFound
from .search import search_notes
from .storage import Note, NoteStore, resolve_data_path


def positive_int(value: str) -> int:
    """Parse a positive integer note id, rejecting zero and negatives."""

    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "id must be a positive integer"
        ) from exc
    if number < 1:
        raise argparse.ArgumentTypeError("id must be a positive integer")
    return number


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="notes.py",
        description="Store, list, search and delete notes in a local JSON file.",
    )
    subparsers = parser.add_subparsers(
        dest="command", metavar="command", required=True
    )

    add_parser = subparsers.add_parser("add", help="store a note and print its id")
    add_parser.add_argument("text", help="note text")

    subparsers.add_parser("list", help="list notes in id order")

    search_parser = subparsers.add_parser(
        "search", help="find notes containing a term (case-insensitive)"
    )
    search_parser.add_argument("term", help="literal text to find")

    delete_parser = subparsers.add_parser("delete", help="delete a note by id")
    delete_parser.add_argument("note_id", type=positive_int, metavar="id")

    return parser


def format_note(note: Note) -> str:
    return f"{note.id}: {note.text}"


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        store = NoteStore(resolve_data_path())

        if args.command == "add":
            note = store.add(args.text)
            print(note.id)
        elif args.command == "list":
            for note in store.load():
                print(format_note(note))
        elif args.command == "search":
            matches = search_notes(store.load(), args.term)
            if matches:
                for note in matches:
                    print(format_note(note))
            else:
                print("No matches.", file=sys.stderr)
        elif args.command == "delete":
            note = store.delete(args.note_id)
            print(f"Deleted note {note.id}.")
        else:  # pragma: no cover - argparse requires a known subcommand
            parser.error(f"unknown command {args.command!r}")
    except InputError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    except (NoteNotFound, DataError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    return 0
