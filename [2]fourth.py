# 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random
import os
import re

# ... 
os.system('cls')

# ... 
N = ""
L = []

# Interface
while N == "":
    print("Set numeric:".format(N))
    m = re.search('^[0-9]+$', input())
    if(m is not None):
        N = int(m.group(0))

# ... 
os.system('cls')

# ...
for i in range(0,N):
    L.append(random.random())

print(L)

# Get max,min
min = 1
max = 0
for i in range(0,N):
    d = divmod(L[i],1)
    if d[1] > max:
        max = d[1]

    if d[1] < min:
        min = d[1]

print("Max not fully integer path: {0}".format(max))
print("Min not fully integer path: {0}".format(min))
print("Difference: {0}".format(max-min))
