# Задание 4 - Найти элементы списка не имеющие повторений

from random import randint
originalList = []
for i in range(0, 10):
    originalList.append(randint(1, 10))
print(f'Оригинальный список: {originalList}')
finalList = [el for el in originalList if originalList.count(el) == 1]
print(f'элементы {finalList} не повторяются')
