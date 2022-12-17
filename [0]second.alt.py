# Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

import os

os.system('cls')
data = { 'W':False, 'Z':False, 'Y':False, 'X':False }

# Clear input
os.system('cls')

# Get result
for i in range(1,17):
    print(i)
    result = (data["W"] and data["Z"]) or not data["Y"] or (not data["X"] is not data["W"])

print(result)
