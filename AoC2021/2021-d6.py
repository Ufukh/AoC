import numpy as np
from collections import Counter

with open("inputd6.txt") as file:
    puzzle = file.readline().split(",")
    puzzle = list(map(int, puzzle))
    fishes = np.array([puzzle, [0] * len(puzzle)])
    for i in range(0, 80):  # change to 256 to brut force part 2
        nnewfish = np.count_nonzero(fishes[0, :] == 0)  # count number of new fish
        fishes[1, fishes[0, :] == 0] = 1  # add flag to fish that gave birth
        fishes[0, fishes[0, :] == 0] = 6  # reinitialize fish that gave birth
        fishes = np.append(
            fishes, [[8] * nnewfish, [1] * nnewfish], axis=1
        )  # append new lantern fish with flag
        fishes[0, fishes[1, :] != 1] -= 1  # substract one to fish without flag
        fishes[1, fishes[1, :] == 1] = 0  # remove flag
    print(fishes.shape[1])  # part 1

    # part 2
    compact = np.zeros(9, dtype=np.int64)
    part2 = np.array(puzzle)
    for i in range(9):
        compact[i] = (part2 == i).sum()
    print(compact)
    for i in range(256):
        compact = np.roll(compact, -1)
        compact[6] += compact[8]
    print(compact.sum())
