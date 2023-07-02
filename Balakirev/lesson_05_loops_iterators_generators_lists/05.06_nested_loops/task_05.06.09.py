""" Подвиг 8. В некоторой стране используются денежные купюры достоинством в 1,
2, 4, 8, 16, 32 и 64. Вводится натуральное число n. Как наименьшим количеством
таких денежных купюр можно выплатить сумму n? Вывести на экран список купюр для
формирования суммы n (в одну строчку через пробел, начиная с наибольшей и
заканчивая наименьшей). Предполагается, что имеется достаточно большое
количество купюр всех достоинств."""

n = int(input())
coin = [1, 2, 4, 8, 16, 32, 64]
for i in range(len(coin) - 1, -1, -1):
    while n >= coin[i]:
        print(coin[i], end=' ')
        n -= coin[i]
