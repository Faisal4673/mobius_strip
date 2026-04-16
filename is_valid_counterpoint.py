
import itertools

from basic_functions import get_prev_pitches

CONSONANT_INTERVALS = [0, 2, 4, 5, 7]


def is_consonant(pitch1, pitch2):
    
    if abs(pitch1 - pitch2) in CONSONANT_INTERVALS:
        return True
    else: return False

def is_stepwise_dissonance(pitch,  index, index2, series):
    if get_prev_pitches(series, index, index2) and abs(get_prev_pitches(series, index, index2)[-1] - pitch) == 1:
        return True
    else: return False

def parallel_fifths(pitch1, pitch2, index, index2, series1, series2):
    if abs(pitch1 - pitch2) == 4 and get_prev_pitches(series1, index, index2) and get_prev_pitches(series2, index, index2) and abs(get_prev_pitches(series1, index, index2)[-1] - get_prev_pitches(series2, index, index2)[-1]) == 4:
        return True
    else: return False

def parallel_octaves(pitch1, pitch2, index, index2, series1, series2):
    if (abs(pitch1 - pitch2) == 0 or abs(pitch1 - pitch2) == 7) and get_prev_pitches(series1, index, index2) and get_prev_pitches(series2, index, index2) and abs(get_prev_pitches(series1, index, index2)[-1] - get_prev_pitches(series2, index, index2)[-1]) == 0:
        return True
    else: return False
    
def jump_to_fifth()

def is_valid_counterpoint(series1, series2):
    counter = 0
    for index, (beat1, beat2) in enumerate(zip(series1, series2)):
        counter2 = 0
        if len(beat1) > len(beat2):
            for index2, (pitch1, pitch2) in enumerate(zip(beat1, itertools.cycle(beat2))):
                if is_consonant(pitch1, pitch2) or (index2 == 1 and is_stepwise_dissonance(pitch1, index, index2, series1)):
                    counter2 += 1
            if counter2 == len(beat1):
                counter += 1
        if len(beat2) > len(beat1):
            for index2, (pitch1, pitch2) in enumerate(zip(itertools.cycle(beat1), beat2)):
                if is_consonant(pitch1, pitch2) or (index2 == 1 and is_stepwise_dissonance(pitch2, index, index2, series2)):
                    counter2 += 1
            if counter2 == len(beat2):
                counter += 1
        if len(beat1) == len(beat2):
            for index2, (pitch1, pitch2) in enumerate(zip(beat1, beat2)):
                if (is_consonant(pitch1, pitch2) and not parallel_fifths(pitch1, pitch2, index, index2, series1, series2) and not parallel_octaves(pitch1, pitch2, index, index2, series1, series2)) or (index2== 1 and is_stepwise_dissonance(pitch1, index, index2, series1) and is_stepwise_dissonance(pitch2, index, index2, series2)):
                    counter2 += 1
            if counter2 == len(beat1):
                counter += 1
            
       
        
    if counter == len(series1):
        return True
    else: return False


            

