import numpy as np
import re
from collections import Counter

with open("inputd5.txt") as file:
    puzzle = file.readlines()
    mymap = np.zeros(shape=(1, 1), dtype=int)
    points = []
    points += [range(0, 5)]
    points += range(6, 10)
    print(points)
    for coordinates in puzzle:
        coord = re.findall(r"\d+", coordinates)
        x1 = int(coord[0])
        y1 = int(coord[1])
        x2 = int(coord[2])
        y2 = int(coord[3])
        if x1 == x2 or y1 == y2:
            points += [
                (x, y)
                for x in range(min(x1, x2), max(x1, x2) + 1)
                for y in range(min(y1, y2), max(y1, y2) + 1)
            ]
    p1 = [pt for pt in Counter(points).values() if pt > 1]
    print(len(p1))
