# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным

import os
import re

os.system('cls')

N = ""

# Interface
while N == "":
    print("Set numeric between 1 and 7:".format(N))
    m = re.search('^[0-9]+$', input())
    if(m is not None):
        N = int(m.group(0))

# ... 
os.system('cls')

# do while emulation 
if N in [6,7]:
    print('{0} is weekend'.format(N))
else:
    print('{0} isn\'t weekend'.format(N))
