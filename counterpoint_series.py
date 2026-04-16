from note_series import Note_Series
from reroll_counterpoint import reroll_counterpoint, reroll_counterpoint_series1, reroll_counterpoint_series2, reroll_mobius_strip
from basic_functions import convert_to_notes

class Counterpoint_series:
    def __init__(self, name):
        self.name = name
        length = int(input("input series length for " + self.name + ": "))
        self.series1 = Note_Series(f"series 1 in {self.name}", length)
        self.series2 = Note_Series(f"series2 in {self.name}", length)
        fixed_series = reroll_counterpoint(self.series1, self.series2)
        self.series1 = fixed_series[0]
        self.series2 = fixed_series[1]
    
    def get_series1_notes(self):
        return convert_to_notes(self.series1.series)
    
    def get_series2_notes(self):
        return convert_to_notes(self.series2.series)
    
    def mobius_strip(self):
        self.series1 = reroll_mobius_strip(self.series1)
        self.series2.overwrite(self.series1.reverse_series)
    


counterpoint_series = Counterpoint_series("counterpoint_series")
counterpoint_series.mobius_strip()
print("Series 1 notes:")
print(counterpoint_series.get_series1_notes())
print("Series 2 notes:")
print(counterpoint_series.get_series2_notes())

