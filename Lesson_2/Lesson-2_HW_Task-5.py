# Задание 5 - Рейтинг.
print('Задание 4 - Рейтинг.')
rating = [7, 6, 6, 5, 3, 2]
print(f'Текущий рейтинг: {rating}')
# Ввод данных реализован бесконечным циклом,
# чтобы можно было ввести в рейтинг несколько значений
while True:
    # Проверяем, ввел ли пользователь число
    # Если введены данные другого типа, заканчиваем ввод и выводим итоговый рейтинг
    try:
        userNum = int(input('Добавьте новый элемент в рейтинг: '))
    except ValueError:
        print('Вы ввели не целое число, ввод данных окончен')
        print(f'Итоговый рейтинг: {rating}')
        break
    if userNum <= rating[-1]:
        rating.append(userNum)
    else:
        for ind in range(0, len(rating)):
            if userNum > rating[ind]:
                rating.insert(ind, userNum)
                break
    print(f'Текущий рейтинг: {rating}')