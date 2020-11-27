# Задание 4 - Ввод строки из нескольких слов.
print('Задание 4 - Ввод строки из нескольких слов.')
userString = input('Введите строку из нескольких слов:\n')
for ind, word in enumerate(userString.split()):
    print (ind + 1, word[:10])