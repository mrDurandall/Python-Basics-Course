# Задание 7
# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка,
# издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json


firmsList = [{}]
print('Перечень фирм:\n'
      'Название  | Форма | Выручка | Издержки\n'
      '----------------------------------------')
with open('Task-7-file.txt', 'r') as firms:
    for line in firms:
        print(f'{line.split()[0]:<10}|{line.split()[1]:^7}|{int(line.split()[2]):>9}|{int(line.split()[3]):>9}')
        firmsList[0].update({line.split()[0]: int(line.split()[2]) - int(line.split()[3])})

print('\nПрибыль фирм составила:')
for firm in firmsList[0]:
    print(f'{firm:<8}|{firmsList[0].get(firm):>6}')

avrgProfit = sum([el for el in firmsList[0].values() if el > 0]) / len([el for el in firmsList[0].values() if el > 0])
print('\nСредняя прибыль: ', avrgProfit)
firmsList.append({'Average profit': avrgProfit})
print(firmsList)

with open('Task-7-file.json', 'w') as jsonWrite:
    json.dump(firmsList, jsonWrite)
