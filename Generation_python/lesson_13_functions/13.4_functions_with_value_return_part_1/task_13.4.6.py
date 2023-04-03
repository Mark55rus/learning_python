"""Количество дней.
Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней
    в данном месяце.
Примечание 1. Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.
Примечание 2. Считайте, что год является невисокосным.
Примечание 3. Следующий программный код:
print(get_days(1))
print(get_days(2))
print(get_days(9))
должен выводить:
31
28
30"""


def get_days(month):
    if month == 2:
        return 28
    elif month % 2 == 0:
        if month > 7:
            return 31
        else:
            return 30
    else:
        if month <= 7:
            return 31
        else:
            return 30
    pass


print(get_days(int(input())))
