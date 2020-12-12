# Задание 1
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
from itertools import cycle


class TrafficLight:
    __color = 'Red'

    def __init__(self, green_time):
        self.color_times = {
            'Red': 7,
            'Yellow': 2,
            'Green': green_time
        }

    def running(self):
        count = 0
        next_color = 'Red'
        for el in cycle(self.color_times.keys()):
            self.__color = el
            if count > 5:               # Данный переключатель сделан для демонстрации
                self.__color = 'Red'    # отключения при сбое порядка цветов
            print(self.__color)
            if self.__color != next_color:
                print('Ошибка порядка цветов!')
                break
            sleep(self.color_times.get(el))
            if self.__color == 'Red':
                next_color = 'Yellow'
            elif self.__color == 'Yellow':
                next_color = 'Green'
            elif self.__color == 'Green':
                next_color = 'Red'
            count += 1


tl1 = TrafficLight(15)
tl1.running()
