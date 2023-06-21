""" На вход программе поступает целое число n. Вам необходимо создать словарь, который будет включать в себя ключи от 1
до n, а значениями соответствующего ключа будет значение ключа в квадрате.
В качестве ответа выведите полученный словарь"""

# variant 1:
lst = [[i, i ** 2] for i in range(1, int(input()) + 1)]
dct = {}
for i in lst:
    dct[i[0]] = i[0] ** 2
print(dct)

# variant 2:
print({i: i ** 2 for i in range(1, int(input()) + 1)})

# variant 3:
n = int(input())
num = {}
for i in range(1, n + 1):
    num[i] = i ** 2
print(num)
