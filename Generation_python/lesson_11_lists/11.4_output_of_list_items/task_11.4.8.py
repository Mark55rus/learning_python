"""Negatives, Zeros and Positives.
На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая сначала выводит все
 отрицательные числа, затем нули, а затем все положительные числа, каждое на отдельной строке. Числа должны быть
 выведены в том же порядке, в котором они были введены.
Формат входных данных
На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи."""

initial_list = [int(input()) for _ in range(int(input()))]
negative_list = []
positive_list = []
zero_list = []
for i in initial_list:
    if i > 0:
        positive_list.append(i)
    elif i < 0:
        negative_list.append(i)
    else:
        zero_list.append(i)
print(*negative_list + zero_list + positive_list, sep='\n')
