# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
class School:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name



class Class_room:
    def __init__(self, name, school):
        self. name = name
        self.school = school
    def __str__(self):
        return f'{self.name} {self.school}'


school1 = School('Лицей 35')
class1 = Class_room('5 A', school1)
class2 = Class_room('5 B', school1)
class3 = Class_room('10 A', school1)

class People:
    def __init__(self, name, surname, b_date, sex):
        self.name = name
        self.surname = surname
        self.b_date = b_date
        self.sex = sex
    def __str__(self):
        return f'{self.surname} {self.name}, {self.b_date}, {self.sex}'

class Student(People, Class_room):
    def __init__(self,name,surname,b_date,sex,school, class_room, dad=None, mama=None):
        self.dad= dad
        self.mama = mama
        Class_room.__init__(self,class_room ,school)
        People.__init__(self, name, surname, b_date, sex)
    def __str__(self):
        return f'{self.surname} {self.name}'
    def paren(self):
        return f'{self.dad}  {self.mama}'


class Teacher(People,Class_room):
    def __init__(self, name, surname, b_date, sex, school, class_room,subject ):
        self.subject = subject
        People.__init__(self,name, surname, b_date, sex)
        Class_room.__init__(self, class_room, school)
    def fio(self):
        return f'{People.__str__(self)} - {self.subject}'


class Parents(People):
    def __init__(self, name, surname, b_date, sex, parent, kind_name, kind_b_date):
        self.parent = parent
        self.kind_name = kind_name
        self.kind_b_date = kind_b_date
        People.__init__(self, name, surname, b_date, sex)

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'
parent1=Parents('Николай','Петров','1968-03-02','муж','папа','Илья','1985-10-22')
parent2=Parents('Светлана','Петрова', '1989-10-12','жен','мама','Илья','1985-10-22')
student1=Student('Илья','Петров','1985-10-12','муж','Лицей 35','5 A',parent1, parent2)

print(student1.paren())


