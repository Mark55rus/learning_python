""" На вход программе подается строка, состоящая из различных символов: буквы, цифры, знаки препинания и т.д. Ваша
задача определить сколько символов в данной строке являются цифрами и также найти сумму всех этих цифр. Например, в
строке "Комната 1408" содержится 4 цифры и их сумма равна 13.
    В качестве ответа необходимо через пробел вывести 2 числа - количество цифр в введенной строке и их сумму"""

# variant 1:
text = input()
count_digit = 0
total_digit = 0
for c in text:
    if c.isdigit():
        count_digit += 1
        total_digit += int(c)
print(count_digit, total_digit)

# variant 2:
text = [int(char) for char in input() if char.isdigit()]
print(len(text), sum(text))

