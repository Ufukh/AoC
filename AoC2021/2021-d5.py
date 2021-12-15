import numpy as np
import re
from collections import Counter

with open("inputd5.txt") as file:
    puzzle = file.readlines()
    mymap = np.zeros(shape=(1, 1), dtype=int)
    part1 = []
    diag = []
    count = 0
    count1 = 0
    print(len(puzzle))
    for coordinates in puzzle:
        coord = re.findall(r"\d+", coordinates)
        x1 = int(coord[0])
        y1 = int(coord[1])
        x2 = int(coord[2])
        y2 = int(coord[3])
        if x1 == x2 or y1 == y2:
            part1 += [
                (x, y)
                for x in range(min(x1, x2), max(x1, x2) + 1)
                for y in range(min(y1, y2), max(y1, y2) + 1)
            ]
        else:
            print(x1, y1, x2, y2)
            if x1 > x2:
                if y1 < y2:
                    diag += [(x, y2 - idx) for idx, x in enumerate(range(x2, x1 + 1))]
                if y1 > y2:
                    diag += [(x, y2 + idx) for idx, x in enumerate(range(x2, x1 + 1))]
                # print(list(enumerate(range(x2, x1))))
            else:
                if y1 < y2:
                    diag += [(x, y1 + idx) for idx, x in enumerate(range(x1, x2 + 1))]
                if y1 > y2:
                    diag += [(x, y1 - idx) for idx, x in enumerate(range(x1, x2 + 1))]
    p1 = [pt for pt in Counter(part1).values() if pt > 1]
    part1 += diag
    p2 = [pt for pt in Counter(part1).values() if pt > 1]
    print(len(p1))
    print(len(p2))
