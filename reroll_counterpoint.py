from note_series import Note_Series
from is_valid_counterpoint import is_valid_counterpoint

def reroll_counterpoint(series1, series2):
    local_series1 = series1
    local_series2 = series2

    while True:
        local_series1.reroll()
        local_series2.reroll()
        if is_valid_counterpoint(local_series1.series, local_series2.series):
            break

    
    return local_series1, local_series2
    


