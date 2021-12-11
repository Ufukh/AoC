import numpy as np
import re

with open("inputd5.txt") as file:
    puzzle = file.readlines()
    mymap = np.zeros(shape=(1, 1), dtype=int)
    line = []
    for coordinates in puzzle:
        line.append(re.findall(r"\d+", coordinates))
    myarray = np.array(line, dtype=np.int64)
    for i in range(0, myarray.shape[1]):
        print(np.max(myarray[:, i]))
