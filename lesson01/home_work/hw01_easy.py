
__author__ = 'Шредер Ю.В.'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
import random

a = random.randint(1,10000000)
# print(a)
str_a=str(a)

i=0

while i<len(str_a):
   print(str_a[i])
   i+=1

print()

for j in str_a:
    print(j)





# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = input("Введите значение переменной 'a' ")
b = input("Введите значение переменной 'b' ")
c=int(a)+int(b)
a=c-int(a)
b=c-a
print("Значение переменной a=" + str(a) + " \nЗначение переменной b=" + str(b))


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Укажите свой возраст "))
if age >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
