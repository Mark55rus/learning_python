""" Спираль
Требуется вывести квадрат, состоящий из N×N клеток, заполненных числами от 1 до N2 по спирали (см. примеры).
    Входные данные
Программа получает на вход одно число n.
    Выходные данные
Программа должна вывести матрицу, заполненную числами от 1 до N2 по спирали, при этом между числами может быть любое
количество пробелов. Не допускается начинать спираль в ином, кроме верхнего левого, углу, закручивать спираль против
часовой стрелки или изнутри наружу."""

n = int(input())
matrix = [[0] * n for _ in range(n)]
row = 0  # Начальная позиция по строке
column = -1  # Начальная позиция по столбцу
go_row = 0  # Движение по строке
go_column = 1  # Движение по столбцу
i = 1  # Начальное значение заполнения
length = len(str(n ** 2))  # Максимально возможная длина цифры
while i <= n ** 2:
    if row + go_row < n and column + go_column < n and matrix[row + go_row][column + go_column] == 0:
        row += go_row
        column += go_column
        matrix[row][column] = i
        i += 1
    else:
        if go_column == 1:
            go_column = 0
            go_row = 1
        elif go_row == 1:
            go_row = 0
            go_column = -1
        elif go_column == -1:
            go_column = 0
            go_row = -1
        elif go_row == -1:
            go_row = 0
            go_column = 1
for row in matrix:
    for elem in row:
        print(str(elem).rjust(length), end=' ')
    print()
