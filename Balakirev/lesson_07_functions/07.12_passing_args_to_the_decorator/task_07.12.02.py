""" Подвиг 1. Вводится строка целых чисел через пробел. Напишите функцию,
которая преобразовывает эту строку в список чисел и возвращает их сумму.

Определите декоратор для этой функции, который имеет один параметр start -
начальное значение суммы. Примените декоратор со значением start=5 к функции
и вызовите декорированную функцию для введенной строки s:

s = input()

Результат отобразите на экране."""

from functools import wraps


def args_decorator(start=5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal start
            start += func(*args, *kwargs)
            return start

        return wrapper

    return decorator


@args_decorator()
def addition(text):
    lst = list(map(int, text.split()))
    return sum(lst)


s = input()
print(addition(s))
