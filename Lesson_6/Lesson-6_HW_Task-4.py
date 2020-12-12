# Задание 4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты
# speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self):
        self.speed = 0
        self.color = 'Black'
        self.name = 'A111AA'
        self.is_police = False

    def go(self):
        self.speed = 40
        print(f'Автомобиль {self.name} начал движение')

    def stop(self):
        self.speed = 0
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direct):
        print(f'Автомобиль {self.name} повернул {direct}')

    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed}')


class SportCar(Car):

    def __init__(self, color, name):
        self.color = color
        self.speed = 180
        self.name = name


class TownCar(Car):

    def __init__(self, color, name):
        self.color = color
        self.speed = 60
        self.name = name

    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed}')
        if self.speed > 60:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ!!!')


class PoliceCar(Car):

    def __init__(self, name):
        self.color = 'Black and White'
        self.speed = 60
        self.name = name
        self.is_police = True


class WorkCar(Car):

    def __init__(self, name):
        self.color = 'Green'
        self.speed = 40
        self.name = name

    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed}')
        if self.speed > 40:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ!!!')


car1 = WorkCar('B777BB')
car2 = PoliceCar('P111PP')
car3 = TownCar('Yellow', 'T666TT')
car4 = SportCar('Red', 'C999CC')

car1.show_speed()
car2.show_speed()
car3.show_speed()
car4.show_speed()

car1.speed = 120
car2.speed = 120
car3.speed = 120
car4.speed = 120

car1.show_speed()
car2.show_speed()
car3.show_speed()
car4.show_speed()

car1.go()
car2.stop()
car3.turn('Налево')
car4.turn('Направо')
