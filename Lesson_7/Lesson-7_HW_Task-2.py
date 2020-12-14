# Задание 2
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes:

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def clothusage(self):
        pass


class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def clothusage(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def clothusage(self):
        return self.height * 2 + 0.3


c1 = Costume('Тройка', 5)
print(c1.name)
print(c1.height)
print(c1.clothusage)
c2 = Coat('Летучая мышь', 45)
print(c2.name)
print(c2.size)
print(c2.clothusage)
