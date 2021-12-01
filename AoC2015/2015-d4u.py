import hashlib

puzzle = "bgvyzdsv"
result = hashlib.md5(puzzle.encode())
i = 0
# while result.hexdigest()[0:5] != "00000": # for p1
while result.hexdigest()[0:6] != "000000":
    temp = puzzle + str(i)
    result = hashlib.md5(temp.encode())
    i += 1
print(i - 1)
