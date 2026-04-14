from note_series import Note_Series

def main():
    length = int(input("Input Series Length: "))
    species = int(input("Input Species (1 or 2): "))
    note_series = Note_Series(length, species)
    print("Series: ", note_series.series)
    print("Reverse Series: ", note_series.reverse_series)

main()