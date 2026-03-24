import random

def new_series():
    series = [0]
    for i in range(1, 8):
        while True:
            next_pitch = random.randint(0, 7)
            last_pitch = series[-1]
            next_last_pitch = series[-2] if len(series) > 1 else None
            leap_rule_down = next_last_pitch is not None and next_last_pitch - last_pitch > 1 and next_pitch - last_pitch != 1
            leap_rule_up = next_last_pitch is not None and next_last_pitch - last_pitch < -1 and next_pitch - last_pitch != -1
            if next_pitch == last_pitch or abs(next_pitch - last_pitch) > 4 or leap_rule_down or leap_rule_up:
                continue                    
            series.append(next_pitch)
            break
    return series


def make_series_set():
    series_set = set()
    attempts_without_new = 0
    while True and attempts_without_new < 100000:
        series = tuple(new_series())
        if series not in series_set:
            series_set.add(series)
            attempts_without_new = 0
        else:
            attempts_without_new += 1
    series_list = list(series_set)
    return series_list

def compare_series(series_list):
    reversable_series = []
    for series in series_list:
        reverse_series = series[::-1]
        counter = 0
        for pitch, reverse_pitch in zip(series, reverse_series):
            if abs(pitch - reverse_pitch) == 0 or abs(pitch - reverse_pitch) == 2 or abs(pitch - reverse_pitch) == 4 or abs(pitch - reverse_pitch) == 5 or abs(pitch - reverse_pitch) == 7:
                counter += 1
        if counter == len(series):
            reversable_series.append(series)
    return reversable_series

def print_series(result):
    for series in result:
        print(series)

print("Generating series...")
result = compare_series(make_series_set())
print(f"Generated {len(result)} reversible series.")
print_series(result)



    
