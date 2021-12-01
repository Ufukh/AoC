import re

vowels = set("aeiou")
badstrings = {"ab", "cd", "pq", "xy"}

test = "suerykeptdsutidb"
test2 = "arrrrrrrrrrrrr"
test3 = "abcdpqxy"
test4 = "aa"

if any(c in test2 for c in badstrings):
    print("I found a bad string")

if any(c in vowels for c in test2):
    print("I found a voewl")


if len(re.findall(r"((\w)\2{1})", test2)) != 0:
    print("I found a double letter")

if len(re.findall(r"\b(?:\w*[aeiyouAEIYOU]){3}\w*", test2)) != 0:
    print("I found 3 voewls")
# if (
#     any(c in vowels for c in test)
#     and not (any(c in test for c in badstrings))
#     and (len(re.findall(r"((\w)\2{1})", test)) == 0)
# ):
#     print("I found a voewl")
#     print("No bad string")
#     print("and no double letter")
