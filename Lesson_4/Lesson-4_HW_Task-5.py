# Задание 5 - Произведение четных чисел от 100 до 1000
from functools import reduce


def mult(el1, el2):
    """Функция перемножающая два элемента"""
    return el1 * el2


numbers = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(mult, numbers))
