""" На свой день рождения Петя купил красивый и вкусный торт, который имел идеально круглую форму. Петя не знал, сколько
гостей придет на его день рождения, поэтому вынужден был разработать алгоритм, согласно которому он сможет быстро
разрезать торт на N равных частей. Следует учесть, что разрезы торта можно производить как по радиусу, так и по
диаметру.
    Помогите Пете решить эту задачу, определив наименьшее число разрезов торта по заданному числу гостей.
Входные данные:
    Программа получает на вход натуральное число N – число гостей, включая самого виновника торжества
Выходные данные:
    Выведите минимально возможное число разрезов торта."""

n = int(input())
if n > 1:
    if n % 2 == 0:
        print(n // 2)
    else:
        print(n)
else:
    print(0)
