#
# 5. Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

n = len(nouns) * len(adverbs) * len(adjectives)
r = []

for i in range(0,n):
    s = nouns[random.randrange(0,len(nouns)-1)]
    s += " "+adverbs[random.randrange(0,len(adverbs)-1)]
    s += " "+adjectives[random.randrange(0,len(adjectives)-1)]
    r.append(s.capitalize() + ".")

for fun in r:
    print(fun)
