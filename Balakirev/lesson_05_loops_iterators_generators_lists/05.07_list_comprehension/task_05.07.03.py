""" Подвиг 2. Вводится семизначное целое положительное число. С помощью list
comprehension сформировать список lst, содержащий цифры этого числа (в списке
должны быть записаны числа, а не строки). Результат вывести на экран список
командой:"""

lst = [int(i) for i in input()]
print(lst)
