import random


def get_prev_pitches(series, index, index2):
    prev_pitches = []

    #Last Beat exists:
    last_beat_exists = index - 1 >= 0
    #Second to Last Beat exists:
    second_to_last_beat_exists = index - 2 >= 0
    #Cases of 2 previous pitches:
    # First note in beat, two notes in previous beat:
    two_previous_pitches_case1 = index2 == 0 and len(series[index - 1]) == 2 and last_beat_exists
    # Second note in beat, one note in previous beat:
    two_previous_pitches_case2 = index2 == 1 and len(series[index - 1]) == 1 and last_beat_exists
    # Second note in beat, two notes in previous beat:
    two_previous_pitches_case3 = index2 == 1 and len(series[index - 1]) == 2 and last_beat_exists
    # First note in beat, one note in previous 2 beats:
    two_previous_pitches_case4 = index2 == 0 and len(series[index - 1]) == 1 and len(series[index - 2]) == 1 and last_beat_exists and second_to_last_beat_exists
    # First note in beat, one note in previous beat, two notes in previous 2 beats:
    two_previous_pitches_case5 = index2 == 0 and len(series[index - 1]) == 1 and len(series[index - 2]) == 2 and last_beat_exists and second_to_last_beat_exists

    #Cases of 1 previous pitch:
    # First note in beat, one note in previous beat:
    one_previous_pitch_case1 = index2 == 0 and len(series[index - 1]) == 1 and last_beat_exists
    # Second note in beat, first beat:
    one_previous_pitch_case2 = index == 0 and len(series[index]) == 2 and index2 == 1
    
    if two_previous_pitches_case1:
        prev_pitches.append(series[index - 1][0])
        prev_pitches.append(series[index - 1][1])
    elif two_previous_pitches_case2:
        prev_pitches.append(series[index - 1][0])
        prev_pitches.append(series[index][0])
    elif two_previous_pitches_case3:
        prev_pitches.append(series[index - 1][1])
        prev_pitches.append(series[index][0])
    elif two_previous_pitches_case4:
        prev_pitches.append(series[index - 2][0])
        prev_pitches.append(series[index - 1][0])
    elif two_previous_pitches_case5:
        prev_pitches.append(series[index - 2][1])
        prev_pitches.append(series[index - 1][0])
    elif one_previous_pitch_case1:
        prev_pitches.append(series[index - 1][0])
    elif one_previous_pitch_case2:
        prev_pitches.append(series[index][0])
    else:       
        print("No previous pitches found.")

    return prev_pitches



    

    

def new_multi_species_series():

    
    #length = int(input("Input Series Length: "))
    series = []
    for i in range(8):
        series.append([])


    for beat in series:
        num_pitches = random.randint(1, 2)
        if num_pitches == 1:
            beat.append(random.randint(0, 7))
        else:
            beat.append(random.randint(0, 7))
            beat.append(random.randint(0, 7))

    print("Generated Series: ", series)
    return series


def is_valid_motion(pitch, previous_pitches):
    #Case of no previous pitches:
    no_previous_pitches = len(previous_pitches) == 0
    #Case of one previous pitch:
    one_previous_pitch = len(previous_pitches) == 1
    two_previous_pitches = len(previous_pitches) == 2

    if no_previous_pitches:
        if pitch == 0:
            return True
        else:
            return False  
    elif one_previous_pitch:
        if abs(pitch - previous_pitches[0]) <= 3 and pitch != previous_pitches[0]:
            return True
        else:
            return False
    else:
        last_pitch = previous_pitches[-1]
        second_to_last_pitch = previous_pitches[-2]
        leap_rule_down = second_to_last_pitch - last_pitch > 2 and pitch - last_pitch != 1
        leap_rule_up = second_to_last_pitch - last_pitch < -2 and pitch - last_pitch != -1
        large_jump = abs(pitch - last_pitch) > 3 
        same_note = pitch == last_pitch
        if not same_note and not large_jump and not leap_rule_down and not leap_rule_up:
            return True
        else:            return False
    
def fix_series(series):
    for index, beat in enumerate(series):
        for index2, pitch in enumerate(beat):
            prev_pitches = get_prev_pitches(series, index, index2)
            while not is_valid_motion(pitch, prev_pitches):
                print(f"Invalid motion found at beat {index}, pitch {pitch}. Previous pitches: {prev_pitches}")
                new_pitch = random.randint(0, 7)
                print(f"Trying new pitch: {new_pitch}")
                if is_valid_motion(new_pitch, prev_pitches):
                    print(f"New pitch {new_pitch} is valid. Updating series.")
                    series[index][index2] = new_pitch
                    break
                else:
                    print(f"New pitch {new_pitch} is still invalid. Retrying.")
    print(series)
    return series

fix_series(new_multi_species_series())

    
    


    
    
    
#def return_prev_pitches(series):
    #for index, beat in enumerate(series):
        #for index2, pitch in enumerate(beat):
            #prev_pitches = get_prev_pitches(series, index, index2)
            #print(f"Current pitch: {pitch}, Previous pitches: {prev_pitches}")


            



#new_multi_species_series()

#return_prev_pitches(new_multi_species_series())

#print(type(get_prev_pitches(new_multi_species_series(), 0, 0)))
