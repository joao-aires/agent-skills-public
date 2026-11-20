NOTES = {1: {"owner": "alice", "body": "alice private"}, 2: {"owner": "bob", "body": "bob private"}}


def read_note(user, note_id):
    note = NOTES.get(note_id)
    if note is None or user is None or note["owner"] != user:
        return None
    return note
