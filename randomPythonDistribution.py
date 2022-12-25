from collections import OrderedDict
import random
import os
import time

os.system('cls')

L = {}

for i in range(1,10000):
    r = random.randint(0, 5)
    if r in L.keys():
        L[r] += 1
    else:
        L[r] = 1

for key in sorted(L.keys()):
    print("{0} -> {1}".format(key, L[key]))

a = input()
