""" Подвиг 10. Работа светофора для пешеходов запрограммирована следующим
образом: в начале каждого часа в течение трех минут горит зеленый сигнал,
затем в течение двух минут – красный, в течение трех минут – опять зеленый и
т.д. Дано вещественное число t, означающее время в минутах, прошедшее с начала
очередного часа. Определить, сигнал какого цвета горит для пешеходов в этот
момент. На экран вывести сообщение (без кавычек) "green" - для зеленого и "red"
 - для красного."""

t = float(input())
if t % 5 <= 3:
    print("green")
else:
    print("red")
