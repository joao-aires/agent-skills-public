from app.notes import all_notes


def search(term, path=None):
    term = term.lower()
    return [note for note in all_notes(path) if term in note["body"].lower()]
