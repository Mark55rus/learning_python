""" Подвиг 2. Вводится строка вещественных чисел через пробел. Необходимо
определить, есть ли среди них хотя бы одно отрицательное. Вывести True,
если это так и False - в противном случае.

Задачу реализовать с использованием одной из функций: any или all."""

lst = map(float, input().split())
print(any(map(lambda x: x < 0, lst)))
# or:
# print(any(float(c) < 0 for c in input().split()))
# or
# print(not all(map(lambda x: x > 0, lst)))
