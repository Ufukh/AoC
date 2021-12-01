with open("inputd1p1.txt") as file:
    puzzle = file.readlines()
    puzzle = list(map(int, puzzle))
    i = 0
    increased = 0
    # change range for part 1
    for i in range(len(puzzle) - 3):
        if (sum(puzzle[i + 1 : i + 4]) - sum(puzzle[i : i + 3])) > 0:
            increased += 1
        i += 1
    print(increased)
