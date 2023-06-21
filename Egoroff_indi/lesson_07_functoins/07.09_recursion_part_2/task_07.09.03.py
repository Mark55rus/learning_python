""" Сортировка слиянием (merge sort).
    Есть несколько типов сортировки, которые используют рекурсию. Одна из них называется сортировка слиянием.
    Ваша задача реализовать этот алгоритм. Для этого нужно будет создать функцию merge_sort, которая будет принимать
исходный список и возвращать новый отсортированный в порядке неубывания список.
    Также для реализации функции merge_sort вам понадобится реализовать функцию merge_two_list. Функция merge_two_list
должна принимать два отсортиванных по неубыванию списка, сливать их в один большой список также отсортированный по
неубыванию (задача Слияние списков ) и возвращать его.
    Ваша задача написать только определение функций merge_sort и merge_two_list, при этом нельзя пользоваться
встроенными сортировками в Python"""


# функция merge_two_list должна объединить два списка
def merge_two_list(a: list, b: list):
    sort_list = []
    a.extend(b)
    while len(a) > 0:
        sort_list.append(min(a))
        a.remove(min(a))
    return sort_list


# функция merge_sort должна выполнить сортировку
def merge_sort(s):
    if len(s) <= 1:
        return s

        # Рекурсивно разбиваем список на две половины и сортируем их
    mid = len(s) // 2
    left_half = s[:mid]
    right_half = s[mid:]
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Объединяем две отсортированные половины в один отсортированный список
    return merge_two_list(left_sorted, right_sorted)


x = list(map(int, input().split()))
y = list(map(int, input().split()))
print(merge_sort(x + y))