""" Та же самая задача, необходимо найти НОД двух чисел, только теперь нужно модернизировать свой код при помощи
нахождения остатка от деления"""

a, b = map(int, input().split())
while b > 0:
    a, b = b, a % b
print(a)