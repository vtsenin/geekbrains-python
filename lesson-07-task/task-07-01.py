"""
 Урок 7. Задание 1.
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix_data: list[list]):
        self.matrix_data = matrix_data
        matrix_rows = len(self.matrix_data)
        self._matrix_size = ([(matrix_rows, len(row)) for row in self.matrix_data])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix_data])

    def __add__(self, matrix_other):
        # other = Matrix(matrix_other)
        if not isinstance(matrix_other, Matrix):
            raise TypeError(f"{matrix_other.__class__.__name__} не подходящий тип объекта")
        if self._matrix_size != matrix_other._matrix_size:
            raise ValueError(f"Размеры матриц отличаются")
        result = []
        numbers = []
        for i in range(len(self.matrix_data)):
            for j in range(len(self.matrix_data[0])):
                summa = matrix_other[i][j] + self.matrix_data[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix_data):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

    def __getitem__(self, index):
        return self.matrix_data[index]


matrix_test1 = Matrix([[10, 20], [11, 21]])
print(matrix_test1)

matrix_test2 = Matrix([[100, 200], [101, 201]])
print(matrix_test2)

print(f"Результат операции сложения двух объектов класса Matrix \n{matrix_test1 + matrix_test2}")
