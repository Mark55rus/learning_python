""" На вход вашей программе поступает два неравных друг другу целых числа в отдельных строках.
Ваша задача сохранить наименьшее из этих чисел в переменную minimum, а наибольшее - в maximum.
В качестве ответа выведите через пробел сперва minimum, а потом maximum"""

x, y = int(input()), int(input())
maximum = x if x > y else y
minimum = x if x < y else y
print(minimum, maximum)
