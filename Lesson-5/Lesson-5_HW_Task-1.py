# Задание 1
# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

from os import remove

# Если создаваемый файл уже существует - удаляем его.
try:
    remove('Task-1-file.txt')
except FileNotFoundError:
    pass

task1file = open('Task-1-file.txt', 'a')
while True:
    newString = input('Введите новую строку текста и нажмите Enter.\n'
                      'Для завершения ввода нажимте Enter при пустой строке:\n')
    if newString == '':
        task1file.close()
        break
    else:
        task1file.write(newString + '\n')

with open('Task-1-file.txt', 'r') as task1file:
    fileContent = task1file.read()
print('Содержимое созданного фала:\n\n', fileContent, sep='')
