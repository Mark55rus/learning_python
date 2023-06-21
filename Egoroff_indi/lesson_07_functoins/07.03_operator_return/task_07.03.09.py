""" Fizz Buzz  список.
    Напишите функцию generate_fizz_buzz_list, которая принимает одно целое число n - размер списка. Функция
generate_fizz_buzz_list должна:
1 - обойти числа от 1 до n включительно и для каждого такого числа выполнить последовательно проверки с пункта 2 по
пункт 5:
2 - Если число кратно и трем, и пяти, то в список заносим строку FizzBuzz
3 - Если число кратно трем, то в список заносим строку Fizz
4 - Если число кратно пяти, то в список заносим строку Buzz
5 - Если число не кратно ни трем ни пяти, то в список заносим само это число
    В итоге функция generate_fizz_buzz_list должна вернуть сформированный список из n элементов. Ниже показаны примеры
вызова:
- generate_fizz_buzz_list(3)  => [1, 2, 'Fizz']
- generate_fizz_buzz_list(7)  => [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7]
- generate_fizz_buzz_list(15) => [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
Ваша задача написать только определение функции generate_fizz_buzz_list"""


def generate_fizz_buzz_list(n):
    lst = []
    for i in range(1, n + 1):
        if not i % 3 and not i % 5:
            lst.append('FizzBuzz')
        elif not i % 3:
            lst.append('Fizz')
        elif not i % 5:
            lst.append('Buzz')
        else:
            lst.append(i)
    return lst
