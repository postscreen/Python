# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

import os

os.system('cls')

print("Input float: ")
numeric = input()
print("Input number of digits: ")
digits = input()
os.system('cls')
print("{0:.Nf} - Result formated value ... ".replace("N", digits).format(float(numeric)))
