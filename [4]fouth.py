# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import os
import random

os.system('cls')

candy = 2021
player = 1 if random.randint(1, 2) == 1 else 2

while(candy > 0):
    os.system('cls')
    print("Total candy: {0}".format(candy))
    print("Player {0}, how many candy do you get:".format(player))

    HeIsGet = 0
    while HeIsGet <= 0 or HeIsGet > 28:
        HeIsGet = int(input())
        if HeIsGet <= 0 or HeIsGet > 28:
            print("Oh no! You can get between 1 and 28 candy!")

    candy -= HeIsGet
    if candy > 0:
        player = 1 if player == 2 else 2

os.system('cls')
print("Congratulations! Player {0} you are victorius!".format(player))
