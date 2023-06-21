""" Напишите функцию is_between, которая принимает три аргумента и печатает True, если первое число находится между
двумя вторыми включительно, и False в противном случае.
Ваша задача дописать только тело функции is_between"""


def is_between(name, surname, middlename):
    print(True if surname <= name <= middlename or middlename <= name <= surname else False)
