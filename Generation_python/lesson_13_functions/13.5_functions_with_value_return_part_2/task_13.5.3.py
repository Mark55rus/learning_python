"""Is a Number Prime? 🌶️.
Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True
    если число является простым и False в противном случае.
Примечание. Следующий программный код:
print(is_prime(1))
print(is_prime(10))
print(is_prime(17))
должен выводить:
False
False
True"""


def is_prime(num):
    count = 0
    for i in range(2, num + 1):
        if num % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False


print(is_prime(int(input())))
