import random

def new_single_species_series(length):
    # Generate a series of {length} pitches (0-7) with specific rules: 
    series = [0]
    for i in range(1, length):
        while True:
            next_pitch = random.randint(0, 7)
            last_pitch = series[-1]
            next_last_pitch = series[-2] if len(series) > 1 else None
            # Rules:
            leap_rule_down = next_last_pitch is not None and next_last_pitch - last_pitch > 1 and next_pitch - last_pitch != 1
            leap_rule_up = next_last_pitch is not None and next_last_pitch - last_pitch < -1 and next_pitch - last_pitch != -1
            if next_pitch == last_pitch or abs(next_pitch - last_pitch) > 4 or leap_rule_down or leap_rule_up:
                continue                    
            series.append(next_pitch)
            break
    return series