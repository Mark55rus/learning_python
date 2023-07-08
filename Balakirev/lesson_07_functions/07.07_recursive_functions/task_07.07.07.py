""" Подвиг 6. Имеется следующий многомерный список:

d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]],
7.89]
С помощью рекурсивной функции get_line_list создать на его основе
одномерный список из значений элементов списка d. Функция должна возвращать
новый созданный одномерный список.  (Только возвращать, выводить на экран
ничего не нужно.)
Вызывать функцию не нужно, только объявить со следующей сигнатурой:
def get_line_list(d,a=[]): ...
где d - исходный список; a - новый формируемый."""


def get_line_list(d: list, a=[]):
    if len(d) > 0:
        for elem in d:
            if isinstance(elem, list):
                get_line_list(elem, a)
            else:
                a.append(elem)
    return a


d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]],
     7.89]
print(get_line_list(d))
