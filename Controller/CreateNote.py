from Model.Note import Note
from PullNote import pullNote

def CreateNote (title_text: str, content_text: str):
    note = Note(title_text, content_text)
    pullNote(note)
    return note