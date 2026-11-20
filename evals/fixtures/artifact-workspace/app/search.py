def filter_notes(notes, term):
    term = term.lower()
    return [note for note in notes if term in note["body"].lower()]
