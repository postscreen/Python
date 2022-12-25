# Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

import os

# To get Binary as list with limited BITS, default is 4 bits
def decimalToBinary(D, limit=4):
    if D == 0:
        b = []
        while len(b) < limit:
            b.insert(0, 0)
        return b
    r = [D,0]
    b = []
    while r[0] != 1:
        r = divmod(r[0], 2)
        b.insert(0, r[1])
    b.insert(0, 1)
    while len(b) < limit:
        b.insert(0, 0)
    return b

os.system('cls')
data = { 'W':False, 'Z':False, 'Y':False, 'X':False }
variants = 2 ** len(data)
percentage = [0,0]

# Clear input
os.system('cls')

print(f'Possible variants: {variants}')
print()

# Get result
for i in range(0,variants):

    # Get binary as list and change state (true/false) into the main dictionary
    listOf = decimalToBinary(i,4)
    index = 0
    for key in data:
        data[key] = (listOf[index] != 0)
        index += 1
    
    # Calculate result; Show base data as dictionary and bool result of the equation;
    result = (data["W"] and data["Z"]) or not data["Y"] or (not data["X"] is not data["W"])
    print(f'Dictionary of the data: {data}')
    print(f'Result of the equation: {result}')
    print()

    # Counting result to do percentage in the end
    if result:
        percentage[0] += 1
    else:
        percentage[1] += 1

# Print how many percent we have to each result of equation ...
print(f'Percent of positive: {percentage[0]/variants*100}%')
print(f'Percent of negative: {percentage[1]/variants*100}%')
input()
