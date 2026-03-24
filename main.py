import random

def new_series():
    series = []
    for i in range(0, 8):
        series.append(random.randint(1, 7))
    return series


def make_series_set():
    series_set = set()
    for i in range(0, 7**8):
        series_set.add(tuple(new_series()))
    series_list = list(series_set)
    return series_list
    

make_series_set()
print(make_series_set())