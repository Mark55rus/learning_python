"""Суммы двух
На вход программе подается натуральное число n ≥ 2, а затем n целых чисел.
Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел
(0 и 1, 1 и 2, 2 и 3 и т.д.).
Формат входных данных
На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести список, состоящий из сумм соседних чисел."""

lst = [int(input()) for i in range(int(input()))]
new_lst = []
for i in range(len(lst) - 1):
    new_lst.append(lst[i] + lst[i + 1])
print(new_lst)
