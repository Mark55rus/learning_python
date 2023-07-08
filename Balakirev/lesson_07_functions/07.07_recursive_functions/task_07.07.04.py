""" Подвиг 3. Вводится список целых чисел в одну строчку через пробел.
Необходимо вычислить сумму этих введенных значений, используя рекурсивную
функцию (для перебора элементов списка) с именем get_rec_sum. Функция должна
возвращать значение суммы. (Выводить на экран она ничего не должна).

Вызовите эту функцию и выведите вычисленное значение суммы на экран."""


def get_rec_sum(lst: list):
    if not lst:
        return 0
    return lst[0] + get_rec_sum(lst[1:])


value = list(map(int, input().split()))
print(get_rec_sum(value))


# variant 2:
# lst1 = [int(i) for i in input().split()]
#
# def get_rec_sum(lst):
#     head, *tail = lst
#     return head + get_rec_sum(tail) if tail else head
#
# print(get_rec_sum(lst1))
