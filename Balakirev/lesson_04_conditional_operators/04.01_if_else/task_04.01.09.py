""" Подвиг 8. Вводятся четыре целых числа a, b, c, d в одну строку через
пробел. Определить, войдет ли в конверт с внутренними размерами a и b мм
прямоугольная открытка с размерами с и d мм. Для размещения открытки в
конверте необходим зазор в 1 мм с каждой стороны. Открытку можно поворачивать
на 90 градусов. Вывести ДА, если входит и НЕТ - если не входит."""

a, b, c, d = map(int, input().split())
if a >= c + 2 and b >= d + 2 or a >= d + 2 and b >= c + 2:
    print("ДА")
else:
    print("НЕТ")
