import numpy as np

tmp = np.empty((0, 12), int)
gamma = str()
epsilon = str()

oxygen = np.empty((0, 12), int)
co2 = np.empty((0, 12), int)


def mostcommon(puzzle):
    ones = np.count_nonzero(puzzle[:, i] == 1)
    zeros = np.count_nonzero(puzzle[:, i] == 0)
    if ones > zeros:
        return "1"
    elif ones < zeros:
        return "0"
    else:
        return "equal"


with open("inputd3.txt") as file:
    puzzle = file.readlines()
    for binary in puzzle:
        x = [int(a) for a in binary.strip()]
        tmp = np.vstack([tmp, x])
        oxygen = tmp
        co2 = tmp
    for i in range(0, tmp.shape[1]):
        mcommon = mostcommon(tmp)
        mcommonox = mostcommon(oxygen)
        mcommonco2 = mostcommon(co2)
        if mcommon == "1":
            gamma += "1"
            epsilon += "0"
        elif mcommon == "0":
            gamma += "0"
            epsilon += "1"

        if (mcommonox == "1" or mcommonox == "equal") and len(oxygen) > 1:
            oxygen = oxygen[oxygen[:, i] == 1]
        elif mcommonox == "0" and len(oxygen) > 1:
            oxygen = oxygen[oxygen[:, i] == 0]

        if (mcommonco2 == "1" or mcommonco2 == "equal") and len(co2) > 1:
            co2 = co2[co2[:, i] == 0]
        elif mcommonco2 == "0" and len(co2) > 1:
            co2 = co2[co2[:, i] == 1]
    print(int(gamma, 2) * int(epsilon, 2))
    print(oxygen)
    print(co2)
    cco2 = ""
    ooxygen = ""
    for el in co2[0]:
        cco2 += str(el)
    for el in oxygen[0]:
        ooxygen += str(el)
    print(int(cco2, 2) * int(ooxygen, 2))
