#
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#

import re
import os
import time
import random

fInput = open("iRLE.txt", "r")
inputData = fInput.read()
fInput.close()

print(inputData)

for char in range(0,len(inputData)):
    print(inputData[char])
