""" Программа принимает на вход три символа через пробел в одну строку. Необходимо вывести код каждого символа при
помощи функции ord в определенном формате."""

symbol_1, symbol_2, symbol_3 = input().split()
print(f'Simvol code {symbol_1} is {ord(symbol_1)}.')
print(f'Simvol code {symbol_2} is {ord(symbol_2)}.')
print(f'Simvol code {symbol_3} is {ord(symbol_3)}.')
