"""Змеиный регистр.
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и
    преобразует его в «змеиный регистр».
Примечание 1. Почитать подробнее о стилях именования можно тут.
Примечание 2. Следующий программный код:
print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))
должен выводить:
this_is_camel_cased
is_prime_number"""


def convert_to_python_case(text):
    this_is_snake_cased = ''
    for i in range(len(text)):
        if text[i].isupper() and i != 0:
            this_is_snake_cased += '_' + text[i].lower()
        else:
            this_is_snake_cased += text[i].lower()
    return this_is_snake_cased


print(convert_to_python_case(input()))

