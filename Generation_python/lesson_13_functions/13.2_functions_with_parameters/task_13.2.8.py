"""Звездный треугольник.
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
fill – символ заполнитель;
base – величина основания равнобедренного треугольника;
а затем выводит его.
Примечание. Гарантируется, что основание треугольника – нечетное число.
Тестовые данные 🟢"""


def draw_triangle(fill, base):
    for i in range(1, base + 1):
        for j in range(i):
            if i + j <= base:
                print(fill, end='')
        print()
    pass


sign, n = input(), int(input())
draw_triangle(sign, n)
