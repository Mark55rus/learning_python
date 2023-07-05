""" Подвиг 5. Вводятся названия городов в одну строку через пробел. На их
основе формируется кортеж. Если в этом кортеже присутствует город
"Ульяновск", то этот элемент следует удалить (создав новый кортеж).
Результат вывести на экран в виде строки с названиями городов через пробел."""

cities = tuple(input().split())
if cities.count("Ульяновск"):
    index = cities.index("Ульяновск")
    if index == 0:
        cities = cities[1:]
    else:
        cities = cities[0:index] + cities[index + 1:]
print(" ".join(cities))

# variant 2:
# cities = tuple([city for city in input().split() if city != "Ульяновск"])
# print(" ".join(cities))
