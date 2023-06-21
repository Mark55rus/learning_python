""" Калькулятор своими руками.
    Напишите программу, которая считывает с клавиатуры два вещественных числа, а затем строку. Если эта строка является
обозначением одной из четырёх основных математических операций (+, -, * или /), то выведите результат применения этой
операции к введенным ранее числам, в противном случае выведите «Неизвестно». Также «Неизвестно» следует вывести, если
пользователь захочет поделить на ноль.
    Входные данные:
Два вещественных числа в каждой отдельной строчки. На третьей строке вводится символ операции.
    Выходные данные:
Необходимо посчитать значение операции «+», «-», «*», «/». Если ввели символ, который не относится к данным операциям,
необходимо вывести «Неизвестно». «Неизвестно» также выводится при попытке деления на ноль"""

x, y, s = float(input()), float(input()), input()
if s in '+-*/':
    if s == '+':
        print(x + y)
    elif s == '-':
        print(x - y)
    elif s == '*':
        print(x * y)
    elif s == '/':
        if y != 0:
            print(x / y)
        else:
            print('Неизвестно')
else:
    print('Неизвестно')
