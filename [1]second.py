# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

import os
import re

# ... 
os.system('cls')

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
    K = K * (i + 1)
    L.append(K)

# Show list ... 
print(L)
