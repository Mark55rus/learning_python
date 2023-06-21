""" FizzBuzz.
    Ваша программа должна считать одно натуральное число, после чего вывести:
- “Fizz”, если это число делится на 3;
- “Buzz”, если это число делится на 5;
- “FizzBuzz”, если выполнены оба предыдущих условия;
- само это число в остальных случаях."""

num = int(input())
if not num % 3 and not num % 5:
    print('FizzBuzz')
elif not num % 3:
    print('Fizz')
elif not num % 5:
    print("Buzz")
else:
    print(num)
