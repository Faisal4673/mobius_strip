import random
import itertools

def get_prev_pitches(series, index, index2):

    flat = [pitch for beat in series[:index] for pitch in beat] + series[index][:index2]
    
    return flat[-2:]  # Return the last two pitches before the current one

def new_multi_species_series(length, species):

    
    #length = int(input("Input Series Length: "))
    series = []
    for i in range(length):
        series.append([])


    for beat in series:
        num_pitches = random.randint(1, species)
        if num_pitches == 1:
            beat.append(random.randint(0, 7))
        else:
            beat.append(random.randint(0, 7))
            beat.append(random.randint(0, 7))

    #print("Generated Series: ", series)
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
                new_pitch = random.randint(0, 7)
                if is_valid_motion(new_pitch, prev_pitches):
                    series[index][index2] = new_pitch
                    break
    #print("Fixed series: ", series)
    return series



def is_reversable(series):
    reverse_series = [beat[::-1] for beat in series[::-1]]
    counter = 0
    consonant_intervals = [2, 4, 5, 7]
    print("Series: ", series)
    print("Reverse series: ", reverse_series)


    for index, (beat, reverse_beat) in enumerate(zip(series, reverse_series)):
        counter2 = 0
        if len(beat) > len(reverse_beat):
            for index2, (pitch, reverse_pitch) in enumerate(zip(beat, itertools.cycle(reverse_beat))):
                print("pitch: ", pitch, "reverse pitch: ", reverse_pitch)
                if abs(pitch - reverse_pitch) in consonant_intervals:
                    counter2 += 1
                if abs(pitch - reverse_pitch) not in consonant_intervals and counter2 == 1 and get_prev_pitches(series, index, index2)[-1:] and abs(get_prev_pitches(series, index, index2)[-1:][0] - pitch) == 1:
                    counter2+= 1
            if counter2 == len(beat):
                counter += 1
        elif len(beat) < len(reverse_beat):
            for index2, (pitch, reverse_pitch) in enumerate(zip(itertools.cycle(beat), reverse_beat)):
                if abs(pitch - reverse_pitch) in consonant_intervals:
                    counter2 += 1
                if abs(pitch - reverse_pitch) not in consonant_intervals and counter2 == 1 and get_prev_pitches(reverse_series, index, index2)[-1:] and abs(get_prev_pitches(reverse_series, index, index2)[-1:][0] - pitch) == 1:
                    counter2+= 1
            if counter2 == len(beat):
                counter += 1
        else: 
            for pitch, reverse_pitch in zip(beat, reverse_beat):
                if abs(pitch - reverse_pitch) in consonant_intervals:
                    counter2 += 1
            if counter2 == len(beat):
                counter +=1
    


    if counter == len(series):
        return True
    else: return False

def make_reversable_series():

    reversables_found = 0
    while reversables_found == 0:
        series = new_multi_species_series(8, 2)
        if is_reversable(fix_series(series)):
            reversables_found += 1
    print("found reversable series!: ", series)
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

    

#$check_reversable(fix_series(new_multi_species_series()))

convert_to_notes(make_reversable_series())

#is_reversable(fix_series(new_multi_species_series()))

    
    


    
    
    
#def return_prev_pitches(series):
    #for index, beat in enumerate(series):
        #for index2, pitch in enumerate(beat):
            #prev_pitches = get_prev_pitches(series, index, index2)
            #print(f"Current pitch: {pitch}, Previous pitches: {prev_pitches}")


            



#new_multi_species_series()


#print(type(get_prev_pitches(new_multi_species_series(), 0, 0)))
