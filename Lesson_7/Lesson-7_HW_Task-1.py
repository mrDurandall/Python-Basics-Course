# Задание 1
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.


class Matrix:

    def __init__(self, matrix_list):
        if type(matrix_list) != list:
            print('Ошибка! Необходимо ввести список списков!')
            raise TypeError
        for el in matrix_list:
            if type(el) != list:
                print('Ошибка! Необходимо ввести список списков!')
                raise TypeError
            if len(el) != len(matrix_list[0]):
                print('Ошибка! Строки матрицы должны быть одинаковой длины!')
                raise ValueError
        self.matrix = matrix_list

    def __str__(self):
        result = '\n'
        for string in self.matrix:
            for el in string:
                result += f'{el:>5} '
            result += '\n'
        return result

    def __getitem__(self, string):
            return self.matrix[string]

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            print('Ошибка! Нельзя складывать матрицы разных размерностей')
            raise ValueError
        else:
            result = []
            for istrings in range(0, len(self.matrix)):
                resstring = []
                for i in range(0, len(self.matrix[istrings])):
                    resstring.append(self.matrix[istrings][i] + other.matrix[istrings][i])
                result.append(resstring)
            resm = Matrix(result)
            return resm


m = Matrix([[1000, 2, 5, 6], [3, 4, 14, 67], [5, 6, 43, 21]])
print(f'{m}')
print(f'{m[2]}')
m1 = Matrix([[1, 2], [3, 4], [5, 6]])
m2 = Matrix([[3, 4], [5, 7], [8, 4]])
print(m + m1)
print(m1 + m2)
