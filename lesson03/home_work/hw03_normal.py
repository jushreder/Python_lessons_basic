# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    """

    :param n:
    :param m:
    :return:
    """
    f=[1,1]
    for a in range(1,m-1):
        f.append(f[a-1]+f[a])
    return f[n-1:m]

print(fibonacci(6,12))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    """
    Сортирует список по возростанию
    :param origin_list:
    :return:
    """

    n=len(origin_list)

    ind=1
    while ind:
        ind=0
        for j in range(1,n):
            if origin_list[j-1]>origin_list[j]:
                origin_list[j - 1] , origin_list[j]=origin_list[j],origin_list[j-1]
                ind=1
    return origin_list


sort_ist = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0,-15,43])
print(sort_ist)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

itm=[1, 3, "list", True, 20.2, 4, -4, "func", False, 6, 7, 10, 12, -15]

def filter_int(origin_list):
    """
    фильтр возращает целые числа  > 0
    :param origin_list: список
    :return: список
    """
    or_lst=[]
    for t in origin_list:
        if type(t)== int and t>0:
            or_lst.append(t)
    return or_lst

print(filter_int(itm))




# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def polygon(*args):
    """
    Функция по вершинам определяет параллелограмм
    :param point1:
    :param point2:
    :param point3:
    :param point4:
    :return:
    """
    a=[i for i in args]
    a.sort()
    # print(a, a[1][0])
    if a[0][0]+a[3][0] == a[1][0]+a[2][0] and a[0][1]+a[3][1] == a[1][1]+a[2][1]:
         return True

a1=[5,8]
a2=[2,12]
a3=[3,17]
a4=[6,13]

print(polygon(a1,a2,a3,a4))
