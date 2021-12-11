import numpy as np
import re

results = dict()


def msearch(results, key):
    if key in results:
        return results[key]
    else:
        return key


with open("2015/inputd7u.txt") as file:
    puzzle = file.readlines()
    for instruction in puzzle:
        try:
            print(results["a"])
            break
        except KeyError:
            pass
        (ops, res) = instruction.split("->")
        res = res.strip()
        if len(ops.split()) == 1:
            results[res] = int(msearch(results, ops.split()[0]))
        elif len(ops.split()) == 2:
            results[res] = ~int(msearch(results, ops.split()[1])) & 0xFFFF
        elif len(ops.split()) == 3:
            if ops.split()[1] == "AND":
                results[res] = int(msearch(results, ops.split()[0])) & int(
                    msearch(results, ops.split()[2])
                )
            elif ops.split()[1] == "OR":
                results[res] = int(msearch(results, ops.split()[0])) | int(
                    msearch(results, ops.split()[2])
                )
            elif ops.split()[1] == "RSHIFT":
                results[res] = int(msearch(results, ops.split()[0])) >> int(
                    msearch(results, ops.split()[2])
                )
            elif ops.split()[1] == "LSHIFT":
                results[res] = int(msearch(ops.split()[0])) << int(
                    msearch(ops.split()[2])
                )
            else:
                print("Bro, another pb")
        else:
            print("Bro, we have a pb")