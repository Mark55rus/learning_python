""" Подвиг 7. Вводится натуральное число n. С помощью цикла for найти все
делители этого числа. Найденные делители выводить сразу в столбик без
формирования списка."""

n = int(input())
for i in range(1, n + 1):
    if not n % i:
        print(i)
