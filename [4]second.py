# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

import os
import re
os.system('cls')

path = 0
data = { 1 : "x > 0, y > 0", 2 : "x < 0, y > 0", 3 : "x < 0, y < 0", 4 : "x > 0, y < 0"  }

# Interface
while path == 0:
    print("Set path of the cicle [1-4]:")
    m = re.search('^[1-4]$', input())
    if(m is not None):
        path = int(m.group(0))

# Clear input
os.system('cls')

print(data[path])
