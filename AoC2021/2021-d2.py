with open("inputd2.txt") as file:
    puzzle = file.readlines()
    hor = 0
    depth = 0
    aim = 0
    # change range for part 1
    for instruction in puzzle:
        instruction = instruction.strip("\n")
        test = instruction.split(" ")
        if test[0] == "forward":
            hor += int(test[1])
            depth += aim * int(test[1])
        elif test[0] == "down":
            # depth += int(test[1])
            aim += int(test[1])
        elif test[0] == "up":
            # depth -= int(test[1])
            aim -= int(test[1])
        else:
            print("We got a prob bro")

    print(hor)
    print(depth)
    print(hor * depth)

print("4814550")
