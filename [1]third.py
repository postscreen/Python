# 3. Задайте список из n чисел, заполненный по формуле
#  (1 + 1/n) ** n и выведите на экран их сумму.

import os
import re

# ... 
os.system('cls')

# ... 
N = ""
K = 1
L = []

# Interface ... 
while N == "":
    print("Set numeric:".format(N))
    m = re.search('^[0-9]+$', input())
    if(m is not None):
        N = int(m.group(0))

# ... 
os.system('cls')

# ... 
for i in range(0,N):
    K = (1 + 1/N) ** N
    L.append(K)

# Show list ... 
print("Count of numerics: {0}".format(len(L)))
print("Sum: {0}".format(sum(L)))
