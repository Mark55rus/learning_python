""" Даны два списка чисел. Выведите все числа в порядке возрастания, которые входят в первый список, но при этом
отсутствуют во втором. """

my_set_1 = set(map(int, input().split()))
my_set_2 = set(map(int, input().split()))
# variant 1:
print(*sorted(my_set_1.difference(my_set_2)))

# variant 2:
my_set_1.difference_update(my_set_2)
print(*sorted(my_set_1))