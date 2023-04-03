"""Next Prime 🌶️🌶️.
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое
    простое число большее числа num.
Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
Примечание 2. Следующий программный код:
print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))
должен выводить:
7
11
17"""


def get_next_prime(num):
    while True:
        count = 0
        for i in range(2, num + 1):
            if num % i == 0:
                count += 1
        if count == 1:
            return num
        else:
            num += 1


print(get_next_prime(int(input()) + 1))
