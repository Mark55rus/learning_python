""" Напишите функцию count_args, которая принимает произвольное количество аргументов. Данная функция должна возвращать
количество переданных ей на вход аргументов.
    Вам необходимо написать только определение функции count_args"""


def count_args(*args):
    count = len(args)
    return count


assert count_args(1, 2, 3) == 3
assert count_args(1, 3) == 2
assert count_args(2) == 1
assert count_args() == 0
print('Process finished')
