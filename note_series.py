import random
import itertools
from basic_functions import make_series, fix_series, convert_to_notes

class Note_Series:

    def __init__(self, name, length):
        self.name = name
        self.length = length
        species = int(input("input species 1 or 2 for " + self.name + ": "))
        self.species = species
        self.series = fix_series(make_series(length, species))
        self.reverse_series = [beat[::-1] for beat in self.series[::-1]]

    def reroll(self):
        self.series = fix_series(make_series(self.length, self.species))
        self.reverse_series = [beat[::-1] for beat in self.series[::-1]]
