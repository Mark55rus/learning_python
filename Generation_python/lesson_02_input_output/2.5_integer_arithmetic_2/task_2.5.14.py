"""Перестановка цифр
Дано трехзначное число abc, в котором все цифры различны. Напишите программу, которая выводит шесть чисел,
образованных при перестановке цифр заданного числа.
Формат входных данных
На вход программе подаётся положительное трёхзначное целое число, все цифры которого различны.
Формат выходных данных
Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа в следующем порядке:
abc,acb,bac,bca,cab,cba."""

num = int(input())
a_first_digit = num // 100
b_second_digit = num // 10 % 10
c_last_digit = num % 10
print(a_first_digit, b_second_digit, c_last_digit, sep='')
print(a_first_digit, c_last_digit, b_second_digit, sep='')
print(b_second_digit, a_first_digit, c_last_digit, sep='')
print(b_second_digit, c_last_digit, a_first_digit, sep='')
print(c_last_digit, a_first_digit, b_second_digit, sep='')
print(c_last_digit, b_second_digit, a_first_digit, sep='')
