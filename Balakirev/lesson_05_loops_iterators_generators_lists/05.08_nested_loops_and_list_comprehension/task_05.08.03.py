"""Подвиг 2. Вводится список целых чисел в строку через пробел. С помощью
list comprehension сформировать из них двумерный список lst размером N x N (
квадратную таблицу чисел). Гарантируется, что из набора введенных чисел
можно сформировать квадратную матрицу (таблицу). Результат отобразить в виде
списка командой:
print(lst)"""

lst = list(map(int, input().split()))
length = int(len(lst) ** 0.5)
print([[lst[length * i + j] for j in range(length)] for i in range(length)])

# variant 2:
# lst = list(map(int, input().split()))
# length = int((len(lst) ** 0.5))
# it = iter(lst)
# lst = [[next(it) for _ in range(length)] for _ in range(length)]
# print(lst)

# variant 3:
# lst = list(map(int, input().split()))
# length = int((len(lst) ** 0.5))
# lst = [lst[i:i + length] for i in range(0, len(lst), length)]
# print(lst)
