""" Подвиг 5. Вводится список email-адресов в одну строчку через пробел.
Среди них нужно оставить только корректно записанные адреса. Будем полагать,
что к таким относятся те, что используют латинские буквы, цифры и символ
подчеркивания. А также в адресе должен быть символ "@", а после него символ
точки "." (между ними, конечно же, могут быть и другие символы).

Результат отобразить в виде строки email-адресов, записанных через пробел."""

from string import ascii_letters, digits


def filter_func(x: str):
    chars = ascii_letters + digits + '@' + '.' + '_'
    if '@' not in x:
        return False
    if x.rfind("@") > x.rfind("."):
        return False
    for char in x:
        if char not in ascii_letters + chars:
            return False
    return True


lst = input().split()
filter_email = filter(filter_func, lst)
print(*filter_email)
