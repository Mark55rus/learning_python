""" Состязания.
    В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Победителем считается тот спортсмен, у
которого сумма результатов по всем броскам максимальна. Если перенумеровать спортсменов числами от 0 до n-1, а попытки
каждого из них – от 0 до m-1, то на вход программа получает массив A[n][m], состоящий из неотрицательных целых чисел.
Программа должна определить максимальную сумму чисел в одной строке и вывести на экран эту сумму и номер строки, для
которой достигается эта сумма.
    Входные данные:
Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке идет
n строк по m чисел, являющихся элементами массива.
    Выходные данные:
Программа должна вывести 2 числа: сумму и номер строки, для которой эта сумма достигается. Если таких строк несколько,
то выводится номер наименьшей из них. Не забудьте, что нумерация строк (спортсменов) начинается с 0."""

athletes, casts = map(int, input().split())
row = 0
total_row = 0
result = [list(map(int, input().split())) for _ in range(athletes)]
for i in range(athletes):
    total = 0
    for j in range(casts):
        total += result[i][j]
    if total > total_row:
        row = i
        total_row = total
print(total_row)
print(row)

