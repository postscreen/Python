# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.

import math

# The solution for the task
def decimalToBinary(D):
    if D == 0: return [0]
    r = [D,0]
    b = []
    while r[0] != 1:
        r = divmod(r[0], 2)
        b.insert(0, r[1])
    b.insert(0, 1)
    return b

# Example
for i in range(0,100):
    B = decimalToBinary(i)
    print("Decimal: {0}; Binary result: {1}".format(i,B))
