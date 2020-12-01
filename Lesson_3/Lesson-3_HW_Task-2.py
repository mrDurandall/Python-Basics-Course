# Задание 2 - Данные пользователя.
print('Задание 2 - Данные пользователя.')
def userProfile(name, surname, year, city, mail, phonenumber):
    """Функция, принимающая данные пользователя
    и печатающая их одной строкой.
    return возвращает список с полученными данными."""
    print(f'Имя: {name}, Фамилия: {surname}, год рождения: {year}, город: {city}, e-mail: {mail}, тел: {phonenumber}.')
    return name, surname, year, city, mail, phonenumber

userProfile('Василий', 'Уткин', 1975, 'Караганда', 'VasiliyUtkin@mail.ru', '89996665544')