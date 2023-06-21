""" Программа принимает на вход два целых числа a и b.
    Если a<=b необходимо сформировать список квадратов целых чисел на интервале от а до b включительно и вывести его на
экран.
    Если же a>b, необходимо сформировать список кубов целых чисел на интервале от a до b включительно, двигаясь в
порядке убывания, и затем вывести его.
Не забывайте пользоваться генератором списков """

a, b = map(int, input().split())
print([i ** 2 if a <= b else i ** 3 for i in (range(a, b) if a <= b else range(a, b - 1, -1))])
