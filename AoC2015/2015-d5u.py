import re

with open("2015/inputd5u.txt") as file:
    puzzle = file.readlines()
    vowels = set("aeiou")
    badstrings = {"ab", "cd", "pq", "xy"}
    part1 = 0
    part2 = 0
    for txt in puzzle:
        if (
            len(re.findall(r"(\w*[aeuio]\w*){3,}", txt)) != 0
            and len(re.findall(r"(\w)\1", txt)) != 0
            and len(re.findall(r"(ab|cd|pq|xy)", txt)) == 0
        ):
            part1 += 1
        if (
            len(re.findall(r"\w*(\w{2,})\w*\1", txt)) != 0
            and len(re.findall(r"(\w)\w\1", txt)) != 0
        ):
            part2 += 1
    print(part1)
    print(part2)