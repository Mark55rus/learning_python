""" Состязания - 3.
    В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Побеждает спортсмен, у которого
максимален наилучший бросок. Если таких несколько, то из них побеждает тот, у которого наилучшая сумма результатов по
всем попыткам. Если и таких несколько, победителем считается спортсмен с минимальным номером. Определите номер
победителя соревнований.
    Входные данные:
Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке идет n
строк по m чисел, являющихся элементами массива.
    Выходные данные:
Программа должна вывести одно число - номер победителя соревнований. Не забудьте, что  строки  (спортсмены) нумеруются
с 0."""

athletes, casts = map(int, input().split())
max_cast = 0
total_cast = 0
number_athlete = 0
results = [list(map(int, input().split())) for _ in range(athletes)]
for i in range(athletes):
    total_cast_temp = 0
    max_cast_temp = 0
    for j in range(casts):
        total_cast_temp += results[i][j]
        if results[i][j] > max_cast_temp:
            max_cast_temp = results[i][j]
    if max_cast_temp > max_cast:
        max_cast = max_cast_temp
        total_cast = total_cast_temp
        number_athlete = i
    elif max_cast_temp == max_cast:
        if total_cast_temp > total_cast:
            total_cast = total_cast_temp
            number_athlete = i
print(number_athlete)
