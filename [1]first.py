# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным

import os
os.system('cls')

N = 0

while True:

    # Interface
    print("Set numeric between 1 and 7:")
    N = int(input())

    # Get string state
    if N in [6,7]:
        E = "Yes"
    else:
        E = "No"

    print('{0} -> {1}'.format(N, E))

    # do while emulation 
    if N not in [1,7]:
        break
