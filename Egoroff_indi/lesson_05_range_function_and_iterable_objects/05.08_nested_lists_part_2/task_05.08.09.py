""" Заполнение змейкой.
    Даны числа n и column. Создайте массив A[n][column] и заполните его змейкой (см. пример).
    Входные данные:
Программа получает на вход два числа n и column.
    Выходные данные:
Программа должна вывести полученный массив, при этом между числами может быть любое количество пробелов."""

# variant 1:
row, column = map(int, input().split())
matrix = [[0] * column for _ in range(row)]
count = 0
for i in range(row):
    for j in range(column):
        if i % 2 == 0:
            matrix[i][j] = count
            count += 1
        else:
            matrix[i][column - 1 - j] = count
            count += 1
for k in matrix:
    print(*k)

# variant 2:
row, column = map(int, input().split())
matrix = []
for i in range(row):
    if i % 2 == 0:
        matrix.append(list(range(i * column, i * column + column)))
    else:
        matrix.append(list(range(i * column, i * column + column)[::-1]))
for k in matrix:
    print(*k)