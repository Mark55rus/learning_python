"""Подвиг 9. Вводится список целых чисел в одну строчку через пробел.
Необходимо задать функцию, которая принимает два аргумента (максимальное и
минимальное значения из списка) и возвращает их произведение. Вызовите эту
функцию и отобразите на экране полученное числовое значение.
Подсказка: для передачи аргументов функции используйте функции max и min для
введенного списка чисел."""


def product_min_max(largest, smallest):
    return largest * smallest


lst = list(map(int, input().split()))
print(product_min_max(max(lst), min(lst)))
