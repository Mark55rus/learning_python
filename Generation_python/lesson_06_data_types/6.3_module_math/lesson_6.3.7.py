"""Квадратное уравнение 🌶️🌶️.
Даны три вещественных числа a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения
ax ** 2 + bx + c = 0.
Формат входных данных
На вход программе подается три вещественных числа a != 0,b,c, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести вещественные корни уравнения если они существуют или текст «Нет корней» в противном случае.
Примечание. Если уравнение имеет два корня, то следует вывести их в порядке возрастания."""

from math import sqrt

a, b, c = [float(input()) for _ in range(3)]
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    x1 = (-b - sqrt(discriminant)) / (2 * a)
    x2 = (-b + sqrt(discriminant)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
elif discriminant == 0:
    print(-(b / (2 * a)))
else:
    print('Нет корней')
