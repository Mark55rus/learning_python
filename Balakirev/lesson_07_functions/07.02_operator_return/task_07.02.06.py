""" Подвиг 5. Объявите функцию для проверки числа на нечетность (
возвращается True, если переданное число нечетное и False, если число четное).
После объявления функции прочитайте (с помощью функции input) список целых
значений, записанных в одну строку через пробел. И, используя генератор
списков и созданную функцию, сформируйте список из нечетных значений на
основе введенного исходного списка. Результат отобразите на экране командой:
print(*lst)
где lst - сформированный список из нечетных значений."""


def is_odd(x):
    return x % 2


lst = [int(i) for i in input().split() if is_odd(int(i))]
print(*lst)
