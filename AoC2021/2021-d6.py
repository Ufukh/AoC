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
        nnewfish = np.count_nonzero(fishes[0, :] == 0)
        fishes[fishes != 0] -= 1
        fishes[fishes == 0] = 6
        np.append(fishes[[8] * nnewfish, [0] * nnewfish])
