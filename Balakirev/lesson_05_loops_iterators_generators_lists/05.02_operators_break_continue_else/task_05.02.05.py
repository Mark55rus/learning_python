""" Подвиг 4. Вводится список названий городов в одну строчку через пробел.
Определить, что в этом списке все города имеют длину более 5 символов.
Реализовать программу с использованием цикла while и оператора break. Вывести
ДА, если условие выполняется и НЕТ - в противном случае."""

cities = input().split()
i = 0
while i < len(cities):
    if len(cities[i]) < 5:
        print("НЕТ")
        break
    i += 1
else:
    print("ДА")
