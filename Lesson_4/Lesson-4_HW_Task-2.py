# Задание 2 - Получить элементы списка, которые больше предыдущего элемента.
from random import randint
originalList = []
for i in range(0, 10):
    originalList.append(randint(1, 100))
print(f'Оригинальный список: {originalList}')
finalList = [originalList[i] for i in range(1, len(originalList)) if originalList[i] > originalList[i-1]]
print(f'Итоговый список: {finalList}')