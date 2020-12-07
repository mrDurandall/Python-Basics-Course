# Задание 5
# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.

from random import randint


with open('Task-5-file.txt', 'w') as numbers:
    for i in range(0, 10):
        numbers.write(f'{randint(1, 100)} ')

fileSum = 0
with open('Task-5-file.txt', 'r') as fileNum:
    numbers = fileNum.read()
    print('В файле содержится следующее:', numbers, sep='\n')
    for el in numbers.split():
        fileSum += int(el)
print('Сумма чисел в файле:', fileSum)
