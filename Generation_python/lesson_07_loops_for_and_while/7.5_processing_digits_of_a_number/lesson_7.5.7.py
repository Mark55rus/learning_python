"""Все вместе.
Дано натуральное число. Напишите программу, которая вычисляет:
сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке."""

num = int(input())
sum_of_numbers = 0
count_digits = 0
product_of_numbers = 1
arithmetic_mean = 0
first_digit = 0
last_digit_num = num % 10
while num > 0:
    last_digit = num % 10
    sum_of_numbers += last_digit
    count_digits += 1
    product_of_numbers *= last_digit
    if num < 10:
        first_digit = num
    num //= 10
print(sum_of_numbers)
print(count_digits)
print(product_of_numbers)
print(sum_of_numbers / count_digits)
print(first_digit)
print(first_digit + last_digit_num)