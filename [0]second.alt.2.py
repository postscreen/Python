import os

# Imagine what it's numeric and do increment to it each function call
def incrementIt(data):
    for i in data.keys():
        if data[i]:
            data[i] = False
        else:
            data[i] = True
            break
    return data

os.system('cls')
data = { 'W':False, 'Z':False, 'Y':False, 'X':False }
variants = 2 ** len(data)

# Get result
for i in range(0, variants):
    data = incrementIt(data)
    result = (data["W"] and data["Z"]) or not data["Y"] or (not data["X"] is not data["W"])
    print(data)    
    print(result)

input()
