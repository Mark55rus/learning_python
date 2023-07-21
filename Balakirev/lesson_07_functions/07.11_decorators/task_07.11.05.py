""" Подвиг 4. Вводятся две строки из слов (слова записаны через пробел).
Объявите функцию, которая преобразовывает эти две строки в два списка слов и
возвращает эти списки.
Определите декоратор для этой функции, который из двух списков формирует
словарь, в котором ключами являются слова из первого списка, а значениями -
соответствующие элементы из второго списка. Полученный словарь должен
возвращаться при вызове декоратора.
Примените декоратор к первой функции и вызовите ее для введенных строк.
Результат (словарь d) отобразите на экране командой:
print(*sorted(d.items()))"""


def decorator(func):
    def wrapper(*args, **kwargs):
        result: list = func(*args, **kwargs)
        temporary_dict = {}
        for i in range(len(result[0])):
            temporary_dict[result[0][i]] = result[1][i]
        return temporary_dict

    return wrapper


@decorator
def make_lists(l1: str, l2: str):
    return l1.split(), l2.split()


dct = make_lists(input(), input())
print(*sorted(dct.items()))
