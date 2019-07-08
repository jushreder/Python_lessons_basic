# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():

    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def cp_dir():
    pass
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return

    dir_path = os.path.join(os.getcwd(), dir_name)
    name_copy=f'copy_{dir_name}'
    dir_copy = os.path.join(os.getcwd(),name_copy)
    try:
        shutil.copy(dir_path,dir_copy)
        print('копия файла {} создана'.format(dir_name))
    except FileNotFoundError:
        print('файла  {} не существует'.format(dir_name))

def rm_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.remove(dir_path)
        print('файл {} удален'.format(dir_name))
    except FileNotFoundError:
        print('файл {} не существует'.format(dir_name))

def cd_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print('текущая директория изменена на\n{}'.format(dir_name))
    except FileNotFoundError:
        print('директории {} не существует'.format(dir_name))

def ls_dir():
    dir_path = os.path.join(os.getcwd())
    print(dir_path)


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp_dir,
    "rm" : rm_dir,
    "cd" : cd_dir,
    "ls" : ls_dir,
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
