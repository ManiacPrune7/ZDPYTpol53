"""
    Reprezentacja notatki
"""

import datetime


class Note:

    NOTE_ID = 1

    def __init__(self, memo: str, tags: list):
        self.id_ = Note.NOTE_ID
        self.creation_date = datetime.datetime.today()
        self.tags = tags
        self.memo = memo

        Note.NOTE_ID += 1

    def match(self, filter_: str) -> bool:
        if filter_ in self.memo or filter_ in self.tags:
            return True
        return False
        # return None


my_note = Note("14:30 silkaaaaa!!!!1111oneone", ['biceps', 'trening'])
# print(my_note.match('klatka'))
print(my_note.id_)

my_note_2 = Note("14:30 silkaaaaa!!!!1111oneone", ['biceps', 'trening'])
# print(my_note.match('klatka'))
print(my_note_2.id_)
