""" Состязания - 4.
    В метании молота состязается athletes спортcменов. Каждый из них сделал casts бросков. Победитель определяется по лучшему
результату. Определите количество участников состязаний, которые разделили первое место, то есть определите количество
строк в массиве, которые содержат значение, равное наибольшему.
    Входные данные:
Программа получает на вход два числа athletes и casts, являющиеся числом строк и столбцов в массиве. Далее во входном потоке идет
athletes строк по casts чисел, являющихся элементами массива.
    Выходные данные:
Программа должна вывести одно число - количество победителей соревнования."""

athletes, casts = map(int, input().split())
results = [list(map(int, input().split())) for _ in range(athletes)]
max_cast = 0
count = 0
for i in range(athletes):
    max_cast_temp = 0
    for j in range(casts):
        if results[i][j] > max_cast_temp:
            max_cast_temp = results[i][j]
    if max_cast_temp > max_cast:
        max_cast = max_cast_temp
        count = 1
    elif max_cast_temp == max_cast:
        count += 1
print(count)
