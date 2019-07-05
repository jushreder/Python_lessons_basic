# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
lst=[1, 2, 4, 0]
list2=[a*a for a in lst]
print(list2)
# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1=["Яблока","Киви","Груша","Манго","Ананас","Авокада","Хурма","Маракуйя","Папайя"]
fruits2=["Груша","Фейхоа","Хурма","Карамболе","Ананас","Нони","Манго","Тамарилло","Киви"]
fruits=[i for i in fruits1 if i in fruits2]
print(fruits)
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
lst=[1, 3, 4, 12, 5, 7, 4, 10, 33, -3, 8, 9, 32]
lst1=[i for i in lst if i%3==0 and i>0 and i%4!=0]
print(lst1)
