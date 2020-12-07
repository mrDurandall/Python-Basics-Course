# Задание 1 - Рассчет заработной платы.
from sys import argv

script_name, salary, workTime, bonus = argv

wages = float(salary) * float(workTime) + float(bonus)
print(f'Оклад: {salary}\nОтработанное время: {workTime}\nПремия: {bonus}\nЗаработная плата составила: {wages:.2f}')
