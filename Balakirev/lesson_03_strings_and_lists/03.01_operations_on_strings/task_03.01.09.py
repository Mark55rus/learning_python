""" Подвиг 8. Выполняется считывание двух целочисленных значений в
переменные a и b (вводятся в одну строчку через пробел). Необходимо
сформировать строку вида: "Переменная a = <значение>, переменная b =
<значение>", используя оператор конкатенации (соединения) строк. Результат
выведите на экран.
    P.S. F-строки в программе не использовать."""

a, b = map(int, input().split())
print("Переменная a = " + str(a) + ", переменная b = " + str(b))
