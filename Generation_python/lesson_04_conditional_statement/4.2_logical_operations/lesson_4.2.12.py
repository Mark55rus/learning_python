"""Неравенство треугольника.
Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник
 с такими сторонами.
Формат входных данных
На вход программе подаётся три положительных целых числа.
Формат выходных данных
Программа должна вывести «YES» или «NO» в соответствии с условием задачи.
Примечание. Треугольник существует, если выполняется неравенство треугольника."""

ab, bc, ca = int(input()), int(input()), int(input())
if ab < bc + ca and bc < ab + ca and ca < ab + bc:
    print('YES')
else:
    print('NO')
