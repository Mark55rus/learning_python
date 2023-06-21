""" Определите функцию print_from, которая принимает одно натуральное число n и распечатывает на экране убывающую
последовательность целых чисел от n до 1 включительно. Каждое число необходимо выводить на отдельной строке.
    Ваша задача только написать определение функции print_from"""


def print_from(n):
    if n > 0:
        print(n)
        return print_from(n - 1)


print_from(6)

# Пример как работает рекурсия:
# def print_from(n: int) -> None:
#     global depth
#     if n > 0:
#         depth += 1
#         print(f'ПРЯМОЙ ХОД {n = }, {depth =}')
#         print_from(n - 1)
#         depth -= 1
#         print(f'ОБРАТНЫЙ ХОД {n = }, {depth =}')
#
# print_from(10)
