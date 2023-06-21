""" Двойной факториал.
    Описать рекурсивную функцию double_fact, которая принимает на вход целое число и вычисляет значение двойного
факториала по формуле:
double_fact(7) => 105
double_fact(4) => 8
double_fact(1) => 1
double_fact(10) => 3840
    Ваша задача только написать определение функции double_fact"""


def double_fact(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return n * double_fact(n-2)

assert double_fact(7) == 105
assert double_fact(4) == 8
assert double_fact(1) == 1
assert double_fact(10) == 3840
assert double_fact(6) == 48
assert double_fact(5) == 15
assert double_fact(2) == 2
print('OK')
