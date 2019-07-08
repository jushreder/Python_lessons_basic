# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os, sys


def name_d():
    try:
        name = 'dir'
        n = 9
        for i in range(1, n + 1):
            name_dir = f'{os.getcwd()}/{name}_{i}'
            os.mkdir(name_dir)
    except FileExistsError:
        print('Невозможно создать')


def name_r():
    try:
        for i in range(1, n + 1):
            name_dir = f'{os.getcwd()}/{name}_{i}'
            os.rmdir(name_dir)
    except FileNotFoundError:
        print('Невозможно удалить')


def mk_dir():

    try:

        name=input('имя папки: ->')
        name_dir =f'{os.getcwd()}/{name}'
        os.mkdir(name_dir)
        print('Успешно создана')

    except FileExistsError:
        print('Невозможно создать')

def rm_dir():

    try:
        name = input('имя папки: ->')
        name_dir = f'{os.getcwd()}/{name}'
        os.rmdir(name_dir)
        print('Успешно удалена')
    except FileNotFoundError:
        print('Нeвозможно удалить')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def ls_dir():

    temp=os.listdir(os.getcwd())
    temp.sort()
    for n in temp:
        print(n)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_f():

    arg = sys.argv

    with open(arg[0], 'r') as file:
        temp = file.read()

    name_f = os.path.split(arg[0])
    name_copy = f'{name_f[0]}/copy_{name_f[1]}'

    with open(name_copy, 'w') as file:
        file.write(temp)





