"""Арифметическая прогрессия.
Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами
 арифметической прогрессии.
Формат входных данных
На вход программе подаются три числа, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи. """

num_1, num_2, num_3 = int(input()), int(input()), int(input())
if num_1 - num_2 == num_2 - num_3:
    print('YES')
else:
    print('NO')
