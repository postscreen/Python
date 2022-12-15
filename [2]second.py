# Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

import os
import re

os.system('cls')
data = { 'W':None, 'Z':None, 'Y':None, 'X':None }

# Interface
for key in data:
    while data[key] == None:
        print("Set {0} (0=false, Other=true):".format(key))
        m = re.search('^[0-9]$', input())
        if(m is not None):
            value = int(m.group(0))
            if(value == 0):
                data[key] = False
            else:
                data[key] = True

# Clear input
os.system('cls')

#  Show data
print("We are have ... ")
for key in data:
    print('{0} = {1}'.format (key, data[key]))

# Get result
result = (data["W"] and data["Z"]) or not data["Y"] or (not data["X"] is not data["W"])

# Show result
if result:
    print("It's TRUE")
else:
    print("It's FALSE")
