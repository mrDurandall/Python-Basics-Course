# Задание 2
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
# ошибкой.

from sys import exit


class DivNullError(Exception):

    def __init__(self, errmsg):
        self.txt = errmsg


class NotNum(Exception):

    def __init__(self, errmsg):
        self.txt = errmsg


def stop(string):
    if string.lower() == 'stop':
        exit()


def num_input(call):
    """Функция ввода чисел. Работает аналогично input(),
    Но дополнительно проверяет, является ли введенное значение числом.
    Если не является, то запрашивает повторно.
    При вводе текста "stop" завершает программу."""
    while True:
        num = input(call)
        stop(num)
        try:
            if not num.replace('.', '', 1).isnumeric():
                raise NotNum('Вы ввели не число!')
        except NotNum as NN:
            print(NN)
        else:
            return float(num)


while True:
    print('Для выхода введите "stop"')
    a = num_input('Введите числитель: ')
    b = num_input('Введите знаменатель: ')
    try:
        if b == 0:
            raise DivNullError('Делить на ноль нельзя!')
    except DivNullError as err:
        print(err)
    else:
        print(float(a) / float(b))
