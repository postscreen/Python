# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

import os
import re
import math
from decimal import *

# ... 
os.system('cls')

# ...
L = []
numeric = ""

# Interface
while numeric == "":
    print("Input numeric by float:")
    baseInput = input()
    allowString = re.search('^[0-9,.]+$', baseInput)
    if(allowString is not None):
        fullInt = re.sub('[.,]', '', allowString.group(0))
        numeric = int(fullInt)

# ...
os.system('cls')

# Get full len
len = (int)(math.log10(numeric) + 1)

# Collect the values of the digits of the numeric
for index in range(1,len+1):
    numByIndex = (int)(numeric / math.pow(10, (int)(math.log10(numeric) + 1) - index)) % 10;
    L.append(numByIndex)

# ... 
totalSum = sum(L)

# ... 
print("Input: {0}".format(baseInput))
print("Total Sum: {0}".format(totalSum))
