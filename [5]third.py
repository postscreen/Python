#
# Написать функцию, аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.
# 

def solution(l = ["Ivan", "Lena", "Tanya", "Petia", "Sonya", "Toma", "Ibragim", "Tom"]):
    d = {}
    for n in l:
        d[n[0]] = [x for x in l if x[0] == n[0]]
    return d

print(solution())
