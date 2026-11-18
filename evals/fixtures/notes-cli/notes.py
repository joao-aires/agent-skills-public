#!/usr/bin/env python3
"""Small local notes CLI used by the requirements-to-scope eval case."""
import json
import os
import sys
from pathlib import Path

DATA = Path(os.environ.get("NOTES_DATA", "notes.json"))


def load():
    return json.loads(DATA.read_text()) if DATA.exists() else []


def save(notes):
    DATA.write_text(json.dumps(notes, indent=2))


def add(text):
    notes = load()
    notes.append({"id": len(notes) + 1, "text": text})
    save(notes)


def list_notes():
    for note in load():
        print(f"{note['id']}: {note['text']}")


def search(term):
    for note in load():
        if term.lower() in note["text"].lower():
            print(f"{note['id']}: {note['text']}")


def delete(identifier):
    notes = [note for note in load() if note["id"] != identifier]
    save(notes)


if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "list"
    if command == "add":
        add(sys.argv[2])
    elif command == "search":
        search(sys.argv[2])
    elif command == "delete":
        delete(int(sys.argv[2]))
    else:
        list_notes()
