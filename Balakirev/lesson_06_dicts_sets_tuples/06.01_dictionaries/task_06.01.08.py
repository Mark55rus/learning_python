""" Подвиг 7. Вводятся номера телефонов в одну строчку через пробел с разными
кодами стран: +7, +6, +2, +4 и т.д. Необходимо составить словарь d, где ключи -
это коды +7, +6, +2 и т.п., а значения - список номеров (следующих в том же
порядке, что и во входной строке) с соответствующими кодами. Полученный словарь
вывести командой:
print(*sorted(d.items()))"""

lst = input().split()
d = {}
for i in lst:
    if i[0:2] not in d:
        d[i[0:2]] = [i]
    else:
        d[i[0:2]].append(i)
print(*sorted(d.items()))
