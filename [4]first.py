#
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 

import re
import os
import time

text = "Абвр барвар вабвры рыбы вырвыр рабабв или бырвырбы но субабв АБВ9!"

# My first ... 
def byRegEx(text):
    result = text
    for word in re.findall("[а-яА-Я_\-0-9]+", text):
        if re.search('абв', word, re.IGNORECASE):
            result = re.sub('([\s]{1}'+word+'|'+word+'[\s]{1})', "", result, re.IGNORECASE)
    return result

# My second ...
def byOneByOne(text):
    result = ""
    pos = False
    space = 0
    for char in range(0,len(text)):
        result += text[char]
        if result[-1:] == " " and pos:
            pos = False
            result = result[:space]
        elif len(text)-1 == char and pos:
            pos = False
            result = result[:space-1] + result[-1:]
        if "абв" == result[-3:].lower():
            pos = True
        if text[char] == " ":
            space = len(result) 
    return result

# Simple ... Ольга Тоцкая (С телеграма взял)
def byLumbda(text):
    return ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), text.split())))

# Show it ... 
os.system('cls')
print(text)

print("\nRegExp is slowly, but accuracy:")
print(byRegEx(text))

print("\nLetter one-by-one is slowly, large code, but accuracy:")
print(byOneByOne(text))

print("\nFilter method is fast and short code, but isn't accuracy:")
print(byLumbda(text))

# ... 
# executionStartTime = time.time()

# for i in range(0,100000):
#     byRegEx(text)

# print("Execution time {0} seconds".format(time.time() - executionStartTime))
