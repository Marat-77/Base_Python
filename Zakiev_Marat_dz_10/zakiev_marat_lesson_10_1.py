# /Zakiev_Marat_dz_10/zakiev_marat_lesson_10_1.py
# zakiev_marat_lesson_10_1
#
# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
#
class Matrix:
    def __init__(self, input_list: list):
        self.m_list = input_list

    def __str__(self):
        # метод для вывода print
        output = ''
        for i in self.m_list:
            line_j = ''
            for j in i:
                line_j += f'{j:5}'
            output += line_j + '\n'
        return output

    def __add__(self, other):
        output_list = []
        # output_list = Matrix()
        for i, row in enumerate(self.m_list):
            new_list = list(map(lambda x, y: x + y, row, other.m_list[i]))
            output_list.append(new_list)
        # print(output_list)
        output_matrix = Matrix(output_list)
        return output_matrix
    # l1 = [1, 2, 3]
    # l2 = [4, 5, 6]
    # new_list = list(map(lambda x, y: x + y, l1, l2))
    # print(new_list)
    # # http://pythonicway.com/python-functinal-programming
    # с enumerate разобрался, а вот с map всё ещё туплю...
    # не совсем понял как, но это работает ;)


def main():
    first_list = [[2, 5, 64, 32], [25, 3, 48, 22], [73, 0, 14, 8]]
    second_list = [[3, 0, 55, 41], [7, 2, 17, 9], [21, 5, 18, 63]]
    first_matrix = Matrix(first_list)
    second_matrix = Matrix(second_list)
    print(first_matrix)
    print(second_matrix)
    third_matrix = first_matrix + second_matrix
    print(third_matrix)
    print(type(third_matrix))  # <class '__main__.Matrix'>


if __name__ == '__main__':
    main()
#
