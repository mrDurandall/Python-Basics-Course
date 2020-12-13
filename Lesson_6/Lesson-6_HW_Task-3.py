# Задание 3
# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'Wage': int(wage),
            'Bonus': int(bonus)
        }


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('Wage') + self._income.get('Bonus')


ivanov = Position('Василий', 'Иванов', 'Уборщик', 15000, 6500)
print(ivanov.name)
print(ivanov.surname)
print(ivanov.position)
print(ivanov._income)
print(ivanov.get_full_name())
print(ivanov.get_total_income())
