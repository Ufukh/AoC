import numpy as np

with open("inputd6.txt") as file:
    puzzle = file.readline().split(",")
    puzzle = list(map(int, puzzle))

    fishes = np.array([puzzle, [0] * len(puzzle)])
    # print(test[1, :])
    print(np.count_nonzero(fishes[0, :] == 0))
    fishes[0, 0] = 0
    print(fishes[0, :])
    fishes[fishes[0, :] != 0] -= 1
    print(fishes[0, :])
    fishes[fishes[0, :] == 0] = 5
    print(fishes[0, 0])
    print(fishes[0, :])

    print(fishes[0, :])
    fishes[0, :] -= 1
    print(fishes[0, :])
    for i in range(0, 79):
        nnewfish = np.count_nonzero(fishes[0, :] == 0)  # count number of new fish
        fishes[fishes[:, 0] == 0, 1] = 1  # add flag to fish that gave birth
        fishes[fishes[0, :] == 0] = 6  # reinitialize fish that gave birth
        np.append(
            fishes[[8] * nnewfish, [1] * nnewfish]
        )  # append new lantern fish with flag
        fishes[fishes[:, 1] == 1, 0] -= 1  # substract one to fish without flag
        fishes[fishes[1, :] == 1] = 0  # remove flag
    print(fishes.shape)
