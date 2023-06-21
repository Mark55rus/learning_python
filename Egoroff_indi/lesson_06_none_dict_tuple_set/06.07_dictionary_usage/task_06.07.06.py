""" Анаграмма.
    Строка S1 называется анаграммой строки S2, если она получается из S2 перестановкой символов.
Программа получает на вход две строки S1 и S2. Если строка S1 является анаграммой строки S2 нужно вывести YES, в
противном случае - NO"""

s1 = input()
s2 = input()
d1 = {s: s1.count(s) for s in s1}
d2 = {s: s2.count(s) for s in s2}
print('YES' if d1 == d2 and len(d1) == len(d2) else 'NO')
