# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

import os

N = 10
L = [0,1]

# Do it ...
for i in range(2,N):
    F = L[i-1] + L[i-2]
    L.append(F)

# ... 
os.system('cls')

# Show it ...
for i in range(-10,10):
    print(L[i])
