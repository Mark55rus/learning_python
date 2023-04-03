"""Good password 🌶️.
Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password
    и возвращает значение True если пароль является надежным и False в противном случае.
Пароль является надежным если:
его длина не менее
8 символов;
он содержит как минимум одну заглавную букву (верхний регистр);
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
 Примечание. Следующий программный код:
print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))
должен выводить:
True
False"""


def is_password_good(password):
    count_upper = 0
    count_lower = 0
    count_digit = 0
    for c in password:
        if c.isupper():
            count_upper += 1
        elif c.islower():
            count_lower += 1
        elif c.isdigit():
            count_digit += 1
    if len(password) >= 8 and count_upper != 0 and count_lower != 0 and count_digit != 0:
        return True
    else:
        return False


print(is_password_good(input()))
