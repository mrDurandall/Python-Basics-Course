# Задание 5 - выручка и издержки
print('Задание 5 - выручка и издержки')
proceeds = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
if proceeds > costs:
    profit = proceeds - costs
    print(f'Поздравляем! Вы работаете с прибылью! Прибыль составляет {profit} тэнге.')
    print(f'Рентабельность выручки составляет {profit / proceeds}.')
    crew = int(input('Введите число сотрудников фирмы: '))
    print(f'На одного сотрудника прихдится {profit / crew} тэнге прибыли.')
else:
    print(f'Время затянуть пояса.Вы работаете с убытками! Убыток составляет {costs - proceeds} тэнге.')