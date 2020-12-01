# Задание 5 - Сумма чисел из строки.
print('Задание 5 - Сумма чисел из строки\n\n')

def total_sum():
    """Функция total_sum повторяет функцию string_sum пока переменная isEnd не примет значение True"""
    total = 0
    isEnd = False

    def string_sum(string):
        """Функция принимает строку чисел, записанных через пробел и считает их сумму
        Если в строке встречается не целое число - оно игнорируется
        Если пользователь вводит слово End - то выполнение программы заканчивается"""
        nonlocal isEnd
        strSum = 0
        for el in string.split():
            if el.capitalize() == 'End':
                isEnd = True
                return strSum
            try:
                strSum += int(el)
            except ValueError:
                continue
        return strSum

    while not isEnd:
        total += string_sum(input('Введите строку чисел (Для завершения программы введите End): '))
        if not isEnd:
            print(f'Текущая сумма: {total}')
    print(f'Выполнение программы завершено. Итоговая сумма: {total}')

total_sum()
