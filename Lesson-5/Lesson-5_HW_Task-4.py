# Задание 4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

numDict = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'}

numbersEng = open('Task-4-file-Eng.txt', 'r')
engText = numbersEng.readlines()
print('Сожержимое оригинального файла:\n')
with open('Task-4-file-Rus.txt', 'w') as numberRus:
    for line in engText:
        print(line, end='')
        numberRus.write(numDict[line.split(' - ')[0]] + ' - ' + line.split(' - ')[1])
print('\n\nПеревод сохранен в фал "Task-4-file-Rus.txt"')
numbersEng.close()
