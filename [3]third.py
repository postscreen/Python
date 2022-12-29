# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
#

import os
import re
import random

N = ""
baseList = []

# Interface
while N == "":
    print("Set numeric:".format(N))
    m = re.search('^[0-9]+$', input())
    if(m is not None):
        N = int(m.group(0))

# ... 
os.system('cls')

for i in range(0,N):
    baseList.append(random.choice(range(0,10)))

print(f"Base list: {baseList}")
print(f"Qnique elements: {list(set(baseList))}")
