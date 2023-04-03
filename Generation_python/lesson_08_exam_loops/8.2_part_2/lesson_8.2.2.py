"""Ревью кода - 8 🌶️.
На обработку поступает последовательность из 8 целых чисел. Известно, что вводимые числа по абсолютной величине
не превышают 10 ** 12.
Нужно написать программу, которая выводит на экран количество делящихся нацело на 4 чисел в исходной последовательности
и максимальное делящееся нацело на 4 число. Если делящихся нацело на 4 чисел нет, требуется на экран вывести «NO».
Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только
одну строку и может быть исправлена без изменения других строк.
Примечание. Обратите внимание, что требуется найти ошибки в имеющейся программе, а не написать свою, возможно,
использующую другой алгоритм решения.

n = 7
count = 0
maximum = 1000
for i in range(1, n + 1):
    x = int(input())
    if x // 4 == 0:
        count += 1
        if x < maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')"""

n = 8
count = 0
maximum = -10 ** 6
for i in range(n):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if maximum < x:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
