"""Цифровой корень.
На вход программе подается натуральное число n. Напишите программу, которая находит цифровой корень данного числа.
Цифровой корень числа n получается следующим образом: если сложить все цифры этого числа, затем все цифры найденной
суммы и повторить этот процесс, то в результате будет получено однозначное число (цифра), которое и называется цифровым
корнем данного числа.
Формат входных данных
На вход программе подается одно натуральное число.
Формат выходных данных
Программа должна вывести цифровой корень введенного числа.
Примечание. Используйте вложенные циклы while."""

num = int(input())
while num > 9:
    count = 0
    while num > 0:
        last_digit = num % 10
        count += last_digit
        num //= 10
    else:
        num = count
else:
    print(num)
