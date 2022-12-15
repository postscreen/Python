# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

import os
import re
os.system('cls')

data = { 'X':0, 'Y':0 }

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
print("We are have ... ")
for key in data:
    print('{0} -> {1}'.format (key, data[key]))

# Check and show reslut
if data["X"] > 0 and data["Y"] > 0:
    print("It's 1st path ... ")
elif data["X"] < 0 and data["Y"] > 0:
    print("It's 2nd path ... ")
elif data["X"] < 0 and data["Y"] < 0:
    print("It's 3rd path ... ")
elif data["X"] > 0 and data["Y"] < 0:
    print("It's 4th path ... ")
