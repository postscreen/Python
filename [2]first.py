# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

import random
import os
import re

os.system('cls')

N = ""

# Interface
while N == "":
    print("Set numeric:".format(N))
    m = re.search('^[0-9]+$', input())
    if(m is not None):
        N = int(m.group(0))

# ... 
os.system('cls')

# Do List. Generate random elements for the each index of the list
# Sum of elements at not even indexes

L = []
Sum = 0

for i in range(N):
    L.append(random.choice(range(0,10)))
    if i % 2 == 0 and i != 0:
        Sum += L[i]

print("Full list is: {0}".format(L))
print("Sum is: {0}".format(Sum))
