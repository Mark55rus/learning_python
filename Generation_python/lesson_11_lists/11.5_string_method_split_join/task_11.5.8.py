"""Добавь разделитель.
На вход программе подается строка текста и строка разделитель. Напишите программу, которая вставляет указанный
 разделитель между каждым символом введенной строки текста.
Формат входных данных
    На вход программе подается строка текста и строка разделитель, каждая на отдельной строке
Формат выходных данных
    Программа должна вывести текст в соответствии с условием задачи."""

text = input()
separator = input()
lst = separator.join(text)
print(lst)
