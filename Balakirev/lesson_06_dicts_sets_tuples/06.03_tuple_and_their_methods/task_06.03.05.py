""" Подвиг 4. Вводятся названия городов в одну строку через пробел. На их
основе формируется кортеж. Если в этом кортеже нет города "Москва",
то следует его добавить в конец кортежа. Результат вывести на экран в виде
строки с названиями городов через пробел."""

cities = tuple(input().split())
if "Москва" not in cities:
    cities += ("Москва",)
print(" ".join(cities))
