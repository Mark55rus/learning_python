"""Даны три натуральных числа a, b, c записанные в отдельных строках. Ваша задача определить, существует ли треугольник
с такими сторонами.
    Для этого вспоминаем теорему о существовании треугольника. Она утверждает, что треугольник существует, если сумма
любых двух сторон больше оставшейся третьей.
    Выведите строку YES, если условие теоремы выполняется, иначе выведите строку NO."""

a, b, c = [int(input()) for _ in range(3)]
if a + b > c and b + c > a and c + a > b:
    print('YES')
else:
    print('NO')
