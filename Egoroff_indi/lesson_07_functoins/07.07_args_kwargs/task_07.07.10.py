""" Напишите функцию multiply, которая принимает произвольное количество числовых аргументов. Данная функция должна
находить произведение всех переданных значений и возвращать его в качестве результата
    Вам необходимо написать только определение функции multiply"""


def multiply(*args: int):
    prod = 1
    for i in args:
        prod *= i
    return prod


assert multiply(1, 2, 3) == 6
assert multiply(1, 3) == 3
assert multiply(2) == 2
assert multiply() == 1
print('Process finished')
