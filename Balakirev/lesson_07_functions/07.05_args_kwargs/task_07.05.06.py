""" Подвиг 5. Объявите функцию с именем get_data_fig для вычисления
периметра произвольного N-угольника. На вход этой функции передаются N длин
сторон через аргументы. Дополнительно могут быть указаны именованные аргументы:
type - булево значение True/False
color - целое числовое значение
closed - булево значение True/False
width - целое значение
Функция должна возвращать в виде кортежа периметр многоугольника и указанные
значения именованных параметров в порядке их перечисления в тексте задания (
если они были переданы). Если какой-либо параметр отсутствует,
его возвращать не нужно (пропустить).
Функцию выполнять не нужно, только определить."""


def get_data_fig(*args, **kwargs):
    lst = [sum(args)]
    for i in ['type', 'color', 'closed', 'width']:
        if i in kwargs:
            lst.append(kwargs[i])
    return tuple(lst)


# variant 2:
# def get_data_fig(*args, **kwargs):
#     kwargs = [kwargs[i] for i in ['type', 'color', 'closed', 'width'] if
#               i in kwargs]
#     return (sum(args), *kwargs)


assert get_data_fig(5, 4, 9, 9, 9, 9, type=False, color='Yellow', closed=True,
                    width=10) == (45, False, 'Yellow', True, 10)
assert get_data_fig(5, 4, 9, 9, 9, 9, color='Yellow', type=False, closed=True,
                    width=10) == (45, False, 'Yellow', True, 10)
assert get_data_fig(5, 4, color='Yellow', type=False, closed=True) == (
    9, False, 'Yellow', True)
print("OK")

print(get_data_fig(5, 4, 9, 9, 9, 9, type=False, color='Yellow', closed=True,
                   width=10))
print(get_data_fig(5, 4, 9, 9, 9, 9, color='Yellow', type=False, closed=True,
                   width=10))
print(get_data_fig(5, 4, color='Yellow', type=False, closed=True))
