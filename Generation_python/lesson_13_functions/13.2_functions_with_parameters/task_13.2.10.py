"""Сумма цифр.
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр."""


def print_digit_num(num):
    print(sum(num))


lst = [int(i) for i in input()]
print_digit_num(lst)
