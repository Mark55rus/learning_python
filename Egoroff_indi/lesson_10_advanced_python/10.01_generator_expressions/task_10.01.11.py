""" Ниже представлен код, который вам нужно будет дописать.
    В переменную from_10_to_20 при помощи генератора-выражения сохраните последовательность от 10 до 20 включительно.
Затем при помощи функции next выведите первые три элемента. И остается вывести оставшиеся элементы в цикле"""

# Создайте генератор
from_10_to_20 = (i for i in range(10, 21))

# Распечатайте три первых значения
print(next(from_10_to_20))
print(next(from_10_to_20))
print(next(from_10_to_20))

# выведите все оставшиеся
for value in from_10_to_20:
    print(value)
