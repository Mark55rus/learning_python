""" Программа принимает на вход одно натуральное число и выводит на экран минимальную и максимальную цифры данного числа
в отдельных строчках"""

n = int(input())
largest = 0
smallest = 10
while n > 0:
    if n % 10 > largest:
        largest = n % 10
    if n % 10 < smallest:
        smallest = n % 10
    n //= 10
print(smallest)
print(largest)
