# Задание 5
# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут
# title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self):
        self.title = ''

    def draw(self):
        print('Запуск Отрисовки.')


class Pen(Stationery):

    def __init__(self):
        self.title = 'Ручка'

    def draw(self):
        print('Запуск Отрисовки.')
        print('Рисунок ручки')


class Pencil(Stationery):

    def __init__(self):
        self.title = 'Карандаш'

    def draw(self):
        print('Запуск Отрисовки.')
        print('Рисунок карандаша')


class Handle(Stationery):

    def __init__(self):
        self.title = 'Маркер'

    def draw(self):
        print('Запуск Отрисовки.')
        print('Рисунок маркера')


pen1 = Pen()
pencil1 = Pencil()
handle1 = Handle()

pen1.draw()
pencil1.draw()
handle1.draw()