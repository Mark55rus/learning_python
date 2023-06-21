""" Напишите программу, которая печатает словарь alphabet, где ключи - строчные английские символы, а значения -
порядковые номера букв в алфавите начиная с 1.
Начало вашего словаря должны быть таким {"a": 1, "b": 2 ... }
В качестве ответа распечатайте полученный словарь alphabet
Весь английский алфавит можно взять в переменной ascii_lowercase из модуля string:"""

# variant 1:
from string import ascii_lowercase
count = 1
alphabet = {}
for i in ascii_lowercase:
    alphabet[i] = count
    count += 1
print(alphabet)

# variant 2:
from string import ascii_lowercase

alphabet = {ascii_lowercase[i]: i for i in range(26)}
print(alphabet)
