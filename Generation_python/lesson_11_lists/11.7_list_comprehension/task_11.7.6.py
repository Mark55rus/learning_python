"""Дополните приведенный код, используя списочное выражение, так, чтобы получить список всех чисел палиндромов от
    100 до 1000.

palindromes =
print(palindromes)"""

palindromes = [i for i in range(100, 1000) if str(i) == str(i)[::-1]]
print(palindromes)
