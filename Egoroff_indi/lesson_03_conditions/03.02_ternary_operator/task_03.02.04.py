""" На вход программе поступает целое число
Ваша задача сохранить в переменную text строку Even, если введенное число четное, иначе сохраните строку Odd.
В качестве ответа необходимо вывести переменную text"""

n = int(input())
text = 'Even' if not n % 2 else 'Odd'
print(text)
