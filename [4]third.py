#
# Создайте программу для игры в ""Крестики-нолики"".
# 

import re
import os
import time
import random

place = [["-","-","-"],["-","-","-"],["-","-","-"]]
player = 1 if random.randint(1, 2) == 1 else 2
turn = 0
winner = 0

while(turn < 8):

    # Show place and interface
    os.system('cls')
    for line in place:
        print(line)
    print("Player {0}, pls set coordinate, divide by comma:".format(player))

    # Get turn' coordinates: correct and unused
    while True:
        # Get coordinate ... 
        try:
            coordinate = list(filter(lambda elem: int(elem) in range(0,3), input().split(',')))
        except:
            coordinate = []
        # Exeptional if I haven't two valid coordinate
        if len(coordinate) != 2:
            print("Oh no! Set two coordinate, example: 1,2!")
        else:
            # Set new value 
            x = int(coordinate[0])
            y = int(coordinate[1])
            if place[x][y] not in ["O","X"]:
                place[x][y] = "O" if player == 1 else "X"
                break
            else:
                print("Impossoble turn!")

    # Condtions to win
    win = [ [[0,0],[0,1],[0,2]] , [[1,0],[1,1],[1,2]] , [[2,0],[2,1],[2,2]],
            [[0,0],[1,0],[2,0]] , [[0,1],[1,1],[2,1]] , [[0,2],[1,2],[2,2]],
            [[0,1],[1,1],[2,2]] , [[2,0],[1,1],[0,2]]
        ]

    # Check, maybe anybody won
    for w in win:
        r = {"X":0,"O":0,"-":0}
        for c in w:
            x = c[0]
            y = c[1]
            r[place[x][y]] += 1
        if r["X"] == 3:
            winner = 2
            break
        if  r["O"] == 3:
            winner = 1
            break

    # Winner!
    if winner != 0:
        break

    # Change player
    if (turn < 8):
        player = 1 if player == 2 else 2

    # Increment turn 
    turn += 1

os.system('cls')
for line in place:
    print(line)

if winner == 0:
    print("Congratulations! Player {0} you are victorius!".format(winner))
else:
    print("Draw ... ")
