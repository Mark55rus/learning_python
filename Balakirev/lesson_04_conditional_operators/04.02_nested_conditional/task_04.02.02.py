""" Подвиг 1. Имеется следующее меню:
m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''
В программе вводится целое число от 1 до 6. Нужно вывести пункт меню, связанный
 с этим числом. Реализовать программу с использованием операторов if-elif"""

num = int(input())
if num == 1:
    print("1. Введение в Python")
elif num == 2:
    print("2. Строки и списки")
elif num == 3:
    print("3. Условные операторы")
elif num == 4:
    print("4. Циклы")
elif num == 5:
    print("5. Словари, кортежи и множества")
elif num == 6:
    print("6. Выход")
