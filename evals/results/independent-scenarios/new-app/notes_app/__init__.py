"""Local notes application: storage, search and command-line layers."""

from .storage import Note, NoteStore, resolve_data_path

__all__ = ["Note", "NoteStore", "resolve_data_path"]
