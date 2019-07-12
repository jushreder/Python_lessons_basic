# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
import os

class StaffList:
    def __init__(self, name ,surname, salary, position, norm):
        self.name = name
        self.surname = surname
        self.salary = int(salary)
        self.position = position
        self.norm = int(norm)
    def __str__(self):
        return f'{self.surname} {self.name}'
    def fio(self):
        return f'{self.surname} {self.name}'
    def hour_solory(self):
        return self.salary/self.norm

with open('data/workers', 'r') as file:
    temp = [line.rstrip() for line in file.readlines()]
temp.pop(0)
stafflst=[]
for num, person  in enumerate(temp, start=1):
    person=[itm for itm in person.split(' ') if itm.isalnum()]
    stafflst.append(StaffList(person[0],person[1],person[2],person[3],person[4]))

class ReportCart:
    def __init__(self, name ,surname, worked):
        self.name = name
        self.surname = surname
        self.worked = int(worked)

    def __str__(self):
        return f'{self.surname} {self.name}'
    def fio(self):
        return f'{self.surname} {self.name}'

with open('data/hours_of', 'r') as file:
    temp = [line.rstrip() for line in file.readlines()]
temp.pop(0)
report=[]
for num, person  in enumerate(temp, start=1):
    person=[itm for itm in person.split(' ') if itm.isalnum()]
    report.append(ReportCart(person[0],person[1],person[2]))

with open('data/hours_out', 'w') as file:
    file.write('{:<10}{:<10}{:>10}\n'.format('Имя','Фамилия','Начислено'))

for emp in stafflst:
    for wmp in report:
        if emp.fio()==wmp.fio():
            if emp.norm>=wmp.worked:
                accrued =emp.hour_solory()*wmp.worked
            else:
                accrued= emp.salary + (wmp.worked-emp.norm)*emp.hour_solory()*2
            with open('data/hours_out', 'a') as file:
                file.write('{:<10}{:<10}{:>10}\n'.format(emp.name, emp.surname, int(accrued)))


