# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    """
    Функция округления
    :param number: float
    :param ndigits: int знаков после точки
    :return:
    """
    st_r = str(number).split(".")
    # print(st_r)
    if len(str(number).split(".")[-1]) >= ndigits:
        b = len(str(number).split(".")[-1]) - ndigits
        # print(b)
        ost = int(str(number).split(".")[-1]) // 10 ** b
        # print(ost)
        st_r[-1]=str(ost)
        # print(st_r)
        number_out=float(".".join(st_r))
        # print(number_out)

        if int(str(number).split(".")[-1]) % 10 ** b > int(0.5 * 10 ** b):
            return number_out + 1/10**ndigits
        else:
            return number_out
    return number

print(my_round(2.12345678, 5))
print(my_round(2.19999678, 5))
print(my_round(2.99999678, 5))



    # Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    """
    Функция определяет счастливый билет
    :param ticket_number:
    :return:
    """
    l_str=list(str(ticket_number))
    l_int = [int(a) for a in l_str]
    return len(l_str)==6 and sum(l_int[0:3]) == sum(l_int[-3:])

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))



