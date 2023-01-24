import os

def begin():
    print("Hi! Pleace, write composition in the strict form how are you do it on the paper:")
    print("Example: 24 + 54 + i98 + 25 - 100 - i900")

def get_expression():
    return input()

def clear():
    os.system('cls')
