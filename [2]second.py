# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math

# The solution for the task
def pairsMultiply(L):
    lenL = len(L)
    mL = []
    for i in range(0,math.floor(lenL/2)):
        mL.append(L[i] * L[lenL-i-1])
    return mL

# Example
L = [1,3,4,7,4,2,5]
r = pairsMultiply(L)
print(L)
print(r)
