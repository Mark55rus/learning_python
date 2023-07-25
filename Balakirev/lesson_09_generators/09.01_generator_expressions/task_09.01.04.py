""" Подвиг 3. На вход программы поступают два целых числа a и b (a < b),
записанные в одну строчку через пробел. Определите генератор, который бы
выдавал модули целых чисел из диапазона [a; b]. В цикле выведите первые пять
значений этого генератора. Каждое значение с новой строки. (Гарантируется,
что пять значений имеются)."""

a, b = map(int, input().split())
gen = (abs(i) for i in range(a, b + 1))
count = 0
while count < 5:
    count += 1
    print(next(gen))

# variant 2:
# for i, j in enumerate(gen):
#     print(j)
#     if i == 4:
#         break

# variant 3:
# for i in range(5):
#     print(next(gen))
