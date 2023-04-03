""" Число словами 🌶️.
Напишите функцию number_to_words(num), которая принимает в качестве аргумента натуральное число num и возвращает его
    словесное описание на русском языке.
Примечание 1. Считайте, что число 1 ≤ num ≤ 99.
Примечание 2. Следующий программный код:
print(number_to_words(7))
print(number_to_words(85))
должен выводить:
семь
восемьдесят пять"""


def number_to_words(num):
    lst1 = [None, 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
            'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
            'девятнадцать']
    lst2 = [None, None, 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
            'девяносто']
    if 1 <= num <= 19:
        return lst1[num]
    elif num % 10 == 0:
        return lst2[num // 10]
    else:
        return lst2[num // 10] + ' ' + lst1[num % 10]


print(number_to_words(int(input())))
