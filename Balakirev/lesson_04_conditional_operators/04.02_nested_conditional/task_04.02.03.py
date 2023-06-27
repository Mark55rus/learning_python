"""Подвиг 2. Вводятся три целых числа в одну строку через пробел. Необходимо
определить наименьшее среди них и вывести его на экран. Реализовать программу,
используя условный оператор, без использования функции min."""

a, b, c = map(int, input().split())
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)

# Variant 2:
# a, b, c = map(int, input().split())
# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# print(a)
