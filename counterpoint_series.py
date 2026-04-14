from note_series import Note_Series
from is_valid_counterpoint import is_valid_counterpoint
from reroll_counterpoint import reroll_counterpoint

class Counterpoint_series:
    def __init__(self, name):
        self.name = name
        length = int(input("input series length for " + self.name + ": "))
        self.series1 = Note_Series(f"series 1 in {self.name}", length)
        self.series2 = Note_Series(f"series2 in {self.name}", length)
        fixed_series = reroll_counterpoint(self.series1, self.series2)
        self.series1 = fixed_series[0]
        self.series2 = fixed_series[1]
    
    def 
        
        


counterpoint_series = Counterpoint_series("counterpoint_series")
print(counterpoint_series.series1.series)
print(counterpoint_series.series2.series)

