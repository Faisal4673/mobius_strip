
#Program currently set to single species series, need to update compare series to work with other species as well.
from single_species import new_single_species_series as new_series


def make_series_set():
    # Makes the set of all possible series, with a limit of 1000 attempts without finding a new series to prevent infinite loops.
    series_set = set()
    attempts_without_new = 0
    length = int(input("Input Series Length: "))
    while True and attempts_without_new < 10000:
        series = tuple(new_series(length))
        if series not in series_set:
            series_set.add(series)
            attempts_without_new = 0
        else:
            attempts_without_new += 1
    series_list = list(series_set)
    return series_list

def compare_series(series_list):
    # Reverses each series and compares it to original, if passes all rules adds to the reversable set
    reversable_series = []
    for series in series_list:
        reverse_series = series[::-1]
        counter = 0
        #print("Series: ", series)
        #print("Reverse Series: ", reverse_series)
        for i, (pitch, reverse_pitch) in enumerate(zip(series, reverse_series)):
            last_pitch = series[i-1] if i > 0 else None
            last_reverse_pitch = reverse_series[i-1] if i > 0 else None
            acceptable_intervals = [0, 2, 4, 5, 7]
            # Rules:
            parallel_fifths = last_pitch is not None and last_reverse_pitch is not None and abs(pitch - reverse_pitch) == 4 and abs(last_pitch - last_reverse_pitch) == 4
            parrallel_octaves = last_pitch is not None and last_reverse_pitch is not None and abs(pitch - reverse_pitch) == 7 and abs(last_pitch - last_reverse_pitch) == 7
            jump_to_fifth = last_pitch is not None and last_reverse_pitch is not None and abs(pitch - reverse_pitch) == 4 and abs(pitch - last_pitch) > 1
            jump_to_octave = last_pitch is not None and last_reverse_pitch is not None and abs(pitch - reverse_pitch) == 7 and abs(pitch - last_pitch) > 1
            if abs(pitch - reverse_pitch) in acceptable_intervals and not parallel_fifths and not parrallel_octaves and not jump_to_fifth and not jump_to_octave:
                counter += 1
        if counter == len(series):
            reversable_series.append(series)
    return reversable_series

def print_series(result):
    print("Generating Series...")
    print(f"Total unique series generated: {len(result)}")
    for series in result:
        print(series)

result = compare_series(make_series_set())
print_series(result)


    
