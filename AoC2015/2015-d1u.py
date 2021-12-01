with open("inputd1p1.txt") as file:
    data = file.read()
    # floor = data.count("(") - data.count(")") #quick sol
    floor = 0
    count = 1
    sol = 0
    for element in data:
        if sol == 0:
            if element == ")":
                floor = floor - 1
            elif element == "(":
                floor = floor + 1
            if floor == -1:
                sol = count
        else:
            if element == ")":
                floor = floor - 1
            elif element == "(":
                floor = floor + 1
        count = count + 1
    print(floor)
    print(sol)
