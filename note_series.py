from basic_functions import make_series, fix_series, convert_to_notes
from note import Note

class Note_Series:

    def __init__(self, name, length):
        self.name = name
        self.length = length
        species = int(input("input species 1 or 2 for " + self.name + ": "))
        self.species = species
        self.series = fix_series(make_series(length, species))
        self.reverse_series = [beat[::-1] for beat in self.series[::-1]]
        self.update_notes()

    def reroll(self):
        self.series = fix_series(make_series(self.length, self.species))
        self.reverse_series = [beat[::-1] for beat in self.series[::-1]]
        self.update_notes()


    def overwrite(self, new_series):
        self.series = new_series
        self.reverse_series = [beat[::-1] for beat in self.series[::-1]]
        self.update_notes()

    def update_notes(self):
        self.notes = [Note(pitch, i, j, self.series) for i, beat in enumerate(self.series) for j, pitch in enumerate(beat)]