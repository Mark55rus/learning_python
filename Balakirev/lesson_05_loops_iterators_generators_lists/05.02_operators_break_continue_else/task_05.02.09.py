""" Подвиг 8. (На использование цикла while). Начав тренировки, лыжник в первый
день пробежал 10 км. Каждый следующий день он увеличивал пробег на 10 % от
пробега предыдущего дня. Определить в какой день он пробежит больше x км
(натуральное число x вводится с клавиатуры). Результат (искомый день) вывести
на экран."""

x = int(input())
days = 1
distance = 10
while distance< x:
    distance *= 1.1
    days += 1
print(days)
