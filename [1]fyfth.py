# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.

import os
import random

# Prepare
os.system('cls')

# Prepare data
listLen = 10
L = []

# Set base list
for i in range(0,listLen):
    L.append(i)

# Algorythm for the mix list
for i in range(0,listLen):
    # Two random values for indexes that will change places
    c1 = random.choice(range(0,10))
    c2 = random.choice(range(0,10))
    # Change places of these indexes
    save = L[c1]
    L[c1] = L[c2]
    L[c2] = save

# Show result
print(len(L))
print(L)
