# Задание 7
# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.


class ComplexNumber:

    def __init__(self, a, b):
        if type(a) not in [int, float] or type(b) not in [int, float]:
            raise ValueError
        self.a = round(a, 5)
        self.b = round(b, 5)

    def __str__(self):
        return '{} + {}j'.format(self.a, self.b)

    def __add__(self, other):
        if type(other) == ComplexNumber:
            return ComplexNumber(self.a + other.a, self.b + other.b)
        elif type(other) == int or type(other) == float:
            return ComplexNumber(self.a + other, self.b)
        else:
            raise ValueError

    def __sub__(self, other):
        if type(other) == ComplexNumber:
            return ComplexNumber(self.a - other.a, self.b - other.b)
        elif type(other) == int or type(other) == float:
            return ComplexNumber(self.a - other, self.b)
        else:
            raise ValueError

    def __mul__(self, other):
        if type(other) == ComplexNumber:
            a = self.a
            b = self.b
            c = other.a
            d = other.b
            return ComplexNumber(a * c - b * d, b * c + a * d)
        elif type(other) in [int, float]:
            return ComplexNumber(self.a * other, self.b)

    @staticmethod
    def manual_input():
        a = float(input('Введите действительную часть комплексного числа: '))
        b = float(input('Введите мнимую часть комплексного числа: '))
        return ComplexNumber(a, b)


cn1 = ComplexNumber(5, 4)
cn2 = ComplexNumber(-1, 7)
cn3 = ComplexNumber(1.2, 5.8)
print(cn1, cn2, sep='; ')
print(cn1 + cn2)
print(cn1 - cn2)
print(cn1 - 2)
print(cn2 - 5.3)
print(cn3 - 3)
print(cn1 * cn2)
print(cn2 * cn3)
print(cn2 * 5)
cn4 = ComplexNumber.manual_input()
# Проверка некорректного типа данных при вводе или операции сложения
# cn4 = ComplexNumber('Hello', 'World!')
# print(cn1 + 'Привет!')
print(cn4)
