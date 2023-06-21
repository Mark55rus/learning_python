""" На вход программе поступает список из целых чисел. Ваша задача найти в данном списке наименьшее положительное
значение. В случае, если положительных значений нет, выведите строку "Empty"""

lst = list(map(int, input().split()))
smallest = max(lst)
for i in range(len(lst)):
    if 0 < lst[i] < smallest:
        smallest = lst[i]
if smallest > 0:
    print(smallest)
else:
    print('Empty')
