#
# Функция принимает в качестве аргументов строки в формате «Имя Фамилия»,
# возвращает словарь, ключи — первые буквы фамилий ... 
# 
# ... Значения — словари, 
# реализованные по схеме предыдущего задания.
# 

def supoort(l):
    d = {}
    for n in l:
        d[n[0]] = [x for x in l if x[0] == n[0]]
    return d

def solution(l = ["Ivan Ivanov", "Lena Petrova", "Tanya Abrams", "Petia Petrov", "Sonya Polna", "Toma Brik", "Ibragim Po", "Tom Sowyer"]):
    d = {}
    sl = []
    for fs in l:
        f = fs.split(' ')[0]
        s = fs.split(' ')[1]
        d[s[0]] = {}
        sl.append(f)
    for i in d:
        d[i] = supoort(l)
    return d

d = solution()
print(d)
