import re

vowels = set("aeiou")
badstrings = {"ab", "cd", "pq", "xy"}

test = "vvxazegovvvv"
test2 = "arrrrrrrrrrrrr"
test3 = "abcdpqxy"
test4 = "aaaa"

print(re.findall(r"\w*(\w{2})\w*\1", test4))

# if len(re.findall(r"(\w*[aeuio]\w*){3,}", test)) != 0:
#     print("I found at least three voewl")

# if len(re.findall(r"(\w)\1", test)) != 0:
#     print("I found a double letter")

# if len(re.findall(r"(ab|cd|pq|xy)", test)) != 0:
#     print("I found a bad string")

# if (
#     len(re.findall(r"(\w*[aeuio]\w*){3,}", test)) != 0
#     and len(re.findall(r"(\w)\1", test)) != 0
#     and len(re.findall(r"(ab|cd|pq|xy)", test)) == 0
# ):
#     print("I found a least three voewl")
#     print("No bad string")
#     print("and no double letter")
