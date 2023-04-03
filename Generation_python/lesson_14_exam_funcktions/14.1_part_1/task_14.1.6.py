"""Биномиальный коэффициент 🌶️.
Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов два натуральных числа n и k и возвращает
    значение биномиального коэффициента, равного n! / (k! * (n - k)!)
Примечание 1. Факториалом натурального числа n, называется произведение всех натуральных чисел от 1 до n, то есть
n! = 1 * 2 * 3 * … * n
Примечание 2. Реализуйте вспомогательную функцию factorial(n), вычисляющую факториал числа или воспользуйтесь уже
готовой функцией из модуля math."""

from math import factorial


def compute_binom(n, k):
    factorial_n = factorial(n)
    factorial_k = factorial(k)
    factorial_n_k = factorial(n - k)
    return factorial_n // (factorial_k * factorial_n_k)


print(compute_binom(int(input()), int(input())))
