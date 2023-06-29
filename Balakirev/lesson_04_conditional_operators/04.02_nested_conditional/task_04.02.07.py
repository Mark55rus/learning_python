""" Подвиг 6. Дата некоторого дня характеризуется двумя натуральными числами:
m (порядковый номер месяца) и n (число). По введенным m и n (в одну строку
через пробел) определить:
а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).
В задаче принять, что год не является високосным. Вывести предыдущую дату и
следующую дату (в формате: mm.dd, где m - число месяца; d - номер дня) в одну
строчку через пробел.
P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31,
30, 31, 30, 31, 31, 30, 31, 30, 31"""

m, n = map(int, input().split())
lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if n == 1:
    print(f"{m - 1:02}.{lst[m - 2]} {m:02}.{n + 1:02}")
elif n == lst[m - 1]:
    print(f"{m:02}.{n - 1} {m + 1:02}.{1:02}")
else:
    print(f"{m:02}.{n - 1:02} {m:02}.{n + 1:02}")
