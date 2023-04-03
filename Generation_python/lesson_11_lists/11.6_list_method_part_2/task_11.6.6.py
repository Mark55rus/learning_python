"""Переставить min и max.
На вход программе подается строка текста, содержащая различные натуральные числа. Из данной строки формируется список
 чисел. Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.
Формат входных данных
    На вход программе подается строка текста, содержащая различные натуральные числа, разделенные символом пробела.
Формат выходных данных
    Программа должна вывести строку текста в соответствии с условием задачи.
Примечание. Используйте подходящие встроенные функции и списочные методы."""

numbers = list(map(int, input().split()))
largest = numbers.index(max(numbers))
smallest = numbers.index(min(numbers))
numbers[largest], numbers[smallest] = numbers[smallest], numbers[largest]
print(numbers)