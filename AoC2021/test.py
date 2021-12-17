import numpy as np

with open("inputd7.txt") as file:
    puzzle = np.array(file.readline().strip("\n").split(","), dtype=np.int64)
    fuel = 0
    for el in puzzle:

