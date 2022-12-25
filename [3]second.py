# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# in
# 54
# out
# [2, 3, 3, 3]

import os

simpleInt = [2,3,5,7,11,13,17,19,23,29,31,37]
inUse = []
i = 0

os.system('cls')

print("Input integer: ")
numeric = int(input())
saveNumeric = numeric

os.system('cls')
while i < len(simpleInt):
    if divmod(numeric, simpleInt[i])[1] == 0:
        numeric = numeric / simpleInt[i]
        inUse.append(simpleInt[i])
        i = 0
    i += 1

print("Base numeric {0}; List of simple multiplies: {1}".format(saveNumeric, inUse))
