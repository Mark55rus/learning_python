""" Программа получает на вход натуральное число n > 1. Выведите минимальный делитель этого числа, отличный от единицы.
К примеру для числа 12 делителями являются 1, 2, 3, 4, 6, 12. """

n = int(input())
i = 2
while i <= n:
    if n % i == 0:
        print(i)
        break
    i += 1
