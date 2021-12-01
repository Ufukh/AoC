# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:59:37 2020

@author: uhalisdemir
"""

import pandas as pd

def seatid(seat):
    rows = [0,127]
    cols = [0,7]
    frow = 0
    fcol = 0
    i=0
    for lett in seat:
        if lett == "F":
            if (i == 6):
                frow = rows[0]
            else:
                if (rows[0]+rows[1])%2== 0:
                    rows[1] = (rows[0]+rows[1])/2
                else:
                    rows[1] = (rows[0]+rows[1]-1)/2
        elif lett == "B":
            if (i == 6):
                frow = rows[1]
            else:
                if (rows[0]+rows[1])%2== 0:
                    rows[0] = ((rows[0]+rows[1])/2)
                else:
                    rows[0] = ((rows[0]+rows[1]+1)/2)
        elif lett == "L":
            if (i == 9):
                fcol = cols[0]
            else:
                if (cols[0]+cols[1])%2== 0:
                    cols[1] = (cols[0]+cols[1])/2
                else:
                    cols[1] = (cols[0]+cols[1]-1)/2
        elif lett == "R":
            if (i == 9):
                fcol = cols[1]
            else:
                if (cols[0]+cols[1])%2== 0:
                    cols[0] = ((cols[0]+cols[1])/2)
                else:
                    cols[0] = ((cols[0]+cols[1]+1)/2)
        i+=1
    return frow, fcol
    
df = pd.read_csv('Data/inputd5.txt', header=None, names=["input"])

# test valid passports
# mys = seatid('FFFBBBFRRR')
# print(mys)
# print(mys[0]*8+mys[1])

seat_ids = []

for seat in df['input']:
    mys = seatid(seat)
    finalid = mys[0]*8+mys[1]
    seat_ids.append(finalid)
    
print(max(seat_ids))

seat_ids_sorted = sorted(seat_ids)

for i in range(int(min(seat_ids)), int(max(seat_ids)+1)):
    if i != seat_ids_sorted[i-int(min(seat_ids))]:
        print("Missing ID:", i)
        break