""" Даны два натуральных числа A и B. Требуется найти их наименьшее общее кратное (НОК)."""

a, b = map(int, input().split())
nok_a, nok_b = a, b
while b > 0:
    a, b = b, a % b
print(nok_a * nok_b // a)
