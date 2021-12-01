# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:14:21 2020

@author: uhalisdemir
"""

import pandas as pd


def day3p1(right=3, down=1):
    lrpos = 0
    hit = 0
    df = pd.read_csv("Data/inputd3.txt", header=None, sep=" ", names=["input"])

    # print(len(df.index) - 1)
    # print(len(df["input"][0]))

    for i in range(0, len(df.index), down):
        # print("iteration n° {}; x = {}; y = {}".format(i, i*right,i))
        # print(df["input"][i])
        # print(df["input"][i][lrpos])
        # print(i)
        if df["input"][i][lrpos] == "#":
            hit += 1
        lrpos += right
        lrpos = lrpos % len(df["input"][0])

    return hit


def day3p2():
    tot = 1
    tot *= day3p1(1, 1)
    tot *= day3p1(3, 1)
    tot *= day3p1(5, 1)
    tot *= day3p1(7, 1)
    tot *= day3p1(1, 2)
    return tot


print("Solution to day 3 part 1 : " + str(day3p1()))
print("Solution to day 3 part 2 : " + str(day3p2()))