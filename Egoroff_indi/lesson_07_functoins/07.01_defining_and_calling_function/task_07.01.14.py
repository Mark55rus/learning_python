""" Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат
проверки.
Сложным паролем будет считаться комбинация символов, в которой:
- Есть хотя бы 3 цифры
- Есть хотя бы одна заглавная буква
- Есть хотя бы один символ из следующего набора "!@#$%*"
- Общая длина не менее 10 символов
Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае -
"Easy peasy"

Вам необходимо написать только определение функции check_password"""


def check_password(password: str):
    count_digit = 0
    count_uppercase = 0
    count_symbol = 0
    for sign in password:
        if sign.isdigit():
            count_digit += 1
        elif sign.isupper():
            count_uppercase += 1
        elif sign in "!@#$%*":
            count_symbol += 1
    if count_digit >= 3 and count_uppercase >= 1 and count_symbol != 0 and len(password) >= 10:
        print("Perfect password")
    else:
        print("Easy peasy")
