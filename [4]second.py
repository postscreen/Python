#
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#

import re
import os
import time
import random

def textToArchive(inputData):
    prev = ""
    count = 1
    result = ""
    for char in range(0,len(inputData)):
        if prev != inputData[char]:
            if prev != "":
                if prev != "\n":
                    result += "{1}{0}".format(prev,count)
                else:
                    result += "\n"
                count = 1
            prev = inputData[char]
        else:
            count += 1
    return result + "{1}{0}".format(prev,count)

def archiveToText(inputData):
    result = ""
    data = re.findall("([0-9]+)([a-zA-Z]+)|([\n])", inputData)
    for elem in data:
        if elem[2] != "\n":
            result += (str(elem[1]) * int(elem[0]))
        else:
            result += elem[2]
    return result

os.system('cls')

# Read text
fInput = open("iRLE.txt", "r")
inputData = fInput.read()
fInput.close()

# Transform text to archive
archiveData = textToArchive(inputData)

# Save archive
fOutput = open("oRLE.txt", "w")
fOutput.write(archiveData)
fOutput.close()

# Return base text
textFromTheArchive = archiveToText(archiveData)

# Compare what they are equal
print("Input text:")
print(inputData)
print()

print("Restored text:")
print(textFromTheArchive)
print()

print("Archive:")
print(archiveData)
print()
