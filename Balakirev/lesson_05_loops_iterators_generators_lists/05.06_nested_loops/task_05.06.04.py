""" Подвиг 3. Вводится натуральное число n. Необходимо найти все простые числа,
которые меньше этого числа n, то есть, в диапазоне [2; n). Результат вывести на
экран в строчку через пробел."""

n = int(input())
for i in range(2, n):
    count = 0
    for j in range(2, i + 1):
        if i % j == 0:
            count += 1
    if count == 1:
        print(i, end=' ')
