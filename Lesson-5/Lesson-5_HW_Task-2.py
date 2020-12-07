# Задание 2
# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

with open('Task-2-file.txt', 'r') as task2file:
    fileContent = task2file.readlines()
print(fileContent)

numOfStrs = 0
for string in fileContent:
    numOfStrs += 1
    print(f'Строка {numOfStrs} сожержит {len(string.split())} слов.')
print(f'В файле всего {numOfStrs} строк.')
