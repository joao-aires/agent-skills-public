"""Errors shared by the notes application layers."""


class NotesError(Exception):
    """Base class for expected, user-facing notes errors."""


class InputError(NotesError):
    """The caller supplied input the application cannot accept."""


class DataError(NotesError):
    """The notes data file cannot be read, parsed or written safely."""


class NoteNotFound(NotesError):
    """The requested note id does not exist."""
