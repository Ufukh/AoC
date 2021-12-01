with open("inputd3.txt") as file:
    instructions = file.read()
    xsanta = 0
    ysanta = 0
    xrobot = 0
    yrobot = 0
    seen = []
    seen.append(str(xsanta) + ";" + str(ysanta))
    seen.append(str(xrobot) + ";" + str(yrobot))
    turn = 0
    for instr in instructions:
        if turn == 0:
            print("santa")
            if instr == "^":
                ysanta += 1
            elif instr == ">":
                xsanta += 1
            elif instr == "<":
                xsanta -= 1
            elif instr == "v":
                ysanta -= 1
            else:
                print("shutup")
            seen.append(str(xsanta) + ";" + str(ysanta))
            turn = 1
        elif turn == 1:
            print("robot")
            if instr == "^":
                yrobot += 1
            elif instr == ">":
                xrobot += 1
            elif instr == "<":
                xrobot -= 1
            elif instr == "v":
                yrobot -= 1
            else:
                print("shutup")
            seen.append(str(xrobot) + ";" + str(yrobot))
            turn = 0
        else:
            print("shutup")
    print(len(set(seen)))
