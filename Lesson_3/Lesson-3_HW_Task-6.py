# Задание 6 - Слова с большой буквы.
print('Задание 6 - Слова с большой буквы.')

def capital_word(word):
    """Функция переводящая первую букву слова в верхний регистр"""
#   Если с использование встроенного метода строк, то так:
#    return word.capitalize()

#   Если без него, то:
    if ord(word[0]) >= 97 and ord(word[0]) <=122:
        return f'{chr(ord(word[0]) - 32)}{word[1:]}'
    return word
#   Проверяем, начинается ли слово с маленькой латинской буквы
#   Если да, то заменяем ее на болшую и возвращаем
#   Если нет, то возвращаем как есть

def capital_string(string):
    """Функция переводящая первые буквы всех слов в строке в верхний регистр"""
    outcome = []
    for el in string.split():
        outcome.append(capital_word(el))
    outcome = ' '.join(outcome)
    return outcome
print(capital_word('lorem'))
print(capital_string('lorem ipsum dolor sit amet, consectetur adipiscing elit'))
