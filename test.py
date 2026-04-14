from multi_species import new_multi_species_series, fix_series, get_prev_pitches
import itertools

#def valid_counterpoint(series, reverse_series, index, index2):
    #consonant_intervals = [2, 4, 5, 7]
    #counter = 0
    #if abs(series[index][index2] - reverse_series[index][index2]) in consonant_intervals:
        #counter += 1
    #if abs(series[index][index2] - reverse_series[index][index2]) not in consonant_intervals and counter2 == 1 and get_prev_pitches(series, index, index2)[-1:] and abs(get_prev_pitches(series, index, index2)[-1:][0] - series[index][index2]) == 1:
        #counter2+= 1
    #if counter == len(series[index]):
        #return true



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
                counter+=1
    


    if counter == len(series):
        return True
    else: return False



        

        

        


is_reversable(fix_series(new_multi_species_series()))

    
        
       