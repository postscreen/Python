# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
import os

os.system('cls')

# Leibniz formula for π
rLeibniz = 0
for i in range(0,1000000):
    rLeibniz += ((-1) ** i) / (2*i + 1)

# Fast method .. by ... 
rFast = 0
for i in range(0,400000):
    rFast += 2 / ((4*i + 1) * (4*i + 3))

print("{0:.10f} - Leibniz (1kk)".format(4*rLeibniz))
print("{0:.10f} - Fast (400k)".format(4*rFast))
print("{0:.10f} - Python math.pi".format(math.pi))
