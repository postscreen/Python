# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

import os
import re
import math

os.system('cls')

data = { 'X1':0, 'X2':0, 'Y1':0, 'Y2':0 }
length = 0

# Interface
for key in data:
    while data[key] == 0:
        print("Set {0}:".format(key))
        m = re.search('^[0-9]+$', input())
        if(m is not None):
            data[key] = int(m.group(0))

# Clear input
os.system('cls')

# Show data
length = math.sqrt(math.pow(data["X2"] - data["X1"], 2) + math.pow(data["Y2"] - data["Y1"], 2))
print("We are have {0} distance: ".format(length))
