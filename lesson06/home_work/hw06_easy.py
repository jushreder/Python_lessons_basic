# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import random


class Triangle:
    def __init__(self, args):
        self.angle1 = args[0]
        self.angle2 = args[1]
        self.angle3 = args[2]
    def __str__(self):
        return f'Треугольник с вершинами А{self.angle1}, В{self.angle2}, С{self.angle3}'

    @property
    def square(self):
        pl=abs(((self.angle1[0]-self.angle3[0])*(self.angle2[1]-self.angle3[1])-
               ((self.angle2[0]-self.angle3[0])*(self.angle1[1]-self.angle3[1])))/2)
        return  pl

    @property
    def val_ab(self):
        ab = ((self.angle2[0] - self.angle1[0]) ** 2 + (self.angle2[1] - self.angle1[1]) ** 2) ** 0.5
        return ab

    @property
    def val_bc(self):
        bc = ((self.angle3[0] - self.angle2[0]) ** 2 + (self.angle3[1] - self.angle2[1]) ** 2) ** 0.5
        return bc

    @property
    def val_ca(self):
        ca = ((self.angle1[0] - self.angle3[0]) ** 2 + (self.angle1[1] - self.angle3[1]) ** 2) ** 0.5
        return ca

    @property
    def perimeter(self):
        pr = self.val_ab + self.val_bc + self.val_ca
        return pr

    @property
    def height(self):
        height_a = (2*self.square())/self.val_bc()
        height_b = (2*self.square())/self.val_ca()
        height_c = (2*self.square())/self.val_ab()
        height_val = min(height_a, height_b, height_c)
        return height_val

# min_i= -10
# max_i = 10
# def coord():
#     return [random.randint(min_i,max_i),random.randint(min_i,max_i)]

# triangle_list=[coord() for i in range(4)]
triang=[-6, -1], [6, 0], [-8, -8]

triangl_1 = Triangle(triang)

print(triangl_1)
print(triangl_1.square)
print(triangl_1.perimeter)
# print(triangl_1.height)
# print(f'{triangl_1},\nплощадь: {triangl_1.square()}\nпериметр: {triangl_1.perimeter()}\n'
#       f'высота: {triangl_1.height()}' )

# Треугольник с вершинами А[-6, -1], В[6, 0], С[-8, -8],
# площадь: 41.0
# периметр: 35.446219964669915
# высота: 5.0854241181575475


#

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trap:
    def __init__(self, angle1,angle2,angle3,angle4):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        self.angle4 = angle4

    @property
    def val_ab(self):
        ab = ((self.angle2[0] - self.angle1[0]) ** 2 + (self.angle2[1] - self.angle1[1]) ** 2) ** 0.5
        return ab

    @property
    def val_bc(self):
        bc = ((self.angle3[0] - self.angle2[0]) ** 2 + (self.angle3[1] - self.angle2[1]) ** 2) ** 0.5
        return bc

    @property
    def val_cd(self):
        cd = ((self.angle4[0] - self.angle3[0]) ** 2 + (self.angle4[1] - self.angle3[1]) ** 2) ** 0.5
        return cd

    @property
    def val_da(self):
        da = ((self.angle1[0] - self.angle4[0]) ** 2 + (self.angle1[1] - self.angle4[1]) ** 2) ** 0.5
        return da

    @property
    def perim(self):
        pr = self.val_ab + self.val_bc + self.val_cd + self.val_da
        return pr

    @property
    def check(self):
        val = self.val_ab == self.val_cd and  \
              (self.angle4[0] - self.angle1[0]) / self.val_da == (self.angle3[0] - self.angle2[0]) / self.val_bc or \
              self.val_bc == self.val_da and \
              (self.angle4[0] - self.angle3[0]) / self.val_cd == (self.angle2[0] - self.angle1[0]) / self.val_ab
        return val


    def square(self):
        pl = abs(((self.angle1[0] - self.angle3[0]) * (self.angle2[1] - self.angle3[1]) -
                  ((self.angle2[0] - self.angle3[0]) * (self.angle1[1] - self.angle3[1]))) / 2) + \
             abs(((self.angle1[0] - self.angle3[0]) * (self.angle4[1] - self.angle3[1]) -
                 ((self.angle4[0] - self.angle3[0]) * (self.angle1[1] - self.angle3[1]))) / 2)
        return pl

    def __str__(self):
        return f'Равнобочная трапеция А{self.angle1}, В{self.angle2}, С{self.angle3}, D{self.angle4}'


trapez1 = Trap([3,1], [5,4], [9,4] ,[11,1])
print()
print(trapez1)
print(trapez1.check)
print(f'Периметр равнобокой трапеции : {trapez1.perim}')
print(trapez1.square())
