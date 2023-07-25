""" Подвиг 6. Вводится целое положительное число a. Необходимо определить
генератор, который бы возвращал модули чисел в диапазоне [-a; a], а затем
еще один, который бы вычислял кубы чисел (возведение в степень 3),
возвращаемых первым генератором.

Вывести в одну строчку через пробел первые четыре значения. (Полагается,
что генератор выдает, как минимум четыре значения)."""

# variant with decorator:
from functools import wraps


def get_cube(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result_cube = (i ** 3 for i in func(*args, **kwargs))
        return result_cube

    return wrapper


@get_cube
def get_module(a):
    result_module = (abs(i) for i in range(-a, a + 1))
    return result_module


a = int(input())
gen = get_module(a)
print(*[next(gen) for _ in range(4)])
# or
# print(*list(get_module(a))[:4])

# variant 2:
# a = int(input())
# gen = (j ** 3 for j in (abs(i) for i in range(-a, a + 1)))
# print(*[next(gen) for _ in range(4)])
