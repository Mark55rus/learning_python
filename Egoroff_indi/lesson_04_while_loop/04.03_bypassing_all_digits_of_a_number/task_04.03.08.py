""" Программа принимает на вход одно натуральное число и выводит на экран произведение цифр данного числа"""

n = int(input())
count = 1
while n > 0:
    count *= n % 10
    n //= 10
print(count)
