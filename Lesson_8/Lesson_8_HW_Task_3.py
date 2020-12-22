# Задание 3
# Создайте собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
# запрашивать у пользователя данные и заполнять список только числами. Класс-исключение
# должен контролировать типы данных элементов списка.


class NotNum(Exception):

    def __init__(self, errmsg):
        self.txt = errmsg

def num_input(call):
    """Функция ввода чисел. Работает аналогично input(),
    Но дополнительно проверяет, является ли введенное значение числом.
    Если не является, то запрашивает повторно.
    При вводе текста "stop" завершает программу."""
    global stoped
    while True:
        num = input(call)
        if num.lower() == 'stop':
            stoped = True
            break
        try:
            if not num.replace('.', '', 1).isnumeric():
                raise NotNum('Вы ввели не число!')
        except NotNum as NN:
            print(NN)
        else:
            return float(num)


numlist = []
stoped = False
while not stoped:
    print('Для выхода введите "stop"')
    numlist.append(num_input('Введите число: '))
numlist.pop()
print(numlist)
