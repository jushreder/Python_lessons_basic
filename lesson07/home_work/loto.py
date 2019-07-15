#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random
import sys

def barrel():
    lst=[a for a in range(1,91)]
    random.shuffle(lst)
    for i, x in enumerate(lst):
        print(f'   Новый бочонок < {x} > осталось {len(lst)-i-1}')
        yield x

class Player:
    def __init__(self,name,strike=0):
        self.name = name
        self.card = self.__card()
        self.strike = strike
    def __card(self):
        kart = []
        a = [i for i in range(1, 10)]
        for i in range(3):
            b = (random.sample(a, k=5))
            b.sort()
            kart.append(b)
        nom = []
        basa = []
        aa = random.sample(a, k=len(a))
        basa.append(aa)
        c = 0

        for j in range(10, 91):
            c += 1
            nom.append(j)
            if c == 10:
                if j > 88:
                    nom.append(90)
                nom_itm = random.sample(nom, k=len(nom))
                basa.append(nom_itm)
                nom.clear()
                c = 0
        str1 = []
        karta_ = []
        for a in range(3):
            for b in kart[a]:
                str1.append(basa[b - 1].pop())
            karta_.append(str1.copy())
            str1.clear()
        karta=[]
        for a in karta_:
            karta.append(dict(zip(a,a)))
        return karta
    def screen(self):
        print(f'---------- Card {self.name} -------------')
        for itm in self.card:
            # print(list(itm.values())[0])
            print (f' {str(list(itm.values())[0]).rjust((list(itm.keys())[0]//10)*4+1)}'
                  f'{str(list(itm.values())[1]).rjust((list(itm.keys())[1]//10-list(itm.keys())[0]//10)*4)}'
                  f'{str(list(itm.values())[2]).rjust((list(itm.keys())[2]//10-list(itm.keys())[1]//10)*4)}'
                  f'{str(list(itm.values())[3]).rjust((list(itm.keys())[3]//10-list(itm.keys())[2]//10)*4)}'
                  f'{str(list(itm.values())[4]).rjust((list(itm.keys())[4]//10-list(itm.keys())[3]//10)*4)}')
            #
    def check(self,barrel_val):
        for itm in self.card:
            if barrel_val in itm:
                self.strike += 1
                if self.strike==15:
                    print(f'Игра окончена победил {self.name}')
                    sys.exit(1)
                if len(str(barrel_val))==1:
                    itm[barrel_val]='-'
                else:
                    itm[barrel_val] = '--'
                return True
        return False

bar=barrel()
player=Player('player')
comp=Player('comp')

while True:
    barrel_val=next(bar)
    player.screen()
    comp.screen()
    antw= input('Зачеркнуть цифру? (y/n)')
    comp.check(barrel_val)

    while True:
        if antw != 'y' and antw !='n'and antw !='q':
            antw =input('Введите <y> или <n>')
            continue
        break
    if antw=="y":
        if player.check(barrel_val):
            continue
        print('Игра окончена, Вы проиграли!')
        break
    elif antw=="n":
        if not player.check(barrel_val):
            continue
        print('Игра окончена, Вы проиграли!')
        break
    elif antw == "q":
        print('Игра окончена, Вы проиграли!')
        break



