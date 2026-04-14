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