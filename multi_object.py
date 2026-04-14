import random
import itertools
from multi_species import new_multi_species_series, fix_series

class Note_Series:

    def __init__(self, length, species):
        self.length = length
        self.species = species
        self.series = fix_series(new_multi_species_series(length, species))
        self.reverse_series = [beat[::-1] for beat in self.series[::-1]]


