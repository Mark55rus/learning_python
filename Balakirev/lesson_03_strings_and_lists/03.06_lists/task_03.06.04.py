""" Подвиг 3. Вводятся три целых числа в одну строку через пробел. Сформируйте
список lst, хранящий эти значения в порядке их ввода. Результат выведите на
экран, используя команду:
print(lst)"""

lst = list(map(int, input().split()))
print(lst)
