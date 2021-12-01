# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:31:58 2020

@author: uhalisdemir
"""

import pandas as pd

# Passport on single line
with open("Data/inputd4.txt", "r") as r:
    with open("Data/inputd4new.txt", "w") as w:
        w.write(
            r.read()
            .replace("\n\n", "\nFakeline\n")
            .replace("\n", " ")
            .replace(" Fakeline ", "\n")
        )


# create regex pattern to look for
keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
pattern = ""
for el in keys:
    pattern += "(?=.*{})".format(el)


# Load cleaned file
df = pd.read_csv("Data/inputd4new.txt", header=None, names=["PassID"])
print(df["PassID"].str.contains(pattern).sum())
# Valid passports for part 1 rules
partone = df[df["PassID"].str.contains(pattern)]


def test_pass(passport):

    d = dict(x.split(":") for x in passport)

    if len(d["byr"]) != 4 or int(d["byr"]) < 1920 or int(d["byr"]) > 2002:
        return False

    if len(d["iyr"]) != 4 or int(d["iyr"]) < 2010 or int(d["iyr"]) > 2020:
        return False

    if len(d["eyr"]) != 4 or int(d["eyr"]) < 2020 or int(d["eyr"]) > 2030:
        return False

    if d["hgt"][-2:] == "cm":
        if int(d["hgt"][:-2]) < 150 or int(d["hgt"][:-2]) > 193:
            return False
    elif d["hgt"][-2:] == "in":
        if int(d["hgt"][:-2]) < 59 or int(d["hgt"][:-2]) > 76:
            return False
    else:
        return False

    valid_hcl_charset = {
        "#",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    }
    if (
        d["hcl"][0] != "#"
        or len(d["hcl"]) != 7
        or not set(d["hcl"]).issubset(valid_hcl_charset)
    ):
        return False

    valid_ecl_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if d["ecl"] not in valid_ecl_values:
        return False

    if len(d["pid"]) != 9:
        return False

    return True


# test_pass(partone['PassID'][0].split())
partwo = [test_pass(x) for x in partone["PassID"].str.split()]

print(sum(partwo))