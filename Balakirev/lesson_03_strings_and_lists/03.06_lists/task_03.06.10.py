""" Подвиг 9. Вводится число новых подписчиков канала по дням в одну строку
через пробел. На основе введенной строки необходимо сформировать список из
целых чисел. Затем, вывести на экран максимальное, минимальное и суммарное
значения этого списка через пробел."""

lst = list(map(int, input().split()))
print(max(lst), min(lst), sum(lst))
