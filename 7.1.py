"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str("\n".join(["\t".join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        matrix_result = [[0 for el in range(len(self.matrix[0]))] for elem in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(other[i])):
                matrix_result[i][j] = self.matrix[i][j] + other[i][j]
        return str("\n".join(["\t".join([str(i) for i in j]) for j in matrix_result]))

    def __getitem__(self, index):
        return self.matrix[index]


one_matrix = Matrix([
    [5, 5, 4, 6],
    [8, 1, 2, 3],
    [0, 9, 1, 4],
    [0, 6, 1, 3]
])

two_matrix = Matrix([
    [3, 4, 5, 4],
    [1, 2, 3, 2],
    [0, 6, 1, 7],
    [2, 3, 9, 7]
])
print(one_matrix)
print()
print(one_matrix + two_matrix)
