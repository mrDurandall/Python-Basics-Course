# Задание 6 - Итераторы
import itertools


start = int(input('Введите стартовое число: '))
finish = int(input('Введите конечное число: '))
for i in itertools.count(start):
    if i <= finish:
        print(i)
    else:
        break

string = input('Введите строку из нескольких слов через пробел:\n')
number = int(input('Введите число выводимых слов: '))
i = 1
for el in itertools.cycle(string.split()):
    if i <= number:
        print(el)
        i += 1
    else:
        break
