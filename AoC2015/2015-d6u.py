import numpy as np
import re

lights = np.zeros(shape=(1000, 1000), dtype=bool)
part2 = np.zeros(shape=(1000, 1000), dtype=int)

with open("2015/inputd6u.txt") as file:
    puzzle = file.readlines()
    for instruction in puzzle:
        action = re.findall(r"(toggle |turn on |turn off )", instruction)[0]
        startrow = int(re.findall(r"\d{1,3},\d{1,3}", instruction)[0].split(",")[0])
        startcol = int(re.findall(r"\d{1,3},\d{1,3}", instruction)[0].split(",")[1])
        endrow = int(re.findall(r"\d{1,3},\d{1,3}", instruction)[1].split(",")[0]) + 1
        endcol = int(re.findall(r"\d{1,3},\d{1,3}", instruction)[1].split(",")[1]) + 1
        # print(action)
        # print("start row: end row = " + str(startrow) + ":" + str(endrow))
        # print("start col: end col = " + str(startcol) + ":" + str(endcol))
        if action == "turn on ":
            lights[startrow:endrow, startcol:endcol] = True
            part2[startrow:endrow, startcol:endcol] += 1
        elif action == "turn off ":
            lights[startrow:endrow, startcol:endcol] = False
            part2[startrow:endrow, startcol:endcol] -= 1
        elif action == "toggle ":
            lights[startrow:endrow, startcol:endcol] = ~lights[
                startrow:endrow, startcol:endcol
            ]
            part2[startrow:endrow, startcol:endcol] += 2
        else:
            print("hoho")
        part2[part2 < 0] = 0
    print(lights.sum())
    print(part2.sum())
