import numpy as np
import sys


def checkboard(board):
    bcheck = "noob"
    for i in range(0, board.shape[1]):
        if np.isnan(board[:, i]).sum() == 5 or np.isnan(board[i, :]).sum() == 5:
            bcheck = "bingo"
    return bcheck


def replacenum(board, num):
    board[np.where(board == float(num))] = np.nan
    return board


with open("inputd4.txt") as file:
    numbers = file.readline().strip("\n").split(",")
    bingos = np.loadtxt("inputd4.txt", skiprows=1)
    bingos = bingos.reshape(int(len(bingos) / 5), 5, 5)
    winning = []
    for num in numbers:
        for i in range(0, bingos.shape[0]):
            if i in winning:
                continue
            else:
                bingos[i, :, :] = replacenum(bingos[i, :, :], float(num))
                check = checkboard(bingos[i, :, :])
                if check == "bingo":
                    winning.append(i)
                    if len(winning) == 1:
                        sol = np.nansum(bingos[i, :, :]) * float(num)
                        print("Sol to part one is : " + str(int(sol)))
                    elif len(winning) == 100:
                        sol = np.nansum(bingos[i, :, :]) * float(num)
                        print("Sol to part two is : " + str(int(sol)))