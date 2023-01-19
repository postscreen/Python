#
# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# 

import re
import os
import time
import random

n = 101
l = [x for x in range(20,n) if x % 20 == 0 or x % 21 == 0]

print(l)
