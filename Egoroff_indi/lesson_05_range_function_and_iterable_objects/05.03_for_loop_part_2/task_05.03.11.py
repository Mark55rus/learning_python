""" Делимость на 11.
    Для делимости числа на 11 необходимо, чтобы разность между суммой цифр, стоящих на четных местах, и суммой цифр,
стоящих на нечетных местах, делилась на 11. Требуется написать программу, которая проверит делимость заданного числа на
11.
    Входные данные:
Программа получает на вход одно натуральное число N, делимость которого надо проверить (1 ≤ N ≤ 1010000).
    Выходные данные:
Выведите “YES”, если число делится на 11, или “NO” иначе."""

lst = list(map(int, input()))
total_even = 0
total_odd = 0
for i in range(len(lst)):
    if i % 2 == 0:
        total_even += lst[i]
    else:
        total_odd += lst[i]
if abs(total_even - total_odd) % 11 == 0:
    print('YES')
else:
    print('NO')
