# Напишите программу для проверки ложности утверждения

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
