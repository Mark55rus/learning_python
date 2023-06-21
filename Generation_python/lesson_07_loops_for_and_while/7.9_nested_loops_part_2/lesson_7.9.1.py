"""Численный треугольник 3
Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой равной n,
в соответствии с примером:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
...
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести треугольник в соответствии с условием.
Примечание. Используйте вложенный цикл for."""

n = int(input())
total = 0
for i in range(1, n + 1):
    for j in range(i):
        total += 1
        print(total, end=' ')
    print()
