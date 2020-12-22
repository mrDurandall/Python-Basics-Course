# Задание 1
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class DateError(Exception):

    def __init__(self, errmsg):
        self.txt = errmsg


class Date:

    def __init__(self, date):
        """При создании экземпляра класса запрашиваем у пользователя дату в формате
        ДД-ММ-ГГГГ, помощью метода extract преобрауем к словарю и присваеваем его атрибуту date"""
        self.date = self.extract(date)

    def __str__(self):
        return 'День: - {}, Месяц - {}, Год - {}'.format(self.date['Day'], self.date['Month'], self.date['Year'])

    @classmethod
    def extract(cls, date):
        """Функция принимает сроку вида ДД-ММ-ГГГГ,
        Извлекает из нее значения дня, месяца и года и приводит их к числовому формату.
        Проверяет валидность введенной даты.
        Возвращет словарь с ключами Day, Month, Year, которым соответствют полученные значения."""
        day = int(date.split('-')[0])
        month = int(date.split('-')[1])
        year = int(date.split('-')[2])
        day, month, year = cls.validate_date(day, month, year)
        return {'Day': day, 'Month': month, 'Year': year}

    @staticmethod
    def validate_date(day, month, year):
        """Функция, проверяющая значение даты
        получает 3 параметра - day, month, year
        проверяет, существуют ли дни и месяцы с такими номерами.
        Учитывает разную длину месяцев. Не учитытвает високосные годы.
        Проверяет, попадает ли значение года в промежуток 1980-2020.
        Если в каком-то из параметров ошибкаЮ то выводит соответствующее сообщение
        и приводит данный параметр к значению по-умолчанию (1 для месяца и дня и 1980 для года)"""
        try:
            if month not in range(1, 13):
                month = 1
                raise DateError('Ошибка в значении месяца!')
        except DateError as de:
            print(de)
        try:
            if month in [1, 3, 5, 7, 8, 10, 12] and day not in range(1, 32):
                day = 1
                raise DateError('Ошибка в значении дня!')
            elif month in [4, 6, 9, 11] and day not in range(1, 31):
                day = 1
                raise DateError('Ошибка в значении дня!')
            elif month == 2 and day not in rang(1, 29):
                day = 1
                raise DateError('Ошибка в значении дня!')
        except DateError as de:
            print(de)
        try:
            if year not in range(1980, 2020):
                year = 1980
                raise DateError('Ошибка в значении года!')
        except DateError as de:
            print(de)
        else:
            print('Дата корректна')
        return day, month, year


print(Date.validate_date(15, 16, 1988))
print(Date.validate_date(31, 1, 2019))
d1 = Date('15-06-1987')
print(d1)
print(Date.extract('22-1-1999'))
