""" Превращаем вложенный список в плоский.
    Представьте, что у нас есть список целых чисел неограниченной вложенности. То есть наш список может состоять из
списков, внутри которых также могут быть списки. Ваша задача превратить все это в линейный список при помощи функции
flatten.

flatten([1, [2, 3, [4]], 5]) => [1, 2, 3, 4, 5]
flatten([1, [2, 3], [[2], 5], 6]) => [1, 2, 3, 2, 5, 6]
flatten([[[[9]]], [1, 2], [[8]]]) => [9, 1, 2, 8]
Ваша задача только написать определение функции flatten"""


# variant 1:
# def flatten(lst: list):
#     flat_list = []
#     for elem in lst:
#         if isinstance(elem, list):
#             flat_list.extend(flatten(elem))
#         else:
#             flat_list.append(elem)
#     return flat_list
#
#
# assert flatten([1, [2, 3, [4]], 5]) == [1, 2, 3, 4, 5]
# assert flatten([1, [2, 3], [[2], 5], 6]) == [1, 2, 3, 2, 5, 6]
# assert flatten([[[[9]]], [1, 2], [[8]]]) == [9, 1, 2, 8]
# print('Process finished')


# variant 2:
def flat(lst: list):
    if len(lst) < 1:
        return []
    if isinstance(lst[0], list):
        return flat(lst[0]) + flat(lst[1:])
    return lst[:1] + flat(lst[1:])


assert flat([1, [2, 3, [4]], 5]) == [1, 2, 3, 4, 5]
assert flat([1, [2, 3], [[2], 5], 6]) == [1, 2, 3, 2, 5, 6]
assert flat([[[[9]]], [1, 2], [[8]]]) == [9, 1, 2, 8]
print('Process finished')
