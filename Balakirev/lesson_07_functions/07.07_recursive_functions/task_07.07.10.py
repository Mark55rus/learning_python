""" Великий подвиг 8. Вводится список из целых чисел в одну строчку через
пробел. Необходимо выполнить его сортировку по возрастанию с помощью
алгоритма сортировки слиянием. Функция должна возвращать новый
отсортированный список. Вызовите результирующую функцию сортировки для
введенного списка и отобразите результат на экран в виде последовательности
чисел, записанных через пробел.

Подсказка. Для разбиения списка и его последующей сборки используйте
рекурсивные функции.
P.S. Теория сортировки в видео предыдущего шага."""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


lst_no_sort = list(map(int, input().split()))
print(*merge_sort(lst_no_sort))
