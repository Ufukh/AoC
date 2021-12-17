import numpy as np

with open("inputd7.txt") as file:
    puzzle = np.array(file.readline().strip("\n").split(","), dtype=np.int64)
    besthpos = np.median(puzzle)
    besthpos2 = np.mean(puzzle)
    fuelp1 = 0
    best = []
    for position in puzzle:
        fuelp1 += abs(position - besthpos)

    for hpos in range(min(puzzle), max(puzzle) + 1):
        fuelp2 = 0
        for position in puzzle:
            fuelp2 += (abs(position - hpos) * (abs(position - hpos) + 1)) // 2
        best.append(fuelp2)

    print(fuelp1)
    print(min(best))
