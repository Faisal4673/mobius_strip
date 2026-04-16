from basic_functions import get_prev_pitches

class Note:

    def __init__(self, pitch, index, index2, series):
        self.pitch = pitch
        self.index = index
        self.index2 = index2
        self.series = series
        self.last_pitch = get_prev_pitches(self.series, self.index, self.index2)[-1] if get_prev_pitches(self.series, self.index, self.index2) else None
        self.next_last_pitch = get_prev_pitches(self.series, self.index, self.index2)[-2] if len(get_prev_pitches(self.series, self.index, self.index2)) > 1 else None
