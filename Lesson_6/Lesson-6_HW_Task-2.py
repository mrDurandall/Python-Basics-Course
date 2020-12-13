# Задание 2
# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._thickness = 5
        self._mass_for_sqrm = 25

    def asphalt(self):
        mass_of_asphalt = self._length * self._width * self._thickness * self._mass_for_sqrm
        return mass_of_asphalt


m8 = Road(5000, 20)
print(f'{m8.asphalt()/1000} т')
