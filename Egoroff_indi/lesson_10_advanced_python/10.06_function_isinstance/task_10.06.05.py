""" Ваша задача написать функцию count_strings, которая принимает произвольное количество аргументов. Функция должна
среди всех переданных значений найти только строки, найти их количество и  вернуть в качестве результата.
    Ниже представлены примеры:
count_strings(1, 2, 'hello', [2, 3, 4], True) => 1
count_strings('am', 'world', 'hello', 'is') => 4
count_strings() => 0
count_strings(True, False) => 0
Ваша задача написать только определение функции count_strings"""


def count_strings(*args) -> int:
    return sum(1 for v in args if isinstance(v, str))


assert count_strings(1, 2, 'hello', [2, 3, 4], True) == 1
assert count_strings('am', 'world', 'hello', 'is') == 4
assert count_strings() == 0
assert count_strings(True, False) == 0
print('Process finished')
