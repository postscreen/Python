# * 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

import os
import re
import random

k = ""
baseList = []

# Interface
while k == "":
    print("Set numeric:".format(k))
    m = re.search('^[0-9]+$', input())
    if(m is not None):
        k = int(m.group(0))

# ... 
os.system('cls')

# ...
fName = "file.txt"
if os.path.exists(fName):
    os.remove(fName)
f = open(fName, "x")

# Multi k-degree equance
for c in range(0,5):
    s = ""
    for i in range(0,k):
        m = random.choice(range(0,10))
        # Full element
        new = "{0}x^{1} + ".format(m,i)        
        # it's zero
        new = re.sub("(0x\^[0-9]+) \+ ", "", new)        
        # it's numeric
        new = re.sub("([0-9]+)x\^0", r"\g<1>", new)
        # Degree is one
        new = re.sub("([0-9]+)x\^1", r"\g<1>x", new)
        # preffix is one
        new = re.sub("1x", "x", new)
        s = new + s

    s = re.sub("\+ $", "= 0\n", s)
    f.write(s)

f.close()

print("Application is ends ... Press any key to exit ... ")
input()
