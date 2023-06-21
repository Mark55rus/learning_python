""" Напишите функцию list_sum_recursive, которая принимает на вход список из целых чисел и возвращает сумму элементов
переданного списка. Не забывайте, что реализовать это нужно при помощи рекурсии.

Ваша задача только написать определение функции list_sum_recursive"""


def list_sum_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + list_sum_recursive(lst[1:])


print(list_sum_recursive([1, 2, 3]))
