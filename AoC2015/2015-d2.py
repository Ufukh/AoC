import numpy as np

with open("inputd2.txt") as file:
    presents = file.readlines()
    surface = 0
    ribbon = 0
    for present in presents:
        present = present.rstrip("\n")
        dim = list(map(int, present.split("x")))
        surface += 2 * dim[0] * dim[1] + 2 * dim[0] * dim[2] + 2 * dim[1] * dim[2]
        ribbon += dim[0] * dim[1] * dim[2]
        dim.remove(max(dim))
        surface += np.prod(dim)
        ribbon += 2 * dim[0] + 2 * dim[1]
    print(surface)
    print(ribbon)