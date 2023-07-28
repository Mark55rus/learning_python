""" Подвиг 4. Вводится строка из слов, записанных через пробел. Необходимо
на их основе составить прямоугольную таблицу из трех столбцов и N строк (
число строк столько, сколько получится). Лишнее (выходящее) слово -
отбросить. Реализовать эту программу с использованием функции zip. Результат
отобразить на экране в виде прямоугольной таблицы из слов, записанных через
пробел (в каждой строчке)."""

lst = input().split()
z = zip(*[iter(lst)] * 3)
for i in z:
    print(*i)

# primary variant
# lst = input().split()
# lst_multiple_3 = lst[:len(lst) - len(lst) % 3]
# count = 0
# new_lst = []
# while count < len(lst_multiple_3):
#     temple = []
#     for j in range(3):
#         temple.append(lst_multiple_3[count])
#         count += 1
#     new_lst.append(temple)
# z = zip(*new_lst)
# new_z = zip(*z)
# for i in new_z:
#     print(*i)
