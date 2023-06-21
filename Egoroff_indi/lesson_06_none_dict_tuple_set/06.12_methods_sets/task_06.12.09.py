""" Даны два списка чисел.
Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания."""

my_set_1 = set(map(int, input().split()))
my_set_2 = set(map(int, input().split()))
print(*sorted(my_set_1.intersection(my_set_2)))

# variant 2:
# my_set_1.symmetric_difference_update(my_set_2)
# print(my_set_1)
