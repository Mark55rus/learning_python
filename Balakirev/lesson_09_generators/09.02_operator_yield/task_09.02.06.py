""" Подвиг 5. Определите функцию-генератор, которая бы возвращала простые
числа. (Простое число - это натуральное число, которое делится только на
себя и на 1). Выведите с помощью этой функции первые 20 простых чисел
(начиная с 2) в одну строчку через пробел."""


def get_prime_numbers():
    lst = []
    num = 2
    while len(lst) < 20:
        count = 0
        for i in range(2, num + 1):
            if not num % i:
                count += 1
        if count == 1:
            lst.append(num)
            yield num
        num += 1


print(*get_prime_numbers())
