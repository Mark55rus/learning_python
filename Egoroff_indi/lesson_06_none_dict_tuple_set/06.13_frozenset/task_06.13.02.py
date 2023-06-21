""" Притягиваем удачу.
В переменную my_frozen, сохраните объект frozenset, содержащий 77 элементов
Сами элементы это последовательность из 77-ми следующих чисел: 7, 77, 777, 7777, 77777, 777777, .....
В конце этой последовательности стоит число из 77-ми цифр 7, на предпоследнем месте - число из 76-ти цифр 7.
Выводить ничего не нужно, только создать переменную my_frozen и правильно ее заполнить"""

my_frozen = frozenset([int('7' * i) for i in range(1, 78)])
print(my_frozen)
print(len(my_frozen))
