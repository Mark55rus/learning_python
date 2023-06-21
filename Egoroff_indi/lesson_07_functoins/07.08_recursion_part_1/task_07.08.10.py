""" Числа Трибоначчи.
    Описать рекурсивную функцию tribonacci, которая принимает на вход целое число n - порядковый номер чисел Трибоначчи.
Функция по параметру n должна вычислить и вернуть значение, стоящее на n-м месте в ряде чисел Трибоначчи"""


def tribonacci(n):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


assert tribonacci(0) == 0
assert tribonacci(2) == 1
assert tribonacci(4) == 2
assert tribonacci(6) == 7
assert tribonacci(7) == 13
print('Process finished')
