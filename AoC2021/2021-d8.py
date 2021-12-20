import numpy as np

with open("inputd8.txt") as file:
    puzzle = file.readlines()
    count = 0
    for screen in puzzle:
        signals, notes = screen.strip("\n").split("|")
        numbers = notes.lstrip().split(" ")

        for el in numbers:
            if len(el) in (2, 3, 4, 7):
                count += 1
    print(count)
