import logging
import re
import time
from datetime import datetime

def give_me_answer(expression):

    # get essences
    composition = re.findall(r'([0-9\.]{0,19})|(i[0-9\.]{0,19})|([\)]{1})|([\(]{1})|([\+\-\*\/]{1})', expression)
    print(composition)

    # Isn't fully ... I skip it and do simple list of them ...
    l = []
    for single_search in composition:
        for element in single_search:
            if element != '':
                l.append(element)

    # one-by-one with some espenses ... oh-oh-oh ...
    real = 0
    fantasy = 0
    symbol = 1
    #action = 0
    k = 0

    for essense in l:
        if essense in ["-"]:
            symbol *= -1
            if l[k-1] == ")":
                boof = "-"
        #elif essense in ["/","*"]:            
        elif "(" in essense and boof == "-":
            symbol *= -1
        elif "i" in essense:
            fantasy += bool(essense.replace("i", "")) * symbol
        else:
            real += bool(essense) * symbol
        k += 1

    # Result ... 
    l.append("=")
    l.append(str(real) + " +")
    l.append("i"+str(fantasy))

    # time market
    time_marker = time.time()
    l.append(str(time_marker))

    # logging
    archive_string = "\t".join(l) + "\n"
    logging.store_it(archive_string)
