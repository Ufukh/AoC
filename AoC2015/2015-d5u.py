import re

with open("2015/inputd5u.txt") as file:
    puzzle = file.readlines()
    vowels = set("aeiou")
    badstrings = {"ab", "cd", "pq", "xy"}
    nice = 0
    bad = 0
    for txt in puzzle:
        if len(re.findall("[aeiou]", txt)) > 2:
            if re.search(r"(\w)(\1)", txt):
                if not re.search(r"ab|cd|pq|xy", txt):
                    nice += 1
        # if (
        #     len(re.findall(r"\b(?:\w*[aeiyou]){3}\w*", txt)) != 0
        #     and not (any(c in txt for c in badstrings))
        #     and (len(re.findall(r"((\w)\2{1})", txt)) == 0)
        # ):
        #     nice += 1
        # else:
        #     bad += 1
    print(nice)
    # print(bad)
