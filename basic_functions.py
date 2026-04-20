import random
from is_valid_motion import is_valid_motion

def make_series(length, species): 
    series = []
    for i in range(length):
        series.append([])

    for beat in series:
        if species == 1:
            beat.append(random.randint(0, 7))
        elif species == 2:
            beat.append(random.randint(0, 7))
            beat.append(random.randint(0, 7))
        elif species == 3:
            num_pitches = random.randint(1, 2)
            if num_pitches == 1:
                beat.append(random.randint(0, 7))
            else:
                beat.append(random.randint(0, 7))
                beat.append(random.randint(0, 7))
        else: raise Exception("Invalid species number. Must be 1, 2, or 3.")

    #print("Generated Series: ", series)
    return series

def get_prev_pitches(series, index, index2):

    flat = [pitch for beat in series[:index] for pitch in beat] + series[index][:index2]
    
    return flat[-2:]  # Return the last two pitches before the current one

def fix_series(series):
    for index, beat in enumerate(series):
        for index2, pitch in enumerate(beat):
            prev_pitches = get_prev_pitches(series, index, index2)
            while not is_valid_motion(pitch, prev_pitches):
                new_pitch = random.randint(0, 7)
                if is_valid_motion(new_pitch, prev_pitches):
                    series[index][index2] = new_pitch
                    break
    #print("Fixed series: ", series)
    return series

def convert_to_notes(series):
    note_dict = { 
        0: "C",
        1: "D",
        2: "E",
        3: "F",
        4: "G",
        5: "A",
        6: "B",
        7: "C"
    }
    converted_series = [[note_dict[pitch] for pitch in beat] for beat in series]
    print(converted_series)