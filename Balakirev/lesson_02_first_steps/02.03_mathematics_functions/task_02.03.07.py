""" Подвиг 6. Допишите программу для нахождения числа сочетаний из n по k (
значения вводятся в программе), используя формулу n! / (k! * (n - k)!).
Выведите результат в консоль в виде целого числа с помощью функции print.
    Для вычисления факториалов воспользуйтесь соответствующей функцией из
библиотеки math."""

from math import factorial as f

# ввод данных
n, k = map(int, input().split())

# здесь продолжите программу
c = f(n) / (f(k) * f(n - k))
print(int(c))
