# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:59:37 2020

@author: uhalisdemir
"""

import pandas as pd

countsp1 = 0
countsp2 = 0

with open("Data/inputd63.txt", "r") as inputd6:
    groups = inputd6.read()
    for group in groups.split("\n\n"):

        # part1
        groupp1 = group.replace("\n", "")
        countsp1 += len(set(groupp1))  # Sum the count of unique characters in strings

        # part 2
        group2 = group.split("\n")
        answers = set(group2[0])
        for forms in group2:
            answers = answers & set(forms)
        countsp2 += len(answers)

print("Answer to part 1 is : ", countsp1)
print("Answer to part 2 is : ", countsp2)
