# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:19:03 2020

@author: uhalisdemir

puzzle: https://adventofcode.com/2020/day/1

"""

import pandas as pd

# part1
goodsol = 0
sols = []

df = pd.read_csv("Data/inputd1p1.txt", header=None, names=["input"])

for i in range(0, df.size - 1):
    for j in range(i + 1, df.size - 1):
        if df.input[i] + df.input[j] == 2020:
            goodsol += 1
            print(
                "Solution {}. Le produit de {} et {} = {}".format(
                    goodsol, df.input[i], df.input[j], df.input[i] * df.input[j]
                )
            )

# part2
for i in range(0, df.size - 1):
    for j in range(i + 1, df.size - 1):
        for k in range(j + 1, df.size - 2):
            if df.input[i] + df.input[j] + df.input[k] == 2020:
                goodsol += 1
                print(
                    "Solution {}. Le produit de {} et {} et {} = {}".format(
                        goodsol,
                        df.input[i],
                        df.input[j],
                        df.input[k],
                        df.input[i] * df.input[j] * df.input[k],
                    )
                )
